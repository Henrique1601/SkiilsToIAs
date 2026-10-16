# 🔄 DevSync MCP Server (`devsync`)

> **Servidor Model Context Protocol (MCP) nativo do DevSync v0.4.0**  
> Desenvolvido por Henrique Bezerra Dos Santos para sincronização e coordenação Git multi-máquina (Casa vs. Trabalho) controlada diretamente por agentes de IA.

---

## 🎯 1. Visão Geral

O **DevSync MCP Server** expõe as operações centrais do DevSync através do protocolo padrão MCP (JSON-RPC 2.0 via `stdio`). Permite que o [`git-master-agent`](../../custom-agents/git-master-agent.md), o [`skills-orchestrator`](../../custom-agents/skills-orchestrator.md) e o [`global-master-agent`](../../custom-agents/global-master-agent.md) monitorem o estado de sincronização, inspecionem diffs sem expor segredos e executem sincronizações atômicas diretamente durante as sessões de desenvolvimento.

- **Localização do Código Fonte:** `C:\Users\henri\Programacao\Projetos\devsync`
- **Ponto de Entrada do Servidor:** `C:\Users\henri\Programacao\Projetos\devsync\src\cli.js mcp`
- **Versão:** `0.4.0`
- **Protocol Version:** `2024-11-05`
- **Transport:** `stdio` (Node.js nativo sem dependências externas)

---

## 🛠️ 2. Ferramentas Disponíveis (MCP Tools)

| Tool Name | Parâmetros | Descrição |
| :--- | :--- | :--- |
| `devsync_status` | *(nenhum)* | Lista todos os projetos cadastrados no DevSync, branches, status Git (`synced`, `dirty`, `ahead`, `behind`, `diverged`, `paused`) e estado do painel/coordenador remoto. |
| `devsync_sync` | `id` *(string, obrigatório)* | Sincroniza imediatamente um projeto cadastrado pelo ID ou nome (fast-forward seguro e auto-push se habilitado). |
| `devsync_sync_all` | *(nenhum)* | Sincroniza em lote todos os projetos ativos (não pausados) cadastrados no computador. |
| `devsync_diff` | `id` *(string, obrigatório)* | Inspeciona arquivos modificados, commits pendentes e diff sanitizado (ocultando segredos como `.env`, `*.key`, `*.pem`). |
| `devsync_stash_sync` | `id` *(string)*, `pop` *(boolean, opcional, padrão: true)* | Guarda alterações pendentes em Stash seguro, sincroniza com o remoto e opcionalmente reaplica as alterações locais. |
| `devsync_diagnose` | `path` *(string, obrigatório)* | Verifica sem mutações se uma pasta possui repositório Git válido, branch ativa, upstream, commits e identidade. |
| `devsync_history` | `projectId` *(string, opcional)*, `limit` *(int, padrão: 25)* | Consulta o histórico persistente em SQLite de sincronizações e eventos do DevSync. |
| `devsync_pause_resume` | `id` *(string)*, `action` *(enum: 'pause' \| 'resume')* | Pausa ou retoma o monitoramento e sincronização automática de um projeto. |

---

## ⚙️ 3. Configuração nos Clientes MCP

### Antigravity / Gemini CLI (`~/.gemini/config/mcp_config.json`)

```json
{
  "mcpServers": {
    "devsync": {
      "command": "node",
      "args": [
        "C:\\Users\\henri\\Programacao\\Projetos\\devsync\\src\\cli.js",
        "mcp"
      ]
    }
  }
}
```

### Claude Desktop / Claude Code (`claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "devsync": {
      "command": "node",
      "args": [
        "C:\\Users\\henri\\Programacao\\Projetos\\devsync\\src\\cli.js",
        "mcp"
      ]
    }
  }
}
```

### Cursor (`.cursor/mcp.json`)

```json
{
  "mcpServers": {
    "devsync": {
      "command": "node",
      "args": [
        "C:\\Users\\henri\\Programacao\\Projetos\\devsync\\src\\cli.js",
        "mcp"
      ]
    }
  }
}
```

---

## 🤝 4. Integração com os Agentes Customizados

- **[`git-master-agent`](../../custom-agents/git-master-agent.md):** Utiliza o `devsync_status` e `devsync_diff` no **Protocolo 5 (Sincronização Multi-Máquina)** para comparar estados do PC Casa vs. PC Trabalho sem conflitos, e executa `devsync_stash_sync` quando há alterações locais não salvas.
- **[`skills-orchestrator`](../../custom-agents/skills-orchestrator.md):** Usa o `devsync_diagnose` no **Passo 1 do Diagnóstico Dinâmico ("O Que Tem vs. O Que Precisa")** para validar a integridade de branches e repositórios.
- **[`global-master-agent`](../../custom-agents/global-master-agent.md):** Permite ao usuário rodar *"Sincroniza todos os meus projetos"* disparando `devsync_sync_all` em lote.
