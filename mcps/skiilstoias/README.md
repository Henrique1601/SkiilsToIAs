# 🧠 SkiilsToIAs MCP Server (`skiilstoias`)

Servidor MCP **Stdio zero-dependência** nativo deste repositório (`scripts/skills_mcp.py`), permitindo que qualquer agente ou IDE consulte diretamente o RAG local, o catálogo, o healthcheck de MCPs e o bootstrap Padrão Ouro.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Stdio (Local Python 3, zero dependências externas)
- **Script:** `scripts/skills_mcp.py`

```json
{
  "mcpServers": {
    "skiilstoias": {
      "command": "python",
      "args": ["c:/Users/henri/.agents/skills/scripts/skills_mcp.py"]
    }
  }
}
```

## 🛠️ Ferramentas Expostas (`5`)
- `skills_rag_search`: Busca híbrida local FTS5/BM25 em `.cache/rag_index.db`.
- `skills_catalog_lookup`: Consulta e filtra itens em `docs/catalog/catalog.json`.
- `skills_mcp_health`: Executa checagem mascarada dos MCPs configurados.
- `skills_bootstrap_project`: Gera scaffold Padrão Ouro (`dry_run=true` por padrão).
- `skills_graph_query`: Consulta nós e vizinhos 1-hop em `graphify-out/graph.json`.
