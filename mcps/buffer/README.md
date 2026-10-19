# 📱 Buffer MCP Server

O servidor MCP do **Buffer** conecta o ecossistema de agentes diretamente à API oficial do Buffer, permitindo gerenciamento multicanal de mídias sociais (LinkedIn, Twitter/X, Instagram, Facebook, Pinterest, etc.), agendamento de posts, análise de métricas e gerenciamento de ideias.

---

## ⚙️ Configuração

### 1. Antigravity IDE / Gemini CLI
Adicione ao seu `mcp_config.json`:
```json
{
  "mcpServers": {
    "buffer": {
      "serverUrl": "https://mcp.buffer.com/mcp"
    }
  }
}
```

### 2. Claude CLI / Claude Desktop
Adicione ao seu `.claude.json`:
```json
{
  "mcpServers": {
    "buffer": {
      "type": "http",
      "url": "https://mcp.buffer.com/mcp"
    }
  }
}
```

---

## 🛠️ Ferramentas Disponíveis (20 Tools)

| Ferramenta | Descrição |
| :--- | :--- |
| `get_account` | Obtém informações da conta conectada no Buffer. |
| `list_channels` | Lista todos os canais de redes sociais vinculados (Instagram, LinkedIn, X, etc.). |
| `get_channel` | Detalhes de um canal específico por ID. |
| `list_posts` | Lista posts agendados, enviados ou rascunhos de um canal. |
| `get_post` | Obtém detalhes de um post específico. |
| `create_post` | Cria ou agenda uma nova publicação para um ou múltiplos canais. |
| `edit_post` | Atualiza o conteúdo ou data de agendamento de um post existente. |
| `delete_post` | Remove uma publicação agendada da fila. |
| `get_aggregated_post_metrics` | Obtém métricas de engajamento consolidadas (cliques, impressões, reações). |
| `list_ideas` | Lista ideias de conteúdo salvas no Buffer Idea Board. |
| `list_idea_groups` | Lista grupos e categorias de ideias. |
| `create_idea` | Salva uma nova ideia no quadro do Buffer. |
| `list_post_templates` | Lista modelos e templates reutilizáveis de posts. |
| `get_post_template` | Obtém detalhes de um template específico. |
| `create_post_template` | Cria um novo modelo reutilizável de postagem. |
| `update_post_template` | Atualiza um modelo de post existente. |
| `delete_post_template` | Exclui um modelo de post. |
| `introspect_schema` | Introspecção do schema GraphQL da API do Buffer. |
| `execute_query` | Executa consultas GraphQL personalizadas no Buffer. |
| `execute_mutation` | Executa mutações GraphQL personalizadas no Buffer. |

---

## 🤖 Sinergia com Agentes

- **`growth-marketing-agent`**: Utiliza para agendamento direto de posts gerados por `linkedin-post-writer`, `muapi-instagram-post` e campanhas de lançamento.
- **`github-profile-agent`**: Pode agendar posts técnicos sobre atualizações de repositórios e releases.
