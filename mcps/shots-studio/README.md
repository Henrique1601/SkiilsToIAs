# 📸 Shots Studio / FrameCraft MCP Server

O servidor MCP do **FrameCraft / Shots Studio** conecta os agentes de design, marketing e desenvolvimento à suíte de geração programática de mockups, frames e layouts visuais de alta fidelidade para apresentações, redes sociais (X/Twitter, LinkedIn, Instagram, Dribbble, YouTube, Product Hunt) e snippets de código elegantes.

---

## ⚙️ Configuração

### 1. Antigravity IDE / Gemini CLI
Configuração ativa no seu `~/.gemini/config/mcp_config.json`:
```json
{
  "mcpServers": {
    "shots-studio": {
      "command": "node",
      "args": [
        "--experimental-strip-types",
        "c:\\Users\\Public\\Downloads\\shots-studio\\mcp-server\\index.ts"
      ]
    }
  }
}
```

### 2. Claude CLI / Claude Desktop
Configuração ativa no seu `%APPDATA%\Claude\claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "shots-studio": {
      "command": "node",
      "args": [
        "--experimental-strip-types",
        "c:\\Users\\Public\\Downloads\\shots-studio\\mcp-server\\index.ts"
      ]
    }
  }
}
```

---

## 🛠️ Ferramentas Disponíveis (5 Tools Oficiais `framecraft_*`)

| Ferramenta | Descrição | Casos de Uso |
| :--- | :--- | :--- |
| `framecraft_list_presets` | Lista todos os dispositivos suportados (iPhone 17, MacBook Pro 16, Apple Watch, iPad Pro, Safari/Chrome Browser), presets sociais e paletas de fundo. | Inspeção do catálogo e escolha de molduras para capturas de tela. |
| `framecraft_create_mockup` | Cria configurações completas de mockup com molduras de dispositivos, gradientes, rotação 3D, sombras realistas e anotações. | Vitrines de produto, landing pages, pitch decks e materiais promocionais. |
| `framecraft_social_post` | Gera mockups pré-otimizados em proporções exatas para redes sociais (Twitter Post 16:9, Instagram Square 1:1, Stories 9:16, LinkedIn 1200x627, etc.). | Campanhas de lançamento pelo `growth-marketing-agent` e posts de autoridade. |
| `framecraft_code_snippet` | Cria molduras profissionais de código-fonte (estilo Ray.so / Carbon) com temas elegantes, títulos de IDE e numeração. | Compartilhamento de snippets técnicos no LinkedIn e documentações visuais. |
| `framecraft_magic_palette` | Gera automaticamente 4 gradientes harmônicos e modernos a partir de uma ou mais cores hexadecimais. | Composição de fundos estilizados para banners e mockups. |

---

## 🤝 Integração com Agentes Especialistas

- 🎨 **`design-engineer-agent`**: Utiliza as ferramentas de mockup para prototipagem de vitrines e apresentações visuais de componentes.
- 📈 **`growth-marketing-agent`**: Automatiza a criação de assets para lançamentos no Product Hunt, banners do LinkedIn e posts do Twitter/X.
- 🐙 **`github-profile-agent`**: Gera previews de alta resolução para inclusão no `README.md` de repositório e banners de portfólio.
