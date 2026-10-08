# 🤖 Custom Agents (`custom-agents/`)

> **Repositório central de Agentes Especialistas e Orquestradores para ecossistemas de Inteligência Artificial.**

Enquanto as **skills** (distribuídas nas 11 categorias deste repositório) representam as *ferramentas e capacidades atômicas* ("o que pode ser feito"), os **agentes** definidos nesta pasta representam os *operadores e líderes de engenharia* ("quem executa, planeja e coordena").

---

## 📋 Agentes Disponíveis

| Agente | Arquivo | Descrição |
| :--- | :--- | :--- |
| 👑 **`global-master-agent`** (Agente Global Supremo) | [`global-master-agent.md`](global-master-agent.md) | **Ponto único de comando e entrada.** Você só precisa chamar ele: ele orquestra nos bastidores todos os outros 11 agentes e as 511 skills do repositório. |
| 🎯 **`skills-orchestrator`** (Agente Mestre de Projetos) | [`skills-orchestrator.md`](skills-orchestrator.md) | Orquestrador mestre das 511 skills (541 globais). Conduz qualquer projeto técnico ou de negócio com metodologia em 9 fases (da ideação ao go-to-market). |
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

## 🤝 Sinergia Operacional: Hierarquia de Comando

O ecossistema é organizado de forma hierárquica para eliminar esforço cognitivo do desenvolvedor:

```mermaid
flowchart TD
    User["👤 Usuário (Comando Único)"] --> GMA["👑 global-master-agent<br/>(Comandante Supremo & Ponto de Entrada Único)"]

    GMA -->|"1. Versionamento, Backups & Sincronização"| GitMaster["🛡️ git-master-agent<br/>- Checkpoint preventivo antes de mexer<br/>- Conventional Commits e Push<br/>- Sync PC Trabalho vs PC Pessoal"]
    
    GMA -->|"2. Metodologia, Arquitetura & Fases"| Orch["🎯 skills-orchestrator<br/>- 9 Fases do Ciclo de Vida<br/>- Diagnóstico da fase atual<br/>- Prescrição do pipeline de skills"]

    GMA -.->|"3. Especialistas Verticais Adicionais"| Future["🤖 Novos Agentes Customizados<br/>(ex: security-agent, devops-agent)"]

    GitMaster --> Skills["🧰 511 Skills Especializadas em 11 Categorias"]
    Orch --> Skills
```

1. **Chamada Única:** Em vez de lembrar qual agente acionar, você simplesmente conversa com o **`global-master-agent`**.
2. **Proteção Automática:** Ele aciona o `git-master-agent` para garantir checkpoints de backup e sincronização multi-máquinas antes de qualquer alteração.
3. **Execução Metódica:** Ele aciona o `skills-orchestrator` para conduzir as 9 fases e selecionar as skills ideais entre as 511 disponíveis.
4. **Entrega Blindada:** Ele aciona o `git-master-agent` para auditar secrets, rodar o `verification-loop`, fazer o commit convencional e enviar ao GitHub.

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
