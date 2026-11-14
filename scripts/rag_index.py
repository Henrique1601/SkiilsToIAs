#!/usr/bin/env python3
"""Lean RAG indexer for SkiilsToIAs (SQLite FTS5/BM25 + optional pgvector export)."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_DB = Path(".cache/rag_index.db")
DEFAULT_EMBED_MODEL = "text-embedding-3-small"
MAX_CHUNK_CHARS = 2000
IGNORED_DIRS = {".git", ".agents", ".cache", "node_modules", "__pycache__", ".venv", "venv"}

HEADING_RE = re.compile(r"^(#{1,2})\s+(.*?)\s*$")
FENCE_RE = re.compile(r"^(`{3,}|~{3,})")


def configure_utf8_stdio() -> None:
    """Ensure UTF-8 output on Windows consoles."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def discover_files(root: Path) -> list[tuple[Path, str]]:
    """Discover repository markdown files with their doc_type."""
    found: dict[str, tuple[Path, str]] = {}

    def add(path: Path, doc_type: str) -> None:
        if not path.is_file():
            return
        rel = path.relative_to(root)
        if any(part in IGNORED_DIRS or part.startswith(".") for part in rel.parts):
            return
        key = rel.as_posix()
        found.setdefault(key, (path, doc_type))

    for p in root.rglob("SKILL.md"):
        add(p, "skill")
    for p in (root / "custom-agents").glob("*.md"):
        add(p, "agent")
    for p in (root / "mcps").glob("*/README.md"):
        add(p, "mcp")
    for p in (root / "docs" / "brain").glob("*.md"):
        add(p, "brain")

    return [found[k] for k in sorted(found)]


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Extract simple YAML frontmatter key/value pairs without external deps."""
    if not text.startswith("---"):
        return {}, text
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return {}, text

    meta: dict[str, str] = {}
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
        line = lines[i].strip()
        if ":" in line and not line.startswith("#"):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip("\"'")

    if end_idx is None:
        return {}, text
    return meta, "".join(lines[end_idx + 1 :])


def split_large_text(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list[str]:
    """Split oversized sections on paragraph boundaries."""
    text = text.strip()
    if not text:
        return []
    if len(text) <= max_chars:
        return [text]

    parts: list[str] = []
    current: list[str] = []
    current_len = 0
    for para in re.split(r"\n\s*\n", text):
        para = para.strip()
        if not para:
            continue
        if current and current_len + len(para) + 2 > max_chars:
            parts.append("\n\n".join(current))
            current = [para]
            current_len = len(para)
        else:
            current.append(para)
            current_len += len(para) + (2 if current_len else 0)
    if current:
        parts.append("\n\n".join(current))
    return parts


def parse_markdown_chunks(
    text: str, rel_path: str, doc_type: str
) -> tuple[str, dict[str, str], list[dict[str, Any]]]:
    """Parse markdown into heading-based semantic chunks."""
    frontmatter, body = parse_frontmatter(text)
    h1 = frontmatter.get("name", "")
    h2 = ""
    in_fence = False
    fence_marker = ""
    sections: list[tuple[str, list[str]]] = []
    current_lines: list[str] = []
    current_section = h1 or Path(rel_path).stem

    for line in body.splitlines():
        fence_match = FENCE_RE.match(line.lstrip())
        if fence_match:
            marker = fence_match.group(1)[0]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            current_lines.append(line)
            continue

        if not in_fence:
            heading_match = HEADING_RE.match(line)
            if heading_match:
                content = "\n".join(current_lines).strip()
                if content:
                    sections.append((current_section, [content]))
                level = len(heading_match.group(1))
                heading_text = heading_match.group(2).strip()
                if level == 1:
                    h1 = heading_text
                    h2 = ""
                    current_section = h1
                else:
                    h2 = heading_text
                    current_section = f"{h1} > {h2}" if h1 else h2
                current_lines = [line]
                continue

        current_lines.append(line)

    tail = "\n".join(current_lines).strip()
    if tail:
        sections.append((current_section, [tail]))

    title = h1 or frontmatter.get("name") or Path(rel_path).stem
    chunks: list[dict[str, Any]] = []
    idx = 0
    for section_name, raw_parts in sections:
        for part in split_large_text("\n".join(raw_parts)):
            if not re.search(r"[\w\u00C0-\u024F]", part):
                continue
            chunks.append(
                {
                    "chunk_index": idx,
                    "section": section_name,
                    "content": part,
                    "token_count": len(part.split()),
                    "metadata": {
                        "path": rel_path,
                        "doc_type": doc_type,
                        "title": title,
                        "section": section_name,
                        **({k: v for k, v in frontmatter.items() if k in {"name", "description"}}),
                    },
                }
            )
            idx += 1

    return title, frontmatter, chunks


def init_sqlite(conn: sqlite3.Connection, rebuild: bool = False) -> None:
    """Create SQLite schema and FTS5 virtual table."""
    conn.execute("PRAGMA foreign_keys = ON;")
    if rebuild:
        conn.executescript(
            """
            DROP TABLE IF EXISTS chunks_fts;
            DROP TABLE IF EXISTS chunks;
            DROP TABLE IF EXISTS documents;
            """
        )

    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT NOT NULL UNIQUE,
            doc_type TEXT NOT NULL,
            title TEXT NOT NULL DEFAULT '',
            content_hash TEXT NOT NULL,
            metadata TEXT NOT NULL DEFAULT '{}',
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
            path TEXT NOT NULL,
            doc_type TEXT NOT NULL,
            chunk_index INTEGER NOT NULL,
            section TEXT NOT NULL DEFAULT '',
            content TEXT NOT NULL,
            token_count INTEGER NOT NULL DEFAULT 0,
            metadata TEXT NOT NULL DEFAULT '{}',
            UNIQUE (document_id, chunk_index)
        );

        CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
            path,
            doc_type,
            section,
            content,
            content='chunks',
            content_rowid='id',
            tokenize='porter unicode61'
        );
        """
    )


