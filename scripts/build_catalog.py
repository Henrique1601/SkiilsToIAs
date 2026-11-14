#!/usr/bin/env python3
"""Build docs/catalog/catalog.json from categorized skills, custom agents, and MCPs."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPO_ROOT / "docs" / "catalog" / "catalog.json"

EXCLUDED_SKILL_DIRS = {"custom-agents", "mcps", "docs", "scripts", "assets"}
EXCLUDED_AGENT_DOCS = {"README.md", "PROMPTS_MOTION_SOCIAL.md"}
REPO_SLUG = "Henrique1601/SkiilsToIAs"


def _strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        return value[1:-1].strip()
    return value


def parse_frontmatter(text: str) -> dict[str, str]:
    """Extract top-level scalar/multiline fields from YAML frontmatter without external deps."""
    clean = text.lstrip("\ufeff")
    if not clean.startswith("---"):
        return {}

    lines = clean.splitlines()
    end_idx = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
    if end_idx is None:
        return {}

    fm_lines = lines[1:end_idx]
    data: dict[str, str] = {}
    i = 0
    while i < len(fm_lines):
        line = fm_lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue

        match = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", line)
        if not match:
            i += 1
            continue

        key, raw_val = match.group(1), match.group(2).strip()
        if raw_val in ("|", "|-", ">", ">-"):
            block_lines: list[str] = []
            i += 1
            while i < len(fm_lines):
                nxt = fm_lines[i]
                if nxt.startswith((" ", "\t")) or not nxt.strip():
                    block_lines.append(nxt.strip())
                    i += 1
                else:
                    break
            data[key] = " ".join(part for part in block_lines if part).strip()
            continue

        if raw_val == "":
            # Possibly a YAML list or indented multiline scalar
            cont_lines: list[str] = []
            i += 1
            while i < len(fm_lines):
                nxt = fm_lines[i]
                if nxt.startswith((" ", "\t")) and not nxt.lstrip().startswith("- "):
                    cont_lines.append(nxt.strip())
                    i += 1
                elif nxt.startswith((" ", "\t")):
                    i += 1
                else:
                    break
            if cont_lines:
                data[key] = " ".join(cont_lines).strip()
            continue

        # Single-line or wrapped plain/quoted scalar
        val_parts = [raw_val]
        i += 1
        while i < len(fm_lines):
            nxt = fm_lines[i]
            if nxt.startswith((" ", "\t")) and not nxt.lstrip().startswith("- "):
                val_parts.append(nxt.strip())
                i += 1
            else:
                break
        data[key] = _strip_quotes(" ".join(val_parts))

    return data


def clean_markdown_text(text: str) -> str:
    """Strip common inline markdown formatting for concise plain-text descriptions."""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_mcp_description(text: str) -> str:
    """Extract the first descriptive paragraph or blockquote from an MCP README."""
    clean = text.lstrip("\ufeff")
    lines = clean.splitlines()
    # Skip frontmatter if present
    start = 0
    if clean.startswith("---"):
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                start = idx + 1
                break

    paragraph: list[str] = []
    for line in lines[start:]:
        stripped = line.strip()
        if not stripped:
            if paragraph:
                break
            continue
        if stripped.startswith("#") or stripped == "---" or stripped.startswith("```"):
            if paragraph:
                break
            continue
        if stripped.startswith(">"):
            stripped = stripped.lstrip(">").strip()
            if not stripped:
                continue
        paragraph.append(stripped)

    desc = clean_markdown_text(" ".join(paragraph))
    if len(desc) > 280:
        desc = desc[:277].rstrip() + "..."
    return desc


def collect_skills(root: Path) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for skill_md in sorted(root.glob("*/*/SKILL.md")):
        rel = skill_md.relative_to(root)
        category = rel.parts[0]
        if category.startswith(".") or category in EXCLUDED_SKILL_DIRS:
            continue

        content = skill_md.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(content)
        name = fm.get("name") or rel.parts[1]
        description = clean_markdown_text(fm.get("description", ""))
        items.append(
            {
                "name": name,
                "category": category,
                "type": "skill",
                "description": description,
                "path": rel.as_posix(),
                "install_hint": f"npx skills add {REPO_SLUG} --skill {name}",
            }
        )
    return items


def collect_agents(root: Path) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    agents_dir = root / "custom-agents"
    if not agents_dir.is_dir():
        return items

    for agent_md in sorted(agents_dir.glob("*.md")):
        if agent_md.name in EXCLUDED_AGENT_DOCS:
            continue
        rel = agent_md.relative_to(root)
        content = agent_md.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(content)
        name = fm.get("name") or agent_md.stem
        description = clean_markdown_text(fm.get("description", ""))
        items.append(
            {
                "name": name,
                "category": "custom-agents",
                "type": "agent",
                "description": description,
                "path": rel.as_posix(),
                "install_hint": rel.as_posix(),
            }
        )
    return items


def collect_mcps(root: Path) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    mcps_dir = root / "mcps"
    if not mcps_dir.is_dir():
        return items

    for readme in sorted(mcps_dir.glob("*/README.md")):
        rel = readme.relative_to(root)
        name = rel.parts[1]
        content = readme.read_text(encoding="utf-8", errors="replace")
        description = extract_mcp_description(content)
        items.append(
            {
                "name": name,
                "category": "mcps",
                "type": "mcp",
                "description": description,
                "path": rel.as_posix(),
                "install_hint": rel.as_posix(),
            }
        )
    return items


def build_catalog(root: Path = REPO_ROOT, output: Path = OUTPUT_PATH) -> dict:
    skills = collect_skills(root)
    agents = collect_agents(root)
    mcps = collect_mcps(root)
    items = skills + agents + mcps

    cat_counts = Counter(item["category"] for item in items)
    categories = [
        {"name": cat, "count": count}
        for cat, count in sorted(cat_counts.items(), key=lambda x: (-x[1], x[0]))
    ]

    catalog = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "counts": {
            "total": len(items),
            "skills": len(skills),
            "agents": len(agents),
            "mcps": len(mcps),
        },
        "categories": categories,
        "items": items,
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return catalog


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    catalog = build_catalog()
    c = catalog["counts"]
    print(
        f"Generated {OUTPUT_PATH.relative_to(REPO_ROOT).as_posix()}: "
        f"{c['total']} items ({c['skills']} skills, {c['agents']} agents, {c['mcps']} mcps)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
