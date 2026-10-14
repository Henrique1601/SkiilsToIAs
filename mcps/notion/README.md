# 📝 Notion — Servidor MCP Oficial

Servidor oficial de **Model Context Protocol (MCP)** mantido pela Notion (`@notionhq/notion-mcp-server`) para conectar agentes de IA diretamente a workspaces, bancos de dados, wikis e páginas de documentação.

---

## 📌 Metadados Técnicos

* **Nome do Servidor:** `notion-mcp-server`
* **Transporte:** Stdio (Local Node/npx)
* **Pacote npm:** `@notionhq/notion-mcp-server`
* **Comando:** `npx -y @notionhq/notion-mcp-server`
* **Variável de Ambiente Obrigatória:**
  * `OPENAPI_MCP_HEADERS`: String JSON contendo o token de integração do Notion e a versão da API.
  * Formato: `{"Authorization": "Bearer ntn_...", "Notion-Version": "2022-06-28"}`

---

## 🛠️ Principais Ferramentas Expostas (*Tools*)

* `API-post-search`: Busca global por texto em títulos de páginas, databases e conteúdos do workspace.
* `API-retrieve-a-database`: Recupera a estrutura, propriedades, fórmulas e schemas de uma base de dados.
* `API-query-data-source`: Executa queries filtradas e ordenadas em bancos de dados do Notion.
* `API-retrieve-a-page`: Lê os metadados e propriedades de uma página específica.
* `API-retrieve-page-markdown`: Obtém o conteúdo de uma página formatado em Markdown pronto para a IA.
* `API-post-page`: Cria uma nova página ou adiciona registros a um database.
* `API-patch-page`: Atualiza títulos, status, tags ou propriedades de páginas existentes.
* `API-get-block-children`: Lê os blocos filhos estruturados de uma página.

---

## 🚀 Como Configurar

### No Google Antigravity / Gemini CLI (`mcp_config.json`):
```json
{
  "mcpServers": {
    "notion-mcp-server": {
      "command": "npx",
      "args": [
        "-y",
        "@notionhq/notion-mcp-server"
      ],
      "env": {
        "OPENAPI_MCP_HEADERS": "{\"Authorization\": \"Bearer SUA_NOTION_INTEGRATION_KEY\", \"Notion-Version\": \"2022-06-28\"}"
      }
    }
  }
}
```

### No Claude Desktop (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "notion-mcp-server": {
      "command": "npx",
      "args": [
        "-y",
        "@notionhq/notion-mcp-server"
      ],
      "env": {
        "OPENAPI_MCP_HEADERS": "{\"Authorization\": \"Bearer SUA_NOTION_INTEGRATION_KEY\", \"Notion-Version\": \"2022-06-28\"}"
      }
    }
  }
}
```
