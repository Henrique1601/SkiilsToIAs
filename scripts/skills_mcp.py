#!/usr/bin/env python3
"""Zero-dependency stdio MCP server exposing SkiilsToIAs RAG, Catalog, Bootstrap, and Healthcheck."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import mcp_health
import rag_search

SERVER_INFO = {"name": "skiilstoias-mcp", "version": "1.1.0"}
PROTOCOL_VERSION = "2024-11-05"

TOOLS: list[dict[str, Any]] = [
    {
        "name": "skills_rag_search",
        "description": "Search the local SkiilsToIAs SQLite FTS5/BM25 RAG index across skills, agents, MCPs, and brain docs.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query text"},
                "top_k": {"type": "integer", "default": 5, "minimum": 1, "maximum": 20},
                "doc_type": {"type": "string", "enum": ["skill", "agent", "mcp", "brain"]},
            },
            "required": ["query"],
        },
    },
    {
        "name": "skills_catalog_lookup",
        "description": "Filter and search items in docs/catalog/catalog.json by query, type, or category.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "default": ""},
                "item_type": {"type": "string", "enum": ["skill", "agent", "mcp"]},
                "category": {"type": "string"},
                "limit": {"type": "integer", "default": 15, "minimum": 1, "maximum": 50},
            },
        },
    },
    {
        "name": "skills_mcp_health",
        "description": "Run masked healthchecks across configured MCP servers in mcp_config.json.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "timeout": {"type": "number", "default": 3.0},
            },
        },
    },
    {
        "name": "skills_bootstrap_project",
        "description": "Scaffold a Padrao Ouro project structure (defaults to dry_run=true for safety).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "project_type": {"type": "string", "enum": ["web", "desktop", "lib"], "default": "web"},
                "out_dir": {"type": "string"},
                "dry_run": {"type": "boolean", "default": True},
            },
            "required": ["name", "out_dir"],
        },
    },
]


def catalog_lookup(
    query: str = "",
    item_type: str | None = None,
    category: str | None = None,
    limit: int = 15,
    catalog_path: Path | None = None,
) -> dict[str, Any]:
    path = catalog_path or (REPO_ROOT / "docs" / "catalog" / "catalog.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    q = query.strip().lower()
    matches = []
    for item in data.get("items", []):
        if item_type and item.get("type") != item_type:
            continue
        if category and item.get("category") != category:
            continue
        if q and q not in item.get("name", "").lower() and q not in item.get("description", "").lower():
            continue
        matches.append(item)
        if len(matches) >= limit:
            break
    return {"counts": data.get("counts", {}), "matched": len(matches), "items": matches}


def execute_tool(name: str, args: dict[str, Any]) -> Any:
    if name == "skills_rag_search":
        db = REPO_ROOT / ".cache" / "rag_index.db"
        return rag_search.search_index(
            db,
            str(args["query"]),
            top_k=max(1, min(20, int(args.get("top_k", 5)))),
            doc_type=args.get("doc_type"),
        )
    if name == "skills_catalog_lookup":
        return catalog_lookup(
            query=str(args.get("query", "")),
            item_type=args.get("item_type"),
            category=args.get("category"),
            limit=max(1, min(50, int(args.get("limit", 15)))),
        )
    if name == "skills_mcp_health":
        timeout = float(args.get("timeout", 3.0))
        cfg_path = mcp_health.DEFAULT_CONFIG_PATH
        raw = json.loads(cfg_path.read_text(encoding="utf-8"))
        servers = raw.get("mcpServers", {})
        results = [mcp_health.check_server(k, v, timeout) for k, v in servers.items()]
        return [
            {"name": r.name, "type": r.transport, "status": r.status, "latency_ms": r.latency_ms, "detail": r.detail}
            for r in results
        ]
    if name == "skills_bootstrap_project":
        cmd = [
            sys.executable,
            str(SCRIPTS_DIR / "bootstrap_project.py"),
            "--name",
            str(args["name"]),
            "--type",
            str(args.get("project_type", "web")),
            "--out",
            str(args["out_dir"]),
        ]
        if args.get("dry_run", True):
            cmd.append("--dry-run")
        proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=True)
        return {"returncode": proc.returncode, "output": proc.stdout.strip()}
    raise KeyError(f"Unknown tool: {name}")


def handle_request(req: dict[str, Any]) -> dict[str, Any] | None:
    req_id = req.get("id")
    method = req.get("method", "")
    params = req.get("params") or {}

    if method == "notifications/initialized" or req_id is None:
        return None

    try:
        if method == "initialize":
            result: Any = {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {}},
                "serverInfo": SERVER_INFO,
            }
        elif method == "tools/list":
            result = {"tools": TOOLS}
        elif method == "tools/call":
            tool_name = params.get("name", "")
            tool_args = params.get("arguments") or {}
            payload = execute_tool(tool_name, tool_args)
            result = {
                "content": [{"type": "text", "text": json.dumps(payload, indent=2, ensure_ascii=False)}],
                "isError": False,
            }
        elif method == "ping":
            result = {}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method not found: {method}"}}
        return {"jsonrpc": "2.0", "id": req_id, "result": result}
    except Exception as exc:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"content": [{"type": "text", "text": f"Error: {exc}"}], "isError": True},
        }


def main() -> int:
    if hasattr(sys.stdin, "reconfigure"):
        sys.stdin.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    for line in sys.stdin:
        raw = line.strip()
        if not raw:
            continue
        try:
            req = json.loads(raw)
        except json.JSONDecodeError as exc:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(exc)}}) + "\n")
            sys.stdout.flush()
            continue

        resp = handle_request(req)
        if resp is not None:
            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
