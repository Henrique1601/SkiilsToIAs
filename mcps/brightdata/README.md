# 🌐 Bright Data MCP Server (`brightdata`)

Servidor oficial do **Bright Data MCP** para web scraping em larga escala, proxies residenciais inteligentes, desbloqueio de sites complexos (Web Unlocker), coleta de dados públicos sem bloqueios de CAPTCHA e parsing estruturado.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Streamable HTTP (Remoto)
- **Endpoint:** `https://mcp.brightdata.com/mcp?token=YOUR_API_TOKEN`
- **Autenticação:** Parâmetro `token` na URL da API

### Exemplo de Configuração:

```json
{
  "mcpServers": {
    "brightdata": {
      "httpUrl": "https://mcp.brightdata.com/mcp?token=SEU_TOKEN_BRIGHTDATA_AQUI"
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades
- **Web Scraping Desbloqueado:** Extração de conteúdo de páginas protegidas por CAPTCHA, Cloudflare ou CloudFront.
- **Rede de Proxies Globais:** Roteamento por IPs residenciais e móveis em mais de 195 países.
- **Estruturação de Dados:** Coleta de dados de e-commerce, mecanismos de busca, redes sociais e notícias.
