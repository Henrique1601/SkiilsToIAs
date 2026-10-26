# ADR-003: Padrão Ouro de README.md, CI/CD de Releases v1.0.0+ e Enforce Obrigatório de TypeSafe AI

- **Status:** Aceito
- **Data:** 2026-10-26
- **Autor:** Henrique Bezerra dos Santos (`@Henrique1601`) & AI Agentic Architecture
- **Contexto:** Governança de novos projetos, distribuição de apps executáveis/instaláveis e uso mandatório de TypeSafe AI no ecossistema `SkiilsToIAs`.

---

## 1. Contexto e Problema

No ecossistema de agentes autônomos (`global-master-agent`, `git-master-agent`, `skills-orchestrator`), a criação de novos softwares e atualizações de projetos existentes exige consistência extrema tanto na experiência do usuário final quanto na robustez dos pipelines de IA:

1. **Apresentação e Distribuição de Software:** Projetos sem um padrão rigoroso de `README.md` dificultam a adoção. Usuários precisam encontrar imediatamente:
   - Ícone/Logo ou GIF animado demonstrando o produto em ação.
   - Links diretos e visíveis para Download, Primeiros Passos, Website, Documentação e Releases.
   - Se o projeto for um aplicativo para PC (Desktop CLI ou GUI), os binários devem ser **instaláveis e executáveis** (`.exe`, `.msi`, `.zip`) e estar publicados nas **GitHub Releases desde a versão `v1.0.0` inicial**.
2. **Confiabilidade em Decisões de IA (`TypeSafe AI`):** Em aplicações com inteligência artificial, o uso de texto livre não estruturado gera alucinações e falhas de runtime. É indispensável que o **TypeSafe AI** seja mandatório em todas as decisões, rotas estruturadas, julgamentos de System One e retornos tipados.

---

## 2. Decisões Arquiteturais

### A. Enforce Obrigatório de `typesafe-ai` no Kit Universal
- A skill [`typesafe-ai`](../../ai-agents/typesafe-ai/SKILL.md) torna-se **requisito estrito e mandatório** em qualquer fluxo que envolva chamadas a LLMs, extração de dados, rotas de IA, classificação semântica, validação com Zod/JSON Schema ou julgamentos tipados (System One / Jev).
- Proibido o retorno de respostas cruas de IA sem schemas tipados e tratamento de confiança/incerteza.

### B. Especificação Padrão Ouro do `README.md`
Todo projeto criado ou auditado pelo `git-master-agent` deve conter obrigatoriamente a seguinte estrutura visual e informativa:

1. **Header Visual de Alto Impacto:**
   - Ícone, Logotipo ou GIF animado demonstrando o software em funcionamento centralizado no topo (`<p align="center"><img src="..." /></p>`).
   - Título impactante com Badges dinâmicos (Stack, Versão, Downloads, GitHub Releases, Licença MIT, Status do CI).
2. **Barra de Acesso Rápido (Quick Links):**
   - Links diretos e destacados:
     `[🚀 Download do Instalador (.exe)]` | `[⚡ Primeiros Passos]` | `[🌐 Website]` | `[📚 Documentação]` | `[📦 Releases]`
3. **Visão Geral & Problema que Resolve:**
   - 2-3 parágrafos objetivos explicando o valor prático do produto.
4. **Instalação & Guia para Aplicativos de PC:**
   - Instruções passo a passo tanto para o usuário final (download do executável/instalador nas Releases) quanto para desenvolvedores (`git clone`, dependências, compilação).
5. **Capturas de Tela & Demonstração Interativa:**
   - GIFs ou imagens reais da interface.
6. **Variáveis de Ambiente & Configuração:**
   - `.env.example` documentado.
7. **Arquitetura & Como Contribuir:**
   - Diagrama Mermaid de arquitetura e instruções de PR/commits convencionais.

### C. Pipeline de CI/CD de Releases Automatizadas desde a v1.0.0
- Se o projeto for ou contiver um aplicativo desktop/CLI para computador:
  1. O arquivo `.github/workflows/release.yml` deve ser gerado **desde o scaffold inicial**.
  2. A cada tag de versão (iniciando em `v1.0.0`) ou disparo manual, a GitHub Action compila o executável limpo (ex: `windows-latest` para `.exe`, `.msi`, `.zip`).
  3. O binário é publicado automaticamente na aba de **Releases** do GitHub, com changelog e hashes SHA-256 de verificação.
  4. Binários compilados permanecem estritamente ignorados no `.gitignore` e **nunca** são comitados diretamente na árvore do Git.

---

## 3. Consequências

- **Adoção Instantânea:** Qualquer pessoa que chegue ao repositório consegue baixar o executável com 1 clique e entender o produto visualmente por GIFs e documentação.
- **Robustez de Engenharia:** Todo software gerado nasce com padrão profissional de distribuição corporativa (releases automatizadas, versionamento semântico e IA tipada).
