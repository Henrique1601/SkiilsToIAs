# 🗺️ Google Maps MCP Server (`google-maps`)

Servidor do **Google Maps MCP** (`@cablate/mcp-google-map`) para geocodificação, busca de pontos de interesse (Places), rotas, distâncias, matriz de tráfego e dados geoespaciais integrados com a Google Maps Platform.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Stdio (Execução local via Node/npx)
- **Pacote:** `@cablate/mcp-google-map`
- **Variável de Ambiente:** `GOOGLE_MAPS_API_KEY`

### Exemplo de Configuração:

```json
{
  "mcpServers": {
    "google-maps": {
      "command": "npx",
      "args": ["-y", "@cablate/mcp-google-map", "--stdio"],
      "env": {
        "GOOGLE_MAPS_API_KEY": "SUA_CHAVE_API_DO_GOOGLE_MAPS"
      }
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades
- **Geocoding & Reverse Geocoding:** Conversão de endereços em coordenadas de latitude/longitude e vice-versa.
- **Places API:** Busca e detalhes de estabelecimentos comerciais, avaliações e horários.
- **Directions & Distance Matrix:** Cálculo de rotas e estimativas de deslocamento e tráfego.
- **Sinergia:** Conecta-se com as skills `google-maps-platform` e `google-maps-scraper`.
