# 🌐 Chrome DevTools — Servidor MCP

Servidor de **Model Context Protocol (MCP)** para automação, depuração e inspeção profunda de aplicações web através do **Chrome DevTools Protocol (CDP)**.

---

## 📌 Metadados Técnicos

* **Nome do Servidor:** `chrome-devtools-mcp`
* **Transporte:** Stdio (Local Node/npx)
* **Pacote npm:** `chrome-devtools-mcp@latest`
* **Comando:** `npx -y chrome-devtools-mcp@latest`
* **Dependências Externas:** Google Chrome ou Chromium instalado na máquina.

---

## 🛠️ Principais Ferramentas Expostas (*Tools*)

* `navigate_page`: Navega para qualquer URL (ex: `http://localhost:3000` ou sites externos).
* `take_screenshot`: Captura prints visuais da tela inteira ou de elementos específicos.
* `take_snapshot`: Extrai o DOM renderizado em formato acessível para análise de layout.
* `list_console_messages`: Lê erros de JavaScript, avisos e logs do console do navegador.
* `list_network_requests`: Inspeciona requisições HTTP, headers, payloads e falhas de rede.
* `click`, `type_text`, `fill_form`, `press_key`: Interage programaticamente com botões, inputs e formulários.
* `evaluate_script`: Executa expressões JavaScript diretamente no contexto da página.
* `lighthouse_audit`: Realiza auditoria automatizada de Performance, Acessibilidade e SEO com nota e métricas.

---

## 🚀 Como Configurar

### No Google Antigravity / Gemini CLI (`mcp_config.json`):
```json
{
  "mcpServers": {
    "chrome-devtools-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@latest"
      ]
    }
  }
}
```

### No Claude Desktop (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "chrome-devtools-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@latest"
      ]
    }
  }
}
```
