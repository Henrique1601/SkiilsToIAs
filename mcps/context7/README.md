# 📚 Context7 MCP Server (`context7`)

Servidor oficial do **Context7 MCP** para busca de documentação oficial atualizada de bibliotecas e frameworks em tempo real, evitando APIs depreciadas e alucinações.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Streamable HTTP (Remoto)
- **Endpoint Oficial:** `https://mcp.context7.com/mcp`
- **Autenticação:** Header `CONTEXT7_API_KEY: <CONTEXT7_API_KEY>` (ou acesso público com rate-limit padrão).

```json
{
  "mcpServers": {
    "context7": {
      "serverUrl": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "${CONTEXT7_API_KEY}"
      }
    }
  }
}
```

## 🛠️ Principais Capacidades
- `resolve-library-id`: Resolve o identificador canônico de uma biblioteca/SDK.
- `query-docs`: Consulta documentação e exemplos atualizados por tópico/versão.
