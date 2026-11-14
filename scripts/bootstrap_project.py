#!/usr/bin/env python3
"""Zero-dependency CLI to scaffold a project in Padrão Ouro (ADR-003 & ADR-004)."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

VALID_TYPES = ("web", "desktop", "lib")


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")
    return slug or "project"


def build_readme(name: str, slug: str, proj_type: str) -> str:
    download_label = (
        "[🚀 Download (.exe)](../../releases/latest)"
        if proj_type == "desktop"
        else "[🚀 Download](../../releases/latest)"
    )
    quick_links = (
        f"{download_label} | "
        "[⚡ Quick Start](#-setup--instalação) | "
        "[🌐 Website](#) | "
        "[📚 Docs](docs/brain/INDEX.md) | "
        "[📦 Releases](../../releases)"
    )

    if proj_type == "desktop":
        install_section = (
            "### Usuário Final (Windows)\n"
            "1. Baixe o instalador/executável mais recente em [Releases](../../releases/latest).\n"
            "2. Verifique o hash em `SHA256SUMS.txt` e execute o binário.\n\n"
            "### Desenvolvimento\n"
            "```bash\n"
            f"git clone https://github.com/<org>/{slug}.git\n"
            f"cd {slug}\n"
            "cp .env.example .env\n"
            "# Instale as dependências e execute o build local\n"
            "```"
        )
    elif proj_type == "web":
        install_section = (
            "```bash\n"
            f"git clone https://github.com/<org>/{slug}.git\n"
            f"cd {slug}\n"
            "cp .env.example .env\n"
            "# Instale as dependências (ex: npm install / pnpm install) e inicie o dev server\n"
            "```"
        )
    else:
        install_section = (
            "```bash\n"
            f"git clone https://github.com/<org>/{slug}.git\n"
            f"cd {slug}\n"
            "cp .env.example .env\n"
            "# Instale em modo editável / execute a suíte de testes\n"
            "```"
        )

    return f"""<p align="center">
  <img src="assets/logo.png" alt="{name} Logo" width="140" />
</p>

<h1 align="center">{name}</h1>

<p align="center">
  <img src="https://img.shields.io/badge/type-{proj_type}-blue" alt="Type" />
  <img src="https://img.shields.io/badge/version-v1.0.0-green" alt="Version" />
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="License" />
  <img src="https://img.shields.io/github/actions/workflow/status/<org>/{slug}/release.yml?label=release" alt="Release CI" />
</p>

<p align="center">
  {quick_links}
</p>

---

## Visão Geral

**{name}** é um projeto `{proj_type}` estruturado no **Padrão Ouro** (ADR-003 & ADR-004), com pipeline de release automatizada, documentação viva em `docs/brain/` e contratos tipados (TypeSafe AI) quando aplicável.

## ⚡ Setup & Instalação

{install_section}

## ⚙️ Variáveis de Ambiente

Copie `.env.example` para `.env` e preencha os valores necessários antes de executar o projeto.

## 🧱 Arquitetura

```mermaid
flowchart LR
    User([Usuário]) --> App["{name} ({proj_type})"]
    App --> Brain["docs/brain/ (Segundo Cérebro)"]
    App --> CI[".github/workflows/release.yml"]
```

## 🤝 Como Contribuir

1. Crie uma branch a partir de `main` (`feat/...` ou `fix/...`).
2. Siga Conventional Commits e mantenha `docs/brain/` atualizado.
3. Abra um Pull Request após validar testes e lint.
"""


def build_changelog(name: str, today: str) -> str:
    return f"""# Changelog

