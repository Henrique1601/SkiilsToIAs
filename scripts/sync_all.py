#!/usr/bin/env python3
"""Sync all custom agents to SKILL.md and ~/.gemini/config/, rebuild catalog, and verify parity."""

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
GEM_AGENTS = Path.home() / ".gemini" / "config" / "agents"
GEM_SKILLS = Path.home() / ".gemini" / "config" / "skills"
GEM_MCP = Path.home() / ".gemini" / "config" / "mcp_config.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sync_agents() -> tuple[int, list[str]]:
    GEM_AGENTS.mkdir(parents=True, exist_ok=True)
    GEM_SKILLS.mkdir(parents=True, exist_ok=True)

    agent_mds = sorted(
        p
        for p in (REPO / "custom-agents").glob("*.md")
        if p.name.lower() not in ("readme.md", "prompts_motion_social.md")
    )
    errors: list[str] = []
    for md in agent_mds:
        stem = md.stem
        skill_dir = REPO / "custom-agents" / stem
        skill_dir.mkdir(parents=True, exist_ok=True)
        skill_md = skill_dir / "SKILL.md"
        shutil.copy2(md, skill_md)
        shutil.copy2(md, GEM_AGENTS / md.name)
        if (GEM_AGENTS / stem).is_dir():
            shutil.copy2(skill_md, GEM_AGENTS / stem / "SKILL.md")
        (GEM_SKILLS / stem).mkdir(parents=True, exist_ok=True)
        shutil.copy2(skill_md, GEM_SKILLS / stem / "SKILL.md")

        if not (
            sha256(md)
            == sha256(skill_md)
            == sha256(GEM_AGENTS / md.name)
            == sha256(GEM_SKILLS / stem / "SKILL.md")
        ):
            errors.append(stem)

    return len(agent_mds), errors


def check_mcps() -> list[str]:
    tpl = json.loads((REPO / "mcps" / "mcp_template.json").read_text(encoding="utf-8"))["mcpServers"]
    if not GEM_MCP.exists():
        return sorted(tpl.keys())
    gem = json.loads(GEM_MCP.read_text(encoding="utf-8"))["mcpServers"]
    return sorted(set(tpl) - set(gem))


def main() -> int:
    total_agents, agent_errors = sync_agents()
    missing_mcps = check_mcps()

    res_build = subprocess.run([sys.executable, str(REPO / "scripts" / "build_catalog.py")], check=False)
    res_check = subprocess.run([sys.executable, str(REPO / "scripts" / "build_catalog.py"), "--check"], check=False)

    print(f"Agents synced: {total_agents}, parity errors: {agent_errors}")
    print(f"Template MCPs missing in Gemini config: {missing_mcps}")

    if agent_errors or missing_mcps or res_build.returncode != 0 or res_check.returncode != 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
