-- PostgreSQL + pgvector schema for SkiilsToIAs RAG engine.
-- Requires PostgreSQL 15+ and pgvector extension.

CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS documents (
    id BIGSERIAL PRIMARY KEY,
    path TEXT NOT NULL UNIQUE,
    doc_type TEXT NOT NULL,
    title TEXT NOT NULL DEFAULT '',
    content_hash TEXT NOT NULL,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS chunks (
    id BIGSERIAL PRIMARY KEY,
    document_id BIGINT NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    chunk_index INTEGER NOT NULL,
    section TEXT NOT NULL DEFAULT '',
    content TEXT NOT NULL,
    token_count INTEGER NOT NULL DEFAULT 0,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    embedding vector(1536),
    fts tsvector GENERATED ALWAYS AS (
        to_tsvector('english', coalesce(section, '') || ' ' || content)
    ) STORED,
    UNIQUE (document_id, chunk_index)
);

CREATE INDEX IF NOT EXISTS idx_documents_doc_type
    ON documents (doc_type);

CREATE INDEX IF NOT EXISTS idx_chunks_document_id
    ON chunks (document_id);

CREATE INDEX IF NOT EXISTS idx_chunks_fts_gin
    ON chunks USING GIN (fts);

CREATE INDEX IF NOT EXISTS idx_chunks_embedding_hnsw
    ON chunks USING hnsw (embedding vector_cosine_ops)
    WITH (m = 16, ef_construction = 64);
