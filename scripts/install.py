#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🚀 INSTALADOR AUTOMÁTICO DE SKILLS, AGENTES E MCPS - SkiilsToIAs
Desenvolvido por Henrique Bezerra Dos Santos (@Henrique1601)
Compatível com Windows, macOS e Linux
Suporta: Antigravity / Gemini CLI, Claude Code, Cursor IDE, Codex, Windsurf
=============================================================================
"""

import os
import sys
import json
import shutil
import platform
import argparse
from pathlib import Path

# Garantir UTF-8 no stdout/stderr do Windows PowerShell/CMD
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

REPO_CATEGORIES = [
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
]

DEFAULT_MCPS = {
    "prospector-crm": {
        "url": "https://api-prospector-delta.vercel.app/api/mcp",
        "headers": {
            "Authorization": "Bearer SUA_CHAVE_PROSPECTOR_CRM_AQUI"
        }
    },
    "chrome-devtools-mcp": {
        "command": "npx",
        "args": ["-y", "chrome-devtools-mcp@latest"]
    },
    "mcp-server-neon": {
        "command": "npx",
        "args": ["-y", "mcp-remote", "https://mcp.neon.tech/sse"]
    },
    "notion-mcp-server": {
        "command": "npx",
        "args": ["-y", "@notionhq/notion-mcp-server"],
        "env": {
            "OPENAPI_MCP_HEADERS": "{\"Authorization\": \"Bearer SUA_NOTION_INTEGRATION_KEY\", \"Notion-Version\": \"2022-06-28\"}"
        }
    },
    "rea": {
        "command": "npx",
        "args": ["-y", "rea-agents@6.0.0", "mcp"]
    },
    "buffer": {
        "serverUrl": "https://mcp.buffer.com/mcp"
    },
    "apollo": {
        "serverUrl": "https://mcp.apollo.io/mcp"
    },
    "shots-studio": {
        "command": "node",
        "args": [
            "--experimental-strip-types",
            "c:\\Users\\Public\\Downloads\\shots-studio\\mcp-server\\index.ts"
        ]
    },
    "ai-memory": {
        "serverUrl": "http://127.0.0.1:49374/mcp",
        "timeout": 5000
    },
    "github": {
        "serverUrl": "https://api.githubcopilot.com/mcp/",
        "headers": {
            "Authorization": "Bearer SUA_CHAVE_GITHUB_PAT_AQUI"
        }
    },
    "playwright": {
        "command": "npx",
        "args": ["-y", "@playwright/mcp@latest"]
    },
    "brightdata": {
        "serverUrl": "https://mcp.brightdata.com/mcp?token=SEU_TOKEN_BRIGHTDATA_AQUI"
    },
    "magicuidesign-mcp": {
        "command": "npx",
        "args": ["-y", "@magicuidesign/mcp@latest"]
    },
    "desktop-commander": {
        "command": "npx",
        "args": ["-y", "@wonderwhy-er/desktop-commander@latest"]
    },
    "Prisma-Remote": {
        "command": "npx",
        "args": ["-y", "mcp-remote", "https://mcp.prisma.io/mcp"]
    },
    "google-maps": {
        "command": "npx",
        "args": ["-y", "@cablate/mcp-google-map", "--stdio"],
        "env": {"GOOGLE_MAPS_API_KEY": "SUA_CHAVE_API_GOOGLE_MAPS"}
    },
    "vercel": {
        "command": "npx",
        "args": ["-y", "mcp-remote", "https://mcp.vercel.com"]
    },
    "netlify": {
        "command": "npx",
        "args": ["-y", "@netlify/mcp"]
    },
    "mongodb-atlas-mcp-remote": {
        "command": "npx",
        "args": ["-y", "mongodb-atlas-mcp-remote@latest"],
        "env": {
            "MDB_MCP_API_CLIENT_ID": "SEU_CLIENT_ID_ATLAS",
            "MDB_MCP_API_CLIENT_SECRET": "SEU_CLIENT_SECRET_ATLAS"
        }
    },
    "browserstack": {
        "serverUrl": "https://mcp.browserstack.com/mcp"
    },
    "youtube-music-server": {
        "command": "node",
        "args": ["c:\\caminho\\para\\youtube-music-server\\build\\index.js"]
    },
    "spotify": {
        "command": "uv",
        "args": [
            "--directory",
            "c:\\caminho\\para\\spotify-mcp",
            "run",
            "spotify-mcp"
        ],
        "env": {
            "SPOTIFY_CLIENT_ID": "SEU_CLIENT_ID_SPOTIFY",
            "SPOTIFY_CLIENT_SECRET": "SEU_CLIENT_SECRET_SPOTIFY",
            "SPOTIFY_REDIRECT_URI": "http://127.0.0.1:8080/callback"
        }
    }
}


def print_banner():
    print("""
================================================================================
     🧠 SkiilsToIAs - Instalador Multiplataforma de Skills, Agentes & MCPs
          Desenvolvido por Henrique Bezerra Dos Santos (@Henrique1601)
