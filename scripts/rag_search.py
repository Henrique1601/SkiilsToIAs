#!/usr/bin/env python3
"""Lean CLI search over the SkiilsToIAs SQLite FTS5/BM25 RAG index."""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path
from typing import Any

DEFAULT_DB = Path(".cache/rag_index.db")


def configure_utf8_stdio() -> None:
    """Ensure UTF-8 output on Windows consoles."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def build_fts_query(raw_query: str, operator: str = "AND") -> str:
    """Sanitize a free-text query into a safe FTS5 MATCH expression."""
    tokens = re.findall(r"[\w\u00C0-\u024F]+", raw_query, flags=re.UNICODE)
    if not tokens:
        return ""
    escaped = [f'"{tok.replace(chr(34), chr(34) * 2)}"' for tok in tokens]
    return f" {operator} ".join(escaped)


def make_snippet(text: str, max_len: int = 220) -> str:
    """Produce a single-line preview snippet from chunk content."""
    compact = re.sub(r"\s+", " ", text).strip()
    if len(compact) <= max_len:
        return compact
    return compact[: max_len - 3].rstrip() + "..."


def search_index(
    db_path: Path, query: str, top_k: int = 5, doc_type: str | None = None
) -> list[dict[str, Any]]:
    """Query SQLite FTS5 using BM25 ranking."""
    if not db_path.is_file():
        raise FileNotFoundError(
            f"RAG index not found at '{db_path}'. Run 'python scripts/rag_index.py' first."
        )

    fts_and = build_fts_query(query, "AND")
    if not fts_and:
        return []

    sql = """
        SELECT
            c.path,
            c.doc_type,
            c.section,
            c.content,
            -bm25(chunks_fts, 2.0, 0.5, 3.0, 1.0) AS score
        FROM chunks_fts
        JOIN chunks c ON c.id = chunks_fts.rowid
        WHERE chunks_fts MATCH ?
    """
    params: list[Any] = [fts_and]
    if doc_type:
        sql += " AND c.doc_type = ?"
        params.append(doc_type)
    sql += " ORDER BY score DESC LIMIT ?"
    params.append(top_k)

    with sqlite3.connect(db_path) as conn:
        rows = conn.execute(sql, params).fetchall()
        if not rows and " AND " in fts_and:
            fts_or = build_fts_query(query, "OR")
            params[0] = fts_or
            rows = conn.execute(sql, params).fetchall()

    results: list[dict[str, Any]] = []
    for path, dtype, section, content, score in rows:
        results.append(
            {
                "path": path,
                "doc_type": dtype,
                "section": section,
                "score": round(float(score), 4),
                "snippet": make_snippet(content),
                "content": content,
            }
        )
    return results


def main() -> int:
    configure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Search SkiilsToIAs local RAG index.")
    parser.add_argument("query", help="Search query string")
    parser.add_argument("--top", type=int, default=5, help="Maximum results to return (default: 5)")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="SQLite FTS5 database path")
    parser.add_argument(
        "--type",
        choices=["skill", "agent", "mcp", "brain"],
        default=None,
        help="Filter by document type",
    )
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output JSON")
    args = parser.parse_args()

    try:
        results = search_index(args.db, args.query, top_k=max(1, args.top), doc_type=args.type)
    except FileNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.as_json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 0

    if not results:
        print("No matching results.")
        return 0

    for rank, item in enumerate(results, start=1):
        print(
            f"[{rank}] {item['path']} | {item['section']} "
            f"(type={item['doc_type']}, score={item['score']})"
        )
        print(f"    {item['snippet']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
