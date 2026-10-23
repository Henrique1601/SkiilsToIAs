# 💼 LinkedIn MCP Server (`mcp-server-linkedin`)

Servidor do **LinkedIn MCP** (`mcp-server-linkedin@latest` via `uvx`) para automação de publicações profissionais, leitura e postagem de conteúdo no LinkedIn, monitoramento de feed, agendamento de artigos e gestão de presença executiva na rede.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Stdio (Execução via `uvx`)
- **Pacote:** `mcp-server-linkedin@latest`
- **Variáveis de Ambiente:** `UV_HTTP_TIMEOUT: "300"`

### Exemplo de Configuração:

```json
{
  "mcpServers": {
    "mcp-server-linkedin": {
      "command": "uvx",
      "args": [
        "mcp-server-linkedin@latest"
      ],
      "env": {
        "UV_HTTP_TIMEOUT": "300"
      }
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades
- **Publicação de Posts:** Criação e compartilhamento de posts em texto, carrosséis e mídias profissionais.
- **Engajamento & Interação:** Leitura de interações, comentários e métricas de postagens.
- **Personal Branding:** Distribuição de autoridade e conteúdo de liderança técnica no LinkedIn.
- **Sinergia:** Conecta-se diretamente com o `growth-marketing-agent`, `github-profile-agent` e skills da suíte LinkedIn (`linkedin-marketing`, `linkedin-post-writer`, `linkedin-article-drafter`).