Todas as mudanças notáveis de **{name}** serão documentadas neste arquivo.

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.0.0] - {today}
### Added
- Scaffold inicial no Padrão Ouro (ADR-003 & ADR-004).
- Pipeline automatizada de release em `.github/workflows/release.yml`.
- Segundo Cérebro local inicializado em `docs/brain/`.
"""


def build_env_example(slug: str, proj_type: str) -> str:
    extra = ""
    if proj_type == "web":
        extra = "PORT=3000\nDATABASE_URL=postgresql://user:pass@localhost:5432/" + slug + "\n"
    elif proj_type == "desktop":
        extra = "AUTO_UPDATE=true\n"
    return (
        f"APP_NAME={slug}\n"
        "APP_ENV=development\n"
        "LOG_LEVEL=info\n"
        f"{extra}"
        "# Preencha somente se o projeto utilizar LLMs (TypeSafe AI obrigatório)\n"
        "OPENAI_API_KEY=\n"
    )


def build_gitignore(proj_type: str) -> str:
    common = """# Secrets & environment
.env
.env.local
.env.*.local

# Build & release artifacts (ADR-003: never commit binaries)
dist/
build/
out/
release/
*.exe
*.msi
*.zip
*.tar.gz
SHA256SUMS.txt

# Caches & dependencies
.cache/
__pycache__/
*.py[cod]
.venv/
venv/
node_modules/

# Logs & OS
*.log
.DS_Store
Thumbs.db
"""
    if proj_type == "web":
        common += "\n# Web\n.next/\n.nuxt/\n"
    return common


def build_release_workflow(slug: str, proj_type: str) -> str:
    if proj_type == "desktop":
        return f"""name: Release Desktop

on:
  push:
    tags:
      - "v*"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  build-windows:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build Windows Executable
        shell: pwsh
        run: |
          New-Item -ItemType Directory -Force -Path dist | Out-Null
          # Substitua pelo comando real de build (ex: PyInstaller, Tauri, Electron)
          Set-Content -Path "dist/{slug}.exe.placeholder" -Value "Replace with actual .exe build step"
          Compress-Archive -Path "dist/*" -DestinationPath "dist/{slug}-windows-x64.zip" -Force

      - name: Generate SHA-256 Checksums
        shell: pwsh
        run: |
          Get-FileHash "dist/{slug}-windows-x64.zip" -Algorithm SHA256 |
            ForEach-Object {{ "$($_.Hash.ToLower())  $(Split-Path $_.Path -Leaf)" }} |
            Set-Content -Path "dist/SHA256SUMS.txt"

      - name: Publish GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          generate_release_notes: true
          files: |
            dist/{slug}-windows-x64.zip
            dist/SHA256SUMS.txt
"""

    if proj_type == "web":
        return f"""name: Release Web

on:
  push:
    tags:
      - "v*"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  release-web:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build Web Bundle
        run: |
          mkdir -p dist
          # Substitua pelo comando real de build (ex: npm ci && npm run build)
          echo "Web bundle placeholder for {slug}" > dist/BUILD_INFO.txt
          tar -czf "{slug}-web-bundle.tar.gz" -C dist .
          sha256sum "{slug}-web-bundle.tar.gz" > SHA256SUMS.txt

      - name: Publish GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          generate_release_notes: true
          files: |
            {slug}-web-bundle.tar.gz
            SHA256SUMS.txt
"""

    return f"""name: Release Library

on:
  push:
    tags:
      - "v*"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  release-lib:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Test & Package Library
        run: |
          mkdir -p dist
          # Substitua pelos comandos reais de teste e empacotamento (ex: pytest && python -m build)
          echo "Library artifact placeholder for {slug}" > dist/PACKAGE_INFO.txt
          tar -czf "{slug}-lib.tar.gz" -C dist .
          sha256sum "{slug}-lib.tar.gz" > SHA256SUMS.txt

      - name: Publish GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          generate_release_notes: true
          files: |
            {slug}-lib.tar.gz
            SHA256SUMS.txt
"""


def build_brain_index(name: str) -> str:
    return f"""# 🧠 Segundo Cérebro — {name}

Base de conhecimento persistente do projeto **{name}** (ADR-004).

## 🧭 Índice (Wikilinks)
- [[DECISIONS]] — Decisões arquiteturais e regras do projeto.
- [[GOTCHAS]] — Armadilhas conhecidas e soluções validadas.

