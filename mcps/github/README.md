# 🐙 GitHub MCP Server (`github`)

Servidor oficial do **GitHub MCP** integrado à API do GitHub e Copilot para permitir que agentes de IA inspecionem repositórios, pull requests, issues, branches, commits e interajam com a plataforma GitHub de forma nativa.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Streamable HTTP (Remoto)
- **Endpoint:** `https://api.githubcopilot.com/mcp/`
- **Autenticação:** Header HTTP `Authorization: Bearer $GITHUB_MCP_PAT`

### Exemplo de Configuração (`mcp_config.json` / Claude Desktop):

```json
{
  "mcpServers": {
    "github": {
      "httpUrl": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer SUA_CHAVE_GITHUB_PAT_AQUI"
      }
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades
- **Gestão de Repositórios:** Leitura de arquivos, árvores de diretórios, commits e branches.
- **Pull Requests & Code Reviews:** Leitura, criação e comentários em PRs.
- **Issues & Projetos:** Busca, abertura e fechamento de issues.
- **Workflow & Actions:** Acompanhamento do status de execuções de CI/CD.
