---
name: desktop-packaging-release
description: "Empacotamento, assinatura, auto-update e publicação de Releases v1.0.0+ para apps desktop Windows (.exe/.msi), macOS (.dmg) e Linux (.AppImage) com Electron, Tauri ou PyInstaller."
---

# 📦 Empacotamento & Release Desktop (`desktop-packaging-release`)

Padrão institucional (ADR-003) para gerar instaladores nativos e publicar **GitHub Releases** desde a `v1.0.0`.

## 🎯 Checklist de Build & Release

1. **Escolha Enxuta da Stack (Ponytail):**
   - **WebView leve:** Tauri (`src-tauri/tauri.conf.json`, binário pequeno).
   - **Ecossistema Node completo:** Electron + `electron-builder`.
   - **CLI / Utilitário Python:** `pyinstaller --onefile --windowed` ou Inno Setup para `.exe`.
2. **Versão Única & Changelog:**
   - Mantenha `version` sincronizada (`package.json` / `Cargo.toml` / `pyproject.toml`), atualize `CHANGELOG.md` e crie tag semântica `vX.Y.Z`.
3. **Artefatos por Plataforma:**
   - **Windows:** instalador NSIS/MSI (`.exe` / `.msi`) + checksum `SHA256SUMS.txt`.
   - **macOS / Linux:** `.dmg` / `.AppImage` (quando aplicável).
4. **GitHub Actions Automático (`release.yml`):**
   - Dispara em tags `v*.*.*`, roda testes antes do build e publica os binários anexados à GitHub Release (`softprops/action-gh-release`).
5. **Segurança:**
   - Nunca inclua `.env` ou certificados privados no repositório; use GitHub Secrets (`CSC_LINK`, `CSC_KEY_PASSWORD`) para code signing.
