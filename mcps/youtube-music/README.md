# 🎵 YouTube Music MCP Server (`youtube-music-server`)

Servidor do **YouTube Music MCP** para controle, busca semântica de músicas, execução de playlists, controle de reprodução e gerenciamento de biblioteca de áudio via IA.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Stdio (Execução local via Node)
- **Executável:** Script compilado em JavaScript/Node

### Exemplo de Configuração:

```json
{
  "mcpServers": {
    "youtube-music-server": {
      "command": "node",
      "args": ["c:\\caminho\\para\\youtube-music-server\\build\\index.js"]
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades
- **Busca Musical:** Pesquisa de faixas, álbuns, artistas e playlists no YouTube Music.
- **Controle de Playback:** Play, pause, pular faixa, controle de volume e histórico de reprodução.
- **Sinergia:** Conecta-se a agentes de áudio e produtores multimídia (`video-producer-agent` e skills de áudio).
