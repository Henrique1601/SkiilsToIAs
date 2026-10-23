# 🧠 AI-Memory MCP Server (`ai-memory`)

Servidor de **Memória Semântica Persistente e Grafo de Conhecimento** (`ai-memory`), rodando localmente para garantir continuidade de contexto entre sessões, registro de decisões históricas, manutenção contínua de Wiki e auto-auditoria de coerência com `memory_lint`.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Streamable HTTP (Local)
- **Endpoint:** `http://127.0.0.1:49374/mcp`
- **Timeout Padrão:** 5000 ms

### Exemplo de Configuração:

```json
{
  "mcpServers": {
    "ai-memory": {
      "serverUrl": "http://127.0.0.1:49374/mcp",
      "timeout": 5000
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades (23 Ferramentas Integradas)
- **Session Bootstrap:** Recuperação de contexto inicial com `memory_list` e `memory_search`.
- **Entidades & Grafo:** Criação e consulta de entidades atômicas com `memory_create_entity`, `memory_create_relation` e `memory_batch_create`.
- **Notas & Reflexões:** Gravação de memórias episódicas com `memory_write_memo` e `memory_record_reflection`.
- **Documentação & Wiki:** Páginas conectadas com `memory_wiki_create_page`, `memory_wiki_search` e `memory_wiki_compile`.
- **Governança:** Detecção de contradições e auditoria com `memory_lint` e `memory_detect_contradictions`.
- **Sinergia:** Operado nativamente pelo [`memory-architect-agent`](../../custom-agents/memory-architect-agent.md).
