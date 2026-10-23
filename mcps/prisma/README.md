# ◬ Prisma Remote MCP Server (`Prisma-Remote`)

Servidor do **Prisma Remote MCP** (`mcp-remote https://mcp.prisma.io/mcp`) para gerenciamento de schemas Prisma ORM, migrations, inspeção de modelos relacionais e otimização de consultas ao banco de dados com a plataforma Prisma.

---

## ⚡ Configuração & Transporte

- **Tipo / Transporte:** Stdio / Bridge Remoto (`mcp-remote`)
- **Endpoint:** `https://mcp.prisma.io/mcp`
- **Comando:** `npx -y mcp-remote https://mcp.prisma.io/mcp`

### Exemplo de Configuração:

```json
{
  "mcpServers": {
    "Prisma-Remote": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.prisma.io/mcp"
      ]
    }
  }
}
```

---

## 🛠️ Principais Recursos e Capacidades
- **Inspeção de Schema Prisma:** Leitura e validação de modelos (`schema.prisma`).
- **Migrações e Modelagem:** Análise de relações (`@relation`), índices e performance de queries.
- **Sinergia:** Conecta-se diretamente com o `database-architect-agent` e as skills `prisma-patterns` e `postgres-patterns`.
