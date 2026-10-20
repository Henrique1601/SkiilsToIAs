# ADR-001: Arquitetura dos 3 Pilares com Hub Híbrido e Git Master Obrigatório

## Status
**Aceito (Accepted)** — Alinhado via `/grill-me` e `/grill-with-docs` em 2026-10-20.

---

## Contexto & Problema
O ecossistema contém 12 Agentes Especialistas, 658 Skills locais (688 globais) e múltiplos servidores MCP. Havia a necessidade de clarificar e enrijecer como as chamadas entre as camadas ocorrem:
1. Como o `global-master-agent` aciona os especialistas.
2. Como os especialistas consomem suas skills e quando chamam o `skills-orchestrator`.
3. Como garantir que o **Kit Universal das 20 Skills** esteja sempre presente.
4. Como transformar o `git-master-agent` no ponto de convergência obrigatório ao final de qualquer tarefa ou pilar em qualquer projeto.
5. Como padronizar a catalogação de repositórios com descrições, tags e metadados no Git local e remoto (GitHub).

---

## Decisões Tomadas

### 1. Arquitetura das 3 Camadas
* **Camada 1 (Agentes & Orquestração):**
  * O `global-master-agent` é o ponto de contato supremo que comanda a mesa diretora dos 12 agentes.
  * O `skills-orchestrator` atua como Hub Central metodológico (9 Fases).
* **Camada 2 (Skills & Execução):**
  * **Padrão Híbrido:** Cada agente especialista executa diretamente suas skills nativas especializadas. Quando o agente necessitar de competências transversais ou do **Kit Universal Top 20**, ele consulta o `skills-orchestrator`, que redireciona e garante a execução das 658 skills.
* **Camada 3 (MCPs & Infraestrutura):**
  * Conexão com serviços de dados e APIs externas (Neon, Supabase, Buffer, Prospector CRM, DevSync, Chrome DevTools).

### 2. O Portão Obrigatório Final: Git Master Agent
* **Regra Fundamental:** Nenhuma tarefa ou pilar arquitetural é considerada concluída sem passar pelo `git-master-agent`.
* O `git-master-agent` é o meio principal de encerramento em **100% dos projetos**, executando:
  1. Verificação de integridade e `verification-loop`.
  2. Commit semântico convencional com guardrails ativos (`git-guardrails-claude-code`).
  3. Sincronização multi-máquina (`git pull --ff-only` e `git push`).
  4. Catalogação ativa do repositório.

### 3. Catalogação de Repositórios (Tags, Tópicos e Descrição)
* Em novos repositórios ou atualizações estruturais, o `git-master-agent` deve:
  * Gerar descrição clara e taxonomia de tópicos/tags no `README.md` e manifesto do projeto (`package.json`, `pyproject.toml`, etc.).
  * Se a CLI do GitHub (`gh`) estiver autenticada ou houver acesso à API, sincronizar diretamente a descrição e os tópicos com `gh repo edit --description "..." --add-topic "..."`.
  * Criar ou atualizar a documentação viva em Markdown.

---

## Consequências
* **Positivas:**
  * Fluxo unificado, previsível e à prova de falhas.
  * Zero perda de dados e commits padronizados em todos os projetos.
  * Preservação da economia de tokens com navegação híbrida pelas 658 skills.
* **Negativas / Cuidados:**
  * Requer rigor disciplinar em todos os agentes para sempre delegar o fechamento ao `git-master-agent`.
