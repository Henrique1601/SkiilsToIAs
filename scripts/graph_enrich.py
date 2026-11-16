#!/usr/bin/env python3
"""Deterministically extract agent/MCP/brain nodes and cross-references for graphify."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
BACKTICK_RE = re.compile(r"`([a-z0-9][a-z0-9-]{2,60})`")


def _node_id(prefix: str, slug: str) -> str:
    clean = re.sub(r"[^a-zA-Z0-9_]", "_", f"{prefix}_{slug}")
    return re.sub(r"_+", "_", clean).strip("_")


def build_ecosystem_semantic(root: Path = REPO_ROOT) -> dict[str, Any]:
    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []
    seen_nodes: set[str] = set()
    known_ids: dict[str, str] = {}

    def add_node(nid: str, label: str, file_type: str, source_file: str) -> None:
        if nid in seen_nodes:
            return
        seen_nodes.add(nid)
        nodes.append(
            {
                "id": nid,
                "label": label,
                "file_type": file_type,
                "source_file": source_file,
                "_origin": "semantic",
            }
        )

    # 1. Register MCP nodes
    for readme in sorted((root / "mcps").glob("*/README.md")):
        slug = readme.parent.name
        nid = _node_id("mcp", slug)
        rel = readme.relative_to(root).as_posix()
        add_node(nid, f"MCP: {slug}", "document", rel)
        known_ids[slug] = nid

    # 2. Register Brain doc nodes
    for doc in sorted((root / "docs" / "brain").glob("*.md")):
        slug = doc.stem
        nid = _node_id("brain", slug.lower())
        rel = doc.relative_to(root).as_posix()
        add_node(nid, f"Brain: {slug}", "document", rel)
        known_ids[slug] = nid
        known_ids[slug.lower()] = nid

    # 3. Register Skill index nodes (lightweight, only referenced ones or all categorized)
    skill_nodes: dict[str, str] = {}
    for skill_md in sorted(root.glob("*/*/SKILL.md")):
        cat = skill_md.parent.parent.name
        if cat in {"custom-agents", "mcps", "docs", "scripts", "assets", "tests"}:
            continue
        slug = skill_md.parent.name
        skill_nodes[slug] = skill_md.relative_to(root).as_posix()

    # 4. Register Agent nodes and extract cross-references
    agent_files = sorted(
        p for p in (root / "custom-agents").glob("*.md")
        if p.name not in {"README.md", "PROMPTS_MOTION_SOCIAL.md"}
    )
    for af in agent_files:
        known_ids[af.stem] = _node_id("agent", af.stem)

    seen_edges: set[tuple[str, str, str]] = set()

    def add_edge(src: str, tgt: str, relation: str, source_file: str) -> None:
        if src == tgt or (src, tgt, relation) in seen_edges:
            return
        seen_edges.add((src, tgt, relation))
        edges.append(
            {
                "source": src,
                "target": tgt,
                "relation": relation,
                "confidence": "EXTRACTED",
                "source_file": source_file,
                "_origin": "semantic",
            }
        )

    for af in agent_files:
        src_id = _node_id("agent", af.stem)
        rel = af.relative_to(root).as_posix()
        add_node(src_id, f"Agent: {af.stem}", "document", rel)
        text = af.read_text(encoding="utf-8", errors="replace")

        for match in BACKTICK_RE.findall(text):
            if match in known_ids:
                add_edge(src_id, known_ids[match], "references", rel)
            elif match in skill_nodes:
                sk_id = _node_id("skill", match)
                add_node(sk_id, f"Skill: {match}", "document", skill_nodes[match])
                add_edge(src_id, sk_id, "uses_skill", rel)

        for link in LINK_RE.findall(text):
            stem = Path(link.split("#")[0]).stem
            if stem in known_ids:
                add_edge(src_id, known_ids[stem], "references", rel)

    for doc in sorted((root / "docs" / "brain").glob("*.md")):
        src_id = _node_id("brain", doc.stem.lower())
        rel = doc.relative_to(root).as_posix()
        text = doc.read_text(encoding="utf-8", errors="replace")
        for wl in WIKILINK_RE.findall(text):
            target = wl.split("|")[0].strip().lower()
            if target in known_ids:
                add_edge(src_id, known_ids[target], "links_to", rel)

    return {"nodes": nodes, "edges": edges, "hyperedges": [], "input_tokens": 0, "output_tokens": 0}


def main() -> int:
    out_dir = REPO_ROOT / "graphify-out"
    out_dir.mkdir(parents=True, exist_ok=True)
    sem = build_ecosystem_semantic(REPO_ROOT)
    (out_dir / ".graphify_semantic.json").write_text(
        json.dumps(sem, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Ecosystem semantic graph: {len(sem['nodes'])} nodes, {len(sem['edges'])} edges")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
