# 🔎 Perplexity Ask MCP Server (`perplexity-ask`)

Servidor do **Perplexity Ask MCP** (`server-perplexity-ask`) para pesquisa web em tempo real com síntese e citações de fontes usando a Sonar API da Perplexity.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Stdio (Local via `npx`)
- **Pacote:** `server-perplexity-ask`
- **Autenticação:** Variável de ambiente `PERPLEXITY_API_KEY`.

```json
{
  "mcpServers": {
    "perplexity-ask": {
      "command": "npx",
      "args": ["-y", "server-perplexity-ask"],
      "env": {
        "PERPLEXITY_API_KEY": "${PERPLEXITY_API_KEY}"
      }
    }
  }
}
```

## 🛠️ Principais Capacidades
- `perplexity_ask`: Realiza consultas web atualizadas com resposta fundamentada e URLs de referência.
