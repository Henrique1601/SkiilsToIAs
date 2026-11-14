#!/usr/bin/env python3
"""Run catalog build, RAG index sync, and repository audit in sequence."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def run_step(label: str, script_rel: str) -> int:
    print(f"\n==> [{label}] python {script_rel}")
    proc = subprocess.run([sys.executable, str(REPO_ROOT / script_rel)], cwd=REPO_ROOT)
    return proc.returncode


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        description="Synchronize catalog, RAG index, and repository audit."
    )
    parser.add_argument(
        "--skip-rag",
        action="store_true",
        help="Skip local RAG index update (useful in CI).",
    )
    args = parser.parse_args()

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
