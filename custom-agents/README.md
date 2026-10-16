# 🤖 Custom Agents (`custom-agents/`)

> **Repositório central de Agentes Especialistas e Orquestradores para ecossistemas de Inteligência Artificial.**

Enquanto as **skills** (distribuídas nas 11 categorias deste repositório) representam as *ferramentas e capacidades atômicas* ("o que pode ser feito"), os **agentes** definidos nesta pasta representam os *operadores e líderes de engenharia* ("quem executa, planeja e coordena").

---

## 📋 Agentes Disponíveis

| Agente | Arquivo | Descrição |
| :--- | :--- | :--- |
| 👑 **`global-master-agent`** (Agente Global Supremo) | [`global-master-agent.md`](global-master-agent.md) | **Ponto único de comando e entrada.** Você só precisa chamar ele: ele orquestra nos bastidores todos os outros 11 agentes e as 512 skills do repositório. |
| 🎯 **`skills-orchestrator`** (Agente Mestre de Projetos) | [`skills-orchestrator.md`](skills-orchestrator.md) | Orquestrador mestre das 512 skills (542 globais). Conduz qualquer projeto técnico ou de negócio com metodologia em 9 fases (da ideação ao go-to-market). |
| 🛡️ **`git-master-agent`** (Agente Mestre de Git & GitHub) | [`git-master-agent.md`](git-master-agent.md) | Especialista em backups preventivos (`backup/checkpoint-...`), Conventional Commits seguros, bootstrap de novos projetos (README, MIT License, .gitignore) e sincronização multi-máquina (PC Trabalho vs. PC Pessoal). |
| 🎨 **`design-engineer-agent`** (Engenheiro de UI/UX) | [`design-engineer-agent.md`](design-engineer-agent.md) | Interfaces refinadas, microinterações, Framer Motion, layouts bento-grid, acessibilidade WCAG 2.2 e design anti-template. |
| 🛡️ **`security-auditor-agent`** (Auditor de Segurança) | [`security-auditor-agent.md`](security-auditor-agent.md) | Auditoria defensiva/ofensiva OWASP Top 10, autenticação segura (JWT/OAuth), proteção contra injection e bloqueio de vazamento de secrets. |
| 🗄️ **`database-architect-agent`** (Arquiteto de Banco) | [`database-architect-agent.md`](database-architect-agent.md) | Modelagem relacional e NoSQL (Postgres, Supabase, Neon, Mongo), migrations seguras, otimização de queries lentas e cache Redis. |
| 🧪 **`qa-testing-agent`** (Engenheiro de Testes & TDD) | [`qa-testing-agent.md`](qa-testing-agent.md) | Cultura TDD (Red-Green-Refactor), testes unitários e de integração sem flakiness, e automação end-to-end com Playwright. |
| ☁️ **`devops-cloud-agent`** (Arquiteto Cloud & Deploy) | [`devops-cloud-agent.md`](devops-cloud-agent.md) | Dockerfiles multi-stage ultraleves, compose, pipelines CI/CD no GitHub Actions, deploys na Vercel/Cloudflare/Azure e auditoria de produção. |
| 🤖 **`ai-engineer-agent`** (Engenheiro de IA & Agentes) | [`ai-engineer-agent.md`](ai-engineer-agent.md) | Desenvolvimento de agentes autônomos, servidores MCP, saídas estruturadas tipadas (TypeSafe AI), controle de custos de tokens e RAG sem alucinação. |
| 📈 **`growth-marketing-agent`** (Estrategista de Growth) | [`growth-marketing-agent.md`](growth-marketing-agent.md) | SEO técnico (Core Web Vitals nota 90+), posts magnéticos para LinkedIn, sequências de e-mail de onboarding e propostas comerciais. |
| 🎬 **`video-producer-agent`** (Produtor de Vídeos Remotion) | [`video-producer-agent.md`](video-producer-agent.md) | Produção programática de vídeos com React/Remotion, kinetic typography, legendas automáticas, áudio sincronizado e teasers de SaaS. |
| 🐙 **`github-profile-agent`** (Especialista em Perfil do GitHub) | [`github-profile-agent.md`](github-profile-agent.md) | Otimização do perfil público (`username/username`), README dinâmico, badges visuais, métricas em tempo real e curadoria de pinned repos. |

---

## 🌐 Sinergia Operacional: Rede Conectada (Full-Mesh) & Kit Universal

Todos os **12 Agentes** estão interconectados em malha (*Full-Mesh*) através do **`skills-orchestrator`** e comandados pelo **`global-master-agent`**. Dependendo do projeto, os agentes inspecionam **o que o projeto já tem** e **o que precisa**, selecionando as melhores skills das 512 disponíveis em conjunto com o **Kit Universal Obrigatório de 10 Skills & MCPs**:

