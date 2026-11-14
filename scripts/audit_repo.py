#!/usr/bin/env python3
"""Repository integrity, frontmatter, secret, and README link audit."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent

EXCLUDED_AGENT_DOCS = {"README.md", "PROMPTS_MOTION_SOCIAL.md"}
EXCLUDED_SECRET_FILES = {"mcps/mcp_template.json", ".env.example"}
SKIP_DIRS = {".git", "node_modules", ".cache", "__pycache__", ".venv", "venv"}
BINARY_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".svg", ".pdf",
    ".zip", ".tar", ".gz", ".exe", ".dll", ".so", ".dylib", ".woff", ".woff2",
    ".ttf", ".eot", ".mp3", ".mp4", ".webm", ".db", ".sqlite", ".pyc",
}

SECRET_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("sk_ token", re.compile(r"\bsk_[A-Za-z0-9_-]{16,}")),
    ("napi_ token", re.compile(r"\bnapi_[A-Za-z0-9_-]{12,}")),
    ("ctx7sk- token", re.compile(r"\bctx7sk-[A-Za-z0-9_-]{12,}")),
    ("Bearer token", re.compile(r"\bBearer\s+([A-Za-z0-9_.-]{20,})")),
)

PLACEHOLDER_MARKERS = (
    "SUA_CHAVE",
    "SUA_NOTION",
    "YOUR_",
    "INSERT_",
    "PASTE_",
    "PLACEHOLDER",
    "EXAMPLE",
    "TOKEN_HERE",
    "_HERE",
    "CHANGEME",
    "REPLACE_ME",
    "DUMMY",
    "TEST_KEY",
    "API_KEY",
)

FRONTMATTER_RE = re.compile(r"^---\s*\r?\n(.*?)\r?\n---(?:\s*\r?\n|$)", re.DOTALL)
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def configure_utf8() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def mask_secret(value: str) -> str:
    if len(value) <= 12:
        return value[:4] + "..."
    return f"{value[:8]}...{value[-4:]}"


def is_placeholder(token: str, line: str) -> bool:
    if token.endswith("..."):
        return True
    upper = token.upper()
    if any(marker in upper for marker in PLACEHOLDER_MARKERS):
        return True
    if len(set(token)) <= 3:
        return True
    idx = line.find(token)
    if idx != -1 and line[idx + len(token):].startswith("..."):
        return True
    return False


def has_yaml_field(fm: str, key: str) -> bool:
    pattern = re.compile(rf"^{re.escape(key)}\s*:\s*(.*)$", re.MULTILINE)
    match = pattern.search(fm)
    if not match:
        return False
    val = match.group(1).strip()
    if val and val not in ('""', "''", "|", ">", "|-", ">-"):
        return True
    if val in ("|", ">", "|-", ">-"):
        after = fm[match.end():].splitlines()
        for next_line in after[1:]:
            if not next_line.strip():
                continue
            return next_line.startswith((" ", "\t"))
    return False


def get_tracked_files(root: Path) -> list[Path]:
    try:
        raw = subprocess.check_output(
            ["git", "ls-files", "-z"],
            cwd=root,
            stderr=subprocess.DEVNULL,
        )
        paths = [root / p for p in raw.decode("utf-8", errors="replace").split("\0") if p]
        if paths:
            return paths
    except (subprocess.SubprocessError, OSError):
        pass

    result: list[Path] = []
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file():
            result.append(path)
    return result


def check_agents(root: Path) -> tuple[int, list[str]]:
    agents_dir = root / "custom-agents"
    if not agents_dir.is_dir():
        return 0, ["custom-agents/ directory not found"]

    agent_files = sorted(
        p for p in agents_dir.glob("*.md") if p.name not in EXCLUDED_AGENT_DOCS
    )
    errors: list[str] = []
    for md_file in agent_files:
        skill_md = agents_dir / md_file.stem / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"Missing SKILL.md for agent: custom-agents/{md_file.name}")
        elif skill_md.stat().st_size == 0:
            errors.append(f"Empty SKILL.md for agent: custom-agents/{md_file.stem}/SKILL.md")
    return len(agent_files), errors


def check_skills(root: Path) -> tuple[int, list[str]]:
    skill_files = sorted(
        p for p in root.rglob("SKILL.md")
        if not any(part in SKIP_DIRS for part in p.parts)
    )
    warnings: list[str] = []
    for skill_path in skill_files:
        rel = skill_path.relative_to(root).as_posix()
        try:
            text = skill_path.read_text(encoding="utf-8-sig", errors="replace")
        except OSError as exc:
            warnings.append(f"{rel}: unable to read ({exc})")
            continue

        match = FRONTMATTER_RE.match(text)
        if not match:
            warnings.append(f"{rel}: missing YAML frontmatter")
            continue

        fm = match.group(1)
        if not fm.strip():
            warnings.append(f"{rel}: empty YAML frontmatter")
            continue

        missing = [k for k in ("name", "description") if not has_yaml_field(fm, k)]
        if missing:
            warnings.append(f"{rel}: frontmatter missing {', '.join(missing)}")
    return len(skill_files), warnings


def check_secrets(root: Path, tracked_files: list[Path]) -> list[str]:
    findings: list[str] = []
    for file_path in tracked_files:
        if not file_path.is_file():
            continue
        rel = file_path.relative_to(root).as_posix()
        if rel in EXCLUDED_SECRET_FILES or file_path.suffix.lower() in BINARY_EXTS:
            continue
        try:
            raw = file_path.read_bytes()
        except OSError:
            continue
        if b"\x00" in raw[:4096]:
            continue

        text = raw.decode("utf-8", errors="replace")
        for line_no, line in enumerate(text.splitlines(), 1):
            for label, pattern in SECRET_PATTERNS:
                for match in pattern.finditer(line):
                    token = match.group(1) if match.lastindex else match.group(0)
                    if is_placeholder(token, line):
                        continue
                    findings.append(f"{rel}:{line_no} [{label}] {mask_secret(token)}")
    return findings


def check_readme_links(root: Path) -> tuple[int, list[str]]:
    readme = root / "README.md"
    if not readme.is_file():
        return 0, ["README.md not found"]

    text = readme.read_text(encoding="utf-8", errors="replace")
    checked = 0
    broken: list[str] = []
    in_fence = False

    for line_no, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        for match in LINK_RE.finditer(line):
            raw_target = match.group(1).strip()
            if not raw_target:
                continue
            target = raw_target.split()[0].strip("<>")
            if target.startswith(("#", "http://", "https://", "mailto:", "tel:", "data:")):
                continue
            path_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not path_part:
                continue
            checked += 1
            if not (root / path_part).exists():
                broken.append(f"README.md:{line_no} -> {target}")
    return checked, broken


def main() -> int:
    configure_utf8()
    parser = argparse.ArgumentParser(description="Audit SkiilsToIAs repository health.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Also exit non-zero on frontmatter or README link warnings.",
    )
    args = parser.parse_args()

    tracked = get_tracked_files(ROOT)
    agent_count, agent_errors = check_agents(ROOT)
    skill_count, skill_warnings = check_skills(ROOT)
    secret_hits = check_secrets(ROOT, tracked)
    link_count, broken_links = check_readme_links(ROOT)

    print(f"[agents] checked={agent_count}, missing_or_empty={len(agent_errors)}")
    for err in agent_errors:
        print(f"  ERROR: {err}")

    print(f"[skills] checked={skill_count}, warnings={len(skill_warnings)}")
    for warn in skill_warnings[:20]:
        print(f"  WARN:  {warn}")
    if len(skill_warnings) > 20:
        print(f"  ... and {len(skill_warnings) - 20} more warnings")

    print(f"[secrets] scanned_files={len(tracked)}, findings={len(secret_hits)}")
    for hit in secret_hits:
        print(f"  ERROR: {hit}")

    print(f"[readme] relative_links_checked={link_count}, broken={len(broken_links)}")
    for broken in broken_links[:20]:
        print(f"  WARN:  {broken}")
    if len(broken_links) > 20:
        print(f"  ... and {len(broken_links) - 20} more broken links")

    critical_count = len(agent_errors) + len(secret_hits)
    warning_count = len(skill_warnings) + len(broken_links)

    if critical_count > 0:
        print(f"\nAUDIT FAILED: {critical_count} critical error(s), {warning_count} warning(s).")
        return 1
    if args.strict and warning_count > 0:
        print(f"\nAUDIT FAILED (--strict): {warning_count} warning(s).")
        return 1

    print(f"\nAUDIT PASSED: 0 critical errors, {warning_count} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
