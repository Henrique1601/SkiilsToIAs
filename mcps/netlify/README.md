# 🌐 Netlify MCP Server (`netlify`)

Servidor oficial do **Netlify MCP** (`@netlify/mcp`) para gerenciamento de deploys, builds, sites, DNS, formulários e funções serverless na plataforma Netlify.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Stdio (Execução local via Node/npx)
- **Pacote:** `@netlify/mcp`

### Exemplo de Configuração:

```json
{
  "mcpServers": {
    "netlify": {
      "command": "npx",
      "args": [
        "-y",
        "@netlify/mcp"
      ]
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades
- **Gestão de Sites Netlify:** Listagem de sites, deploys de preview e status de builds.
- **Serverless & Edge Functions:** Inspeção de funções e logs de execução.
- **Domínios & DNS:** Verificação de registros e roteamento.
- **Sinergia:** Conecta-se diretamente com o `devops-cloud-agent` e a skill `netlify-deploy`.
