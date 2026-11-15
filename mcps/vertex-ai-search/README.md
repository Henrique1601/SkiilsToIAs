# 🔍 Vertex AI Search MCP Server (`vertex-ai-search`)

Servidor oficial do **Google Vertex AI Search (Discovery Engine) MCP** para busca semântica empresarial, grounded search e recuperação de documentos em data stores do Google Cloud.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Streamable HTTP (Remoto)
- **Endpoint Oficial:** `https://discoveryengine.googleapis.com/mcp`
- **Autenticação:** Google OAuth / IAM Token (`Authorization: Bearer <GOOGLE_ACCESS_TOKEN>`).

```json
{
  "mcpServers": {
    "vertex-ai-search": {
      "serverUrl": "https://discoveryengine.googleapis.com/mcp",
      "headers": {
        "Authorization": "Bearer ${GOOGLE_ACCESS_TOKEN}"
      }
    }
  }
}
```

## 🛠️ Principais Capacidades
- Busca semântica e RAG gerenciado sobre data stores no Google Cloud Discovery Engine.
- Respostas fundamentadas com citações e controle de acesso IAM.
