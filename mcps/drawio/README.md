# 📐 Draw.io MCP Server (`drawio`)

Servidor oficial do **Draw.io MCP** (`@next-ai-drawio/mcp-server@latest`) para criação, edição programática, renderização e exportação de diagramas de arquitetura técnica, fluxogramas, diagramas de sequência e modelagens visuais de sistemas diretamente em Draw.io (XML/SVG/PNG).

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Stdio (Execução local via Node/npx)
- **Pacote:** `@next-ai-drawio/mcp-server@latest`

### Exemplo de Configuração:

```json
{
  "mcpServers": {
    "drawio": {
      "command": "npx",
      "args": [
        "-y",
        "@next-ai-drawio/mcp-server@latest"
      ]
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades
- **Criação de Diagramas:** Geração de diagramas de arquitetura, UML, C4 model e fluxos de dados em XML Draw.io.
- **Edição & Modificação:** Adição e remoção de nós, conexões e legendas em diagramas existentes.
- **Exportação Visual:** Renderização e exportação de artefatos visuais prontos para documentação técnica.
- **Sinergia:** Conecta-se diretamente com o `planning-master-agent`, `skills-orchestrator` e skills de arquitetura (`architecture`, `architecture-decision-records`).
