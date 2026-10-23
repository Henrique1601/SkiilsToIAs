# 🍃 MongoDB Atlas MCP Server (`mongodb-atlas-mcp-remote`)

Servidor oficial do **MongoDB Atlas MCP** (`mongodb-atlas-mcp-remote@latest`) para gerenciamento de bancos de dados NoSQL na nuvem Atlas, inspeção de coleções, execução de agregações, índices e monitoramento de clusters.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Stdio (Execução local via Node/npx)
- **Pacote:** `mongodb-atlas-mcp-remote@latest`
- **Variáveis de Ambiente:** `MDB_MCP_API_CLIENT_ID`, `MDB_MCP_API_CLIENT_SECRET`

### Exemplo de Configuração:

```json
{
  "mcpServers": {
    "mongodb-atlas-mcp-remote": {
      "command": "npx",
      "args": ["-y", "mongodb-atlas-mcp-remote@latest"],
      "env": {
        "MDB_MCP_API_CLIENT_ID": "SEU_CLIENT_ID_DO_ATLAS",
        "MDB_MCP_API_CLIENT_SECRET": "SEU_SECRET_DO_ATLAS"
      }
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades
- **Gestão de Clusters Atlas:** Listagem de clusters, status e métricas de infraestrutura.
- **Modelagem & Consultas NoSQL:** Execução de pipelines de agregação, consultas JSON e criação de índices.
- **Sinergia:** Conecta-se diretamente com o `database-architect-agent` e as skills `mongodb-schema-design`, `mongodb-query-optimizer` e `mongodb-atlas-stream-processing`.
