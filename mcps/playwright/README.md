# 🎭 Playwright MCP Server (`playwright`)

Servidor oficial do **Playwright MCP** (`@playwright/mcp`) para automação de testes end-to-end, controle de navegadores headless ou reais (Chromium, Firefox, WebKit), navegação interativa, preenchimento de formulários e captura de telas e traces.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Stdio (Execução local via Node/npx)
- **Pacote:** `@playwright/mcp@latest`

### Exemplo de Configuração:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "-y",
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades
- **Navegação & Interação:** Acesso a URLs, cliques em botões, preenchimento de inputs e submissão de formulários.
- **Validação E2E:** Verificação de assertivas em tela, visibilidade de elementos e textos.
- **Evidências Visuais:** Captura de screenshots em alta resolução e gravação de traces de execução.
- **Sinergia:** Conecta-se diretamente com o `qa-testing-agent` e com a skill `e2e-testing`.
