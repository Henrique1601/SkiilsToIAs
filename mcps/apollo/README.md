# 🎯 Apollo.io MCP Server

O servidor MCP oficial do **Apollo.io** conecta o ecossistema de agentes diretamente ao maior banco de dados de inteligência B2B, enriquecimento de leads e prospecção de vendas do mundo (mais de 275 milhões de contatos e 73 milhões de empresas).

---

## ⚙️ Configuração

### 1. Antigravity IDE / Gemini CLI
Adicione ao seu `~/.gemini/config/mcp_config.json`:
```json
{
  "mcpServers": {
    "apollo": {
      "serverUrl": "https://mcp.apollo.io/mcp",
      "headers": {
        "X-Api-Key": "SUA_CHAVE_API_APOLLO_AQUI"
      }
    }
  }
}
```

> **Nota de Autenticação:** O servidor MCP do Apollo suporta autenticação via header `X-Api-Key` com sua chave de API do Apollo.io ou fluxo OAuth Bearer token.

### 2. Claude CLI / Claude Desktop
Adicione ao seu `%APPDATA%\Claude\claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "apollo": {
      "type": "http",
      "url": "https://mcp.apollo.io/mcp",
      "headers": {
        "X-Api-Key": "SUA_CHAVE_API_APOLLO_AQUI"
      }
    }
  }
}
```

---

## 🛠️ Principais Capacidades

- 🔍 **Busca de Pessoas & Leads:** Filtro granular por cargo, senioridade, localização, setor e palavras-chave.
- 🏢 **Enriquecimento de Empresas:** Dados firmográficos completos (tamanho, receita estimada, tecnologias utilizadas, funding).
- 📧 **Enriquecimento de E-mails & Telefones:** Obtenção de e-mails corporativos verificados e números diretos.
- 🎯 **Integração de Outbound:** Handoff de leads qualificados diretamente para cadências de e-mail e CRM.

---

## 🤝 Integração com Agentes Especialistas

- 💼 **`prospector-crm`**: Combina a base do Apollo para abastecer automaticamente os leads do seu CRM no Neon Postgres.
- 📈 **`growth-marketing-agent`**: Pesquisa de ICP (Ideal Customer Profile), enriquecimento de contas-alvo para campanhas de Account-Based Marketing (ABM) e cold email.
- 📋 **`planning-master-agent`**: Validação de mercado e tamanho de oportunidade (TAM/SAM).
