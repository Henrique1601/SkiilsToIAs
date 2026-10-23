# 📱 BrowserStack MCP Server (`browserstack`)

Servidor oficial do **BrowserStack MCP** para execução remota e paralela de testes automatizados em nuvem através de centenas de navegadores reais, sistemas operacionais (Windows, macOS, Linux) e dispositivos móveis reais (iOS e Android).

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Streamable HTTP (Remoto)
- **Endpoint:** `https://mcp.browserstack.com/mcp`

### Exemplo de Configuração:

```json
{
  "mcpServers": {
    "browserstack": {
      "serverUrl": "https://mcp.browserstack.com/mcp"
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades
- **Cross-Browser & Cross-Platform Testing:** Execução de testes em matrizes combinadas de navegadores e sistemas operacionais.
- **Dispositivos Móveis Reais:** Testes responsivos em iPhones, iPads e smartphones Android físicos.
- **Relatórios de Execução:** Gravação de vídeos da sessão, logs de rede e console da sessão remota.
- **Sinergia:** Conecta-se diretamente com o `qa-testing-agent` e as skills `e2e-testing`, `browser-qa` e `playwright-cli`.
