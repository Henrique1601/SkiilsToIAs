# 🎥 OpenScreen MCP Server (`openscreen`)

Servidor do **OpenScreen MCP** (`openscreen v2.1.2+`) para gravação inteligente de tela, controle de timelines, edição baseada em transcrição Whisper (on-device), auto-zoom em cliques, efeitos de shader WGSL, legendas automáticas e exportação de vídeos para redes sociais e demonstrações de produto.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Streamable HTTP / Server-Sent Events (SSE)
- **Endpoint Local:** `http://127.0.0.1:47821/mcp`
- **Autenticação:** Bearer Token via Header HTTP `Authorization: Bearer <TOKEN>` ou variável de ambiente `OPENSCREEN_MCP_TOKEN`.
- **Protocolo:** MCP `2024-11-05` (Capabilities: `tools`, `resources`).

### Configuração no `mcp_config.json`:

```json
{
  "mcpServers": {
    "openscreen": {
      "serverUrl": "http://127.0.0.1:47821/mcp",
      "headers": {
        "Authorization": "Bearer hw9LpTNFHtvvL-AVRrDPe2we4Y7N2Aa-mQmeFTb8WsM"
      }
    }
  }
}
```

### Configuração via Template Parametrizado (`mcp_template.json`):

```json
{
  "mcpServers": {
    "openscreen": {
      "serverUrl": "http://127.0.0.1:47821/mcp",
      "headers": {
        "Authorization": "Bearer ${OPENSCREEN_MCP_TOKEN}"
      }
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades (55 Ferramentas)

1. **Gravação & Fontes:**
   - `listSources`: Lista monitores e janelas disponíveis para captura.
   - `startRecording` / `stopRecording`: Inicia e finaliza a gravação, gerando um novo `projectId` e `checkpointId`.
   - `setPointerTrack`: Injeta telemetria de cursor caso a interface seja manipulada por scripts automatizados (Playwright/CDP).

2. **Edição Não-Linear & Linha do Tempo:**
   - `listProjects`, `getCurrentDocument`, `createProject`, `createCheckpoint`, `restoreCheckpoint`.
   - `addTrim`, `addTrims`, `setTrim`, `removeTrim`: Remove pausas, silêncios e hesitações na régua de tempo.
   - `setClipRange`, `moveClip`, `insertClip`, `duplicateClip`, `replaceTimeline`.

3. **Auto-Zoom & Telemetria do Cursor:**
   - `addAutoZooms`: Aplica zoom cinemático dinâmico focado nas coordenadas dos cliques registrados durante a captura.
   - `addZoom`, `setZoom`, `getCursorTrack`: Controle fino de aproximação (níveis 1 a 6) e acompanhamento do ponteiro.

4. **Transcrição Whisper & Legendas Inteligentes:**
   - `transcribe`: Gera transcrição on-device rápida com modelo Whisper.
   - `getTranscript`, `getTranscriptWords`, `removeWords`, `setWordText`: Corte preciso de palavras de preenchimento ("hum", repetições) por ID de palavra.
   - `getCaptions`, `setCaptionSettings`, `getCaptionTranslationUnits`, `putCaptionTranslation`: Geração e estilização de legendas dinâmicas e bilíngues.

5. **Anotações, Shaders & Exportação:**
   - `addAnnotation`: Insere textos, setas e desfoques de privacidade (blur de senhas, chaves de API e e-mails).
   - `setEditorSettings`: Ajusta moldura de dispositivo, fundo (wallpaper/blur), cantos arredondados, sombras e proporção (16:9, 9:16 vertical para Instagram Reels).
   - `exportVideo` & `getFrames`: Renderiza o vídeo final e extrai frames para validação antes da publicação.

---

## 🤝 Sinergia com Agentes

- **`social-publisher-agent`:** Gravação primária de fluxos de telas, edição automática com cortes de silêncio, auto-zoom em interações e exportação em 9:16 ou 1:1 para Instagram e LinkedIn.
- **`global-master-agent`:** Orquestração de evidências visuais de releases e documentação em vídeo de novas features.
- **`qa-testing-agent`:** Gravação visual automatizada de testes E2E executados via Playwright.