def delete_doc_fts(conn: sqlite3.Connection, doc_id: int) -> None:
    """Remove existing FTS5 entries for a document before updating/deleting chunks."""
    rows = conn.execute(
        "SELECT id, path, doc_type, section, content FROM chunks WHERE document_id = ?",
        (doc_id,),
    ).fetchall()
    for row_id, path, doc_type, section, content in rows:
        conn.execute(
            "INSERT INTO chunks_fts(chunks_fts, rowid, path, doc_type, section, content) "
            "VALUES ('delete', ?, ?, ?, ?, ?)",
            (row_id, path, doc_type, section, content),
        )


def index_sqlite(
    root: Path, db_path: Path, rebuild: bool = False
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    """Index all discovered markdown files into SQLite FTS5."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    files = discover_files(root)
    now = datetime.now(timezone.utc).isoformat()
    stats = {"total_files": len(files), "indexed": 0, "skipped": 0, "removed": 0, "chunks": 0}
    export_docs: list[dict[str, Any]] = []

    with sqlite3.connect(db_path) as conn:
        init_sqlite(conn, rebuild=rebuild)
        existing = {
            row[0]: (row[1], row[2])
            for row in conn.execute("SELECT path, id, content_hash FROM documents").fetchall()
        }
        seen_paths: set[str] = set()

        for file_path, doc_type in files:
            rel_path = file_path.relative_to(root).as_posix()
            seen_paths.add(rel_path)
            raw_text = file_path.read_text(encoding="utf-8", errors="replace")
            content_hash = hashlib.sha256(raw_text.encode("utf-8")).hexdigest()

            title, frontmatter, chunks = parse_markdown_chunks(raw_text, rel_path, doc_type)
            export_docs.append(
                {
                    "path": rel_path,
                    "doc_type": doc_type,
                    "title": title,
                    "content_hash": content_hash,
                    "metadata": frontmatter,
                    "chunks": chunks,
                }
            )

            prev = existing.get(rel_path)
            if prev and prev[1] == content_hash and not rebuild:
                stats["skipped"] += 1
                stats["chunks"] += len(chunks)
                continue

            if prev:
                doc_id = prev[0]
                delete_doc_fts(conn, doc_id)
                conn.execute("DELETE FROM chunks WHERE document_id = ?", (doc_id,))
                conn.execute(
                    "UPDATE documents SET doc_type = ?, title = ?, content_hash = ?, "
                    "metadata = ?, updated_at = ? WHERE id = ?",
                    (doc_type, title, content_hash, json.dumps(frontmatter, ensure_ascii=False), now, doc_id),
                )
            else:
                cur = conn.execute(
                    "INSERT INTO documents (path, doc_type, title, content_hash, metadata, updated_at) "
                    "VALUES (?, ?, ?, ?, ?, ?)",
                    (rel_path, doc_type, title, content_hash, json.dumps(frontmatter, ensure_ascii=False), now),
                )
                doc_id = int(cur.lastrowid)

            for chunk in chunks:
                cur = conn.execute(
                    "INSERT INTO chunks (document_id, path, doc_type, chunk_index, section, content, token_count, metadata) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        doc_id,
                        rel_path,
                        doc_type,
                        chunk["chunk_index"],
                        chunk["section"],
                        chunk["content"],
                        chunk["token_count"],
                        json.dumps(chunk["metadata"], ensure_ascii=False),
                    ),
                )
                chunk_id = int(cur.lastrowid)
                conn.execute(
                    "INSERT INTO chunks_fts(rowid, path, doc_type, section, content) VALUES (?, ?, ?, ?, ?)",
                    (chunk_id, rel_path, doc_type, chunk["section"], chunk["content"]),
                )

            stats["indexed"] += 1
            stats["chunks"] += len(chunks)

        for stale_path, (stale_id, _) in existing.items():
            if stale_path not in seen_paths:
                delete_doc_fts(conn, stale_id)
                conn.execute("DELETE FROM documents WHERE id = ?", (stale_id,))
                stats["removed"] += 1

        conn.commit()

    return export_docs, stats


def fetch_openai_embeddings(texts: list[str], api_key: str, model: str) -> list[list[float]]:
    """Fetch embeddings from OpenAI API using stdlib urllib."""
    embeddings: list[list[float]] = []
    batch_size = 64
    for i in range(0, len(texts), batch_size):
        batch = [t[:8000] for t in texts[i : i + batch_size]]
        payload = json.dumps({"model": model, "input": batch}).encode("utf-8")
        req = urllib.request.Request(
            "https://api.openai.com/v1/embeddings",
            data=payload,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"OpenAI embeddings API error {exc.code}: {detail}") from exc

        ordered = sorted(data["data"], key=lambda item: item["index"])
        embeddings.extend(item["embedding"] for item in ordered)
    return embeddings


def export_pgvector(docs: list[dict[str, Any]], database_url: str, api_key: str, model: str) -> int:
    """Generate embeddings and upsert documents/chunks into PostgreSQL pgvector."""
    all_chunks = [c for d in docs for c in d["chunks"]]
    if not all_chunks:
        return 0

    texts = [f"{c['section']}\n\n{c['content']}" for c in all_chunks]
    vectors = fetch_openai_embeddings(texts, api_key, model)
    vec_iter = iter(vectors)

    try:
        import psycopg  # type: ignore[import-not-found]

        with psycopg.connect(database_url) as pg_conn:
            with pg_conn.cursor() as cur:
                for doc in docs:
                    cur.execute(
                        """
                        INSERT INTO documents (path, doc_type, title, content_hash, metadata, updated_at)
                        VALUES (%s, %s, %s, %s, %s::jsonb, NOW())
                        ON CONFLICT (path) DO UPDATE SET
                            doc_type = EXCLUDED.doc_type,
                            title = EXCLUDED.title,
                            content_hash = EXCLUDED.content_hash,
                            metadata = EXCLUDED.metadata,
                            updated_at = NOW()
                        RETURNING id
                        """,
                        (doc["path"], doc["doc_type"], doc["title"], doc["content_hash"], json.dumps(doc["metadata"])),
                    )
                    doc_id = cur.fetchone()[0]
                    cur.execute("DELETE FROM chunks WHERE document_id = %s", (doc_id,))
                    for c in doc["chunks"]:
                        vec = next(vec_iter)
                        vec_literal = "[" + ",".join(f"{x:.8f}" for x in vec) + "]"
                        cur.execute(
                            """
                            INSERT INTO chunks (document_id, chunk_index, section, content, token_count, metadata, embedding)
                            VALUES (%s, %s, %s, %s, %s, %s::jsonb, %s::vector)
                            """,
                            (doc_id, c["chunk_index"], c["section"], c["content"], c["token_count"], json.dumps(c["metadata"]), vec_literal),
                        )
            pg_conn.commit()
        return len(all_chunks)
    except ImportError:
        pass

    # Fallback: emit SQL file and attempt psql if available.
    sql_out = Path(".cache/pgvector_upsert.sql")
    sql_out.parent.mkdir(parents=True, exist_ok=True)
    with sql_out.open("w", encoding="utf-8") as fh:
        fh.write("BEGIN;\n")
        for doc in docs:
            p = doc["path"].replace("'", "''")
            dt = doc["doc_type"].replace("'", "''")
            tt = doc["title"].replace("'", "''")
            ch = doc["content_hash"].replace("'", "''")
            md = json.dumps(doc["metadata"], ensure_ascii=False).replace("'", "''")
            fh.write(
                f"INSERT INTO documents (path, doc_type, title, content_hash, metadata, updated_at) "
                f"VALUES ('{p}', '{dt}', '{tt}', '{ch}', '{md}'::jsonb, NOW()) "
                f"ON CONFLICT (path) DO UPDATE SET doc_type=EXCLUDED.doc_type, title=EXCLUDED.title, "
                f"content_hash=EXCLUDED.content_hash, metadata=EXCLUDED.metadata, updated_at=NOW();\n"
            )
            fh.write(f"DELETE FROM chunks WHERE document_id = (SELECT id FROM documents WHERE path = '{p}');\n")
            for c in doc["chunks"]:
                vec = next(vec_iter)
                vec_literal = "[" + ",".join(f"{x:.8f}" for x in vec) + "]"
                sec = c["section"].replace("'", "''")
                cnt = c["content"].replace("'", "''")
                cmd = json.dumps(c["metadata"], ensure_ascii=False).replace("'", "''")
                fh.write(
                    f"INSERT INTO chunks (document_id, chunk_index, section, content, token_count, metadata, embedding) "
                    f"VALUES ((SELECT id FROM documents WHERE path = '{p}'), {c['chunk_index']}, '{sec}', '{cnt}', "
                    f"{c['token_count']}, '{cmd}'::jsonb, '{vec_literal}'::vector);\n"
                )
        fh.write("COMMIT;\n")

    try:
        subprocess.run(["psql", database_url, "-v", "ON_ERROR_STOP=1", "-f", str(sql_out)], check=True)
    except FileNotFoundError as exc:
        raise RuntimeError(
            f"Neither 'psycopg' nor 'psql' found; generated {sql_out} with {len(all_chunks)} embedded chunks."
        ) from exc

    return len(all_chunks)


def main() -> int:
    configure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Index SkiilsToIAs markdown knowledge base.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent, help="Repo root path")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="SQLite FTS5 database path")
    parser.add_argument("--rebuild", action="store_true", help="Drop and rebuild SQLite index from scratch")
    parser.add_argument("--pgvector", action="store_true", help="Also export embeddings/rows to PostgreSQL pgvector")
    args = parser.parse_args()

    docs, stats = index_sqlite(args.root.resolve(), args.db, rebuild=args.rebuild)
    print(
        f"SQLite FTS5 indexed: files={stats['total_files']} updated={stats['indexed']} "
        f"skipped={stats['skipped']} removed={stats['removed']} chunks={stats['chunks']} db={args.db}"
    )

    if args.pgvector:
        database_url = os.environ.get("DATABASE_URL", "").strip()
        api_key = os.environ.get("OPENAI_API_KEY", "").strip()
        if not database_url or not api_key:
            print("Error: --pgvector requires DATABASE_URL and OPENAI_API_KEY environment variables.", file=sys.stderr)
            return 1
        model = os.environ.get("OPENAI_EMBEDDING_MODEL", DEFAULT_EMBED_MODEL).strip() or DEFAULT_EMBED_MODEL
        exported = export_pgvector(docs, database_url, api_key, model)
        print(f"pgvector exported: chunks={exported} model={model}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
