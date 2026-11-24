# 🎞️ Concat Video Editor MCP Server (`concat`)

Servidor MCP nativo oficial do editor de vídeo **Concat** (`--mcp`), com suporte a criação/edição de projetos, timeline, mídia, templates e renderização/exportação.

---

## ⚡ Configuração & Transporte (Stdio Nativo)

- **Tipo / Transporte:** Stdio (Executável nativo com `--mcp`)

### Windows (`mcp_config.json`):

```json
{
  "mcpServers": {
    "concat": {
      "command": "C:\\Users\\henri\\AppData\\Local\\Programs\\Concat\\concat.exe",
      "args": ["--mcp"]
    }
  }
}
```

### macOS (`mcp_config.json`):

```json
{
  "mcpServers": {
    "concat": {
      "command": "/Applications/Concat.app/Contents/MacOS/concat",
      "args": ["--mcp"]
    }
  }
}
```

> **Alternativa via TCP Daemon (`127.0.0.1:7420`):** caso utilize o daemon TCP autenticado por token, este repositório também inclui a bridge zero-dependência [`scripts/concat_mcp.py`](../../scripts/concat_mcp.py) (`CONCAT_HOST`, `CONCAT_PORT`, `CONCAT_TOKEN`).