```mermaid
flowchart TD
    User["👤 Usuário (Comando Único)"] --> GMA["👑 global-master-agent<br/>(Comandante Supremo & Ponto de Entrada Único)"]

    GMA <--> Orch["🎯 skills-orchestrator<br/>(Hub Central: 9 Fases + 512 Skills + 10 Universais)"]
    GMA <--> GitMaster["🛡️ git-master-agent<br/>(Backups, Commits, Sync Multi-PC)"]

    Orch <--> UI["🎨 design-engineer-agent"]
    Orch <--> DB["🗄️ database-architect-agent"]
    Orch <--> AI["🤖 ai-engineer-agent"]
    Orch <--> QA["🧪 qa-testing-agent"]
    Orch <--> Sec["🛡️ security-auditor-agent"]
    Orch <--> DevOps["☁️ devops-cloud-agent"]
    Orch <--> Growth["📈 growth-marketing-agent"]
    Orch <--> Video["🎬 video-producer-agent"]
    Orch <--> Profile["🐙 github-profile-agent"]

    DB <--> Sec
    UI <--> QA
    QA <--> DevOps
    DevOps <--> Growth
    DevOps <--> GitMaster
```

### 🔥 Kit Universal Obrigatório (Top 20 Skills & MCPs em Todos os Agentes e Projetos)

| # | Ferramenta / Pilar | Skills Nativas & MCPs Associados | Função Transversal em Qualquer Projeto |
| :---: | :--- | :--- | :--- |
| **1** | 🧠 **Brainstorm** | `brainstorming` | Ideação criativa e exploração de requisitos ocultos antes de codificar. |
| **2** | 🔥 **Grill Me** | `grill-me`, `grill-with-docs` | Sabatina implacável para encontrar furos de lógica, produto e arquitetura. |
| **3** | 🏛️ **Architecture** | `architecture`, `architecture-decision-records`, `hexagonal-architecture` | Desenho de arquitetura limpa, desacoplamento e registro formal de ADRs. |
| **4** | 📚 **Context7** | `context7-mcp`, `context7-cli` | Documentação oficial em tempo real para zero código alucinado ou defasado. |
| **5** | 💎 **Obsidian** | `obsidian-vault`, `obsidian-markdown` | Gestão de conhecimento persistente (*Second Brain*), wikilinks e notas. |
| **6** | 🪨 **Caveman** | `caveman`, `caveman-commit`, `caveman-review`, `caveman-compress` | Economia extrema de tokens, concisão cirúrgica e commits diretos. |
| **7** | 🔍 **Code Review** | `code-review`, `caveman-review` | Revisão estática e estrutural rigorosa (SOLID, DRY, segurança e tipagem). |
| **8** | 🌐 **Agente Browser** | `agent-browser`, `browser-qa`, `webapp-testing` + `chrome-devtools-mcp` | Navegação autônoma, inspeção visual de UI/DOM e testes interativos no browser. |
| **9** | 🚨 **Lighthouse** | `lighthouse`, `performance` + `chrome-devtools-mcp` | Auditoria contínua de Performance, Acessibilidade, SEO e Core Web Vitals (90+). |
| **10** | ▲ **Vercel** | `deploy-to-vercel`, `vercel-react-best-practices`, `vercel-composition-patterns` | Boas práticas de engenharia React/Next.js e deploy contínuo na Vercel. |
| **11** | 🛡️ **Security & Data Guard** | `security-review`, `accidental-data-loss-prevention` | Proteção OWASP, zero vazamento de secrets (`.env`) e prevenção contra perda de dados. |
| **12** | 🔄 **Verification Loop** | `verification-loop` | Loop automático (`build` + `typecheck` + `lint` + `test`) antes de concluir entregas. |
| **13** | 🧪 **TDD Workflow** | `tdd-workflow`, `tdd` | Ciclo *Red-Green-Refactor* com meta de 80%+ de cobertura e zero regressões. |
| **14** | 🎨 **Design Taste & Polish** | `design-taste-frontend`, `emil-design-eng` | Estética premium anti-template e microinterações nível Linear/Stripe/Apple. |
| **15** | 📝 **Write Spec (PRD)** | `write-spec` | Especificação técnica formal e critérios de aceite claros após o `grill-me`. |
| **16** | 🔎 **Search First & Repo Scan** | `search-first`, `repo-scan` | Auditoria do código existente e busca de soluções prontas antes de reinventar a roda. |
| **17** | 🧱 **Coding Standards & Errors** | `coding-standards`, `error-handling` | Padronização de código limpo, imutabilidade, erros tipados e retries resilientes. |
| **18** | 🗄️ **Postgres & Migrations** | `postgres-patterns`, `database-migrations` + MCPs `supabase` / `Neon` | Schemas relacionais com RLS, índices estratégicos e migrações zero-downtime. |
| **19** | 🤖 **TypeSafe & Cost-Aware AI** | `typesafe-ai`, `cost-aware-llm-pipeline` | Schemas validados (Zod/JSON) para IA e roteamento inteligente de custos de tokens. |
| **20** | 🚀 **Production & SEO Audit** | `production-audit`, `seo-audit` | Checklist pré/pós-lançamento: variáveis de produção, HTTPS, OpenGraph e indexação. |