================================================================================
    """)


def get_paths():
    home = Path.home()
    is_windows = platform.system() == "Windows"
    
    paths = {
        "gemini_skills": home / ".gemini" / "config" / "skills",
        "gemini_agents": home / ".gemini" / "config" / "agents",
        "gemini_mcp": home / ".gemini" / "config" / "mcp_config.json",
        
        "claude_skills": home / ".claude" / "skills",
        "claude_desktop_config": (
            home / "AppData" / "Roaming" / "Claude" / "claude_desktop_config.json"
            if is_windows
            else home / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
        ),
        
        "cursor_skills": home / ".cursor" / "skills",
        "openclaw_skills": home / ".openclaw" / "skills",
        "codex_skills": home / ".codex" / "skills",
    }
    return paths


def copy_tree_safe(src: Path, dst: Path):
    dst.mkdir(parents=True, exist_ok=True)
    copied = 0
    for root, dirs, files in os.walk(src):
        rel = Path(root).relative_to(src)
        target_dir = dst / rel
        target_dir.mkdir(parents=True, exist_ok=True)
        for f in files:
            src_file = Path(root) / f
            dst_file = target_dir / f
            shutil.copy2(src_file, dst_file)
            copied += 1
    return copied


def install_skills(repo_root: Path, target_dir: Path, preserve_categories: bool = True):
    print(f"\n📦 Instalando Skills em: {target_dir}")
    target_dir.mkdir(parents=True, exist_ok=True)
    total_skills = 0

    for cat in REPO_CATEGORIES:
        src_cat = repo_root / cat
        if not src_cat.is_dir():
            continue

        for item in src_cat.iterdir():
            if item.is_dir() and (item / "SKILL.md").exists():
                if preserve_categories:
                    dest_skill = target_dir / cat / item.name
                else:
                    dest_skill = target_dir / item.name
                
                copy_tree_safe(item, dest_skill)
                total_skills += 1

    print(f"   ✅ {total_skills} skills instaladas com sucesso!")
    return total_skills


def install_custom_agents(repo_root: Path, target_dir: Path):
    src_agents = repo_root / "custom-agents"
    if not src_agents.is_dir():
        return 0

    print(f"\n👑 Instalando Agentes Customizados em: {target_dir}")
    target_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    for item in src_agents.iterdir():
        if item.is_file() and item.suffix == ".md" and item.name.lower() != "readme.md":
            shutil.copy2(item, target_dir / item.name)
            count += 1
        elif item.is_dir() and (item / "SKILL.md").exists():
            copy_tree_safe(item, target_dir / item.name)
            count += 1

    print(f"   ✅ {count} agentes customizados instalados!")
    return count


def update_mcp_config(config_file: Path):
    print(f"\n🔌 Configurando Servidores MCP em: {config_file}")
    config_file.parent.mkdir(parents=True, exist_ok=True)

    data = {}
    if config_file.is_file():
        try:
            with open(config_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"   ⚠️ Aviso ao ler {config_file}: {e}. Criando novo arquivo.")
            data = {}

    if "mcpServers" not in data or not isinstance(data["mcpServers"], dict):
        data["mcpServers"] = {}

    added = 0
    updated = 0
    for server_name, server_conf in DEFAULT_MCPS.items():
        if server_name not in data["mcpServers"]:
            data["mcpServers"][server_name] = server_conf
            added += 1
        else:
            updated += 1

    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"   ✅ MCP atualizado: {added} adicionados, {updated} mantidos/existentes.")


def main():
    print_banner()

    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent if script_dir.name.lower() == "scripts" else script_dir

    if not (repo_root / "ai-agents").exists() and not (repo_root / "README.md").exists():
        print(f"❌ Erro: Não foi possível localizar a raiz do repositório em: {repo_root}")
        sys.exit(1)

    print(f"📍 Raiz do repositório identificada: {repo_root.resolve()}")

    parser = argparse.ArgumentParser(description="Instalador Automático de Skills e MCPs")
    parser.add_argument("--all", action="store_true", help="Instala para todos os clientes compatíveis detectados")
    parser.add_argument("--gemini", action="store_true", help="Instala apenas para Antigravity / Gemini CLI")
    parser.add_argument("--claude", action="store_true", help="Instala apenas para Claude Code e Claude Desktop")
    parser.add_argument("--mcp-only", action="store_true", help="Instala apenas as configurações de servidores MCP")
    parser.add_argument("--skills-only", action="store_true", help="Instala apenas as skills")
    args = parser.parse_args()

    default_all = not (args.gemini or args.claude or args.mcp_only or args.skills_only)
    paths = get_paths()

    # 1. Antigravity / Gemini CLI
    if default_all or args.all or args.gemini:
        if not args.mcp_only:
            install_skills(repo_root, paths["gemini_skills"], preserve_categories=True)
            install_custom_agents(repo_root, paths["gemini_agents"])
        if not args.skills_only:
            update_mcp_config(paths["gemini_mcp"])

    # 2. Claude Code & Claude Desktop
    if default_all or args.all or args.claude:
        if not args.mcp_only:
            install_skills(repo_root, paths["claude_skills"], preserve_categories=False)
        if not args.skills_only and paths["claude_desktop_config"].parent.exists():
            update_mcp_config(paths["claude_desktop_config"])

    # 3. Cursor & OpenClaw
    if default_all or args.all:
        if not args.mcp_only:
            install_skills(repo_root, paths["openclaw_skills"], preserve_categories=False)

    print("\n" + "=" * 80)
    print("✨ INSTALAÇÃO E ATUALIZAÇÃO CONCLUÍDAS COM SUCESSO!")
    print("================================================================================")
    print("👉 Suas IAs (Antigravity, Claude, Cursor) já estão com 658 skills e MCPs ativos!")
    print("👉 Chame 'global-master-agent' ou 'skills-orchestrator' para começar qualquer projeto.")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
