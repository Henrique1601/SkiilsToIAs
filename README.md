# 🧠 Skills to IAs (`SkiilsToIAs`)

Repositório centralizado e categorizado contendo **128 skills especializadas** para agentes autônomos de Inteligência Artificial (compatível com **Antigravity**, **Claude Code**, **Cursor**, **Copilot CLI**, entre outros).

---

## 📊 Visão Geral das Categorias

| Categoria | Pasta | Quantidade | Foco Principal |
|---|---|:---:|---|
| [🎨 Design & UI/UX](#design) | [`design/`](design/) | **34** | Skills especializadas em interface de usuário, design systems, estética anti-slop, micro-interações, tipografia, animações e tokens visuais. |
| [🔍 SEO & Mecanismos de Busca](#seo) | [`seo/`](seo/) | **3** | Skills dedicadas a auditoria técnica de SEO, otimização de Core Web Vitals, indexação e inteligência competitiva. |
| [📣 Marketing & Vendas](#marketing) | [`marketing/`](marketing/) | **6** | Skills para comunicação de marca, criação de campanhas visuais, réguas de e-mail marketing, relatórios de performance e pesquisa de contas. |
| [💻 Desenvolvimento & Testes](#development) | [`development/`](development/) | **17** | Engenharia de software, automação com Playwright, frameworks modernos (React, Next.js, Swift), depuração estruturada e TDD. |
| [☁️ Cloud & DevOps](#devops-cloud) | [`devops-cloud/`](devops-cloud/) | **9** | Infraestrutura como código, nuvem Microsoft Azure, migração de cargas de trabalho, checklists pré-deploy e autenticação Entra ID. |
| [🗄️ Backend & Banco de Dados](#backend-database) | [`backend-database/`](backend-database/) | **4** | Bancos de dados serverless (Neon Postgres, Supabase) e padrões de arquitetura de software (ADRs e análise de acoplamento). |
| [🤖 Agentes de IA & Metaprogramação](#ai-agents) | [`ai-agents/`](ai-agents/) | **22** | Criação e engenharia de subagentes autônomos, servidores MCP (Model Context Protocol), plugins para Claude Code, hooks de ciclo de vida e novas skills. |
| [📄 Documentos & Produtividade](#documents-productivity) | [`documents-productivity/`](documents-productivity/) | **14** | Manipulação automatizada de documentos de escritório (Word, Excel, PowerPoint, PDF), vault do Obsidian e especificações técnicas. |
| [📊 Gestão & Negócios](#business-management) | [`business-management/`](business-management/) | **14** | Análise de métricas e KPIs, governança, conformidade SOX, planejamento de capacidade de equipe, calibração de RH e briefings diários. |
| [🛠️ Utilitários & Otimização](#utilities) | [`utilities/`](utilities/) | **5** | Modo ultra-conciso (Caveman) para economia massiva de tokens de contexto, playbooks interativos e helpers. |

> **Total de Skills catalogadas:** 128 skills

---

## 🚀 Como Utilizar

### 1. Clonar ou copiar para o diretório de skills do seu agente

#### No Antigravity / Gemini CLI:
```bash
# Copiar para o diretório de skills do usuário
cp -r <categoria>/<skill-desejada> ~/.gemini/config/skills/
```

#### No Claude Code:
```bash
# Copiar para o diretório de skills do Claude Code
cp -r <categoria>/<skill-desejada> ~/.claude/skills/
# ou no projeto local:
cp -r <categoria>/<skill-desejada> .claude/skills/
```

#### No Cursor / Agentes Genéricos:
Você pode referenciar diretamente o arquivo `SKILL.md` nas regras de projeto (`.cursorrules` ou prompt de sistema).

---

## 📂 Catálogo Completo de Skills por Categoria

<a id="design"></a>
### 🎨 Design & UI/UX (34 skills)

**Caminho no repositório:** [`design/`](design/)

Skills especializadas em interface de usuário, design systems, estética anti-slop, micro-interações, tipografia, animações e tokens visuais.

| Skill | Descrição | Link |
|---|---|:---:|
| **`accessibility-review`** | Run a WCAG 2.1 AA accessibility audit on a design or page. Trigger with "audit accessibility", "check a11y", "is this accessible?", or when reviewing a desig... | [`SKILL.md`](design/accessibility-review/SKILL.md) |
| **`animate`** | Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at all, what purpose, which too... | [`SKILL.md`](design/animate/SKILL.md) |
| **`animate-expo`** | Build animations in React Native and Expo, making the decisions in the order that determines whether they feel right — should it animate, which thread it run... | [`SKILL.md`](design/animate-expo/SKILL.md) |
| **`animation-vocabulary`** | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover opens" → Pop... | [`SKILL.md`](design/animation-vocabulary/SKILL.md) |
| **`apple-design`** | Apple's approach to interface design and fluid, physical motion, translated for the web. | [`SKILL.md`](design/apple-design/SKILL.md) |
| **`ask-sonner`** | Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call, promise and loading toasts, updating, dismissing and... | [`SKILL.md`](design/ask-sonner/SKILL.md) |
| **`brandkit`** | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. | [`SKILL.md`](design/brandkit/SKILL.md) |
| **`canvas-design`** | Create beautiful visual art in .png and .pdf documents using design philosophy. | [`SKILL.md`](design/canvas-design/SKILL.md) |
| **`design-critique`** | Get structured design feedback on usability, hierarchy, and consistency. | [`SKILL.md`](design/design-critique/SKILL.md) |
| **`design-system`** | Audit, document, or extend your design system. Use when checking for naming inconsistencies or hardcoded values across components, writing documentation for ... | [`SKILL.md`](design/design-system/SKILL.md) |
| **`design-taste-frontend`** | Anti-slop frontend skill for landing pages, portfolios, and redesigns. | [`SKILL.md`](design/design-taste-frontend/SKILL.md) |
| **`design-taste-frontend-v1`** | The original v1 taste-skill, preserved for projects depending on its exact behavior. | [`SKILL.md`](design/design-taste-frontend-v1/SKILL.md) |
| **`emil-design-eng`** | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great. | [`SKILL.md`](design/emil-design-eng/SKILL.md) |
| **`find-animation-opportunities`** | Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. | [`SKILL.md`](design/find-animation-opportunities/SKILL.md) |
| **`frontend-design`** | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. | [`SKILL.md`](design/frontend-design/SKILL.md) |
| **`gpt-taste`** | Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide editorial typogr... | [`SKILL.md`](design/gpt-taste/SKILL.md) |
| **`high-end-visual-design`** | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensive. | [`SKILL.md`](design/high-end-visual-design/SKILL.md) |
| **`image-to-code`** | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, then i... | [`SKILL.md`](design/image-to-code/SKILL.md) |
| **`imagegen-frontend-mobile`** | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. | [`SKILL.md`](design/imagegen-frontend-mobile/SKILL.md) |
| **`imagegen-frontend-web`** | Elite frontend image-direction skill for generating premium, conversion-aware website design references. | [`SKILL.md`](design/imagegen-frontend-web/SKILL.md) |
| **`improve-animations`** | Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained implementation plans for other ... | [`SKILL.md`](design/improve-animations/SKILL.md) |
| **`industrial-brutalist-ui`** | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. | [`SKILL.md`](design/industrial-brutalist-ui/SKILL.md) |
| **`minimalist-ui`** | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. | [`SKILL.md`](design/minimalist-ui/SKILL.md) |
| **`mobile-native`** | Make a web app feel native on a phone — the small CSS and meta-tag fixes that separate "a website in a browser" from something that feels installed. | [`SKILL.md`](design/mobile-native/SKILL.md) |
| **`pick-ui-library`** | Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs, charts, command menus, virtualization, drag and drop... | [`SKILL.md`](design/pick-ui-library/SKILL.md) |
| **`prototype`** | Build multiple genuinely different versions of a UI piece you describe, rendered behind a visual picker so you can flip through them live and promote the one... | [`SKILL.md`](design/prototype/SKILL.md) |
| **`redesign-existing-projects`** | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without ... | [`SKILL.md`](design/redesign-existing-projects/SKILL.md) |
| **`review-animations`** | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. | [`SKILL.md`](design/review-animations/SKILL.md) |
| **`slack-gif-creator`** | Knowledge and utilities for creating animated GIFs optimized for Slack. | [`SKILL.md`](design/slack-gif-creator/SKILL.md) |
| **`stitch-design-taste`** | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography,... | [`SKILL.md`](design/stitch-design-taste/SKILL.md) |
| **`theme-factory`** | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. | [`SKILL.md`](design/theme-factory/SKILL.md) |
| **`ui-toolkit-web`** | Reference skill for Zoom Video SDK UI Toolkit. Use after routing to a web video workflow when you want prebuilt React UI instead of building a fully custom V... | [`SKILL.md`](design/ui-toolkit-web/SKILL.md) |
| **`ux-copy`** | Write or review UX copy — microcopy, error messages, empty states, CTAs. | [`SKILL.md`](design/ux-copy/SKILL.md) |
| **`web-design-guidelines`** | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my si... | [`SKILL.md`](design/web-design-guidelines/SKILL.md) |

---

<a id="seo"></a>
### 🔍 SEO & Mecanismos de Busca (3 skills)

**Caminho no repositório:** [`seo/`](seo/)

Skills dedicadas a auditoria técnica de SEO, otimização de Core Web Vitals, indexação e inteligência competitiva.

| Skill | Descrição | Link |
|---|---|:---:|
| **`competitive-brief`** | Research competitors and generate a positioning and messaging comparison with content gaps, opportunities, and threats. | [`SKILL.md`](seo/competitive-brief/SKILL.md) |
| **`competitive-intelligence`** | Research your competitors and build an interactive battlecard. | [`SKILL.md`](seo/competitive-intelligence/SKILL.md) |
| **`seo-audit`** | When the user wants to audit, review, or diagnose SEO issues on their site. | [`SKILL.md`](seo/seo-audit/SKILL.md) |

---

<a id="marketing"></a>
### 📣 Marketing & Vendas (6 skills)

**Caminho no repositório:** [`marketing/`](marketing/)

Skills para comunicação de marca, criação de campanhas visuais, réguas de e-mail marketing, relatórios de performance e pesquisa de contas.

| Skill | Descrição | Link |
|---|---|:---:|
| **`account-research`** | Research a company or person and get actionable sales intel. | [`SKILL.md`](marketing/account-research/SKILL.md) |
| **`brand-review`** | Review content against your brand voice, style guide, and messaging pillars, flagging deviations by severity with specific before/after fixes. | [`SKILL.md`](marketing/brand-review/SKILL.md) |
| **`brand-voice-enforcement`** | >   This skill applies brand guidelines to content creation. | [`SKILL.md`](marketing/brand-voice-enforcement/SKILL.md) |
| **`canva-creator`** | >   Takes an approved content brief and executes a campaign end-to-end: builds   the posting calendar, generates Canva designs for social posts, drafts   cap... | [`SKILL.md`](marketing/canva-creator/SKILL.md) |
| **`email-sequence`** | Design and draft multi-email sequences with full copy, timing, branching logic, exit conditions, and performance benchmarks. | [`SKILL.md`](marketing/email-sequence/SKILL.md) |
| **`performance-report`** | Build a marketing performance report with key metrics, trend analysis, wins and misses, and prioritized optimization recommendations. | [`SKILL.md`](marketing/performance-report/SKILL.md) |

---

<a id="development"></a>
### 💻 Desenvolvimento & Testes (17 skills)

**Caminho no repositório:** [`development/`](development/)

Engenharia de software, automação com Playwright, frameworks modernos (React, Next.js, Swift), depuração estruturada e TDD.

| Skill | Descrição | Link |
|---|---|:---:|
| **`agent-browser`** | Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating pages, filling forms, clicking buttons, taking ... | [`SKILL.md`](development/agent-browser/SKILL.md) |
| **`build-dashboard`** | Build an interactive HTML dashboard with charts, filters, and tables. | [`SKILL.md`](development/build-dashboard/SKILL.md) |
| **`build-zoom-bot`** | Build a Zoom meeting bot, recorder, or real-time media workflow. | [`SKILL.md`](development/build-zoom-bot/SKILL.md) |
| **`code-review`** | Review code changes for security, performance, and correctness. | [`SKILL.md`](development/code-review/SKILL.md) |
| **`context7-cli`** | Use the ctx7 CLI to fetch library documentation, manage AI coding skills, and configure Context7 MCP. | [`SKILL.md`](development/context7-cli/SKILL.md) |
| **`debug`** | Structured debugging session — reproduce, isolate, diagnose, and fix. | [`SKILL.md`](development/debug/SKILL.md) |
| **`find-docs`** | >-   Retrieves up-to-date documentation, API references, and code examples for any   developer technology. | [`SKILL.md`](development/find-docs/SKILL.md) |
| **`hyperframes`** | >   READ THIS FIRST for any request to make, create, edit, animate, or render a   video, animation, or motion graphic — a promo, explainer, captioned clip,  ... | [`SKILL.md`](development/hyperframes/SKILL.md) |
| **`hyperframes-cli`** | >   Use the HyperFrames CLI development loop: init, add, catalog, capture, lint, check, snapshot,   compare, grade-compare, preview, play, present, beats, ke... | [`SKILL.md`](development/hyperframes-cli/SKILL.md) |
| **`hyperframes-registry`** | Install and wire registry blocks and components into HyperFrames compositions. | [`SKILL.md`](development/hyperframes-registry/SKILL.md) |
| **`tdd`** | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. | [`SKILL.md`](development/tdd/SKILL.md) |
| **`vercel-composition-patterns`** | React composition patterns that scale. Use when refactoring components with   boolean prop proliferation, building flexible component libraries, or   designi... | [`SKILL.md`](development/vercel-composition-patterns/SKILL.md) |
| **`vercel-react-best-practices`** | React and Next.js performance optimization guidelines from Vercel Engineering. | [`SKILL.md`](development/vercel-react-best-practices/SKILL.md) |
| **`vercel-react-native-skills`** | React Native and Expo best practices for building performant mobile apps. | [`SKILL.md`](development/vercel-react-native-skills/SKILL.md) |
| **`web-artifacts-builder`** | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). | [`SKILL.md`](development/web-artifacts-builder/SKILL.md) |
| **`webapp-testing`** | Toolkit for interacting with and testing local web applications using Playwright. | [`SKILL.md`](development/webapp-testing/SKILL.md) |
| **`write-swift`** | How to write modern Swift well — modeling with value types, Swift 6 data-race safety and approachable concurrency (@concurrent, main-actor-by-default, actors... | [`SKILL.md`](development/write-swift/SKILL.md) |

---

<a id="devops-cloud"></a>
### ☁️ Cloud & DevOps (9 skills)

**Caminho no repositório:** [`devops-cloud/`](devops-cloud/)

Infraestrutura como código, nuvem Microsoft Azure, migração de cargas de trabalho, checklists pré-deploy e autenticação Entra ID.

| Skill | Descrição | Link |
|---|---|:---:|
| **`azure-cloud-migrate`** | Assess and migrate cross-cloud workloads to Azure with reports and code conversion. | [`SKILL.md`](devops-cloud/azure-cloud-migrate/SKILL.md) |
| **`azure-deploy`** | Execute Azure deployments for ALREADY-PREPARED applications that have existing .azure/deployment-plan.md and infrastructure files. | [`SKILL.md`](devops-cloud/azure-deploy/SKILL.md) |
| **`azure-diagnostics`** | Debug Azure production issues on Azure using AppLens, Azure Monitor, resource health, and safe triage. | [`SKILL.md`](devops-cloud/azure-diagnostics/SKILL.md) |
| **`azure-prepare`** | Prepare azd-based Azure projects for deployment: generates azure.yaml, infrastructure (Bicep/Terraform), and Dockerfiles for the Azure Developer CLI (azd) wo... | [`SKILL.md`](devops-cloud/azure-prepare/SKILL.md) |
| **`azure-storage`** | Azure Storage Services including Blob Storage, File Shares, Queue Storage, Table Storage, and Data Lake. | [`SKILL.md`](devops-cloud/azure-storage/SKILL.md) |
| **`azure-validate`** | Pre-deployment validation for Azure readiness. Run deep checks on configuration, infrastructure (Bicep or Terraform), RBAC role assignments, managed identity... | [`SKILL.md`](devops-cloud/azure-validate/SKILL.md) |
| **`deploy-checklist`** | Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI status an... | [`SKILL.md`](devops-cloud/deploy-checklist/SKILL.md) |
| **`entra-app-registration`** | Guides Microsoft Entra ID app registration, OAuth 2.0 authentication, and MSAL integration. | [`SKILL.md`](devops-cloud/entra-app-registration/SKILL.md) |
| **`microsoft-foundry`** | Deploy, evaluate, fine-tune, and manage Foundry agents end-to-end with azd: hosted agent scaffold/run/deploy, prompt agent create, batch eval, continuous eva... | [`SKILL.md`](devops-cloud/microsoft-foundry/SKILL.md) |

---

<a id="backend-database"></a>
### 🗄️ Backend & Banco de Dados (4 skills)

**Caminho no repositório:** [`backend-database/`](backend-database/)

Bancos de dados serverless (Neon Postgres, Supabase) e padrões de arquitetura de software (ADRs e análise de acoplamento).

| Skill | Descrição | Link |
|---|---|:---:|
| **`architecture`** | Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka vs SQS), documenting a design decision with tra... | [`SKILL.md`](backend-database/architecture/SKILL.md) |
| **`improve-codebase-architecture`** | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. | [`SKILL.md`](backend-database/improve-codebase-architecture/SKILL.md) |
| **`neon-postgres`** | >-   Guides and best practices for working with Neon Serverless Postgres. | [`SKILL.md`](backend-database/neon-postgres/SKILL.md) |
| **`supabase`** | Use when doing ANY task involving Supabase. Triggers: Supabase products (Database, Auth, Edge Functions, Realtime, Storage, Vectors, Cron, Queues); client li... | [`SKILL.md`](backend-database/supabase/SKILL.md) |

---

<a id="ai-agents"></a>
### 🤖 Agentes de IA & Metaprogramação (22 skills)

**Caminho no repositório:** [`ai-agents/`](ai-agents/)

Criação e engenharia de subagentes autônomos, servidores MCP (Model Context Protocol), plugins para Claude Code, hooks de ciclo de vida e novas skills.

| Skill | Descrição | Link |
|---|---|:---:|
| **`agent-development`** | This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent... | [`SKILL.md`](ai-agents/agent-development/SKILL.md) |
| **`build-mcp-app`** | This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "... | [`SKILL.md`](ai-agents/build-mcp-app/SKILL.md) |
| **`build-mcp-server`** | This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to... | [`SKILL.md`](ai-agents/build-mcp-server/SKILL.md) |
| **`claude-automation-recommender`** | Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). | [`SKILL.md`](ai-agents/claude-automation-recommender/SKILL.md) |
| **`claude-md-improver`** | Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. | [`SKILL.md`](ai-agents/claude-md-improver/SKILL.md) |
| **`claude-opus-4-5-migration`** | Migrate prompts and code from Claude Sonnet 4.0, Sonnet 4.5, or Opus 4.1 to Opus 4.5. | [`SKILL.md`](ai-agents/claude-opus-4-5-migration/SKILL.md) |
| **`command-development`** | This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command... | [`SKILL.md`](ai-agents/command-development/SKILL.md) |
| **`design-mcp-workflow`** | Design a Zoom MCP workflow for Claude. Use when deciding whether Zoom MCP fits a task, when planning tool-based AI workflows, or when separating MCP responsi... | [`SKILL.md`](ai-agents/design-mcp-workflow/SKILL.md) |
| **`find-skills`** | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express ... | [`SKILL.md`](ai-agents/find-skills/SKILL.md) |
| **`full-output-enforcement`** | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. | [`SKILL.md`](ai-agents/full-output-enforcement/SKILL.md) |
| **`handoff`** | Compact the current conversation into a handoff document for another agent to pick up. | [`SKILL.md`](ai-agents/handoff/SKILL.md) |
| **`hook-development`** | This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks... | [`SKILL.md`](ai-agents/hook-development/SKILL.md) |
| **`mcp-builder`** | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. | [`SKILL.md`](ai-agents/mcp-builder/SKILL.md) |
| **`mcp-integration`** | This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol... | [`SKILL.md`](ai-agents/mcp-integration/SKILL.md) |
| **`plugin-settings`** | This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin st... | [`SKILL.md`](ai-agents/plugin-settings/SKILL.md) |
| **`plugin-structure`** | This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up ... | [`SKILL.md`](ai-agents/plugin-structure/SKILL.md) |
| **`session-report`** | Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts. | [`SKILL.md`](ai-agents/session-report/SKILL.md) |
| **`setup-matt-pocock-skills`** | Configure this repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc layout. | [`SKILL.md`](ai-agents/setup-matt-pocock-skills/SKILL.md) |
| **`skill-creator`** | Create new skills, modify and improve existing skills, and measure skill performance. | [`SKILL.md`](ai-agents/skill-creator/SKILL.md) |
| **`skill-development`** | This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill... | [`SKILL.md`](ai-agents/skill-development/SKILL.md) |
| **`writing-great-skills`** | Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable. | [`SKILL.md`](ai-agents/writing-great-skills/SKILL.md) |
| **`writing-hookify-rules`** | This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on... | [`SKILL.md`](ai-agents/writing-hookify-rules/SKILL.md) |

---

<a id="documents-productivity"></a>
### 📄 Documentos & Produtividade (14 skills)

**Caminho no repositório:** [`documents-productivity/`](documents-productivity/)

Manipulação automatizada de documentos de escritório (Word, Excel, PowerPoint, PDF), vault do Obsidian e especificações técnicas.

| Skill | Descrição | Link |
|---|---|:---:|
| **`doc-coauthoring`** | Guide users through a structured workflow for co-authoring documentation. | [`SKILL.md`](documents-productivity/doc-coauthoring/SKILL.md) |
| **`documentation`** | Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README", "write a runbook", "onboarding guide", or when... | [`SKILL.md`](documents-productivity/documentation/SKILL.md) |
| **`docx`** | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.dotx files). | [`SKILL.md`](documents-productivity/docx/SKILL.md) |
| **`grill-me`** | A relentless interview to sharpen a plan or design. | [`SKILL.md`](documents-productivity/grill-me/SKILL.md) |
| **`grill-with-docs`** | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. | [`SKILL.md`](documents-productivity/grill-with-docs/SKILL.md) |
| **`humanizer`** | \|   Rewrite AI-sounding text so it reads like the writer without changing what it says. | [`SKILL.md`](documents-productivity/humanizer/SKILL.md) |
| **`obsidian-vault`** | Search, create, and manage notes in the Obsidian vault with wikilinks and index notes. | [`SKILL.md`](documents-productivity/obsidian-vault/SKILL.md) |
| **`pdf`** | Use this skill whenever the user wants to do anything with PDF files. | [`SKILL.md`](documents-productivity/pdf/SKILL.md) |
| **`pptx`** | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. | [`SKILL.md`](documents-productivity/pptx/SKILL.md) |
| **`project-artifact`** | Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success criteria, the wo... | [`SKILL.md`](documents-productivity/project-artifact/SKILL.md) |
| **`proposal-writer`** | Create compelling business proposals that win deals and partnerships | [`SKILL.md`](documents-productivity/proposal-writer/SKILL.md) |
| **`view-pdf`** | Interactive PDF viewer. Use when the user wants to open, show, or view a PDF and collaborate on it visually — annotate, highlight, stamp, fill form fields, p... | [`SKILL.md`](documents-productivity/view-pdf/SKILL.md) |
| **`write-spec`** | Write a feature spec or PRD from a problem statement or feature idea. | [`SKILL.md`](documents-productivity/write-spec/SKILL.md) |
| **`xlsx`** | Use this skill any time a spreadsheet file is the primary input or output. | [`SKILL.md`](documents-productivity/xlsx/SKILL.md) |

---

<a id="business-management"></a>
### 📊 Gestão & Negócios (14 skills)

**Caminho no repositório:** [`business-management/`](business-management/)

Análise de métricas e KPIs, governança, conformidade SOX, planejamento de capacidade de equipe, calibração de RH e briefings diários.

| Skill | Descrição | Link |
|---|---|:---:|
| **`access`** | Manage Discord channel access — approve pairings, edit allowlists, set DM/group policy. | [`SKILL.md`](business-management/access/SKILL.md) |
| **`analyze`** | Answer data questions -- from quick lookups to full analyses. | [`SKILL.md`](business-management/analyze/SKILL.md) |
| **`audit-support`** | Support SOX 404 compliance with control testing methodology, sample selection, and documentation standards. | [`SKILL.md`](business-management/audit-support/SKILL.md) |
| **`brief`** | Generate contextual briefings for legal work — daily summary, topic research, or incident response. | [`SKILL.md`](business-management/brief/SKILL.md) |
| **`capacity-plan`** | Plan resource capacity — workload analysis and utilization forecasting. | [`SKILL.md`](business-management/capacity-plan/SKILL.md) |
| **`clinical-trial-protocol-skill`** | Generate clinical trial protocols for medical devices or drugs. | [`SKILL.md`](business-management/clinical-trial-protocol-skill/SKILL.md) |
| **`comp-analysis`** | Analyze compensation — benchmarking, band placement, and equity modeling. | [`SKILL.md`](business-management/comp-analysis/SKILL.md) |
| **`configure`** | Set up the Discord channel — save the bot token and review access policy. | [`SKILL.md`](business-management/configure/SKILL.md) |
| **`daily-briefing`** | Start your day with a prioritized sales briefing. Works standalone when you tell me your meetings and priorities, supercharged when you connect your calendar... | [`SKILL.md`](business-management/daily-briefing/SKILL.md) |
| **`data-context-extractor`** | >   Generate or improve a company-specific data analysis skill by extracting tribal knowledge from analysts. | [`SKILL.md`](business-management/data-context-extractor/SKILL.md) |
| **`data-visualization`** | Create effective data visualizations with Python (matplotlib, seaborn, plotly). | [`SKILL.md`](business-management/data-visualization/SKILL.md) |
| **`performance-review`** | Structure a performance review with self-assessment, manager template, and calibration prep. | [`SKILL.md`](business-management/performance-review/SKILL.md) |
| **`pipeline-review`** | Analyze pipeline health — prioritize deals, flag risks, get a weekly action plan. | [`SKILL.md`](business-management/pipeline-review/SKILL.md) |
| **`triage`** | Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if needed, and write agent-ready briefs. | [`SKILL.md`](business-management/triage/SKILL.md) |

---

<a id="utilities"></a>
### 🛠️ Utilitários & Otimização (5 skills)

**Caminho no repositório:** [`utilities/`](utilities/)

Modo ultra-conciso (Caveman) para economia massiva de tokens de contexto, playbooks interativos e helpers.

| Skill | Descrição | Link |
|---|---|:---:|
| **`caveman`** | >   Ultra-compressed communication mode. Cuts output tokens 65% (measured) by speaking like caveman   while keeping full technical accuracy. | [`SKILL.md`](utilities/caveman/SKILL.md) |
| **`caveman-commit`** | >   Ultra-compressed commit message generator. Cuts noise from commit messages while preserving   intent and reasoning. | [`SKILL.md`](utilities/caveman-commit/SKILL.md) |
| **`caveman-help`** | >   Quick-reference card for all caveman modes, skills, and commands. | [`SKILL.md`](utilities/caveman-help/SKILL.md) |
| **`caveman-review`** | >   Ultra-compressed code review comments. Cuts noise from PR feedback while preserving   the actionable signal. | [`SKILL.md`](utilities/caveman-review/SKILL.md) |
| **`playground`** | Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview,... | [`SKILL.md`](utilities/playground/SKILL.md) |

---

## 🤝 Contribuição e Licença

Para adicionar novas skills a este repositório, basta criar uma pasta com o nome da skill dentro da categoria mais adequada contendo seu respectivo `SKILL.md` formatado com frontmatter YAML.

Repositório mantido por [Henrique1601](https://github.com/Henrique1601).