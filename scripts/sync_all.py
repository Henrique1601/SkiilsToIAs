#!/usr/bin/env python3
"""Sync all skills, custom agents, routes, and catalog to ~/.gemini/config/ and ~/.agents/custom-agents/."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import stat
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
GEM_AGENTS = Path.home() / ".gemini" / "config" / "agents"
GEM_SKILLS = Path.home() / ".gemini" / "config" / "skills"
AGENTS_CUSTOM = Path.home() / ".agents" / "custom-agents"
GEM_MCP = Path.home() / ".gemini" / "config" / "mcp_config.json"

SKILL_CATEGORIES = (
    "ai-agents",
    "backend-database",
    "business-management",
    "career",
    "design",
    "development",
    "devops-cloud",
    "documents-productivity",
    "marketing",
    "seo",
    "utilities",
)

PRE_COMMIT_HOOK = """#!/bin/sh
set -e
python scripts/audit_repo.py
python scripts/build_catalog.py --check
"""

POST_MERGE_HOOK = """#!/bin/sh
python scripts/sync_all.py || true
"""


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sync_skills() -> tuple[int, int, list[str]]:
    """Mirror categorized skills (<cat>/<skill>/) to GEM_SKILLS/<skill>/ when missing or changed."""
    GEM_SKILLS.mkdir(parents=True, exist_ok=True)
    total = 0
    updated = 0
    errors: list[str] = []

    for cat in SKILL_CATEGORIES:
        cat_dir = REPO / cat
        if not cat_dir.is_dir():
            continue
        for skill_md in sorted(cat_dir.glob("*/SKILL.md")):
            src_dir = skill_md.parent
            dst_dir = GEM_SKILLS / src_dir.name
            dst_md = dst_dir / "SKILL.md"
            total += 1
            if dst_md.is_file() and sha256(skill_md) == sha256(dst_md):
                continue
            shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)
            updated += 1
            if not dst_md.is_file() or sha256(skill_md) != sha256(dst_md):
                errors.append(src_dir.name)

    return total, updated, errors


def sync_agents() -> tuple[int, list[str]]:
    GEM_AGENTS.mkdir(parents=True, exist_ok=True)
    GEM_SKILLS.mkdir(parents=True, exist_ok=True)
    AGENTS_CUSTOM.mkdir(parents=True, exist_ok=True)

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
        shutil.copy2(md, AGENTS_CUSTOM / md.name)
        if (GEM_AGENTS / stem).is_dir():
            shutil.copy2(skill_md, GEM_AGENTS / stem / "SKILL.md")
        (GEM_SKILLS / stem).mkdir(parents=True, exist_ok=True)
        shutil.copy2(skill_md, GEM_SKILLS / stem / "SKILL.md")

        if not (
            sha256(md)
            == sha256(skill_md)
            == sha256(GEM_AGENTS / md.name)
            == sha256(AGENTS_CUSTOM / md.name)
            == sha256(GEM_SKILLS / stem / "SKILL.md")
        ):
            errors.append(stem)

    return len(agent_mds), errors


def check_agent_routes() -> list[str]:
    """Verify every custom agent has routing references in global-master-agent and skills-orchestrator."""
    gma_path = REPO / "custom-agents" / "global-master-agent.md"
    orch_path = REPO / "custom-agents" / "skills-orchestrator.md"
    if not gma_path.is_file() or not orch_path.is_file():
        return []
    gma_text = gma_path.read_text(encoding="utf-8", errors="replace")
    orch_text = orch_path.read_text(encoding="utf-8", errors="replace")
    agent_mds = sorted(
        p.stem
        for p in (REPO / "custom-agents").glob("*.md")
        if p.name.lower() not in ("readme.md", "prompts_motion_social.md")
    )
    return [stem for stem in agent_mds if stem not in gma_text or stem not in orch_text]


def check_mcps() -> list[str]:
    tpl = json.loads((REPO / "mcps" / "mcp_template.json").read_text(encoding="utf-8"))["mcpServers"]
    if not GEM_MCP.exists():
        return sorted(tpl.keys())
    gem = json.loads(GEM_MCP.read_text(encoding="utf-8"))["mcpServers"]
    return sorted(set(tpl) - set(gem))


def install_git_hooks(repo_root: Path = REPO) -> list[Path]:
    hooks_dir = repo_root / ".git" / "hooks"
    if not hooks_dir.is_dir():
        raise FileNotFoundError(f"Git hooks directory not found: {hooks_dir}")
    installed = []
    for name, body in (("pre-commit", PRE_COMMIT_HOOK), ("post-merge", POST_MERGE_HOOK)):
        hook_path = hooks_dir / name
        hook_path.write_text(body, encoding="utf-8", newline="\n")
        try:
            mode = hook_path.stat().st_mode
            hook_path.chmod(mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        except OSError:
            pass
        installed.append(hook_path)
    return installed


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync skills, agents, routes, and catalog.")
    parser.add_argument("--install-hooks", action="store_true", help="Install pre-commit and post-merge git hooks.")
    parser.add_argument("--strict-mcps", action="store_true", help="Exit non-zero if template MCPs are missing.")
    args = parser.parse_args()

    if args.install_hooks:
        hooks = install_git_hooks()
        print(f"Installed git hooks: {[h.name for h in hooks]}")

    total_skills, updated_skills, skill_errors = sync_skills()
    total_agents, agent_errors = sync_agents()
    unrouted = check_agent_routes()
    missing_mcps = check_mcps()

    res_build = subprocess.run([sys.executable, str(REPO / "scripts" / "build_catalog.py")], check=False)
    res_check = subprocess.run([sys.executable, str(REPO / "scripts" / "build_catalog.py"), "--check"], check=False)

    print(f"Skills synced: {total_skills} (updated={updated_skills}), skill errors: {skill_errors}")
    print(f"Agents synced: {total_agents}, parity errors: {agent_errors}, unrouted: {unrouted}")
    print(f"Template MCPs missing/optional in Gemini config ({len(missing_mcps)}): {missing_mcps}")

    if skill_errors or agent_errors or unrouted or res_build.returncode != 0 or res_check.returncode != 0:
        return 1
    if args.strict_mcps and missing_mcps:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
