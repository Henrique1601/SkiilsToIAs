# 🧠 Arquitetura RAG no Ecossistema (RAG_ARCHITECTURE)

Este documento registra como aplicar RAG tanto nos seus projetos externos quanto internamente no repositório de skills.

---

## 🚀 1. RAG em Qualquer Projeto / Sistema
RAG pode ser acoplado em:
- **SaaS Web (Next.js/React):** Suporte ao cliente, assistentes de produto, busca inteligente em bases de artigos.
- **Sistemas Internos / ERP / CRM:** Consulta a relatórios financeiros, contratos, notas fiscais e políticas de RH.
- **Aplicativos Desktop / PC (.exe):** Busca offline em bases de manuais ou documentações locais usando SQLite + FTS5.
- **APIs & Microsserviços:** Endpoints `/api/search` e `/api/chat` potencializados por contexto em tempo real.

---

## 🧰 2. RAG no Repositório de Skills (`SkiilsToIAs`)
No `SkiilsToIAs`, temos **685 skills** e **26 MCPs**. Carregar centenas de manuais na janela de contexto de uma LLM estoura limites e gasta tokens desnecessariamente.

A RAG interna funciona da seguinte forma:
1. **Indexação:** Os 685 arquivos `SKILL.md` geram chunks categorizados com metadados `{ skillName, category, description }`.
2. **Embeddings:** Armazenados no banco `Neon Postgres` (já conectado via MCP `Neon`).
3. **Consulta em Tempo Real:** O `global-master-agent` e o `skills-orchestrator` consultam a base via `pgvector` e recuperam cirurgicamente apenas as 2 ou 3 skills exatas que o usuário precisa no momento.
4. **Economia:** 90%+ de economia de tokens com zero latência.
