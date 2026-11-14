# ⚠️ Armadilhas & Lições Aprendidas (GOTCHAS)

Registro de erros comuns e como evitá-los:

1. **RAG Naive vs. RAG de Produção:**
   - *Erro:* Fazer apenas chunking arbitrário de 500 caracteres e busca de similaridade cosseno direta.
   - *Impacto:* Perda de contexto entre parágrafos e alucinações na síntese da resposta.
   - *Solução:* Aplicar chunking semântico/estruturado + busca híbrida (FTS / BM25 + Vetorial) + Reranking.

2. **Over-Engineering em Vetores (Filosofia Ponytail):**
   - *Erro:* Subir um cluster pesado de vector database (Milvus/Pinecone corporativo) para bases menores que 100.000 documentos.
   - *Solução:* Usar `pgvector` nativo no PostgreSQL (Neon/Supabase) ou SQLite com extensão `sqlite-vss`/FTS5 local. Menos infra, menor custo e zero latência adicional de rede.

3. **Injeção de Prompts & Vazamento de Dados via RAG:**
   - *Erro:* Recuperar pedaços de documentos que contêm dados sensíveis ou prompts hostis e injetar sem sanitização no prompt do modelo.
   - *Solução:* TypeSafe AI para validar a resposta do LLM e filtro de permissões (RLS) no momento da busca no banco vetorial.
