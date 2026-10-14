# 💼 Prospector CRM — Servidor MCP

Servidor proprietário de **Model Context Protocol (MCP)** para integração do **Prospector CRM** com agentes de Inteligência Artificial autônomos.

Permite que agentes pesquisem o funil de vendas, consultem clientes existentes para evitar duplicidade de abordagem e realizem ingestão automatizada de novos leads qualificados via Google Maps, scraping ou prospecção ativa.

---

## 📌 Metadados Técnicos

* **Nome do Servidor (`serverName`):** `prospector-crm`
* **Versão:** `1.0.0`
* **Protocolo:** MCP Specification 2024-11-05 / 2025-03-26 (JSON-RPC 2.0)
* **Transporte:** Streamable HTTP (`POST /api/mcp`)
* **Endpoint de Produção:** `https://api-prospector-delta.vercel.app/api/mcp`
* **Endpoint de Status:** `https://api-prospector-delta.vercel.app/api/mcp/status`
* **Endpoint de Teste:** `https://api-prospector-delta.vercel.app/api/mcp/test-connection`
* **Banco de Dados:** Neon Serverless PostgreSQL (tabela relacional com 150+ leads)
* **Autenticação:** Header HTTP `Authorization: Bearer <INTEGRATION_API_KEY>` (verificação criptográfica segura via `timingSafeEqual`)

---

## 🛠️ Ferramentas Disponíveis (*Tools*)

### 1. `list_leads`
Consulta leads já cadastrados no CRM para checar histórico, notas de reuniões, demos geradas e evitar duplicações de prospecção.

* **Anotações:** `readOnlyHint: true`, `destructiveHint: false`, `idempotentHint: true`
* **Parâmetros (`inputSchema`):**
  * `query` *(string, opcional)*: Termo de busca livre (filtra por nome da empresa, segmento ou cidade).
  * `stage` *(enum, opcional)*: Estágio do funil de vendas. Opções:
    * `"new"` (Novo lead descoberto)
    * `"analyzed"` (Diagnóstico de IA concluído)
    * `"contacted"` (Primeiro contato realizado via WhatsApp/E-mail)
    * `"replied"` (Lead respondeu à abordagem)
    * `"meeting"` (Reunião agendada)
    * `"proposal"` (Proposta comercial enviada)
    * `"won"` (Contrato fechado / Ganho)
    * `"lost"` (Lead perdido / Não qualificado)
  * `limit` *(integer, padrão: 25, mín: 1, máx: 100)*: Quantidade máxima de registros a retornar.

#### Exemplo de Chamada:
```json
{
  "name": "list_leads",
  "arguments": {
    "query": "odontologia santos",
    "stage": "new",
    "limit": 10
  }
}
```

---

### 2. `create_leads`
Cadastra em lote de 1 a 25 leads qualificados no CRM. O servidor realiza desduplicação automática comparando o link do Google Maps, número de WhatsApp/telefone e nome normalizado por cidade.

* **Anotações:** `readOnlyHint: false`, `destructiveHint: false`, `idempotentHint: true`
* **Parâmetros (`inputSchema`):**
  * `leads` *(array de objetos, obrigatório, de 1 a 25 itens)*:
    * `name` *(string, obrigatório)*: Razão social ou nome fantasia da empresa.
    * `segment` *(string, obrigatório)*: Nicho de atuação (ex: `"Odontologia"`, `"Restaurante"`, `"Clínica Médica"`).
    * `city` *(string, obrigatório)*: Cidade de localização (ex: `"Santos"`).
    * `state` *(string, padrão: `"SP"`)*: Unidade federativa.
    * `address` *(string, opcional)*: Endereço completo.
    * `mapsUrl` *(string, opcional)*: Link de localização no Google Maps.
    * `website` *(string, opcional)*: URL do website existente (se houver).
    * `phone` *(string, opcional)*: Telefone formatado.
    * `whatsappUrl` *(string, opcional)*: Link direto `https://wa.me/55...` com número validado.
    * `hasWhatsapp` *(boolean, opcional)*: Flag indicando WhatsApp verificado.
    * `demoUrl` *(string, opcional)*: Link da demo visual gerada.
    * `siteStatus` *(enum, opcional)*: `"unknown"` | `"none"` | `"weak"` | `"good"`
    * `digitalPresence` *(enum, opcional)*: `"unknown"` | `"low"` | `"medium"` | `"high"`
    * `opportunity` *(string, opcional)*: Oportunidade identificada na auditoria.
    * `reason` *(string, opcional)*: Motivo da qualificação.
    * `suggestedMessage` *(string, opcional)*: Script de abordagem inicial sugerido pela IA.
    * `nextAction` *(string, opcional)*: Próxima ação recomendada.
    * `priority` *(enum, opcional)*: `"low"` | `"medium"` | `"high"` | `"urgent"`
    * `score` *(integer, opcional, 0 a 100)*: Pontuação de propensão de compra.
    * `sources` *(array de strings, opcional)*: Fontes de prospecção (ex: `["MCP", "Google Maps"]`).
  * `autoAnalyze` *(boolean, padrão: false)*: Se `true`, dispara análise técnica imediata pós-cadastro.

#### Exemplo de Chamada:
```json
{
  "name": "create_leads",
  "arguments": {
    "leads": [
      {
        "name": "Clínica Sorriso Prime",
        "segment": "Odontologia",
        "city": "Santos",
        "state": "SP",
        "phone": "13999998888",
        "hasWhatsapp": true,
        "whatsappUrl": "https://wa.me/5513999998888",
        "siteStatus": "none",
        "opportunity": "Não possui website profissional; depende apenas do perfil do Instagram.",
        "score": 85,
        "sources": ["MCP Prospector"]
      }
    ],
    "autoAnalyze": false
  }
}
```

---

## 🔐 Autenticação & Configuração

Adicione o servidor no arquivo de configuração do seu cliente MCP preferido substituindo `SUA_CHAVE_AQUI` pela sua chave de integração:

### Configuração para Google Antigravity / Gemini CLI (`mcp_config.json`)
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

### Configuração para Claude Desktop (`claude_desktop_config.json`)
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

### Configuração para Cursor IDE (`.cursor/mcp.json`)
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
