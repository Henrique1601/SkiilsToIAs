# 🟢 Supabase MCP Server (`supabase`)

Servidor oficial do **Supabase MCP** para gestão de projetos, execução de SQL, aplicação de migrations, Edge Functions, geração de tipos TypeScript, logs e advisors de segurança/performance.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Streamable HTTP (Remoto)
- **Endpoint Oficial:** `https://mcp.supabase.com/mcp`
- **Autenticação:** OAuth / Personal Access Token (`Authorization: Bearer <SUPABASE_ACCESS_TOKEN>`).

```json
{
  "mcpServers": {
    "supabase": {
      "serverUrl": "https://mcp.supabase.com/mcp",
      "headers": {
        "Authorization": "Bearer ${SUPABASE_ACCESS_TOKEN}"
      }
    }
  }
}
```

## 🛠️ Principais Capacidades
- `list_projects` / `get_project` / `create_project`
- `list_tables` / `execute_sql` / `apply_migration`
- `list_edge_functions` / `deploy_edge_function`
- `get_advisors` / `query_logs` / `generate_typescript_types`
