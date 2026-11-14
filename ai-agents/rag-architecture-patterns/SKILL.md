---
name: rag-architecture-patterns
description: "Padrões arquiteturais e implementação de pipelines RAG (Retrieval-Augmented Generation) de alta fidelidade para qualquer projeto ou sistema. Cobre chunking semântico, embeddings, busca híbrida (pgvector + BM25), reranking, validação via TypeSafe AI e filosofia Ponytail (anti-overengineering)."
---

# 🧠 RAG Architecture Patterns (`rag-architecture-patterns`)

Este manual estabelece as convenções obrigatórias para implementar e operar sistemas de **RAG (Retrieval-Augmented Generation)** em **qualquer projeto ou sistema** (Web SaaS, APIs, CLIs, automações internas ou bases de conhecimento de agentes).

---

## 🎯 1. Quando Aplicar RAG em um Projeto

Use RAG sempre que o sistema precisar:
1. **Responder perguntas sobre dados proprietários:** Documentação interna, contratos, histórico de chamados, wikis ou dados do cliente.
2. **Eliminar alucinações:** Limitar a resposta da LLM estritamente a trechos recuperados de fontes auditáveis.
3. **Superar limites de janela de contexto:** Consultar bases de milhares ou milhões de páginas gastando frações de centavos por requisição.
4. **Semântica + Precisão Cirúrgica:** Combinar busca vetorial (compreensão de sinônimos/ideias) com busca exata (siglas, erros de código, nomes).

---

## 🏛️ 2. Arquitetura Padrão Ouro (Os 5 Módulos)

```mermaid
flowchart TD
    subgraph Ingestao ["1. Ingestão & Chunking"]
        Raw["Documentos Crus (MD, PDF, TXT, JSON)"] --> Parser["Limpeza & Extração de Texto"]
        Parser --> Chunk["Chunking Semântico (500-1000 tokens / 10% overlap)"]
        Chunk --> Meta["Metadados (documentId, título, data, seção)"]
    end

    subgraph Vetores ["2. Embeddings & Armazenamento"]
        Meta --> EmbModel["Modelo de Embeddings (OpenAI / Gemini)"]
        EmbModel --> VectorDB[("PostgreSQL + pgvector (Neon / Supabase)")]
    end

    subgraph Busca ["3. Recuperação Híbrida (Hybrid Retrieval)"]
        UserQ["Pergunta do Usuário"] --> QEmb["Embedding da Pergunta"]
        QEmb --> Cosine["Busca Vetorial (Similaridade Cosseno)"]
        UserQ --> FTS["Busca Textual (BM25 / Full-Text Search)"]
        VectorDB --> Cosine
        VectorDB --> FTS
        Cosine & FTS --> RRF["Reciprocal Rank Fusion (RRF) / Top K"]
    end

    subgraph Geracao ["4. Geração com TypeSafe AI"]
        RRF --> ContextBlock["Bloco de Contexto Formatado"]
        ContextBlock --> LLM["LLM (gpt-4o-mini / Gemini Flash)"]
        LLM --> Zod["Validação Zod (Resposta + Citações + Confiança)"]
        Zod --> Output["✅ Resposta Estruturada & Confiável"]
    end
```

---

## 🪚 3. Princípios Ponytail Mandatórios (Anti-Overengineering)

1. **Reaproveite o Banco Existente:**
   - Se o projeto já tem PostgreSQL, use **`pgvector`** (nativo no Neon e Supabase). Não contrate ou suba clusters dedicados como Pinecone/Milvus antes de ultrapassar 500.000 chunks.
   - Se for um app desktop ou CLI local, use **SQLite com FTS5** ou extensões vetoriais locais.
2. **Evite Abstrações Complexas:**
   - Um script simples de ingestão (`ler arquivo ➔ chunk ➔ embed ➔ INSERT SQL`) é mais confiável e manutenível do que 10 bibliotecas encadeadas com pipelines opacos.
3. **Chunking com Propósito:**
   - Respeite as fronteiras naturais do documento (títulos `#`, `##` e quebras de parágrafo). Nunca corte texto de forma puramente arbitrária por quantidade de caracteres.

---

## 🛡️ 4. Contrato de Resposta TypeSafe AI

Toda chamada de RAG deve retornar uma estrutura fortemente tipada:

```typescript
import { z } from 'zod';

export const RagResponseSchema = z.object({
  answer: z.string().describe('Resposta fundamentada unicamente no contexto fornecido.'),
  confidence: z.enum(['high', 'medium', 'low']).describe('Nível de certeza com base na clareza do contexto.'),
  citations: z.array(z.object({
    source: z.string().describe('Identificador do documento ou arquivo.'),
    excerpt: z.string().describe('Trecho exato do contexto que valida a resposta.')
  })).min(1).describe('Fontes consultadas que comprovam a resposta.'),
  missingInformation: z.string().optional().describe('Lacunas que a pergunta pediu mas não constam na base.')
});

export type RagResponse = z.infer<typeof RagResponseSchema>;
```

---

## 📚 5. Aplicação no Projeto de Skills (`SkiilsToIAs`)

No próprio repositório `SkiilsToIAs`:
- **Base de Conhecimento:** 685 skills, 26 MCPs e manuais de custom-agents.
- **Como o RAG Funciona Aqui:**
  1. Cada arquivo `SKILL.md` ou manual de MCP é indexado com seus metadados (nome, categoria, descrição).
  2. Ao pedir *"como fazer X"*, a busca híbrida encontra instantaneamente as 3 melhores skills e os MCPs necessários sem carregar 700 arquivos na janela de contexto.
  3. Reduz o consumo de tokens em **mais de 90%**, tornando qualquer orquestração instantânea e de baixo custo.
