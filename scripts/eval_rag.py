#!/usr/bin/env python3
"""Zero-dependency RAG precision benchmark (Hit@3 & MRR) over .cache/rag_index.db."""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import rag_search

GOLDEN_CASES: list[tuple[str, str]] = [
    ("pgvector hybrid search", "rag-architecture-patterns"),
    ("supoclip", "mcps/supoclip/README.md"),
    ("netlify deploy", "netlify-deploy"),
    ("global-master-agent", "global-master-agent"),
    ("graphify", "ai-agents/graphify/SKILL.md"),
    ("pix webhook idempotencia", "brazil-payments-pix"),
    ("ponytail anti-overengineering", "ponytail"),
    ("skills_rag_search", "mcps/skiilstoias/README.md"),
]


def evaluate_rag(
    db_path: Path, cases: list[tuple[str, str]] = GOLDEN_CASES, top_k: int = 3
) -> dict[str, float | int]:
    hits = 0
    rr_sum = 0.0
    t0 = time.perf_counter()

    for query, expected in cases:
        results = rag_search.search_index(db_path, query, top_k=top_k)
        rank_found = None
        for idx, item in enumerate(results, start=1):
            haystack = f"{item['path']} {item['section']} {item['content']}".lower()
            if expected.lower() in haystack:
                rank_found = idx
                break
        if rank_found is not None:
            hits += 1
            rr_sum += 1.0 / rank_found
        status = f"HIT@{rank_found}" if rank_found else "MISS"
        print(f"  [{status:5s}] {query!r} -> expected {expected!r}")

    elapsed_ms = round((time.perf_counter() - t0) * 1000, 1)
    total = len(cases)
    hit_rate = hits / total if total else 0.0
    mrr = rr_sum / total if total else 0.0
    return {"total": total, "hits": hits, "hit_rate": hit_rate, "mrr": mrr, "elapsed_ms": elapsed_ms}


def main() -> int:
    rag_search.configure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Benchmark SkiilsToIAs RAG Hit@3 and MRR.")
    parser.add_argument("--db", type=Path, default=rag_search.DEFAULT_DB, help="SQLite FTS5 database path")
    parser.add_argument("--min-hit-rate", type=float, default=0.75, help="Minimum Hit@3 pass threshold")
    args = parser.parse_args()

    print(f"Running RAG precision benchmark on {args.db}...")
    metrics = evaluate_rag(args.db, top_k=3)
    print(
        f"Summary: Hit@3={metrics['hits']}/{metrics['total']} ({metrics['hit_rate']:.0%}), "
        f"MRR={metrics['mrr']:.3f}, elapsed={metrics['elapsed_ms']}ms"
    )
    if metrics["hit_rate"] < args.min_hit_rate:
        print(f"FAIL: Hit@3 {metrics['hit_rate']:.2f} < {args.min_hit_rate:.2f}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
