# 🎞️ Concat Video Editor MCP Server (`concat`)

Bridge MCP **Stdio zero-dependência** (`scripts/concat_mcp.py`) para o daemon JSON-RPC local do editor de vídeo **Concat** (`127.0.0.1:7420`), com autenticação automática na primeira linha (`auth` + `token`).

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Stdio Bridge -> TCP JSON-RPC local (`127.0.0.1:7420`)
- **Script:** `scripts/concat_mcp.py`
- **Autenticação:** Variável de ambiente `CONCAT_TOKEN` (nunca versionar o token real).

### Configuração no `mcp_config.json`:

```json
{
  "mcpServers": {
    "concat": {
      "command": "python",
      "args": ["c:/Users/henri/.agents/skills/scripts/concat_mcp.py"],
      "env": {
        "CONCAT_HOST": "127.0.0.1",
        "CONCAT_PORT": "7420",
        "CONCAT_TOKEN": "${CONCAT_TOKEN}"
      }
    }
  }
}
```

## 🛠️ Ferramentas & Métodos Suportados
- `concat_version` / `concat_project_list` / `concat_project_get`
- `concat_edit_apply` / `concat_export_run`
- `concat_call`: acesso completo aos 22 métodos do Concat (`project.*`, `edit.*`, `media.*`, `catalogue.list`, `template.*`, `export.*`, `preview.frame`, `version`).
