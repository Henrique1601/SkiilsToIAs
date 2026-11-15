# 📱 Mobbin MCP Server (`mobbin`)

Servidor oficial do **Mobbin MCP** para pesquisa de referências reais de UI/UX, fluxos de onboarding, telas e seções de produtos digitais iOS, Android e Web.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Streamable HTTP (Remoto)
- **Endpoint Oficial:** `https://api.mobbin.com/mcp`
- **Autenticação:** OAuth / Bearer Token (`Authorization: Bearer <MOBBIN_TOKEN>`).

```json
{
  "mcpServers": {
    "mobbin": {
      "serverUrl": "https://api.mobbin.com/mcp",
      "headers": {
        "Authorization": "Bearer ${MOBBIN_TOKEN}"
      }
    }
  }
}
```

## 🛠️ Principais Capacidades
- `search_screens` / `search_flows` / `search_sections`
- `list_collections` / `get_collection_contents` / `create_collection`
- `save_content` / `add_comment`
