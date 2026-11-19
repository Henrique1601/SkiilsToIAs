#!/usr/bin/env python3
"""Structured JSONL step logger for job-copilot-agent runs (Dashboard Web ready)."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def get_runs_dir() -> Path:
    runs_dir = Path.home() / ".gemini" / "job-copilot" / "runs"
    runs_dir.mkdir(parents=True, exist_ok=True)
    return runs_dir


def log_event(args: argparse.Namespace) -> Path:
    now = datetime.now(timezone.utc)
    log_file = get_runs_dir() / f"{now.strftime('%Y-%m-%d')}.jsonl"
    entry = {
        "timestamp": now.isoformat(),
        "job_title": args.title,
        "company": args.company,
        "platform": args.platform,
        "track": args.track,
        "language": args.lang,
        "work_model": args.model,
        "match_score": args.score,
        "step": args.step,
        "status": args.status,
        "job_url": args.url,
        "screenshot_path": args.screenshot or "",
        "error_reason": args.error or "",
    }
    with log_file.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return log_file


def show_summary(date_str: str | None) -> None:
    target = date_str or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log_file = get_runs_dir() / f"{target}.jsonl"
    if not log_file.exists():
        print(f"No runs logged for {target} ({log_file}).")
        return
    events = [json.loads(line) for line in log_file.read_text(encoding="utf-8").splitlines() if line.strip()]
    print(f"Runs for {target}: {len(events)} event(s)")
    for ev in events:
        print(f"- [{ev['status']}] {ev['job_title']} @ {ev['company']} ({ev['platform']} | {ev['track']} | {ev['match_score']}%)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Job Copilot structured run logger")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_log = sub.add_parser("log", help="Append a job pipeline event")
    p_log.add_argument("--title", required=True)
    p_log.add_argument("--company", required=True)
    p_log.add_argument("--platform", required=True)
    p_log.add_argument("--track", required=True, choices=["Full-Stack", "Front-End", "Back-End", "AI Engineer"])
    p_log.add_argument("--lang", default="PT-BR", choices=["PT-BR", "PT-PT", "EN"])
    p_log.add_argument("--model", default="Remoto", choices=["Remoto", "Híbrido", "Presencial"])
    p_log.add_argument("--score", type=int, default=0)
    p_log.add_argument("--step", required=True)
    p_log.add_argument("--status", required=True)
    p_log.add_argument("--url", required=True)
    p_log.add_argument("--screenshot", default="")
    p_log.add_argument("--error", default="")

    p_sum = sub.add_parser("summary", help="Show summary for a date (YYYY-MM-DD)")
    p_sum.add_argument("--date", default=None)

    args = parser.parse_args()
    if args.cmd == "log":
        path = log_event(args)
        print(f"Logged event to {path}")
    elif args.cmd == "summary":
        show_summary(args.date)


if __name__ == "__main__":
    main()
