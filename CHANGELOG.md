# 📋 Changelog

Todas as alterações notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e este projeto adere ao [Semantic Versioning (SemVer)](https://semver.org/lang/pt-BR/).

---

## [1.1.0] - 2026-11-16

### ✨ Novidades & Infraestrutura Executável
- **Servidor MCP Nativo (`scripts/skills_mcp.py`):** Servidor stdio zero-dependência expondo `skills_rag_search`, `skills_catalog_lookup`, `skills_mcp_health` e `skills_bootstrap_project`.
- **Motor RAG Executável (`scripts/rag_index.py`, `scripts/rag_search.py`, `scripts/rag_schema.sql`):** Indexação SQLite FTS5/BM25 local + busca híbrida opcional `pgvector` com Reciprocal Rank Fusion (`--semantic`).
- **Orquestração Paralela `/swarm`:** Integrada à Fase 4 do `global-master-agent` e roteamento `RAG + Graphify` no `skills-orchestrator`.
- **Catálogo Web Interativo no Netlify:** `docs/catalog/` publicado em `https://skiilstoias-catalog.netlify.app` com workflow automático (`.github/workflows/deploy-catalog.yml`), botão direto para o GitHub e atalho `/`.
- **Grafo de Conhecimento (`graphify` + `scripts/graph_enrich.py`):** Integração de nós AST de código com agentes, MCPs e Segundo Cérebro.
- **Automação & Qualidade:** `scripts/bootstrap_project.py`, `scripts/audit_repo.py`, `scripts/mcp_health.py`, `scripts/sync_all.py` (`--mirror`, `--install-hook`), suíte `tests/test_core_scripts.py` no CI e 11 novos MCPs + 4 novas skills (`brazil-payments-pix`, `desktop-packaging-release`, `n8n-whatsapp-automation`, `graphify`).

---

## [1.0.0] - 2026-11-14

### 🚀 Lançamento Oficial do Padrão Ouro (v1.0.0)

Primeira versão maior oficial do **`SkiilsToIAs`**, consolidando o Sistema Operacional de Engenharia para Agentes Autônomos de Inteligência Artificial.

#### ✨ Funcionalidades Principais & Arquitetura
- **16 Agentes Especialistas em Rede Full-Mesh (`custom-agents/`):**
  - `global-master-agent`: Comando supremo e orquestração da esteira de 5 fases (ADR-004).
  - `planning-master-agent`: Alinhamento estratégico, sabatina `/grill-me`, riscos e especificações (PRD).
  - `memory-architect-agent`: Segundo Cérebro persistente (`docs/brain/`, Obsidian e MCP `ai-memory`).
  - `skills-orchestrator`: Hub metodológico conectando 9 fases e 685 skills catalogadas.
  - `git-master-agent`: Arquitetura Double-Gate (Portão 0 e Portão Final), governança de releases e sincronização multi-PC.
  - `design-engineer-agent`: Design system, UI/UX Pro Max, tokens e animações fluidas.
  - `database-architect-agent`: Modelagem relacional/NoSQL, migrações seguras e RLS (Postgres/Supabase/Neon).
  - `ai-engineer-agent`: Engenharia de LLMs, metaprogramação e governança de prompts.
  - `qa-testing-agent`: TDD (*Red-Green-Refactor*), testes automatizados e Playwright E2E.
  - `security-auditor-agent`: Proteção OWASP Top 10, sanitização e blindagem de credenciais.
  - `appsec-pentest-agent`: Auditoria de segurança ofensiva, testes de intrusão éticos e SAST/DAST.
  - `devops-cloud-agent`: Infraestrutura em containers, Docker multi-stage, CI/CD e Vercel/Cloudflare.
  - `growth-marketing-agent`: SEO técnico, AI-SEO generativo, CRO e métricas de conversão.
  - `video-producer-agent`: Criação de vídeos em código via Remotion, animações sincronizadas e teasers.
  - `github-profile-agent`: Autoridade profissional e documentação de destaque no GitHub.
  - `social-publisher-agent`: Produção de mockups 3D (Shots Studio), gravação de telas e agendamento multicanal via Buffer MCP.

#### 🧰 Catálogo de Skills & Ferramentaria MCP
- **685 Skills Especializadas:** 11 categorias cobrindo desenvolvimento, arquitetura, design, devops, marketing e utilitários.
- **26 Servidores MCP Documentados:** Suporte para DevSync, OpenScreen, Shots Studio, Neon Postgres, Chrome DevTools, REA, Buffer, Notion, Apollo e outros.
- **Kit Universal Permanente (21 Pilares):** Enforce mandatório de TypeSafe AI (ADR-003) e filosofia anti-overengineering Ponytail (ADR-005).

#### 🛡️ Governança & CI/CD
- Pipeline automatizado de empacotamento e distribuição via GitHub Releases (`.github/workflows/release.yml`).
- Histórico transparente de decisões arquiteturais registradas em ADRs formais (`ADR-001` a `ADR-005`).
