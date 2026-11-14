# ✂️ SupoClip MCP Server (`supoclip`)

Servidor do **SupoClip MCP** (`supoclip_mcp v1.30.0+`) para corte automático e inteligência de vídeos virais curtos (*shorts*, *reels* e *TikTok*), pontuação de viralidade (AI virality score), aplicação de legendas cinéticas (estilo Hormozi, MrBeast), sobreposição de B-roll e exportação em 1080x1920 (9:16).

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Streamable HTTP / Server-Sent Events (SSE)
- **Endpoint Oficial:** `https://mcp.supoclip.com/mcp`
- **Autenticação:** Header HTTP `Authorization: Bearer <API_KEY>` ou variável de ambiente `SUPOCLIP_API_KEY`.
- **Protocolo:** MCP `2024-11-05` (Capabilities: `tools`, `prompts`, `resources`).

### Configuração no `mcp_config.json`:

```json
{
  "mcpServers": {
    "supoclip": {
      "serverUrl": "https://mcp.supoclip.com/mcp",
      "headers": {
        "Authorization": "Bearer sk_HAv2PK7oSdD2nSPpwa3Jh7gaAyf4ekqgRBMN88hX3uY"
      }
    }
  }
}
```

### Configuração via Template Parametrizado (`mcp_template.json`):

```json
{
  "mcpServers": {
    "supoclip": {
      "serverUrl": "https://mcp.supoclip.com/mcp",
      "headers": {
        "Authorization": "Bearer ${SUPOCLIP_API_KEY}"
      }
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades (18 Ferramentas)

1. **Diagnóstico & Billing:**
   - `supoclip_health`: Checagem de conectividade com a API do SupoClip e modo de autenticação.
   - `supoclip_billing_summary`: Consulta do plano, minutos consumidos e minutos restantes disponíveis no mês.

2. **Criação & Processamento de Clipes Inteligentes:**
   - `supoclip_create_clip_task`: Criação de tarefa de clipping a partir de URLs (YouTube, Twitch, VODs) ou uploads de vídeos longos com seleção de duração (15s, 30s, 60s).
   - `supoclip_create_clip`: Criação rápida de clipe individual a partir de um timestamp de corte.
   - `supoclip_wait_for_task`: Aguarda a finalização do processamento em lote da IA.

3. **Legendas, B-Roll & Efeitos Visuais:**
   - `supoclip_list_caption_templates`: Lista templates de legendas cinéticas palavra por palavra (`hormozi`, `mrbeast`, `default`).
   - `supoclip_list_fonts`: Lista fontes suportadas para renderização das legendas.
   - `supoclip_list_transitions`: Lista efeitos de transição disponíveis entre cenas.
   - `supoclip_broll_status`: Verifica suporte ativo a sobreposições automáticas de B-roll contextual.

4. **Gestão & Exportação Multicanal:**
   - `supoclip_list_clips`: Lista os clipes gerados ranqueados por pontuação de viralidade (Virality Score).
   - `supoclip_export_clip`: Exporta e re-encoda o clipe com presets dedicados para redes sociais (`tiktok`, `reels`, `shorts`).
   - `supoclip_download_clip`: Baixa o arquivo MP4 processado em alta resolução localmente.

---

## 🤝 Sinergia com Agentes

- **`social-publisher-agent`:** Automação completa do funil de corte: recebe o vídeo longo ou demo do projeto, seleciona os momentos mais impactantes via `supoclip_create_clip_task`, exporta em preset `reels`/`tiktok` e agenda no Instagram e LinkedIn via Buffer MCP.
- **`video-producer-agent`:** Integração de clipes curtos verticais com teasers em Remotion e legendas cinéticas prontas.
- **`growth-marketing-agent`:** Produção acelerada de dezenas de cortes de marketing para testes A/B de anúncios e engajamento orgânico.
