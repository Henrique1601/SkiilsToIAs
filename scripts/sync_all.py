#!/usr/bin/env python3
"""Run catalog build, RAG index sync, repository audit, Protocol 7 mirror, and hook install."""

from __future__ import annotations

import argparse
import hashlib
import shutil
import stat
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

PRE_COMMIT_HOOK = """#!/bin/sh
set -e
python scripts/audit_repo.py
python scripts/build_catalog.py --check
"""


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_step(label: str, script_rel: str) -> int:
    print(f"\n==> [{label}] python {script_rel}")
    proc = subprocess.run([sys.executable, str(REPO_ROOT / script_rel)], cwd=REPO_ROOT)
    return proc.returncode


def mirror_protocol7(
    repo_root: Path = REPO_ROOT,
    gemini_dir: Path | None = None,
    agents_dir: Path | None = None,
) -> tuple[int, int]:
    """Mirror custom-agents/*.md and global-master-agent/SKILL.md with SHA256 verification."""
    home = Path.home()
    gemini_cfg = gemini_dir or (home / ".gemini" / "config")
    agents_cfg = agents_dir or (home / ".agents" / "custom-agents")

    target_agents = gemini_cfg / "agents"
    target_skills = gemini_cfg / "skills" / "global-master-agent"
    target_agents.mkdir(parents=True, exist_ok=True)
    agents_cfg.mkdir(parents=True, exist_ok=True)
    target_skills.mkdir(parents=True, exist_ok=True)

    copied = 0
    mismatches = 0
    for src in sorted((repo_root / "custom-agents").glob("*.md")):
        src_hash = sha256_file(src)
        for dst in (target_agents / src.name, agents_cfg / src.name):
            shutil.copy2(src, dst)
            copied += 1
            if sha256_file(dst) != src_hash:
                mismatches += 1

    skill_src = repo_root / "custom-agents" / "global-master-agent" / "SKILL.md"
    if skill_src.is_file():
        skill_dst = target_skills / "SKILL.md"
        shutil.copy2(skill_src, skill_dst)
        copied += 1
        if sha256_file(skill_dst) != sha256_file(skill_src):
            mismatches += 1

    return copied, mismatches


def install_pre_commit_hook(repo_root: Path = REPO_ROOT) -> Path:
    """Install .git/hooks/pre-commit running audit_repo.py and build_catalog.py --check."""
    hooks_dir = repo_root / ".git" / "hooks"
    if not hooks_dir.is_dir():
        raise FileNotFoundError(f"Git hooks directory not found: {hooks_dir}")
    hook_path = hooks_dir / "pre-commit"
    hook_path.write_text(PRE_COMMIT_HOOK, encoding="utf-8", newline="\n")
    try:
        mode = hook_path.stat().st_mode
        hook_path.chmod(mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    except OSError:
        pass
    return hook_path


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        description="Synchronize catalog, RAG index, repository audit, and local Protocol 7 mirrors."
    )
    parser.add_argument(
        "--skip-rag",
        action="store_true",
        help="Skip local RAG index update (useful in CI).",
    )
    parser.add_argument(
        "--mirror",
        action="store_true",
        help="Mirror custom-agents and global-master-agent/SKILL.md (Protocol 7) and verify SHA256.",
    )
    parser.add_argument(
        "--install-hook",
        action="store_true",
        help="Install local .git/hooks/pre-commit running audit_repo.py and catalog check.",
    )
    args = parser.parse_args()

    if args.install_hook:
        hook_path = install_pre_commit_hook()
        print(f"Installed pre-commit hook: {hook_path}")
        if not args.mirror and not args.skip_rag:
            # Allow --install-hook alone without forcing full sync unless requested,
            # or continue if user wants full sync? Keep consistent: run full sync too.
            pass

    if args.mirror:
        copied, mismatches = mirror_protocol7()
        print(f"Protocol 7 mirror: files_copied={copied}, mismatches={mismatches}")
        if mismatches:
            return 1

    steps = [("Catalog", "scripts/build_catalog.py")]
    if not args.skip_rag:
        steps.append(("RAG Index", "scripts/rag_index.py"))
    steps.append(("Audit", "scripts/audit_repo.py"))

    for label, script_rel in steps:
        rc = run_step(label, script_rel)
        if rc != 0:
            print(f"\nSYNC FAILED at step [{label}] (exit {rc}).")
            return rc

    print("\nSYNC COMPLETE: all steps passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
