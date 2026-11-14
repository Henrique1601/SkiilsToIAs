#!/usr/bin/env python3
"""Zero-dependency MCP server health checker.

Reads an Antigravity / Gemini ``mcp_config.json`` file, probes ``serverUrl``
endpoints (HTTP JSON-RPC ``initialize`` with 3s timeout), and verifies
``command`` executables and local script paths on disk.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import shutil
import socket
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

DEFAULT_CONFIG_PATH = Path(r"C:\Users\henri\.gemini\config\mcp_config.json")
DEFAULT_TIMEOUT = 3.0

STATUS_OK = "OK"
STATUS_OFFLINE_LOCAL = "OFFLINE/LOCAL_APP_CLOSED"
STATUS_MISSING_BIN = "MISSING_BIN"
STATUS_ERROR = "ERROR"

LOCAL_HOSTS = {"127.0.0.1", "localhost", "::1", "0.0.0.0"}
SCRIPT_EXTENSIONS = {
    ".js", ".mjs", ".cjs", ".ts", ".mts", ".cts",
    ".py", ".sh", ".ps1", ".bat", ".cmd", ".exe",
    ".jar", ".rb", ".php",
}
INTERPRETER_COMMANDS = {
    "node", "nodejs", "python", "python3", "py",
    "ts-node", "tsx", "bun", "deno", "ruby", "php",
    "bash", "sh", "pwsh", "powershell",
}
WINDOWS_ABS_RE = re.compile(r"^[A-Za-z]:[/\\]")
BEARER_RE = re.compile(r"(Bearer\s+)[^\s\"',}]+", re.IGNORECASE)
TOKEN_PREFIX_RE = re.compile(
    r"\b(sk_[A-Za-z0-9_-]{8,}|napi_[A-Za-z0-9_-]{8,}|ctx7sk-[A-Za-z0-9_-]{8,}|"
    r"ntn_[A-Za-z0-9_-]{8,}|pplx-[A-Za-z0-9_-]{8,}|nfp_[A-Za-z0-9_-]{8,}|"
    r"github_pat_[A-Za-z0-9_]{12,}|ghp_[A-Za-z0-9]{12,})"
)


@dataclass
class ServerResult:
    name: str
    kind: str
    status: str
    target: str
    latency_ms: int | None
    detail: str
    disabled: bool = False


def _configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except OSError:
                pass


def _collect_secrets(cfg: dict[str, Any]) -> list[str]:
    secrets: list[str] = []
    for section in ("headers", "env"):
        mapping = cfg.get(section)
        if isinstance(mapping, dict):
            for val in mapping.values():
                if isinstance(val, str) and len(val) >= 8:
                    secrets.append(val)
                    if val.lower().startswith("bearer "):
                        token = val.split(None, 1)[1].strip()
                        if len(token) >= 6:
                            secrets.append(token)
    return secrets


def mask_secrets(text: str, extra_secrets: list[str] | None = None) -> str:
    """Redact tokens, Bearer headers, and configured secret values."""
    if not text:
        return text
    masked = text
    if extra_secrets:
        for secret in sorted(set(extra_secrets), key=len, reverse=True):
            if secret and secret in masked:
                masked = masked.replace(secret, "***REDACTED***")
    masked = BEARER_RE.sub(r"\1***REDACTED***", masked)
    masked = TOKEN_PREFIX_RE.sub("***REDACTED***", masked)
    return masked


def mask_url(raw_url: str) -> str:
    """Strip credentials and sensitive query parameters from a URL for display."""
    try:
        parsed = urllib.parse.urlparse(raw_url)
    except ValueError:
        return "<invalid-url>"
    netloc = parsed.netloc
    if "@" in netloc:
        _, hostpart = netloc.rsplit("@", 1)
        netloc = f"***@{hostpart}"
    query = ""
    if parsed.query:
        params = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
        redacted = [
            (k, "***" if any(s in k.lower() for s in ("key", "token", "secret", "auth", "pass")) else v)
            for k, v in params
        ]
        query = urllib.parse.urlencode(redacted)
    return urllib.parse.urlunparse((parsed.scheme, netloc, parsed.path, parsed.params, query, ""))


def _is_local_url(url: str) -> bool:
    try:
        host = (urllib.parse.urlparse(url).hostname or "").lower()
    except ValueError:
        return False
    return host in LOCAL_HOSTS


def _extract_script_paths(command: str, args: list[Any]) -> list[str]:
    cmd_base = Path(command).stem.lower()
    is_interpreter = cmd_base in INTERPRETER_COMMANDS
    paths: list[str] = []
    first_positional_seen = False

    for raw_arg in args:
        if not isinstance(raw_arg, str) or not raw_arg:
            continue
        arg = raw_arg.strip()
        if arg.startswith("-"):
            continue
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", arg):
            continue

        looks_like_path = bool(
            WINDOWS_ABS_RE.match(arg)
            or arg.startswith(("\\\\", "./", ".\\", "../", "..\\", "~/"))
            or (arg.startswith("/") and not arg.startswith("//"))
            or Path(arg).suffix.lower() in SCRIPT_EXTENSIONS
        )

        if looks_like_path:
            paths.append(arg)
            first_positional_seen = True
        elif is_interpreter and not first_positional_seen:
            first_positional_seen = True
            if "/" in arg or "\\" in arg:
                paths.append(arg)

    return paths


def _probe_http(url: str, headers: dict[str, str], timeout: float) -> tuple[str, str]:
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "mcp-health", "version": "1.0.0"},
        },
    }).encode("utf-8")

    req_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "User-Agent": "mcp-health/1.0",
    }
    for k, v in headers.items():
        if isinstance(k, str) and isinstance(v, str):
            req_headers[k] = v

    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, data=payload, headers=req_headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return STATUS_OK, f"HTTP {resp.status} (initialize)"
    except urllib.error.HTTPError as exc:
        if exc.code in (200, 202, 204):
            return STATUS_OK, f"HTTP {exc.code}"
        if exc.code in (401, 403):
            return STATUS_OK, f"HTTP {exc.code} (reachable, auth required)"
        if exc.code in (405, 406):
            get_req = urllib.request.Request(
                url,
                headers={k: v for k, v in req_headers.items() if k.lower() != "content-type"},
                method="GET",
            )
            try:
                with urllib.request.urlopen(get_req, timeout=timeout, context=ctx) as get_resp:
                    return STATUS_OK, f"HTTP {get_resp.status} (GET)"
            except urllib.error.HTTPError as get_exc:
                if get_exc.code in (401, 403):
                    return STATUS_OK, f"HTTP {get_exc.code} (reachable, auth required)"
                if get_exc.code < 500:
                    return STATUS_OK, f"HTTP {get_exc.code} (reachable)"
                return STATUS_ERROR, f"HTTP {get_exc.code}"
            except (urllib.error.URLError, OSError, TimeoutError) as get_err:
                return _classify_network_error(url, get_err, timeout)
        return STATUS_ERROR, f"HTTP {exc.code}"
    except (urllib.error.URLError, OSError, TimeoutError, ssl.SSLError) as exc:
        return _classify_network_error(url, exc, timeout)


def _classify_network_error(url: str, exc: BaseException, timeout: float) -> tuple[str, str]:
    reason = getattr(exc, "reason", exc)
    is_local = _is_local_url(url)

    if isinstance(reason, (TimeoutError, socket.timeout)) or "timed out" in str(reason).lower():
        if is_local:
            return STATUS_OFFLINE_LOCAL, f"local endpoint timeout ({timeout:.1f}s)"
        return STATUS_ERROR, f"timeout ({timeout:.1f}s)"

    if isinstance(reason, ConnectionRefusedError) or "10061" in str(reason) or "refused" in str(reason).lower():
        if is_local:
            return STATUS_OFFLINE_LOCAL, "connection refused (local app closed)"
        return STATUS_ERROR, "connection refused"

    if is_local:
        return STATUS_OFFLINE_LOCAL, f"local endpoint unreachable ({type(reason).__name__})"
    return STATUS_ERROR, str(reason)


def check_server(name: str, cfg: dict[str, Any], timeout: float) -> ServerResult:
    disabled = bool(cfg.get("disabled", False))
    secrets = _collect_secrets(cfg)
    suffix = " [disabled]" if disabled else ""

    server_url = cfg.get("serverUrl") or cfg.get("url")
    if isinstance(server_url, str) and server_url.strip():
        clean_url = mask_url(server_url.strip())
        headers = cfg.get("headers") if isinstance(cfg.get("headers"), dict) else {}
        t0 = time.perf_counter()
        status, detail = _probe_http(server_url.strip(), headers, timeout)
        elapsed_ms = int((time.perf_counter() - t0) * 1000)
        return ServerResult(
            name=name,
            kind="http",
            status=status,
            target=mask_secrets(clean_url, secrets),
            latency_ms=elapsed_ms,
            detail=mask_secrets(detail, secrets) + suffix,
            disabled=disabled,
        )

    command = cfg.get("command")
    if isinstance(command, str) and command.strip():
        cmd = command.strip()
        args = cfg.get("args") if isinstance(cfg.get("args"), list) else []
        t0 = time.perf_counter()
        resolved = shutil.which(cmd)
        if not resolved:
            elapsed_ms = int((time.perf_counter() - t0) * 1000)
            return ServerResult(
                name=name,
                kind="command",
                status=STATUS_MISSING_BIN,
                target=cmd,
                latency_ms=elapsed_ms,
                detail=f"'{cmd}' not found in PATH{suffix}",
                disabled=disabled,
            )

        script_paths = _extract_script_paths(cmd, args)
        missing_paths = [p for p in script_paths if not Path(os.path.expanduser(p)).exists()]
        elapsed_ms = int((time.perf_counter() - t0) * 1000)

        if missing_paths:
            missing_str = ", ".join(missing_paths)
            return ServerResult(
                name=name,
                kind="command",
                status=STATUS_ERROR,
                target=cmd,
                latency_ms=elapsed_ms,
                detail=mask_secrets(f"missing script: {missing_str}", secrets) + suffix,
                disabled=disabled,
            )

        detail = f"bin={Path(resolved).name}"
        if script_paths:
            detail += f", scripts={len(script_paths)} ok"
        return ServerResult(
            name=name,
            kind="command",
            status=STATUS_OK,
            target=cmd,
            latency_ms=elapsed_ms,
            detail=detail + suffix,
            disabled=disabled,
        )

    return ServerResult(
        name=name,
        kind="unknown",
        status=STATUS_ERROR,
        target="-",
        latency_ms=None,
        detail=f"missing 'serverUrl' or 'command'{suffix}",
        disabled=disabled,
    )


def format_table(results: list[ServerResult]) -> str:
    headers = ("SERVER", "TYPE", "STATUS", "LATENCY", "TARGET", "DETAIL")
    rows = [
        (
            r.name,
            r.kind,
            r.status,
            f"{r.latency_ms}ms" if r.latency_ms is not None else "-",
            r.target,
            r.detail,
        )
        for r in results
    ]

    widths = [len(h) for h in headers]
    for row in rows:
        for idx, cell in enumerate(row):
            widths[idx] = max(widths[idx], len(cell))

    # Cap target/detail display width to keep terminal output readable
    widths[4] = min(widths[4], 48)
    widths[5] = min(widths[5], 54)

    def _fmt(row: tuple[str, ...]) -> str:
        parts = []
        for idx, cell in enumerate(row):
            val = cell if len(cell) <= widths[idx] else cell[: widths[idx] - 3] + "..."
            parts.append(val.ljust(widths[idx]))
        return "  ".join(parts)

    lines = [_fmt(headers), "  ".join("-" * w for w in widths)]
    lines.extend(_fmt(row) for row in rows)

    counts: dict[str, int] = {}
    for r in results:
        counts[r.status] = counts.get(r.status, 0) + 1
    summary_parts = [f"{k}={v}" for k, v in counts.items()]
    lines.append("")
    lines.append(f"Total: {len(results)} | " + ", ".join(summary_parts))
    return "\n".join(lines)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check health of configured MCP servers.")
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help=f"Path to mcp_config.json (default: {DEFAULT_CONFIG_PATH})",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT,
        help=f"HTTP probe timeout in seconds (default: {DEFAULT_TIMEOUT})",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with code 1 if any server is not OK.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    _configure_stdio()
    args = parse_args(argv)

    if not args.config.exists():
        err = {"error": f"Config file not found: {args.config}"}
        if args.json:
            print(json.dumps(err, indent=2))
        else:
            print(err["error"], file=sys.stderr)
        return 2

    try:
        raw = json.loads(args.config.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        err = {"error": f"Failed to read config: {exc}"}
        if args.json:
            print(json.dumps(err, indent=2))
        else:
            print(err["error"], file=sys.stderr)
        return 2

    servers = raw.get("mcpServers")
    if not isinstance(servers, dict):
        err = {"error": "Invalid config: missing 'mcpServers' object"}
        if args.json:
            print(json.dumps(err, indent=2))
        else:
            print(err["error"], file=sys.stderr)
        return 2

    items = [(name, cfg if isinstance(cfg, dict) else {}) for name, cfg in servers.items()]
    results: list[ServerResult | None] = [None] * len(items)

    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        future_map = {
            pool.submit(check_server, name, cfg, args.timeout): idx
            for idx, (name, cfg) in enumerate(items)
        }
        for future in concurrent.futures.as_completed(future_map):
            idx = future_map[future]
            name = items[idx][0]
            try:
                results[idx] = future.result()
            except Exception as exc:  # pragma: no cover - defensive fallback
                results[idx] = ServerResult(
                    name=name,
                    kind="unknown",
                    status=STATUS_ERROR,
                    target="-",
                    latency_ms=None,
                    detail=mask_secrets(str(exc)),
                )

    final_results = [r for r in results if r is not None]

    if args.json:
        counts: dict[str, int] = {}
        for r in final_results:
            counts[r.status] = counts.get(r.status, 0) + 1
        payload = {
            "config": str(args.config),
            "total": len(final_results),
            "summary": counts,
            "servers": [asdict(r) for r in final_results],
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(format_table(final_results))

    if args.strict and any(r.status != STATUS_OK for r in final_results):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
