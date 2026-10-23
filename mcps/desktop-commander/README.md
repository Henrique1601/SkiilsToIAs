# 🖥️ Desktop Commander MCP Server (`desktop-commander`)

Servidor do **Desktop Commander MCP** (`@wonderwhy-er/desktop-commander`) para automação nativa do sistema operacional desktop, gerenciamento de arquivos avançado, execução de comandos locais, controle de processos e controle de periféricos.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Stdio (Execução local via Node/npx)
- **Pacote:** `@wonderwhy-er/desktop-commander@latest`

### Exemplo de Configuração:

```json
{
  "mcpServers": {
    "desktop-commander": {
      "command": "npx",
      "args": ["-y", "@wonderwhy-er/desktop-commander@latest"]
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades
- **Automação Desktop:** Ações diretas no ambiente operacional do usuário.
- **Gerenciamento de Arquivos e Processos:** Manipulação de arquivos, abertura de janelas e leitura de status de execução.
- **Sinergia:** Conecta-se às rotinas de terminal e devops locais (`devops-cloud-agent`).
