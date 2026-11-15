# 🎨 Canva MCP Server (`canva`)

Servidor oficial do **Canva MCP** via `mcp-remote` para criação, edição, busca, comentários, brand templates e exportação de designs e apresentações no Canva.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Bridge Remoto (`npx mcp-remote`)
- **Endpoint Oficial:** `https://mcp.canva.com/mcp`
- **Autenticação:** Fluxo OAuth interativo na primeira conexão.

```json
{
  "mcpServers": {
    "canva": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.canva.com/mcp"]
    }
  }
}
```

## 🛠️ Principais Capacidades
- `search-designs` / `get-design` / `create-design` / `export-design`
- `create-design-from-brand-template` / `list-brand-kits`
- `generate-image` / `remove-background` / `resize-design`
