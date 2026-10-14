# 🔌 Servidores MCP (Model Context Protocol)

O **Model Context Protocol (MCP)** é um padrão aberto que padroniza como agentes de Inteligência Artificial conectam-se com segurança a fontes de dados externas, APIs, bancos de dados e ferramentas locais e remotas.

Esta pasta centraliza os **servidores MCP recomendados, configurados e mantidos** no ecossistema de desenvolvimento, fornecendo documentação técnica, especificações de ferramentas (*tools*), esquemas de transporte e modelos de configuração prontos para uso.

---

## 🧭 Índice do Módulo MCP

* [📊 Catálogo de Servidores MCP](#-catálogo-de-servidores-mcp)
* [⚡ Modos de Transporte (Stdio vs. Streamable HTTP)](#-modos-de-transporte)
* [📁 Estrutura de Servidores Documentados](#-estrutura-de-servidores-documentados)
* [🚀 Como Configurar em Diferentes Ambientes](#-como-configurar-em-diferentes-ambientes)
  * [Google Antigravity / Gemini CLI](#1-google-antigravity--gemini-cli)
  * [Claude Desktop](#2-claude-desktop)
  * [Cursor IDE](#3-cursor-ide)
* [🛡️ Regras de Ouro de Segurança & Git](#-regras-de-ouro-de-segurança--git)
* [📄 Modelos de Configuração (Templates)](#-modelos-de-configuração-templates)

---

## 📊 Catálogo de Servidores MCP

| Identificador | Tipo / Transporte | Pacote / Endpoint | Descrição & Principais Ferramentas |
|---|:---:|---|---|
| 💼 [**`prospector-crm`**](prospector-crm/README.md) | **Streamable HTTP** (Remoto) | `https://api-prospector-delta.vercel.app/api/mcp` | Servidor proprietário do **Prospector CRM** conectado ao Neon Postgres (150+ leads). Expõe [`list_leads`](prospector-crm/README.md#list_leads) (filtro e busca) e [`create_leads`](prospector-crm/README.md#create_leads) (cadastro com desduplicação). |
| 🐘 [**`neon-postgres`**](neon-postgres/README.md) | **Remote SSE / Bridge** | `https://mcp.neon.tech/sse` | Gestão serverless de banco de dados PostgreSQL Neon, branching instantâneo de bancos, inspeção de schemas, migrations zero-downtime e tuning de queries. |
| 📝 [**`notion-mcp-server`**](notion/README.md) | **Stdio** (Local) | `@notionhq/notion-mcp-server` | Integração oficial com workspaces Notion. Leitura/escrita de páginas, manipulação de bancos de dados (*databases*), busca semântica e blocos de conteúdo. |
| 🌐 [**`chrome-devtools-mcp`**](chrome-devtools/README.md) | **Stdio** (Local) | `chrome-devtools-mcp@latest` | Inspeção e controle de browser headless/real. Captura de screenshots, inspeção do console/rede, auditoria Lighthouse e execução de scripts na página. |
| 🔬 [**`rea`**](rea/README.md) | **Stdio** (Local) | `rea-agents@6.0.0` | Engenharia reversa avançada, inspeção e desmontagem de binários nativos (x86/x64/ARM), análise de grafos de chamadas e auditoria de segurança. |
| 🧠 **`ai-memory`** | **Streamable HTTP** (Local) | `http://127.0.0.1:49374/mcp` | Servidor de memória semântica persistente entre sessões, grafo de conhecimento e notas operacionais de contexto. |
| 🎨 **`lovable`** | **Streamable HTTP** (Remoto) | `https://mcp.lovable.dev` | Plataforma de prototipagem rápida e desenvolvimento web assistido por IA. |

---

## ⚡ Modos de Transporte

Os servidores MCP operam primariamente em dois modos de comunicação:

### 1. Stdio (Standard Input/Output)
* **Como funciona:** O cliente MCP (Cursor, Claude Desktop, Antigravity) inicia um subprocesso local (`node`, `npx`, `python`, binário) e troca mensagens JSON-RPC 2.0 através da entrada e saída padrão (`stdin` / `stdout`).
* **Vantagens:** Execução 100% local, latência ultrabaixa, as credenciais residem apenas no ambiente local e não saem da máquina.
* **Exemplo:** `chrome-devtools-mcp`, `notion-mcp-server`, `rea`.

### 2. Streamable HTTP (Remoto)
* **Como funciona:** O servidor MCP roda como um serviço web HTTP acessível pela rede (`/api/mcp`), utilizando requisições POST com suporte a streaming de eventos (`text/event-stream` / `application/json`).
* **Vantagens:** O servidor é atualizado na nuvem (ex: Vercel, Fly.io, Cloudflare) sem precisar que cada desenvolvedor reinstale nada na máquina local; ferramentas centralizadas e bancos de dados em nuvem.
* **Exemplo:** `prospector-crm`, `neon-postgres`.

---

## 📁 Estrutura de Servidores Documentados

Cada servidor possui um subdiretório dedicado com documentação completa:

```text
mcps/
├── README.md                          # Este catálogo geral e guia de uso
├── prospector-crm/
│   └── README.md                      # Documentação do CRM, schema das tools e autenticação
├── neon-postgres/
│   └── README.md                      # Documentação do Neon Serverless Postgres
├── notion/
│   └── README.md                      # Documentação do Notion MCP oficial
├── chrome-devtools/
│   └── README.md                      # Documentação de automação de browser
├── rea/
│   └── README.md                      # Documentação de engenharia reversa e análise de binários
└── templates/
    ├── antigravity-mcp_config.json.example  # Exemplo pronto para Google Antigravity
    ├── claude_desktop_config.json.example   # Exemplo pronto para Claude Desktop
    └── cursor_mcp.json.example              # Exemplo pronto para Cursor IDE
```

---

## 🚀 Como Configurar em Diferentes Ambientes

### 1. Google Antigravity / Gemini CLI

O Antigravity gerencia os servidores MCP globais através do arquivo:
`~/.gemini/config/mcp_config.json` (ou no Windows: `C:\Users\<usuario>\.gemini\config\mcp_config.json`).

Estrutura recomendada:
```json
{
  "mcpServers": {
    "prospector-crm": {
      "url": "https://api-prospector-delta.vercel.app/api/mcp",
      "headers": {
        "Authorization": "Bearer SUA_CHAVE_AQUI"
      }
    },
    "chrome-devtools-mcp": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    },
    "notion-mcp-server": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "OPENAPI_MCP_HEADERS": "{\"Authorization\": \"Bearer SUA_NOTION_KEY\", \"Notion-Version\": \"2022-06-28\"}"
      }
    },
    "rea": {
      "command": "npx",
      "args": ["-y", "rea-agents@6.0.0", "mcp"]
    }
  }
}
```

---

### 2. Claude Desktop

No Claude Desktop, o arquivo de configuração localiza-se em:
* **Windows:** `%APPDATA%\Claude\claude_desktop_config.json` (`C:\Users\<usuario>\AppData\Roaming\Claude\claude_desktop_config.json`)
* **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

Estrutura:
```json
{
  "mcpServers": {
    "prospector-crm": {
      "url": "https://api-prospector-delta.vercel.app/api/mcp",
      "headers": {
        "Authorization": "Bearer SUA_CHAVE_AQUI"
      }
    },
    "rea": {
      "command": "npx",
      "args": ["-y", "rea-agents@6.0.0", "mcp"]
    }
  }
}
```

---

### 3. Cursor IDE

No Cursor:
1. Abra as **Settings** (`Ctrl + ,` ou `Cmd + ,`).
2. Acesse **Features** > **MCP Servers**.
3. Clique em **Add New MCP Server**.
4. Configure como `http`:
   * **Name:** `prospector-crm`
   * **Type:** `http`
   * **URL:** `https://api-prospector-delta.vercel.app/api/mcp`
   * **Headers:** `{"Authorization": "Bearer SUA_CHAVE_AQUI"}`

Ou via arquivo `.cursor/mcp.json` na raiz do projeto:
```json
{
  "mcpServers": {
    "prospector-crm": {
      "url": "https://api-prospector-delta.vercel.app/api/mcp",
      "headers": {
        "Authorization": "Bearer SUA_CHAVE_AQUI"
      }
    }
  }
}
```

---

## 🛡️ Regras de Ouro de Segurança & Git

> [!CAUTION]
> **NUNCA COMITE CHAVES DE API REAIS NO GITHUB!**
> Repositórios públicos e privados são escaneados em segundos por robôs de credenciais vazadas.

1. **Use sempre Placeholders em Documentos:** Em qualquer arquivo rastreado pelo Git, utilize `SUA_CHAVE_AQUI`, `${INTEGRATION_API_KEY}` ou `ntn_...`.
2. **Arquivos `.env` Protegidos:** Mantenha credenciais reais em arquivos `.env.local` ou nas configurações do seu cliente MCP no diretório de usuário (fora de repositórios git).
3. **Auditoria com o Agente Git:** O [`git-master-agent`](../custom-agents/git-master-agent.md) realiza auditoria pré-commit automática para barrar commits com tokens, senhas ou arquivos de ambiente indevidos.

---

## 📄 Modelos de Configuração (Templates)

Consulte a pasta [`templates/`](templates/) para arquivos `.example` prontos para copiar e colar para cada cliente:
* [`templates/antigravity-mcp_config.json.example`](templates/antigravity-mcp_config.json.example)
* [`templates/claude_desktop_config.json.example`](templates/claude_desktop_config.json.example)
* [`templates/cursor_mcp.json.example`](templates/cursor_mcp.json.example)