1. **Diagnóstico "O Que Tem vs. O Que Precisa":** Ao entrar em qualquer projeto, o `skills-orchestrator` analisa os arquivos existentes e aciona os agentes especialistas necessários.
2. **Proteção Automática:** O `git-master-agent` garante checkpoints de backup e sincronização multi-máquinas antes e depois de qualquer alteração.
3. **Execução Conectada:** Os agentes colaboram horizontalmente (ex: `design-engineer-agent` ➡️ `qa-testing-agent` com `agent-browser` ➡️ `devops-cloud-agent` com `deploy-to-vercel` ➡️ `growth-marketing-agent` com `lighthouse`).

---

## 🚀 Como Instalar e Usar os Agentes

### 1. No Google Antigravity / Gemini CLI (Nativo)

O Antigravity suporta os Agentes tanto como **Skills Nativas** (recomendado para auto-descoberta) quanto como **Agentes Customizados**:

```bash
# Windows (PowerShell):
# 1. Copiar todos os 12 Agentes Customizados para o Gemini:
Copy-Item custom-agents\*.md "$HOME\.gemini\config\agents\" -Force

# 2. Espelhar as pastas de skills dos agentes (Auto-descoberta nativa):
Get-ChildItem -Directory custom-agents | ForEach-Object {
    New-Item -ItemType Directory -Force -Path "$HOME\.gemini\config\skills\$($_.Name)"
    Copy-Item "$($_.FullName)\SKILL.md" "$HOME\.gemini\config\skills\$($_.Name)\SKILL.md" -Force
}

# Linux / macOS:
cp custom-agents/*.md ~/.gemini/config/agents/
for d in custom-agents/*/; do
    name=$(basename "$d")
    mkdir -p ~/.gemini/config/skills/"$name"
    cp "$d/SKILL.md" ~/.gemini/config/skills/"$name"/SKILL.md 2>/dev/null || true
done
```

O Antigravity detecta as skills/agentes automaticamente. Para ativá-los em qualquer sessão:
```markdown
# 👑 RECOMENDADO: Ative apenas o Agente Supremo (ele cuida de tudo):
"Ative o global-master-agent para conduzir meu projeto [NOME DO PROJETO]"
"Ative o global-master-agent e implemente a funcionalidade [X]"

# Ou ative os agentes específicos se preferir controle manual:
"Ative o skills-orchestrator para planejar e guiar meu projeto"
"Ative o git-master-agent para salvar minhas alterações com backup e commit seguro"
```

---

### 2. No Claude Code

Copie a definição para o diretório de configuração do Claude ou use como persona de projeto:

```bash
# Global
cp custom-agents/skills-orchestrator.md ~/.claude/agents/

# Ou no projeto local
cp custom-agents/skills-orchestrator.md .claude/agents/
```

---

### 3. No Cursor / VS Code / Copilot CLI

Você pode importar o conteúdo do agente no seu `.cursorrules` ou prompt de sistema:
1. Abra o arquivo [`skills-orchestrator.md`](skills-orchestrator.md).
2. Copie o conteúdo abaixo do cabeçalho YAML.
3. Cole nas instruções de sistema (System Prompt / Custom Instructions) do seu assistente.

---

## 🛠️ Como Criar Novos Agentes nesta Pasta

Para adicionar um novo agente especialista (ex: `frontend-expert.md`, `security-auditor.md`, `devops-architect.md`):

1. Crie um arquivo `.md` com o frontmatter padrão:
   ```yaml
   ---
   name: meu-novo-agente
   description: "Breve resumo do propósito do agente e quando ativá-lo."
   ---
   ```
2. Defina o papel (*Persona*), a missão, as diretrizes de pensamento e quais skills ele deve acionar prioritariamente.
3. Adicione o novo agente à tabela deste `README.md`.
