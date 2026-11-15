# 💜 Lovable MCP Server (`lovable`)

Servidor oficial do **Lovable MCP** para gerenciamento de workspaces, criação e deploy de projetos Lovable, inspeção de arquivos, drafts, banco de dados e analytics.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Streamable HTTP (Remoto)
- **Endpoint Oficial:** `https://mcp.lovable.dev`
- **Autenticação:** OAuth / Bearer Token (`Authorization: Bearer <LOVABLE_TOKEN>`).

```json
{
  "mcpServers": {
    "lovable": {
      "serverUrl": "https://mcp.lovable.dev",
      "headers": {
        "Authorization": "Bearer ${LOVABLE_TOKEN}"
      }
    }
  }
}
```

## 🛠️ Principais Capacidades
- `list_workspaces` / `list_projects` / `create_project` / `deploy_project`
- `list_files` / `read_file` / `get_diff` / `send_message`
- `query_database` / `get_project_analytics`
