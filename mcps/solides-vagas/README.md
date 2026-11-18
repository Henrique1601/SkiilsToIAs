# 💼 Sólides Vagas MCP Server (`solides-vagas`)

Servidor MCP HTTP da **Sólides Vagas (ATS)** para consulta de vagas e suporte à jornada de candidatos via Model Context Protocol.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Streamable HTTP (Remoto)
- **Endpoint Oficial:** `https://mcp.solides.com.br/ats/candidate`

### Configuração no `mcp_config.json`:

```json
{
  "mcpServers": {
    "solides-vagas": {
      "serverUrl": "https://mcp.solides.com.br/ats/candidate"
    }
  }
}
```

### Via Gemini CLI:

```bash
gemini mcp add --transport http solides-vagas https://mcp.solides.com.br/ats/candidate
```
