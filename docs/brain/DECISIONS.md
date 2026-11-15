# 🏛️ Histórico de Decisões Arquiteturais (DECISIONS)

Este documento centraliza as decisões duráveis do projeto:

- **ADR-001:** Arquitetura em 3 Pilares (Orquestração, Conhecimento, MCPs) e Portão Obrigatório Final com `git-master-agent`.
- **ADR-002:** Arquitetura Double-Gate (Portão 0 remoto preventivo multi-PC + Portão Final de fechamento).
- **ADR-003:** Padrão Ouro Institucional (README com Quick Links e logo oficial, Releases v1.0.0+ automáticas, `.env.example`, `CHANGELOG.md` e TypeSafe AI mandatório).
- **ADR-004:** Pipeline Obrigatório em 5 Fases do Global Master Agent (Portão 0 ➔ Segundo Cérebro ➔ Planejamento/Grill-Me ➔ Hub de Execução ➔ Portão Final).
- **ADR-005:** Elevação da Suíte Ponytail ao Kit Universal Permanente (Anti-overengineering estrito, YAGNI e menor código possível em qualquer situação).
- **ADR-006:** Ecossistema Executável Zero-Dependência (Motor RAG local SQLite FTS5/BM25 + `pgvector` opcional, CLI `bootstrap_project.py`, auditoria CI `audit_repo.py`, catálogo estático publicado no Netlify e orquestrador único `sync_all.py`).
