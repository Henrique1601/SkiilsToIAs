# 🤖 Custom Agents (`custom-agents/`)

> **Repositório central de Agentes Especialistas e Orquestradores para ecossistemas de Inteligência Artificial.**

Enquanto as **skills** (distribuídas nas 11 categorias deste repositório) representam as *ferramentas e capacidades atômicas* ("o que pode ser feito"), os **agentes** definidos nesta pasta representam os *operadores e líderes de engenharia* ("quem executa, planeja e coordena").

---

## 📋 Agentes Disponíveis

| Agente | Arquivo | Descrição |
| :--- | :--- | :--- |
| **`skills-orchestrator`** (Agente Mestre) | [`skills-orchestrator.md`](skills-orchestrator.md) | Orquestrador mestre das 509 skills. Conduz qualquer projeto técnico ou de negócio com metodologia em 9 fases (da ideação ao go-to-market), diagnosticando a fase atual e indicando a skill certa com o prompt exato. |

---

## 🚀 Como Instalar e Usar os Agentes

### 1. No Google Antigravity / Gemini CLI (Nativo)

Copie o arquivo `.md` do agente para a pasta global de agentes do Gemini:

```bash
# Windows (PowerShell):
Copy-Item custom-agents\skills-orchestrator.md "$HOME\.gemini\config\agents\"

# Linux / macOS:
cp custom-agents/skills-orchestrator.md ~/.gemini/config/agents/
```

O Antigravity detecta o agente automaticamente. Para ativá-lo em qualquer sessão, basta solicitar:
```markdown
"Ative o skills-orchestrator para planejar e guiar meu projeto [NOME DO PROJETO]"
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