## ⚡ Regras Base
1. **Ponytail:** Simplicidade radical, zero over-engineering.
2. **TypeSafe AI:** Toda saída de LLM deve usar schema tipado.
3. **Sem Binários no Git:** Artefatos compilados vão apenas para GitHub Releases.
"""


def build_brain_decisions(name: str, proj_type: str, today: str) -> str:
    return f"""# 📐 Decisões Arquiteturais (DECISIONS) — {name}

## {today} — Bootstrap Padrão Ouro (`{proj_type}`)
- **Decisão:** Projeto inicializado com estrutura Padrão Ouro (ADR-003 & ADR-004).
- **Inclui:** `README.md` padronizado, `CHANGELOG.md`, `.env.example`, `.gitignore` sem binários, `.github/workflows/release.yml` e `docs/brain/`.
"""


def build_brain_gotchas(name: str) -> str:
    return f"""# ⚠️ Armadilhas & Lições Aprendidas (GOTCHAS) — {name}

1. **Segredos no Repositório:** Nunca comite `.env` ou chaves reais; use apenas `.env.example` com placeholders.
2. **Binários no Git:** Nunca comite `.exe`, `.msi`, `.zip` ou `dist/`; publique sempre via GitHub Releases.
3. **Respostas Cruas de LLM:** Valide qualquer retorno de IA com schema tipado (TypeSafe AI).
"""


def build_files(name: str, proj_type: str, today: str) -> dict[str, str]:
    slug = slugify(name)
    return {
        "README.md": build_readme(name, slug, proj_type),
        "CHANGELOG.md": build_changelog(name, today),
        ".env.example": build_env_example(slug, proj_type),
        ".gitignore": build_gitignore(proj_type),
        ".github/workflows/release.yml": build_release_workflow(slug, proj_type),
        "docs/brain/INDEX.md": build_brain_index(name),
        "docs/brain/DECISIONS.md": build_brain_decisions(name, proj_type, today),
        "docs/brain/GOTCHAS.md": build_brain_gotchas(name),
    }


def scaffold_project(
    name: str,
    proj_type: str,
    out_dir: Path,
    dry_run: bool = False,
    force: bool = False,
) -> int:
    today = date.today().isoformat()
    files = build_files(name, proj_type, today)
    counts = {"create": 0, "overwrite": 0, "skip": 0}

    prefix = "[DRY-RUN] " if dry_run else ""
    print(f"{prefix}Bootstrapping '{name}' (type={proj_type}) -> {out_dir}")

    for rel_path, content in files.items():
        target = out_dir / rel_path
        exists = target.exists()

        if exists and not force:
            counts["skip"] += 1
            print(f"  SKIP      {rel_path} (exists; pass --force to overwrite)")
            continue

        action = "OVERWRITE" if exists else "CREATE"
        counts["overwrite" if exists else "create"] += 1
        print(f"  {action:<9} {rel_path}")

        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8", newline="\n")

    print(
        f"{prefix}Done: {counts['create']} created, "
        f"{counts['overwrite']} overwritten, {counts['skip']} skipped."
    )
    return 0


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scaffold a new project in Padrão Ouro (ADR-003 & ADR-004)."
    )
    parser.add_argument("--name", required=True, help="Project display name.")
    parser.add_argument(
        "--type",
        dest="proj_type",
        required=True,
        choices=VALID_TYPES,
        help="Project type: web, desktop, or lib.",
    )
    parser.add_argument("--out", required=True, help="Target output directory.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview planned file operations without writing to disk.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files instead of skipping them.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    args = parse_args(argv)
    if not args.name.strip():
        print("Error: --name must not be empty.", file=sys.stderr)
        return 2

    return scaffold_project(
        name=args.name.strip(),
        proj_type=args.proj_type,
        out_dir=Path(args.out),
        dry_run=args.dry_run,
        force=args.force,
    )


if __name__ == "__main__":
    raise SystemExit(main())
