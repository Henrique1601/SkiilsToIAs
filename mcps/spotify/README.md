# 🎧 Spotify MCP Server (`spotify`)

Servidor do **Spotify MCP** para controle completo da API Web do Spotify via Python (`uv`), permitindo controle de player, busca semântica de faixas/álbuns/podcasts, recomendações musicais inteligentes e manipulação de playlists.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Stdio (Execução via `uv`)
- **Gerenciador de Pacotes:** `uv` (Python)
- **Variáveis de Ambiente:** `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, `SPOTIFY_REDIRECT_URI`

### Exemplo de Configuração:

```json
{
  "mcpServers": {
    "spotify": {
      "command": "uv",
      "args": [
        "--directory",
        "c:\\caminho\\para\\spotify-mcp",
        "run",
        "spotify-mcp"
      ],
      "env": {
        "SPOTIFY_CLIENT_ID": "SEU_CLIENT_ID",
        "SPOTIFY_CLIENT_SECRET": "SEU_CLIENT_SECRET",
        "SPOTIFY_REDIRECT_URI": "http://127.0.0.1:8080/callback"
      }
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades
- **Controle de Reprodução:** Play, pause, avançar, retroceder e selecionar dispositivo ativo (Connect API).
- **Curadoria e Playlists:** Criação, ordenação e inserção de faixas em playlists.
- **Recomendações e Descoberta:** Busca de faixas semelhantes com base em gênero, energia, valência e dançabilidade.
- **Sinergia:** Conecta-se diretamente com o `video-producer-agent` e skills de multimídia.
