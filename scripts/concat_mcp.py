#!/usr/bin/env python3
"""Zero-dependency Stdio MCP bridge for Concat video editor TCP JSON-RPC daemon."""

from __future__ import annotations

import json
import os
import socket
import sys
from typing import Any

SERVER_INFO = {"name": "concat-mcp", "version": "0.2.9"}
PROTOCOL_VERSION = "2024-11-05"

CONCAT_METHODS = (
    "version",
    "project.create",
    "project.open",
    "project.close",
    "project.list",
    "project.get",
    "project.document",
    "project.save",
    "project.setVideo",
    "edit.apply",
    "edit.undo",
    "edit.redo",
    "media.probe",
    "media.import",
    "catalogue.list",
    "template.list",
    "template.instantiate",
    "template.save",
    "export.run",
    "export.cancel",
    "export.status",
    "preview.frame",
)

TOOLS: list[dict[str, Any]] = [
    {
        "name": "concat_call",
        "description": "Call any Concat video editor JSON-RPC method (project.*, edit.*, media.*, template.*, export.*, catalogue.list, preview.frame, version).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "method": {"type": "string", "enum": list(CONCAT_METHODS)},
                "params": {"type": "object", "default": {}},
            },
            "required": ["method"],
        },
    },
    {
        "name": "concat_version",
        "description": "Get Concat editor version, API version, and capabilities.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "concat_project_list",
        "description": "List recent/open projects in Concat video editor.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "concat_project_get",
        "description": "Get active project details and document state in Concat.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "concat_edit_apply",
        "description": "Apply timeline edit operations in Concat.",
        "inputSchema": {
            "type": "object",
            "properties": {"params": {"type": "object", "default": {}}},
            "required": ["params"],
        },
    },
    {
        "name": "concat_export_run",
        "description": "Start a video export job in Concat.",
        "inputSchema": {
            "type": "object",
            "properties": {"params": {"type": "object", "default": {}}},
        },
    },
]


def call_concat_rpc(
    method: str,
    params: dict[str, Any] | None = None,
    host: str | None = None,
    port: int | None = None,
    token: str | None = None,
    timeout: float = 5.0,
) -> Any:
    if method not in CONCAT_METHODS:
        raise ValueError(f"Unsupported Concat RPC method: {method}")
    target_host = host or os.environ.get("CONCAT_HOST", "127.0.0.1").strip() or "127.0.0.1"
    target_port = port or int(os.environ.get("CONCAT_PORT", "7420"))
    auth_token = token if token is not None else os.environ.get("CONCAT_TOKEN", "").strip()
    if not auth_token:
        raise RuntimeError("CONCAT_TOKEN environment variable is required.")

    with socket.create_connection((target_host, target_port), timeout=timeout) as sock:
        reader = sock.makefile("r", encoding="utf-8", errors="replace")
        auth_req = {"jsonrpc": "2.0", "id": 1, "method": "auth", "params": {"token": auth_token}}
        sock.sendall((json.dumps(auth_req) + "\n").encode("utf-8"))
        auth_resp = json.loads(reader.readline() or "{}")
        if "error" in auth_resp:
            raise RuntimeError(f"Concat auth failed: {auth_resp['error']}")

        rpc_req = {"jsonrpc": "2.0", "id": 2, "method": method, "params": params or {}}
        sock.sendall((json.dumps(rpc_req) + "\n").encode("utf-8"))
        rpc_resp = json.loads(reader.readline() or "{}")
        if "error" in rpc_resp:
            raise RuntimeError(f"Concat RPC error: {rpc_resp['error']}")
        return rpc_resp.get("result")


def execute_tool(name: str, args: dict[str, Any]) -> Any:
    if name == "concat_call":
        return call_concat_rpc(str(args["method"]), args.get("params") or {})
    if name == "concat_version":
        return call_concat_rpc("version")
    if name == "concat_project_list":
        return call_concat_rpc("project.list")
    if name == "concat_project_get":
        return call_concat_rpc("project.get")
    if name == "concat_edit_apply":
        return call_concat_rpc("edit.apply", args.get("params") or {})
    if name == "concat_export_run":
        return call_concat_rpc("export.run", args.get("params") or {})
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
            payload = execute_tool(params.get("name", ""), params.get("arguments") or {})
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
