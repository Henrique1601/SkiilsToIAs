# 📊 Windsor.ai MCP Server (`windsor`)

Servidor oficial do **Windsor.ai MCP** para consulta unificada de dados de marketing, mídia paga, atribuição e analytics conectados ao workspace Windsor.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Streamable HTTP (Remoto)
- **Endpoint Oficial:** `https://mcp.windsor.ai`
- **Autenticação:** OAuth / Bearer Token (`Authorization: Bearer <WINDSOR_API_KEY>`).

```json
{
  "mcpServers": {
    "windsor": {
      "serverUrl": "https://mcp.windsor.ai",
      "headers": {
        "Authorization": "Bearer ${WINDSOR_API_KEY}"
      }
    }
  }
}
```

## 🛠️ Principais Capacidades
- Consulta de métricas de campanhas (Google Ads, Meta Ads, GA4, CRM).
- Extração de dados de atribuição e ROI multi-canal.
