# ▲ Vercel MCP Server (`vercel`)

Servidor oficial do **Vercel MCP** (`mcp-remote https://mcp.vercel.com`) para gerenciamento de projetos, deploys em tempo real, monitoramento de builds, domínios, DNS e variáveis de ambiente na plataforma Vercel.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Stdio / Bridge Remoto (`mcp-remote`)
- **Endpoint:** `https://mcp.vercel.com`
- **Comando:** `npx -y mcp-remote https://mcp.vercel.com`

### Exemplo de Configuração:

```json
{
  "mcpServers": {
    "vercel": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.vercel.com"
      ]
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades
- **Deploy & Preview:** Listagem e acompanhamento de deploys e URLs de preview em tempo real.
- **Projetos & Domínios:** Gestão de domínios customizados, aliases e configurações do projeto.
- **Variáveis de Ambiente:** Consulta e validação de env vars de produção e preview.
- **Sinergia:** Conecta-se diretamente com o `devops-cloud-agent` e as skills `deploy-to-vercel` e `vercel-react-best-practices`.
