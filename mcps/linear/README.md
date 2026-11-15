# 📋 Linear MCP Server (`linear`)

Servidor oficial do **Linear MCP** (`linear-mcp-server`) para gestão de issues, ciclos, projetos, roadmaps, comentários e revisão de diffs no Linear.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Bridge Remoto (`npx mcp-remote`)
- **Endpoint Oficial:** `https://mcp.linear.app/sse`
- **Autenticação:** OAuth interativo ou token do Linear.

```json
{
  "mcpServers": {
    "linear-mcp-server": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.linear.app/sse"]
    }
  }
}
```

## 🛠️ Principais Capacidades
- `list_issues` / `get_issue` / `save_issue`
- `list_projects` / `list_cycles` / `list_milestones`
- `list_comments` / `save_comment` / `list_documents`
