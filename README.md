# 🧠 Skills to IAs (`SkiilsToIAs`)

Repositório centralizado e categorizado contendo **484 skills especializadas** para agentes autônomos de Inteligência Artificial (compatível com **Antigravity**, **Claude Code**, **Cursor**, **Copilot CLI**, entre outros).

> [!TIP]
> ### 🧠 Quer saber como usar, quando usar e quais prompts fazer?
> Consulte o [**Cérebro das Skills (`CEREBRO.md`)**](CEREBRO.md) — o manual mestre completo com:
> - **Como a IA pensa e ativa as skills** (Anatomia, gatilhos e fórmula do prompt perfeito).
> - **Power Combos**: Workflows multi-skill encadeados (Landing pages, Fullstack, Carreira, Cloud, MCP, etc.).
> - **Cheat Sheet**: Tabela rápida de decisão ("O que você quer fazer hoje?").
> - **Prompts Prontos**: Exemplos práticos para copiar e colar para as skills catalogadas!

---

## 📊 Visão Geral das Categorias

| Categoria | Pasta | Quantidade | Foco Principal |
|---|---|:---:|---|
| [🎨 Design & UI/UX](#design) | [`design/`](design/) | **58** | Skills especializadas em interface de usuário, design systems, estética anti-slop, micro-interações, tipografia, animações e tokens visuais. |
| [🔍 SEO & Mecanismos de Busca](#seo) | [`seo/`](seo/) | **8** | Skills dedicadas a auditoria técnica de SEO, otimização de Core Web Vitals, indexação e inteligência competitiva. |
| [📣 Marketing & Vendas](#marketing) | [`marketing/`](marketing/) | **16** | Skills para comunicação de marca, criação de campanhas visuais, réguas de e-mail marketing, LinkedIn marketing e relatórios de performance. |
| [🎯 Carreira & Empregabilidade](#career) | [`career/`](career/) | **22** | Skills para elaboração de currículos de alto impacto (compatíveis com ATS), cartas de apresentação, preparação para entrevistas, otimização de LinkedIn e negociação salarial. |
| [💻 Desenvolvimento & Testes](#development) | [`development/`](development/) | **88** | Engenharia de software, automação com Playwright, frameworks modernos (React, Next.js, Swift, Flutter), arquitetura limpa, depuração estruturada e TDD. |
| [☁️ Cloud & DevOps](#devops-cloud) | [`devops-cloud/`](devops-cloud/) | **39** | Infraestrutura como código, nuvem (AWS, Azure, Cloudflare, Netlify), redes locais/homelab, Docker, Kubernetes, checklists pré-deploy e automação. |
| [🗄️ Backend & Bancos de Dados](#backend-database) | [`backend-database/`](backend-database/) | **61** | Bancos serverless, SQL, NoSQL (MongoDB, Neon Postgres, Supabase, ClickHouse, MySQL, Redis), frameworks backend modernos, ORMs e otimização de queries. |
| [🤖 Agentes de IA & Metaprogramação](#ai-agents) | [`ai-agents/`](ai-agents/) | **94** | Criação e engenharia de subagentes autônomos, servidores MCP (Model Context Protocol), harnesses, loops contínuos de execução, hooks de ciclo de vida e novas skills. |
| [📄 Documentos & Produtividade](#documents-productivity) | [`documents-productivity/`](documents-productivity/) | **26** | Manipulação automatizada de documentos de escritório (Word, Excel, PowerPoint, PDF), pesquisa científica, patentes, Obsidian e especificações técnicas. |
| [📊 Gestão & Negócios](#business-management) | [`business-management/`](business-management/) | **43** | Análise de métricas e KPIs, governança, conformidade regulatória (SOX, HIPAA), supply chain, logística, CRM, faturamento e briefings executivos. |
| [🛠️ Utilitários & Otimização](#utilities) | [`utilities/`](utilities/) | **29** | Modo ultra-conciso (Caveman) para economia massiva de tokens de contexto, web scraping, auditoria de segurança, playbooks interativos e integrações. |

> **Total de Skills catalogadas:** 484 skills em 11 categorias

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
### 🎨 Design & UI/UX (58 skills)

**Caminho no repositório:** [`design/`](design/)

Skills especializadas em interface de usuário, design systems, estética anti-slop, micro-interações, tipografia, animações e tokens visuais.

| Skill | Descrição | Link |
|---|---|:---:|
| **`accessibility-review`** | Run a WCAG 2.1 AA accessibility audit on a design or page. Trigger with "audit accessibility", "check a11y", "is this accessible?", or when reviewing a desig... | [`SKILL.md`](design/accessibility-review/SKILL.md) |
| **`animate`** | Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at all, what purpose, which too... | [`SKILL.md`](design/animate/SKILL.md) |
| **`animate-expo`** | Build animations in React Native and Expo, making the decisions in the order that determines whether they feel right — should it animate, which thread it run... | [`SKILL.md`](design/animate-expo/SKILL.md) |
| **`animation-vocabulary`** | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover opens" → Pop... | [`SKILL.md`](design/animation-vocabulary/SKILL.md) |
| **`apple-design`** | Apple's approach to interface design and fluid, physical motion, translated for the web. Use when building or reviewing gesture-driven UI, spring animations,... | [`SKILL.md`](design/apple-design/SKILL.md) |
| **`ask-sonner`** | Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call, promise and loading toasts, updating, dismissing and... | [`SKILL.md`](design/ask-sonner/SKILL.md) |
| **`blender-motion-state-inspection`** | Use this skill when inspecting Blender characters, rigs, poses, animation retargeting, ground contact, facing direction, or model-vs-motion alignment where s... | [`SKILL.md`](design/blender-motion-state-inspection/SKILL.md) |
| **`brandkit`** | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. Trained... | [`SKILL.md`](design/brandkit/SKILL.md) |
| **`canvas-design`** | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art... | [`SKILL.md`](design/canvas-design/SKILL.md) |
| **`design-critique`** | Get structured design feedback on usability, hierarchy, and consistency. Trigger with "review this design", "critique this mockup", "what do you think of thi... | [`SKILL.md`](design/design-critique/SKILL.md) |
| **`design-system`** | Use this skill to generate or audit design systems, check visual consistency, and review PRs that touch styling. | [`SKILL.md`](design/design-system/SKILL.md) |
| **`design-taste-frontend`** | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces tha... | [`SKILL.md`](design/design-taste-frontend/SKILL.md) |
| **`design-taste-frontend-v1`** | The original v1 taste-skill, preserved for projects depending on its exact behavior. The current default is `design-taste-frontend` (v2 experimental), which ... | [`SKILL.md`](design/design-taste-frontend-v1/SKILL.md) |
| **`emil-design-eng`** | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great. | [`SKILL.md`](design/emil-design-eng/SKILL.md) |
| **`find-animation-opportunities`** | Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. Read-only; it proposes motion with exact values, it d... | [`SKILL.md`](design/find-animation-opportunities/SKILL.md) |
| **`fixing-motion-performance`** | Audit and fix animation performance issues including layout thrashing, compositor properties, scroll-linked motion, and blur effects. Use when animations stu... | [`SKILL.md`](design/fixing-motion-performance/SKILL.md) |
| **`frontend-design`** | Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifact... | [`SKILL.md`](design/frontend-design/SKILL.md) |
| **`frontend-design-direction`** | Set an ECC-specific frontend design direction for production UI work. Use when building or improving websites, dashboards, applications, components, landing ... | [`SKILL.md`](design/frontend-design-direction/SKILL.md) |
| **`frontend-slides`** | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Use when the user wants to build a presentation, convert a... | [`SKILL.md`](design/frontend-slides/SKILL.md) |
| **`gpt-taste`** | Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide editorial typogr... | [`SKILL.md`](design/gpt-taste/SKILL.md) |
| **`gsap`** | GSAP animation reference for HyperFrames. Covers gsap.to(), from(), fromTo(), easing, stagger, defaults, timelines (gsap.timeline(), position parameter, labe... | [`SKILL.md`](design/gsap/SKILL.md) |
| **`high-end-visual-design`** | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensiv... | [`SKILL.md`](design/high-end-visual-design/SKILL.md) |
| **`image-to-code`** | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, then i... | [`SKILL.md`](design/image-to-code/SKILL.md) |
| **`imagegen-frontend-mobile`** | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-platform mobile prod... | [`SKILL.md`](design/imagegen-frontend-mobile/SKILL.md) |
| **`imagegen-frontend-web`** | Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE separate horizon... | [`SKILL.md`](design/imagegen-frontend-web/SKILL.md) |
| **`improve-animations`** | Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained implementation plans for other ... | [`SKILL.md`](design/improve-animations/SKILL.md) |
| **`industrial-brutalist-ui`** | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian color, anal... | [`SKILL.md`](design/industrial-brutalist-ui/SKILL.md) |
| **`liquid-glass-design`** | iOS 26 Liquid Glass design system — dynamic glass material with blur, reflection, and interactive morphing for SwiftUI, UIKit, and WidgetKit. | [`SKILL.md`](design/liquid-glass-design/SKILL.md) |
| **`make-interfaces-feel-better`** | Apply concrete design-engineering details that make interfaces feel polished. Use when reviewing or improving UI spacing, typography, borders, shadows, motio... | [`SKILL.md`](design/make-interfaces-feel-better/SKILL.md) |
| **`manim-video`** | Build reusable Manim explainers for technical concepts, graphs, system diagrams, and product walkthroughs, then hand off to the wider ECC video stack if need... | [`SKILL.md`](design/manim-video/SKILL.md) |
| **`minimalist-ui`** | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows. | [`SKILL.md`](design/minimalist-ui/SKILL.md) |
| **`mobile-native`** | Make a web app feel native on a phone — the small CSS and meta-tag fixes that separate "a website in a browser" from something that feels installed. Covers s... | [`SKILL.md`](design/mobile-native/SKILL.md) |
| **`motion-advanced`** | Advanced motion patterns for React / Next.js — drag & drop, gestures, text animations, SVG path drawing, custom hooks, imperative sequences (useAnimate), loa... | [`SKILL.md`](design/motion-advanced/SKILL.md) |
| **`motion-foundations`** | Motion tokens, spring presets, performance rules, device adaptation, accessibility enforcement, and SSR safety for React / Next.js using motion/react. Founda... | [`SKILL.md`](design/motion-foundations/SKILL.md) |
| **`motion-graphics`** |  | [`SKILL.md`](design/motion-graphics/SKILL.md) |
| **`motion-patterns`** | Production-ready animation patterns for React / Next.js — button, modal, toast, stagger, page transitions, exit animations, scroll, and layout — built on mot... | [`SKILL.md`](design/motion-patterns/SKILL.md) |
| **`motion-ui`** | Production-ready UI motion system for React/Next.js. Use when implementing animations, transitions, or motion patterns. | [`SKILL.md`](design/motion-ui/SKILL.md) |
| **`pick-ui-library`** | Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs, charts, command menus, virtualization, drag and drop... | [`SKILL.md`](design/pick-ui-library/SKILL.md) |
| **`prototype`** | Build multiple genuinely different versions of a UI piece you describe, rendered behind a visual picker so you can flip through them live and promote the one... | [`SKILL.md`](design/prototype/SKILL.md) |
| **`redesign-existing-projects`** | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without ... | [`SKILL.md`](design/redesign-existing-projects/SKILL.md) |
| **`remotion-best-practices`** | Best practices for Remotion | [`SKILL.md`](design/remotion-best-practices/SKILL.md) |
| **`remotion-to-hyperframes`** | Port an existing Remotion (React) composition''s source to HyperFrames HTML. Use ONLY on an explicit ask to port/convert/migrate/translate a Remotion source ... | [`SKILL.md`](design/remotion-to-hyperframes/SKILL.md) |
| **`remotion-video-creation`** | Best practices for Remotion - Video creation in React. 29 domain-specific rules covering 3D, animations, audio, captions, charts, transitions, and more. | [`SKILL.md`](design/remotion-video-creation/SKILL.md) |
| **`review-animations`** | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. Default to flagging; approval is earned. | [`SKILL.md`](design/review-animations/SKILL.md) |
| **`shadcn`** | Manages shadcn components and projects — adding, searching, fixing, debugging, styling, and composing UI. Provides project context, component docs, and usage... | [`SKILL.md`](design/shadcn/SKILL.md) |
| **`slack-gif-creator`** | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users reques... | [`SKILL.md`](design/slack-gif-creator/SKILL.md) |
| **`stitch-design-taste`** | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography,... | [`SKILL.md`](design/stitch-design-taste/SKILL.md) |
| **`taste`** | A creative-direction (taste) layer for music videos and short-form edits in the angelcore / cloud-trance / hyperpop visual family. Distills a named-genre aes... | [`SKILL.md`](design/taste/SKILL.md) |
| **`theme-factory`** | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors... | [`SKILL.md`](design/theme-factory/SKILL.md) |
| **`ui-demo`** | Record polished UI demo videos using Playwright. Use when the user asks to create a demo, walkthrough, screen recording, or tutorial video of a web applicati... | [`SKILL.md`](design/ui-demo/SKILL.md) |
| **`ui-to-vue`** | Use when the user has UI screenshots or design exports that need batch conversion into Vue 3 components, especially with Vant, Element Plus, or Ant Design Vue. | [`SKILL.md`](design/ui-to-vue/SKILL.md) |
| **`ui-toolkit-web`** | Reference skill for Zoom Video SDK UI Toolkit. Use after routing to a web video workflow when you want prebuilt React UI instead of building a fully custom V... | [`SKILL.md`](design/ui-toolkit-web/SKILL.md) |
| **`ui-ux-pro-max`** | UI/UX design intelligence for web and mobile. Includes 50+ styles, 161 color palettes, 57 font pairings, 161 product types, 99 UX guidelines, and 25 chart ty... | [`SKILL.md`](design/ui-ux-pro-max/SKILL.md) |
| **`ux-copy`** | Write or review UX copy — microcopy, error messages, empty states, CTAs. Trigger with "write copy for", "what should this button say?", "review this error me... | [`SKILL.md`](design/ux-copy/SKILL.md) |
| **`video-edit`** |  | [`SKILL.md`](design/video-edit/SKILL.md) |
| **`video-editing`** | AI-assisted video editing workflows for cutting, structuring, and augmenting real footage. Covers the full pipeline from raw capture through FFmpeg, Remotion... | [`SKILL.md`](design/video-editing/SKILL.md) |
| **`videodb`** | See, Understand, Act on video and audio. See- ingest from local files, URLs, RTSP/live feeds, or live record desktop; return realtime context and playable st... | [`SKILL.md`](design/videodb/SKILL.md) |
| **`web-design-guidelines`** | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my si... | [`SKILL.md`](design/web-design-guidelines/SKILL.md) |

---

<a id="seo"></a>
### 🔍 SEO & Mecanismos de Busca (8 skills)

**Caminho no repositório:** [`seo/`](seo/)

Skills dedicadas a auditoria técnica de SEO, otimização de Core Web Vitals, indexação e inteligência competitiva.

| Skill | Descrição | Link |
|---|---|:---:|
| **`click-path-audit`** | Trace every user-facing button/touchpoint through its full state change sequence to find bugs where functions individually work but cancel each other out, pr... | [`SKILL.md`](seo/click-path-audit/SKILL.md) |
| **`competitive-brief`** | Research competitors and generate a positioning and messaging comparison with content gaps, opportunities, and threats. Use when building sales battlecards, ... | [`SKILL.md`](seo/competitive-brief/SKILL.md) |
| **`competitive-intelligence`** | Research your competitors and build an interactive battlecard. Outputs an HTML artifact with clickable competitor cards and a comparison matrix. Trigger with... | [`SKILL.md`](seo/competitive-intelligence/SKILL.md) |
| **`competitive-platform-analysis`** |  | [`SKILL.md`](seo/competitive-platform-analysis/SKILL.md) |
| **`competitive-report-structure`** |  | [`SKILL.md`](seo/competitive-report-structure/SKILL.md) |
| **`lighthouse`** | Google Lighthouse CLI reference for auditing web performance, accessibility, SEO, and best practices. Use this skill when users need to analyze website perfo... | [`SKILL.md`](seo/lighthouse/SKILL.md) |
| **`seo`** | Audit, plan, and implement SEO improvements across technical SEO, on-page optimization, structured data, Core Web Vitals, and content strategy. Use when the ... | [`SKILL.md`](seo/seo/SKILL.md) |
| **`seo-audit`** | When the user wants to audit, review, or diagnose SEO issues on their site. Also use when the user mentions "SEO audit," "technical SEO," "why am I not ranki... | [`SKILL.md`](seo/seo-audit/SKILL.md) |

---

<a id="marketing"></a>
### 📣 Marketing & Vendas (16 skills)

**Caminho no repositório:** [`marketing/`](marketing/)

Skills para comunicação de marca, criação de campanhas visuais, réguas de e-mail marketing, LinkedIn marketing e relatórios de performance.

| Skill | Descrição | Link |
|---|---|:---:|
| **`account-research`** | Research a company or person and get actionable sales intel. Works standalone with web search, supercharged when you connect enrichment tools or your CRM. Tr... | [`SKILL.md`](marketing/account-research/SKILL.md) |
| **`amazon-product-research`** | Comprehensive product research and opportunity analysis for Amazon sellers. Analyzes demand, competition, profit potential, market entry barriers, and valida... | [`SKILL.md`](marketing/amazon-product-research/SKILL.md) |
| **`brand-discovery`** |  | [`SKILL.md`](marketing/brand-discovery/SKILL.md) |
| **`brand-review`** | Review content against your brand voice, style guide, and messaging pillars, flagging deviations by severity with specific before/after fixes. Use when check... | [`SKILL.md`](marketing/brand-review/SKILL.md) |
| **`brand-voice`** | Build a source-derived writing style profile from real posts, essays, launch notes, docs, or site copy, then reuse that profile across content, outreach, and... | [`SKILL.md`](marketing/brand-voice/SKILL.md) |
| **`brand-voice-enforcement`** |  | [`SKILL.md`](marketing/brand-voice-enforcement/SKILL.md) |
| **`canva-creator`** |  | [`SKILL.md`](marketing/canva-creator/SKILL.md) |
| **`content-engine`** | Create platform-native content systems for X, LinkedIn, TikTok, YouTube, newsletters, and repurposed multi-platform campaigns. Use when the user wants social... | [`SKILL.md`](marketing/content-engine/SKILL.md) |
| **`crosspost`** | Multi-platform content distribution across X, LinkedIn, Threads, and Bluesky. Adapts content per platform using content-engine patterns. Never posts identica... | [`SKILL.md`](marketing/crosspost/SKILL.md) |
| **`email-sequence`** | Design and draft multi-email sequences with full copy, timing, branching logic, exit conditions, and performance benchmarks. Use when building onboarding, le... | [`SKILL.md`](marketing/email-sequence/SKILL.md) |
| **`linkedin-marketing`** | Plan, draft, audit, and publish LinkedIn posts and comments. Use when the user wants to write a viral LinkedIn post, draft a comment or reply on any LinkedIn... | [`SKILL.md`](marketing/linkedin-marketing/SKILL.md) |
| **`marketing-campaign`** | End-to-end marketing campaign planning and execution. Covers audience research, positioning, campaign angle definition, landing page copy, email sequences, s... | [`SKILL.md`](marketing/marketing-campaign/SKILL.md) |
| **`performance-report`** | Build a marketing performance report with key metrics, trend analysis, wins and misses, and prioritized optimization recommendations. Use when wrapping a cam... | [`SKILL.md`](marketing/performance-report/SKILL.md) |
| **`social-graph-ranker`** | Weighted social-graph ranking for warm intro discovery, bridge scoring, and network gap analysis across X and LinkedIn. Use when the user wants the reusable ... | [`SKILL.md`](marketing/social-graph-ranker/SKILL.md) |
| **`social-publisher`** | Agent-driven scheduling and publishing of social media posts across 13 platforms via SocialClaw. Use when the user wants to publish to X, LinkedIn, Instagram... | [`SKILL.md`](marketing/social-publisher/SKILL.md) |
| **`x-api`** | X/Twitter API integration for posting tweets, threads, reading timelines, search, and analytics. Covers OAuth auth patterns, rate limits, and platform-native... | [`SKILL.md`](marketing/x-api/SKILL.md) |

---

<a id="career"></a>
### 🎯 Carreira & Empregabilidade (22 skills)

**Caminho no repositório:** [`career/`](career/)

Skills para elaboração de currículos de alto impacto (compatíveis com ATS), cartas de apresentação, preparação para entrevistas, otimização de LinkedIn e negociação salarial.

| Skill | Descrição | Link |
|---|---|:---:|
| **`academic-cv-builder`** | Format CVs for academic positions with publications, grants, and teaching | [`SKILL.md`](career/academic-cv-builder/SKILL.md) |
| **`application-form-filler`** | Fill out job application form fields with context-aware, tailored answers drawn from the candidate's CV and the job description | [`SKILL.md`](career/application-form-filler/SKILL.md) |
| **`career-changer-translator`** | Translate skills from one industry to another, identify transferable skills | [`SKILL.md`](career/career-changer-translator/SKILL.md) |
| **`cold-email-writer`** | Write personalized cold outreach emails to hiring managers and founders — specific, human, not a pitch deck | [`SKILL.md`](career/cold-email-writer/SKILL.md) |
| **`cover-letter-generator`** | Create personalized, compelling cover letters from resume and job description | [`SKILL.md`](career/cover-letter-generator/SKILL.md) |
| **`creative-portfolio-resume`** | Balance visual design with ATS compatibility for creative roles | [`SKILL.md`](career/creative-portfolio-resume/SKILL.md) |
| **`executive-resume-writer`** | Create C-suite and VP level resumes emphasizing strategic leadership | [`SKILL.md`](career/executive-resume-writer/SKILL.md) |
| **`interview-prep-generator`** | Generate STAR stories, practice questions, and talking points from resume | [`SKILL.md`](career/interview-prep-generator/SKILL.md) |
| **`job-description-analyzer`** | Analyze job postings, calculate match scores, identify gaps, and create application strategy | [`SKILL.md`](career/job-description-analyzer/SKILL.md) |
| **`linkedin-profile-optimizer`** | Optimize LinkedIn profile for searchability, recruiter visibility, and engagement | [`SKILL.md`](career/linkedin-profile-optimizer/SKILL.md) |
| **`offer-comparison-analyzer`** | Compare multiple job offers side-by-side with total compensation analysis | [`SKILL.md`](career/offer-comparison-analyzer/SKILL.md) |
| **`portfolio-case-study-writer`** | Transform resume bullets into detailed portfolio case studies | [`SKILL.md`](career/portfolio-case-study-writer/SKILL.md) |
| **`reference-list-builder`** | Format professional references properly and prepare reference materials | [`SKILL.md`](career/reference-list-builder/SKILL.md) |
| **`resume-ats-optimizer`** | Optimize resumes for Applicant Tracking Systems, check ATS compatibility, and analyze keyword match | [`SKILL.md`](career/resume-ats-optimizer/SKILL.md) |
| **`resume-bullet-writer`** | Transform weak resume bullets into achievement-focused statements with metrics and impact | [`SKILL.md`](career/resume-bullet-writer/SKILL.md) |
| **`resume-formatter`** | Ensure ATS-friendly formatting and create clean scannable layouts | [`SKILL.md`](career/resume-formatter/SKILL.md) |
| **`resume-quantifier`** | Find opportunities to add metrics and estimate numbers when exact data unavailable | [`SKILL.md`](career/resume-quantifier/SKILL.md) |
| **`resume-section-builder`** | Create targeted resume sections optimized for different experience levels and roles | [`SKILL.md`](career/resume-section-builder/SKILL.md) |
| **`resume-tailor`** | Customize resume for specific job postings while maintaining truthfulness | [`SKILL.md`](career/resume-tailor/SKILL.md) |
| **`resume-version-manager`** | Track different resume versions, maintain master resume, manage tailored versions | [`SKILL.md`](career/resume-version-manager/SKILL.md) |
| **`salary-negotiation-prep`** | Research market rates, build negotiation strategy, and create counter-offer scripts | [`SKILL.md`](career/salary-negotiation-prep/SKILL.md) |
| **`tech-resume-optimizer`** | Optimize resumes for software engineering, PM, and technical roles | [`SKILL.md`](career/tech-resume-optimizer/SKILL.md) |

---

<a id="development"></a>
### 💻 Desenvolvimento & Testes (88 skills)

**Caminho no repositório:** [`development/`](development/)

Engenharia de software, automação com Playwright, frameworks modernos (React, Next.js, Swift, Flutter), arquitetura limpa, depuração estruturada e TDD.

| Skill | Descrição | Link |
|---|---|:---:|
| **`accessibility`** | Audit and improve web accessibility following WCAG 2.2 guidelines. Use when asked to "improve accessibility", "a11y audit", "WCAG compliance", "screen reader... | [`SKILL.md`](development/accessibility/SKILL.md) |
| **`agent-browser`** | Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating pages, filling forms, clicking buttons, taking ... | [`SKILL.md`](development/agent-browser/SKILL.md) |
| **`android-clean-architecture`** | Clean Architecture patterns for Android and Kotlin Multiplatform projects — module structure, dependency rules, UseCases, Repositories, and data layer patterns. | [`SKILL.md`](development/android-clean-architecture/SKILL.md) |
| **`angular-developer`** | Generates Angular code and provides architectural guidance. Trigger when creating projects, components, or services, or for best practices on reactivity (sig... | [`SKILL.md`](development/angular-developer/SKILL.md) |
| **`benchmark`** | Use this skill to measure performance baselines, detect regressions before/after PRs, and compare stack alternatives. | [`SKILL.md`](development/benchmark/SKILL.md) |
| **`benchmark-methodology`** |  | [`SKILL.md`](development/benchmark-methodology/SKILL.md) |
| **`benchmark-optimization-loop`** | Use when the user asks to make something faster, try many variants, run recursive optimization, benchmark latency/throughput/cost, or choose the best impleme... | [`SKILL.md`](development/benchmark-optimization-loop/SKILL.md) |
| **`blueprint`** |  | [`SKILL.md`](development/blueprint/SKILL.md) |
| **`brainstorming`** | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requi... | [`SKILL.md`](development/brainstorming/SKILL.md) |
| **`browser-qa`** | Use this skill to automate visual testing and UI interaction verification using browser automation after deploying features. | [`SKILL.md`](development/browser-qa/SKILL.md) |
| **`build-dashboard`** | Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive overview with KPI cards, turning query results into a sh... | [`SKILL.md`](development/build-dashboard/SKILL.md) |
| **`build-zoom-bot`** | Build a Zoom meeting bot, recorder, or real-time media workflow. Use when joining meetings programmatically, processing live media or transcripts, or combini... | [`SKILL.md`](development/build-zoom-bot/SKILL.md) |
| **`bun-runtime`** | Bun as runtime, package manager, bundler, and test runner. When to choose Bun vs Node, migration notes, and Vercel support. | [`SKILL.md`](development/bun-runtime/SKILL.md) |
| **`code-review`** | Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when ch... | [`SKILL.md`](development/code-review/SKILL.md) |
| **`code-tour`** | Create CodeTour `.tour` files — persona-targeted, step-by-step walkthroughs with real file and line anchors. Use for onboarding tours, architecture walkthrou... | [`SKILL.md`](development/code-tour/SKILL.md) |
| **`codebase-design`** | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a... | [`SKILL.md`](development/codebase-design/SKILL.md) |
| **`codebase-onboarding`** | Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map, key entry points, conventions, and a starter CLAUDE.md. Use ... | [`SKILL.md`](development/codebase-onboarding/SKILL.md) |
| **`coding-standards`** | Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review. Use detailed frontend or backend skills for framewo... | [`SKILL.md`](development/coding-standards/SKILL.md) |
| **`compose-multiplatform-patterns`** | Compose Multiplatform and Jetpack Compose patterns for KMP projects — state management, navigation, theming, performance, and platform-specific UI. | [`SKILL.md`](development/compose-multiplatform-patterns/SKILL.md) |
| **`context7-cli`** | Use the ctx7 CLI to fetch library documentation, manage AI coding skills, and configure Context7 MCP. Activate when the user mentions "ctx7" or "context7", n... | [`SKILL.md`](development/context7-cli/SKILL.md) |
| **`cpp-coding-standards`** | C++ coding standards based on the C++ Core Guidelines (isocpp.github.io). Use when writing, reviewing, or refactoring C++ code to enforce modern, safe, and i... | [`SKILL.md`](development/cpp-coding-standards/SKILL.md) |
| **`cpp-testing`** | Use only when writing/updating/fixing C++ tests, configuring GoogleTest/CTest, diagnosing failing or flaky tests, or adding coverage/sanitizers. | [`SKILL.md`](development/cpp-testing/SKILL.md) |
| **`csharp-testing`** | C# and .NET testing patterns with xUnit, FluentAssertions, mocking, integration tests, and test organization best practices. | [`SKILL.md`](development/csharp-testing/SKILL.md) |
| **`dart-flutter-patterns`** | Production-ready Dart and Flutter patterns covering null safety, immutable state, async composition, widget architecture, popular state management frameworks... | [`SKILL.md`](development/dart-flutter-patterns/SKILL.md) |
| **`dashboard-builder`** | Build monitoring dashboards that answer real operator questions for Grafana, SigNoz, and similar platforms. Use when turning metrics into a working dashboard... | [`SKILL.md`](development/dashboard-builder/SKILL.md) |
| **`data-throughput-accelerator`** | Use when large data ingestion, backfill, export, ETL, warehouse loading, manifest catch-up, or table synchronization needs to become much faster while preser... | [`SKILL.md`](development/data-throughput-accelerator/SKILL.md) |
| **`debug`** | Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not prod", "so... | [`SKILL.md`](development/debug/SKILL.md) |
| **`dmux-workflows`** | Multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows across Claude Code, Codex, OpenCode, and other ... | [`SKILL.md`](development/dmux-workflows/SKILL.md) |
| **`documentation-lookup`** | Use up-to-date library and framework docs via Context7 MCP instead of training data. Activates for setup questions, API references, code examples, or when th... | [`SKILL.md`](development/documentation-lookup/SKILL.md) |
| **`dotnet-patterns`** | Idiomatic C# and .NET patterns, conventions, dependency injection, async/await, and best practices for building robust, maintainable .NET applications. | [`SKILL.md`](development/dotnet-patterns/SKILL.md) |
| **`e2e-testing`** | Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and flaky test strategies. | [`SKILL.md`](development/e2e-testing/SKILL.md) |
| **`error-handling`** | Patterns for robust error handling across TypeScript, Python, and Go. Covers typed errors, error boundaries, retries, circuit breakers, and user-facing error... | [`SKILL.md`](development/error-handling/SKILL.md) |
| **`find-docs`** |  | [`SKILL.md`](development/find-docs/SKILL.md) |
| **`fixing-accessibility`** | Audit and fix HTML accessibility issues including ARIA labels, keyboard navigation, focus management, color contrast, and form errors. Use when adding intera... | [`SKILL.md`](development/fixing-accessibility/SKILL.md) |
| **`flox-environments`** | Create reproducible, cross-platform (macOS/Linux) development environments with Flox, a declarative Nix-based environment manager. Use when setting up projec... | [`SKILL.md`](development/flox-environments/SKILL.md) |
| **`flutter-dart-code-review`** | Library-agnostic Flutter/Dart code review checklist covering widget best practices, state management patterns (BLoC, Riverpod, Provider, GetX, MobX, Signals)... | [`SKILL.md`](development/flutter-dart-code-review/SKILL.md) |
| **`foundation-models-on-device`** | Apple FoundationModels framework for on-device LLM — text generation, guided generation with @Generable, tool calling, and snapshot streaming in iOS 26+. | [`SKILL.md`](development/foundation-models-on-device/SKILL.md) |
| **`frontend-a11y`** |  | [`SKILL.md`](development/frontend-a11y/SKILL.md) |
| **`frontend-patterns`** | Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices. | [`SKILL.md`](development/frontend-patterns/SKILL.md) |
| **`fsharp-testing`** | F# testing patterns with xUnit, FsUnit, Unquote, FsCheck property-based testing, integration tests, and test organization best practices. | [`SKILL.md`](development/fsharp-testing/SKILL.md) |
| **`generating-python-installer`** | Commercial-grade Python installer expert for Windows: Nuitka extreme compilation, dist slimming, DLL footprint analysis, and Inno Setup packaging to ship the... | [`SKILL.md`](development/generating-python-installer/SKILL.md) |
| **`git-commit`** | Execute git commit with conventional commit message analysis, intelligent staging, and message generation. Use when user asks to commit changes, create a git... | [`SKILL.md`](development/git-commit/SKILL.md) |
| **`git-workflow`** | Git workflow patterns including branching strategies, commit conventions, merge vs rebase, conflict resolution, and collaborative development best practices ... | [`SKILL.md`](development/git-workflow/SKILL.md) |
| **`golang-testing`** | Go testing patterns including table-driven tests, subtests, benchmarks, fuzzing, and test coverage. Follows TDD methodology with idiomatic Go practices. | [`SKILL.md`](development/golang-testing/SKILL.md) |
| **`hyperframes`** |  | [`SKILL.md`](development/hyperframes/SKILL.md) |
| **`hyperframes-animation`** | All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the sev... | [`SKILL.md`](development/hyperframes-animation/SKILL.md) |
| **`hyperframes-cli`** |  | [`SKILL.md`](development/hyperframes-cli/SKILL.md) |
| **`hyperframes-core`** | The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="clip"`, tracks, s... | [`SKILL.md`](development/hyperframes-core/SKILL.md) |
| **`hyperframes-registry`** | Install and wire registry blocks and components into HyperFrames compositions. Use when running hyperframes add, installing a block or component, wiring an i... | [`SKILL.md`](development/hyperframes-registry/SKILL.md) |
| **`inherit-legacy-style`** | Legacy-project style inheritance skill. Use when the user types /inherit-legacy-style, or when onboarding an AI coding agent onto a hand-written legacy proje... | [`SKILL.md`](development/inherit-legacy-style/SKILL.md) |
| **`intent-driven-development`** | Turn ambiguous or high-impact product and engineering changes into scoped, verifiable acceptance criteria before or alongside implementation. Use when a user... | [`SKILL.md`](development/intent-driven-development/SKILL.md) |
| **`java-coding-standards`** | Java coding standards for Spring Boot and Quarkus services: naming, immutability, Optional usage, streams, exceptions, generics, CDI, reactive patterns, and ... | [`SKILL.md`](development/java-coding-standards/SKILL.md) |
| **`kotlin-coroutines-flows`** | Kotlin Coroutines and Flow patterns for Android and KMP — structured concurrency, Flow operators, StateFlow, error handling, and testing. | [`SKILL.md`](development/kotlin-coroutines-flows/SKILL.md) |
| **`kotlin-patterns`** | Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient, and maintainable Kotlin applications with coroutines, null safety,... | [`SKILL.md`](development/kotlin-patterns/SKILL.md) |
| **`kotlin-testing`** | Kotlin testing patterns with Kotest, MockK, coroutine testing, property-based testing, and Kover coverage. Follows TDD methodology with idiomatic Kotlin prac... | [`SKILL.md`](development/kotlin-testing/SKILL.md) |
| **`ml-adoption-playbook`** | End-to-end methodology for AI agents and software engineers to add machine learning algorithms to existing non-ML codebases. Covers problem framing, data rea... | [`SKILL.md`](development/ml-adoption-playbook/SKILL.md) |
| **`mle-workflow`** | Production machine-learning engineering workflow for data contracts, reproducible training, model evaluation, deployment, monitoring, and rollback. Use when ... | [`SKILL.md`](development/mle-workflow/SKILL.md) |
| **`next-best-practices`** | Next.js best practices - file conventions, RSC boundaries, data patterns, async APIs, metadata, error handling, route handlers, image/font optimization, bund... | [`SKILL.md`](development/next-best-practices/SKILL.md) |
| **`nextjs-turbopack`** | Next.js 16+ and Turbopack — incremental bundling, FS caching, dev speed, and when to use Turbopack vs webpack. | [`SKILL.md`](development/nextjs-turbopack/SKILL.md) |
| **`nuxt4-patterns`** | Nuxt 4 app patterns for hydration safety, performance, route rules, lazy loading, and SSR-safe data fetching with useFetch and useAsyncData. | [`SKILL.md`](development/nuxt4-patterns/SKILL.md) |
| **`performance`** | Optimize web performance for faster loading and better user experience. Use when asked to "speed up my site", "optimize performance", "reduce load time", "fi... | [`SKILL.md`](development/performance/SKILL.md) |
| **`perl-testing`** | Perl testing patterns using Test2::V0, Test::More, prove runner, mocking, coverage with Devel::Cover, and TDD methodology. | [`SKILL.md`](development/perl-testing/SKILL.md) |
| **`plankton-code-quality`** | Write-time code quality enforcement using Plankton — auto-formatting, linting, and Claude-powered fixes on every file edit via hooks. | [`SKILL.md`](development/plankton-code-quality/SKILL.md) |
| **`python-testing`** | Python testing strategies using pytest, TDD methodology, fixtures, mocking, parametrization, and coverage requirements. | [`SKILL.md`](development/python-testing/SKILL.md) |
| **`pytorch-patterns`** | PyTorch deep learning patterns and best practices for building robust, efficient, and reproducible training pipelines, model architectures, and data loading. | [`SKILL.md`](development/pytorch-patterns/SKILL.md) |
| **`react-native-patterns`** | React Native and Expo app patterns — Expo Router navigation, state separation (server/client/route/form), TanStack Query data fetching with Zod, performant l... | [`SKILL.md`](development/react-native-patterns/SKILL.md) |
| **`react-patterns`** | React 18/19 patterns including hooks discipline, server/client component boundaries, Suspense + error boundaries, form actions, data fetching, state manageme... | [`SKILL.md`](development/react-patterns/SKILL.md) |
| **`react-performance`** | React and Next.js performance optimization patterns adapted from Vercel Engineering's React Best Practices (https://github.com/vercel-labs/agent-skills). Org... | [`SKILL.md`](development/react-performance/SKILL.md) |
| **`react-testing`** | React component testing with React Testing Library, Vitest/Jest, MSW for network mocking, accessibility assertions with axe, and the decision boundary betwee... | [`SKILL.md`](development/react-testing/SKILL.md) |
| **`recsys-pipeline-architect`** | Design composable recommendation, ranking, and feed pipelines using the six-stage Source→Hydrator→Filter→Scorer→Selector→SideEffect framework popularized by ... | [`SKILL.md`](development/recsys-pipeline-architect/SKILL.md) |
| **`refactor`** | Surgical code refactoring to improve maintainability without changing behavior. Covers extracting functions, renaming variables, breaking down god functions,... | [`SKILL.md`](development/refactor/SKILL.md) |
| **`repo-scan`** | Cross-stack source code asset audit — classifies every file, detects embedded third-party libraries, and delivers actionable four-level verdicts per module w... | [`SKILL.md`](development/repo-scan/SKILL.md) |
| **`rust-testing`** | Rust testing patterns including unit tests, integration tests, async testing, property-based testing, mocking, and coverage. Follows TDD methodology. | [`SKILL.md`](development/rust-testing/SKILL.md) |
| **`swift-actor-persistence`** | Thread-safe data persistence in Swift using actors — in-memory cache with file-backed storage, eliminating data races by design. | [`SKILL.md`](development/swift-actor-persistence/SKILL.md) |
| **`swift-concurrency-6-2`** | Swift 6.2 Approachable Concurrency — single-threaded by default, @concurrent for explicit background offloading, isolated conformances for main actor types. | [`SKILL.md`](development/swift-concurrency-6-2/SKILL.md) |
| **`swift-protocol-di-testing`** | Protocol-based dependency injection for testable Swift code — mock file system, network, and external APIs using focused protocols and Swift Testing. | [`SKILL.md`](development/swift-protocol-di-testing/SKILL.md) |
| **`swiftui-patterns`** | SwiftUI architecture patterns, state management with @Observable, view composition, navigation, performance optimization, and modern iOS/macOS UI best practi... | [`SKILL.md`](development/swiftui-patterns/SKILL.md) |
| **`tdd`** | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. | [`SKILL.md`](development/tdd/SKILL.md) |
| **`tdd-workflow`** | Use this skill when writing new features, fixing bugs, or refactoring code. Enforces test-driven development with 80%+ coverage including unit, integration, ... | [`SKILL.md`](development/tdd-workflow/SKILL.md) |
| **`vercel-composition-patterns`** | React composition patterns that scale. Use when refactoring components with | [`SKILL.md`](development/vercel-composition-patterns/SKILL.md) |
| **`vercel-react-best-practices`** | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.j... | [`SKILL.md`](development/vercel-react-best-practices/SKILL.md) |
| **`vercel-react-native-skills`** | React Native and Expo best practices for building performant mobile apps. Use | [`SKILL.md`](development/vercel-react-native-skills/SKILL.md) |
| **`vite-patterns`** | Vite build tool patterns including config, plugins, HMR, env variables, proxy setup, SSR, library mode, dependency pre-bundling, and build optimization. Acti... | [`SKILL.md`](development/vite-patterns/SKILL.md) |
| **`vue-patterns`** | Vue.js 3 Composition API patterns, component architecture, reactivity best practices, Pinia state management, Vue Router navigation, and Nuxt SSR patterns. A... | [`SKILL.md`](development/vue-patterns/SKILL.md) |
| **`web-artifacts-builder`** | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use ... | [`SKILL.md`](development/web-artifacts-builder/SKILL.md) |
| **`webapp-testing`** | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing... | [`SKILL.md`](development/webapp-testing/SKILL.md) |
| **`windows-desktop-e2e`** | E2E testing for Windows native desktop apps (WPF, WinForms, Win32/MFC, Qt) using pywinauto and Windows UI Automation. | [`SKILL.md`](development/windows-desktop-e2e/SKILL.md) |
| **`write-swift`** | How to write modern Swift well — modeling with value types, Swift 6 data-race safety and approachable concurrency (@concurrent, main-actor-by-default, actors... | [`SKILL.md`](development/write-swift/SKILL.md) |

---

<a id="devops-cloud"></a>
### ☁️ Cloud & DevOps (39 skills)

**Caminho no repositório:** [`devops-cloud/`](devops-cloud/)

Infraestrutura como código, nuvem (AWS, Azure, Cloudflare, Netlify), redes locais/homelab, Docker, Kubernetes, checklists pré-deploy e automação.

| Skill | Descrição | Link |
|---|---|:---:|
| **`aws-billing-and-cost-management`** |  | [`SKILL.md`](devops-cloud/aws-billing-and-cost-management/SKILL.md) |
| **`aws-compute`** | Provisions, scales, and operates Amazon EC2 virtual-machine workloads: instance-type selection (Graviton/Arm64, burstable T credits, GPU, instance store vs E... | [`SKILL.md`](devops-cloud/aws-compute/SKILL.md) |
| **`aws-networking`** | Routes AWS networking requests to the correct service skill for implementation. Covers Route 53 (DNS, health checks, routing policies, Resolver, DNS Firewall... | [`SKILL.md`](devops-cloud/aws-networking/SKILL.md) |
| **`aws-observability`** |  | [`SKILL.md`](devops-cloud/aws-observability/SKILL.md) |
| **`aws-sdk-python-usage`** |  | [`SKILL.md`](devops-cloud/aws-sdk-python-usage/SKILL.md) |
| **`azure-cloud-migrate`** | Assess and migrate cross-cloud workloads to Azure with reports and code conversion. Supports Lambda→Functions, Beanstalk/Heroku/App Engine→App Service, Farga... | [`SKILL.md`](devops-cloud/azure-cloud-migrate/SKILL.md) |
| **`azure-deploy`** | Execute Azure deployments for ALREADY-PREPARED applications that have existing .azure/deployment-plan.md and infrastructure files. DO NOT use this skill when... | [`SKILL.md`](devops-cloud/azure-deploy/SKILL.md) |
| **`azure-diagnostics`** | Debug Azure production issues on Azure using AppLens, Azure Monitor, resource health, and safe triage. WHEN: debug production issues, troubleshoot app servic... | [`SKILL.md`](devops-cloud/azure-diagnostics/SKILL.md) |
| **`azure-prepare`** | Prepare azd-based Azure projects for deployment: generates azure.yaml, infrastructure (Bicep/Terraform), and Dockerfiles for the Azure Developer CLI (azd) wo... | [`SKILL.md`](devops-cloud/azure-prepare/SKILL.md) |
| **`azure-storage`** | Azure Storage Services including Blob Storage, File Shares, Queue Storage, Table Storage, and Data Lake. Answers questions about storage access tiers (hot, c... | [`SKILL.md`](devops-cloud/azure-storage/SKILL.md) |
| **`azure-validate`** | Pre-deployment validation for Azure readiness. Run deep checks on configuration, infrastructure (Bicep or Terraform), RBAC role assignments, managed identity... | [`SKILL.md`](devops-cloud/azure-validate/SKILL.md) |
| **`cisco-ios-patterns`** | Cisco IOS and IOS-XE review patterns for show commands, config hierarchy, wildcard masks, ACL placement, interface hygiene, and safe change-window verification. | [`SKILL.md`](devops-cloud/cisco-ios-patterns/SKILL.md) |
| **`cloudflare-deploy`** | Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform services. Use when the user asks to deploy, host, publish, or... | [`SKILL.md`](devops-cloud/cloudflare-deploy/SKILL.md) |
| **`config-gc`** | Garbage collection for your Claude Code configuration. Periodically scans ~/.claude (skills, memory, hooks, permissions, MCP servers, caches) for redundant, ... | [`SKILL.md`](devops-cloud/config-gc/SKILL.md) |
| **`connections-optimizer`** | Reorganize the user's X and LinkedIn network with review-first pruning, add/follow recommendations, and channel-specific warm outreach drafted in the user's ... | [`SKILL.md`](devops-cloud/connections-optimizer/SKILL.md) |
| **`deploy-checklist`** | Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI status an... | [`SKILL.md`](devops-cloud/deploy-checklist/SKILL.md) |
| **`deploy-to-vercel`** | Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this liv... | [`SKILL.md`](devops-cloud/deploy-to-vercel/SKILL.md) |
| **`deployment-patterns`** | Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback strategies, and production readiness checklists for web appli... | [`SKILL.md`](devops-cloud/deployment-patterns/SKILL.md) |
| **`docker-patterns`** | Docker and Docker Compose patterns for local development, container security, networking, volume strategies, and multi-service orchestration. | [`SKILL.md`](devops-cloud/docker-patterns/SKILL.md) |
| **`entra-app-registration`** | Guides Microsoft Entra ID app registration, OAuth 2.0 authentication, and MSAL integration. USE FOR: create app registration, register Azure AD app, configur... | [`SKILL.md`](devops-cloud/entra-app-registration/SKILL.md) |
| **`github-actions-docs`** | Use when users ask how to write, explain, customize, migrate, secure, or troubleshoot GitHub Actions workflows, workflow syntax, triggers, matrices, runners,... | [`SKILL.md`](devops-cloud/github-actions-docs/SKILL.md) |
| **`github-ops`** | GitHub repository operations, automation, and management. Issue triage, PR management, CI/CD operations, release management, and security monitoring using th... | [`SKILL.md`](devops-cloud/github-ops/SKILL.md) |
| **`homelab-network-readiness`** | Readiness checklist for homelab VLAN segmentation, local DNS filtering, and WireGuard-style remote access before changing router, firewall, DHCP, or VPN conf... | [`SKILL.md`](devops-cloud/homelab-network-readiness/SKILL.md) |
| **`homelab-network-setup`** | Practical home and homelab network planning for gateways, switches, access points, IP ranges, DHCP reservations, DNS, cabling, and common beginner mistakes. | [`SKILL.md`](devops-cloud/homelab-network-setup/SKILL.md) |
| **`homelab-pihole-dns`** | Pi-hole installation, blocklist management, DNS-over-HTTPS setup, DHCP integration, local DNS records, and troubleshooting broken DNS resolution on a home ne... | [`SKILL.md`](devops-cloud/homelab-pihole-dns/SKILL.md) |
| **`homelab-vlan-segmentation`** | Segmenting home networks into VLANs for IoT, guest, trusted, and server traffic using UniFi, pfSense/OPNsense, and MikroTik — including switch trunk config, ... | [`SKILL.md`](devops-cloud/homelab-vlan-segmentation/SKILL.md) |
| **`homelab-wireguard-vpn`** | WireGuard VPN server setup, peer configuration, key generation, split tunneling vs full tunnel routing, and remote access to a home network from mobile and l... | [`SKILL.md`](devops-cloud/homelab-wireguard-vpn/SKILL.md) |
| **`kubernetes-patterns`** | Kubernetes workload patterns, resource management, RBAC, probes, autoscaling, ConfigMap/Secret handling, and kubectl debugging for production-grade deployments. | [`SKILL.md`](devops-cloud/kubernetes-patterns/SKILL.md) |
| **`launching-ec2-instance-with-best-practices`** | Launches an EC2 instance with secure, cost-efficient defaults including AMI selection, burstable instance sizing, least-privilege IAM roles, hardened securit... | [`SKILL.md`](devops-cloud/launching-ec2-instance-with-best-practices/SKILL.md) |
| **`microsoft-foundry`** | Deploy, evaluate, fine-tune, and manage Foundry agents end-to-end with azd: hosted agent scaffold/run/deploy, prompt agent create, batch eval, continuous eva... | [`SKILL.md`](devops-cloud/microsoft-foundry/SKILL.md) |
| **`netlify-deploy`** | Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, includ... | [`SKILL.md`](devops-cloud/netlify-deploy/SKILL.md) |
| **`netmiko-ssh-automation`** | Safe Python Netmiko patterns for read-only collection, bounded batch SSH, TextFSM parsing, guarded config changes, timeouts, and network automation error han... | [`SKILL.md`](devops-cloud/netmiko-ssh-automation/SKILL.md) |
| **`network-bgp-diagnostics`** | Diagnostics-only BGP troubleshooting patterns for neighbor state, route exchange, prefix policy, AS path inspection, and safe evidence collection. | [`SKILL.md`](devops-cloud/network-bgp-diagnostics/SKILL.md) |
| **`network-config-validation`** | Pre-deployment checks for router and switch configuration, including dangerous commands, duplicate addresses, subnet overlaps, stale references, management-p... | [`SKILL.md`](devops-cloud/network-config-validation/SKILL.md) |
| **`network-interface-health`** | Diagnose interface errors, drops, CRCs, duplex mismatches, flapping, speed negotiation issues, and counter trends on routers, switches, and Linux hosts. | [`SKILL.md`](devops-cloud/network-interface-health/SKILL.md) |
| **`production-audit`** | Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks, and "what breaks in prod?" questions without sending repo ... | [`SKILL.md`](devops-cloud/production-audit/SKILL.md) |
| **`sentry-cli`** | Guide for using the Sentry CLI to interact with Sentry from the command line. Use when the user asks about viewing issues, events, projects, organizations, m... | [`SKILL.md`](devops-cloud/sentry-cli/SKILL.md) |
| **`uncloud`** | Use when managing an Uncloud cluster — deploying services, configuring Caddy ingress, adding static proxy routes for non-cluster devices, publishing ports, s... | [`SKILL.md`](devops-cloud/uncloud/SKILL.md) |
| **`use-railway`** |  | [`SKILL.md`](devops-cloud/use-railway/SKILL.md) |

---

<a id="backend-database"></a>
### 🗄️ Backend & Bancos de Dados (61 skills)

**Caminho no repositório:** [`backend-database/`](backend-database/)

Bancos serverless, SQL, NoSQL (MongoDB, Neon Postgres, Supabase, ClickHouse, MySQL, Redis), frameworks backend modernos, ORMs e otimização de queries.

| Skill | Descrição | Link |
|---|---|:---:|
| **`api-connector-builder`** | Build a new API connector or provider by matching the target repo's existing integration pattern exactly. Use when adding one more integration without invent... | [`SKILL.md`](backend-database/api-connector-builder/SKILL.md) |
| **`api-design`** | REST API design patterns including resource naming, status codes, pagination, filtering, error responses, versioning, and rate limiting for production APIs. | [`SKILL.md`](backend-database/api-design/SKILL.md) |
| **`architecture`** | Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka vs SQS), documenting a design decision with tra... | [`SKILL.md`](backend-database/architecture/SKILL.md) |
| **`architecture-decision-records`** | Capture architectural decisions made during Claude Code sessions as structured ADRs. Auto-detects decision moments, records context, alternatives considered,... | [`SKILL.md`](backend-database/architecture-decision-records/SKILL.md) |
| **`backend-patterns`** | Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes. | [`SKILL.md`](backend-database/backend-patterns/SKILL.md) |
| **`better-auth-best-practices`** | Configure Better Auth server and client, set up database adapters, manage sessions, add plugins, and handle environment variables. Use when users mention Bet... | [`SKILL.md`](backend-database/better-auth-best-practices/SKILL.md) |
| **`clickhouse-io`** | ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads. | [`SKILL.md`](backend-database/clickhouse-io/SKILL.md) |
| **`content-hash-cache-pattern`** | Cache expensive file processing results using SHA-256 content hashes — path-independent, auto-invalidating, with service layer separation. | [`SKILL.md`](backend-database/content-hash-cache-pattern/SKILL.md) |
| **`create-auth-skill`** | Scaffold and implement authentication in TypeScript/JavaScript apps using Better Auth. Detect frameworks, configure database adapters, set up route handlers,... | [`SKILL.md`](backend-database/create-auth-skill/SKILL.md) |
| **`database-migrations`** | Database migration best practices for schema changes, data migrations, rollbacks, and zero-downtime deployments across PostgreSQL, MySQL, and common ORMs (Pr... | [`SKILL.md`](backend-database/database-migrations/SKILL.md) |
| **`defi-amm-security`** | Security checklist for Solidity AMM contracts, liquidity pools, and swap flows. Covers reentrancy, CEI ordering, donation or inflation attacks, oracle manipu... | [`SKILL.md`](backend-database/defi-amm-security/SKILL.md) |
| **`django-celery`** | Django + Celery async task patterns — configuration, task design, beat scheduling, retries, canvas workflows, monitoring, and testing. Use when adding backgr... | [`SKILL.md`](backend-database/django-celery/SKILL.md) |
| **`django-patterns`** | Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals, middleware, and production-grade Django apps. | [`SKILL.md`](backend-database/django-patterns/SKILL.md) |
| **`django-security`** | Django security best practices, authentication, authorization, CSRF protection, SQL injection prevention, XSS prevention, and secure deployment configurations. | [`SKILL.md`](backend-database/django-security/SKILL.md) |
| **`django-tdd`** | Django testing strategies with pytest-django, TDD methodology, factory_boy, mocking, coverage, and testing Django REST Framework APIs. | [`SKILL.md`](backend-database/django-tdd/SKILL.md) |
| **`django-verification`** | Verification loop for Django projects: migrations, linting, tests with coverage, security scans, and deployment readiness checks before release or PR. | [`SKILL.md`](backend-database/django-verification/SKILL.md) |
| **`email-and-password-best-practices`** | Configure email verification, implement password reset flows, set password policies, and customise hashing algorithms for Better Auth email/password authenti... | [`SKILL.md`](backend-database/email-and-password-best-practices/SKILL.md) |
| **`evm-token-decimals`** | Prevent silent decimal mismatch bugs across EVM chains. Covers runtime decimal lookup, chain-aware caching, bridged-token precision drift, and safe normaliza... | [`SKILL.md`](backend-database/evm-token-decimals/SKILL.md) |
| **`fastapi-patterns`** | FastAPI best practices covering project structure, Pydantic v2 schemas, dependency injection, async handlers, authentication, authorization, transactional se... | [`SKILL.md`](backend-database/fastapi-patterns/SKILL.md) |
| **`golang-patterns`** | Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go applications. | [`SKILL.md`](backend-database/golang-patterns/SKILL.md) |
| **`hexagonal-architecture`** | Design, implement, and refactor Ports & Adapters systems with clear domain boundaries, dependency inversion, and testable use-case orchestration across TypeS... | [`SKILL.md`](backend-database/hexagonal-architecture/SKILL.md) |
| **`improve-codebase-architecture`** | Find deepening opportunities in a codebase, informed by the domain language in CONTEXT.md and the decisions in docs/adr/. Use when the user wants to improve ... | [`SKILL.md`](backend-database/improve-codebase-architecture/SKILL.md) |
| **`jpa-patterns`** | JPA/Hibernate patterns for entity design, relationships, query optimization, transactions, auditing, indexing, pagination, and pooling in Spring Boot. | [`SKILL.md`](backend-database/jpa-patterns/SKILL.md) |
| **`kotlin-exposed-patterns`** | JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling, Flyway migrations, and repository pattern. | [`SKILL.md`](backend-database/kotlin-exposed-patterns/SKILL.md) |
| **`kotlin-ktor-patterns`** | Ktor server patterns including routing DSL, plugins, authentication, Koin DI, kotlinx.serialization, WebSockets, and testApplication testing. | [`SKILL.md`](backend-database/kotlin-ktor-patterns/SKILL.md) |
| **`laravel-patterns`** | Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events, caching, and API resources for production apps. | [`SKILL.md`](backend-database/laravel-patterns/SKILL.md) |
| **`laravel-plugin-discovery`** | Discover and evaluate Laravel packages via LaraPlugins.io MCP. Use when the user wants to find plugins, check package health, or assess Laravel/PHP compatibi... | [`SKILL.md`](backend-database/laravel-plugin-discovery/SKILL.md) |
| **`laravel-security`** | Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API security, and secure deployment configurations. | [`SKILL.md`](backend-database/laravel-security/SKILL.md) |
| **`laravel-tdd`** | Laravel testing strategies with PHPUnit, Pest, model factories, HTTP tests, Sanctum authentication testing, mocking, and coverage. | [`SKILL.md`](backend-database/laravel-tdd/SKILL.md) |
| **`laravel-verification`** | Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security scans, and deployment readiness. | [`SKILL.md`](backend-database/laravel-verification/SKILL.md) |
| **`latency-critical-systems`** | Use for latency-sensitive systems such as realtime dashboards, market data, streaming agents, execution gateways, queues, caches, or HFT-like infrastructure ... | [`SKILL.md`](backend-database/latency-critical-systems/SKILL.md) |
| **`mongodb-atlas-stream-processing`** | Manages MongoDB Atlas Stream Processing (ASP) workflows. Handles workspace provisioning, data source/sink connections, processor lifecycle operations, debugg... | [`SKILL.md`](backend-database/mongodb-atlas-stream-processing/SKILL.md) |
| **`mongodb-connection`** | Optimize MongoDB client connection configuration (pools, timeouts, patterns) for any supported driver language. Use this skill when working/updating/reviewin... | [`SKILL.md`](backend-database/mongodb-connection/SKILL.md) |
| **`mongodb-mcp-setup`** | Guide users through configuring key MongoDB MCP server options. Use this skill when a user has the MongoDB MCP server installed but hasn't configured the req... | [`SKILL.md`](backend-database/mongodb-mcp-setup/SKILL.md) |
| **`mongodb-natural-language-querying`** | Generate read-only MongoDB queries (find) or aggregation pipelines using natural language, with collection schema context and sample documents. Use this skil... | [`SKILL.md`](backend-database/mongodb-natural-language-querying/SKILL.md) |
| **`mongodb-query-optimizer`** |  | [`SKILL.md`](backend-database/mongodb-query-optimizer/SKILL.md) |
| **`mongodb-schema-design`** | MongoDB schema design patterns and anti-patterns. Use when designing data models, reviewing schemas, migrating from SQL, or troubleshooting performance issue... | [`SKILL.md`](backend-database/mongodb-schema-design/SKILL.md) |
| **`mongodb-search-and-ai`** |  | [`SKILL.md`](backend-database/mongodb-search-and-ai/SKILL.md) |
| **`mysql-patterns`** | MySQL and MariaDB schema, query, indexing, transaction, replication, and connection-pool patterns for production backends. | [`SKILL.md`](backend-database/mysql-patterns/SKILL.md) |
| **`neon-postgres`** |  | [`SKILL.md`](backend-database/neon-postgres/SKILL.md) |
| **`nestjs-patterns`** | NestJS architecture patterns for modules, controllers, providers, DTO validation, guards, interceptors, config, and production-grade TypeScript backends. | [`SKILL.md`](backend-database/nestjs-patterns/SKILL.md) |
| **`nodejs-keccak256`** | Prevent Ethereum hashing bugs in JavaScript and TypeScript. Node's sha3-256 is NIST SHA3, not Ethereum Keccak-256, and silently breaks selectors, signatures,... | [`SKILL.md`](backend-database/nodejs-keccak256/SKILL.md) |
| **`perl-patterns`** | Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications. | [`SKILL.md`](backend-database/perl-patterns/SKILL.md) |
| **`perl-security`** | Comprehensive Perl security covering taint mode, input validation, safe process execution, DBI parameterized queries, web security (XSS/SQLi/CSRF), and perlc... | [`SKILL.md`](backend-database/perl-security/SKILL.md) |
| **`postgres-patterns`** | PostgreSQL database patterns for query optimization, schema design, indexing, and security. Based on Supabase best practices. | [`SKILL.md`](backend-database/postgres-patterns/SKILL.md) |
| **`postgresql-optimization`** | PostgreSQL-specific development assistant focusing on unique PostgreSQL features, advanced data types, and PostgreSQL-exclusive capabilities. Covers JSONB op... | [`SKILL.md`](backend-database/postgresql-optimization/SKILL.md) |
| **`prisma-patterns`** | Prisma ORM patterns for TypeScript backends — schema design, query optimization, transactions, pagination, and critical traps like updateMany returning count... | [`SKILL.md`](backend-database/prisma-patterns/SKILL.md) |
| **`python-patterns`** | Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintainable Python applications. | [`SKILL.md`](backend-database/python-patterns/SKILL.md) |
| **`quarkus-patterns`** | Quarkus 3.x LTS architecture patterns with Camel for messaging, RESTful API design, CDI services, data access with Panache, and async processing. Use for Jav... | [`SKILL.md`](backend-database/quarkus-patterns/SKILL.md) |
| **`quarkus-security`** | Quarkus Security best practices for authentication, authorization, JWT/OIDC, RBAC, input validation, CSRF, secrets management, and dependency security. | [`SKILL.md`](backend-database/quarkus-security/SKILL.md) |
| **`quarkus-tdd`** | Test-driven development for Quarkus 3.x LTS using JUnit 5, Mockito, REST Assured, Camel testing, and JaCoCo. Use when adding features, fixing bugs, or refact... | [`SKILL.md`](backend-database/quarkus-tdd/SKILL.md) |
| **`quarkus-verification`** | Verification loop for Quarkus projects: build, static analysis, tests with coverage, security scans, native compilation, and diff review before release or PR. | [`SKILL.md`](backend-database/quarkus-verification/SKILL.md) |
| **`redis-patterns`** | Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub, and connection management for production applications. | [`SKILL.md`](backend-database/redis-patterns/SKILL.md) |
| **`rust-patterns`** | Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for building safe, performant applications. | [`SKILL.md`](backend-database/rust-patterns/SKILL.md) |
| **`springboot-patterns`** | Spring Boot architecture patterns, REST API design, layered services, data access, caching, async processing, and logging. Use for Java Spring Boot backend w... | [`SKILL.md`](backend-database/springboot-patterns/SKILL.md) |
| **`springboot-security`** | Spring Security best practices for authn/authz, validation, CSRF, secrets, headers, rate limiting, and dependency security in Java Spring Boot services. | [`SKILL.md`](backend-database/springboot-security/SKILL.md) |
| **`springboot-tdd`** | Test-driven development for Spring Boot using JUnit 5, Mockito, MockMvc, Testcontainers, and JaCoCo. Use when adding features, fixing bugs, or refactoring. | [`SKILL.md`](backend-database/springboot-tdd/SKILL.md) |
| **`springboot-verification`** | Verification loop for Spring Boot projects: build, static analysis, tests with coverage, security scans, and diff review before release or PR. | [`SKILL.md`](backend-database/springboot-verification/SKILL.md) |
| **`supabase`** | Use when doing ANY task involving Supabase. Triggers: Supabase products (Database, Auth, Edge Functions, Realtime, Storage, Vectors, Cron, Queues); client li... | [`SKILL.md`](backend-database/supabase/SKILL.md) |
| **`supabase-postgres-best-practices`** | Postgres performance optimization and best practices from Supabase. Use this skill when writing, reviewing, or optimizing Postgres queries, schema designs, o... | [`SKILL.md`](backend-database/supabase-postgres-best-practices/SKILL.md) |
| **`tinystruct-patterns`** | Expert guidance for developing with the tinystruct Java framework. Use when working on the tinystruct codebase or any project built on tinystruct — including... | [`SKILL.md`](backend-database/tinystruct-patterns/SKILL.md) |

---

<a id="ai-agents"></a>
### 🤖 Agentes de IA & Metaprogramação (94 skills)

**Caminho no repositório:** [`ai-agents/`](ai-agents/)

Criação e engenharia de subagentes autônomos, servidores MCP (Model Context Protocol), harnesses, loops contínuos de execução, hooks de ciclo de vida e novas skills.

| Skill | Descrição | Link |
|---|---|:---:|
| **`agent-architecture-audit`** | Full-stack diagnostic for agent and LLM applications. Audits the 12-layer agent stack for wrapper regression, memory pollution, tool discipline failures, hid... | [`SKILL.md`](ai-agents/agent-architecture-audit/SKILL.md) |
| **`agent-development`** | This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent... | [`SKILL.md`](ai-agents/agent-development/SKILL.md) |
| **`agent-eval`** | Head-to-head comparison of coding agents (Claude Code, Aider, Codex, etc.) on custom tasks with pass rate, cost, time, and consistency metrics | [`SKILL.md`](ai-agents/agent-eval/SKILL.md) |
| **`agent-harness-construction`** | Design and optimize AI agent action spaces, tool definitions, and observation formatting for higher completion rates. | [`SKILL.md`](ai-agents/agent-harness-construction/SKILL.md) |
| **`agent-introspection-debugging`** | Structured self-debugging workflow for AI agent failures using capture, diagnosis, contained recovery, and introspection reports. | [`SKILL.md`](ai-agents/agent-introspection-debugging/SKILL.md) |
| **`agent-payment-x402`** | Add x402 payment execution to AI agents with per-task budgets, spending controls, and non-custodial wallets. Supports Base through agentwallet-sdk and X Laye... | [`SKILL.md`](ai-agents/agent-payment-x402/SKILL.md) |
| **`agent-self-evaluation`** | Use after completing any non-trivial task. The agent self-rates its output on 5 axes — accuracy, completeness, clarity, actionability, conciseness — with con... | [`SKILL.md`](ai-agents/agent-self-evaluation/SKILL.md) |
| **`agent-sort`** | Build an evidence-backed ECC install plan for a specific repo by sorting skills, commands, rules, hooks, and extras into DAILY vs LIBRARY buckets using paral... | [`SKILL.md`](ai-agents/agent-sort/SKILL.md) |
| **`agentic-engineering`** | Operate as an agentic engineer using eval-first execution, decomposition, and cost-aware model routing. | [`SKILL.md`](ai-agents/agentic-engineering/SKILL.md) |
| **`agentic-os`** | Build persistent multi-agent operating systems on Claude Code. Covers kernel architecture, specialist agents, slash commands, file-based memory, scheduled au... | [`SKILL.md`](ai-agents/agentic-os/SKILL.md) |
| **`ai-first-engineering`** | Engineering operating model for teams where AI agents generate a large share of implementation output. | [`SKILL.md`](ai-agents/ai-first-engineering/SKILL.md) |
| **`ai-regression-testing`** | Regression testing strategies for AI-assisted development. Sandbox-mode API testing without database dependencies, automated bug-check workflows, and pattern... | [`SKILL.md`](ai-agents/ai-regression-testing/SKILL.md) |
| **`automation-audit-ops`** | Evidence-first automation inventory and overlap audit workflow for ECC. Use when the user wants to know which jobs, hooks, connectors, MCP servers, or wrappe... | [`SKILL.md`](ai-agents/automation-audit-ops/SKILL.md) |
| **`autonomous-agent-harness`** | Transform Claude Code into a fully autonomous agent system with persistent memory, scheduled operations, computer use, and task queuing. Replaces standalone ... | [`SKILL.md`](ai-agents/autonomous-agent-harness/SKILL.md) |
| **`autonomous-loops`** | Patterns and architectures for autonomous Claude Code loops — from simple sequential pipelines to RFC-driven multi-agent DAG systems. | [`SKILL.md`](ai-agents/autonomous-loops/SKILL.md) |
| **`build-mcp-app`** | This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "... | [`SKILL.md`](ai-agents/build-mcp-app/SKILL.md) |
| **`build-mcp-server`** | This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to... | [`SKILL.md`](ai-agents/build-mcp-server/SKILL.md) |
| **`canary-watch`** | Use this skill to monitor and verify a deployed URL after releases — checks HTTP endpoints, SSE streams, static assets, console errors, and performance regre... | [`SKILL.md`](ai-agents/canary-watch/SKILL.md) |
| **`ck`** | Persistent per-project memory for Claude Code. Auto-loads project context on session start, tracks sessions with git activity, and writes to native memory. C... | [`SKILL.md`](ai-agents/ck/SKILL.md) |
| **`claude-automation-recommender`** | Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations,... | [`SKILL.md`](ai-agents/claude-automation-recommender/SKILL.md) |
| **`claude-devfleet`** | Orchestrate multi-agent coding tasks via Claude DevFleet — plan projects, dispatch parallel agents in isolated worktrees, monitor progress, and read structur... | [`SKILL.md`](ai-agents/claude-devfleet/SKILL.md) |
| **`claude-md-improver`** | Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files... | [`SKILL.md`](ai-agents/claude-md-improver/SKILL.md) |
| **`claude-opus-4-5-migration`** | Migrate prompts and code from Claude Sonnet 4.0, Sonnet 4.5, or Opus 4.1 to Opus 4.5. Use when the user wants to update their codebase, prompts, or API calls... | [`SKILL.md`](ai-agents/claude-opus-4-5-migration/SKILL.md) |
| **`codehealth-mcp`** | Real-time structural Code Health via CodeScene MCP — review before edits, verify score deltas after changes, gate commits and PRs. Use when reviewing code qu... | [`SKILL.md`](ai-agents/codehealth-mcp/SKILL.md) |
| **`command-development`** | This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command... | [`SKILL.md`](ai-agents/command-development/SKILL.md) |
| **`configure-ecc`** | Interactive installer for Everything Claude Code — guides users through selecting and installing skills and rules to user-level or project-level directories,... | [`SKILL.md`](ai-agents/configure-ecc/SKILL.md) |
| **`context-budget`** | Audits Claude Code context window consumption across agents, skills, MCP servers, and rules. Identifies bloat, redundant components, and produces prioritized... | [`SKILL.md`](ai-agents/context-budget/SKILL.md) |
| **`context7-mcp`** | This skill should be used when the user asks about libraries, frameworks, API references, or needs code examples. Activates for setup questions, code generat... | [`SKILL.md`](ai-agents/context7-mcp/SKILL.md) |
| **`continuous-agent-loop`** | Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls. | [`SKILL.md`](ai-agents/continuous-agent-loop/SKILL.md) |
| **`continuous-learning`** | [DEPRECATED - use continuous-learning-v2] Legacy v1 stop-hook skill extractor. v2 is a strict superset with instinct-based, project-scoped, hook-reliable lea... | [`SKILL.md`](ai-agents/continuous-learning/SKILL.md) |
| **`continuous-learning-v2`** | Instinct-based learning system that observes sessions via hooks, creates atomic instincts with confidence scoring, and evolves them into skills/commands/agen... | [`SKILL.md`](ai-agents/continuous-learning-v2/SKILL.md) |
| **`cost-aware-llm-pipeline`** | Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic, and prompt caching. | [`SKILL.md`](ai-agents/cost-aware-llm-pipeline/SKILL.md) |
| **`cost-tracking`** | Track and report Claude Code token usage, spending, and budgets from the local ECC cost-tracker metrics log. Use when the user asks about costs, spending, us... | [`SKILL.md`](ai-agents/cost-tracking/SKILL.md) |
| **`council`** | Convene a four-voice council for ambiguous decisions, tradeoffs, and go/no-go calls. Use when multiple valid paths exist and you need structured disagreement... | [`SKILL.md`](ai-agents/council/SKILL.md) |
| **`delivery-gate`** | Stop hook that blocks Claude from finishing until quality checks pass. Detects rationalization patterns (surface text heuristics), stale learning logs (files... | [`SKILL.md`](ai-agents/delivery-gate/SKILL.md) |
| **`design-mcp-workflow`** | Design a Zoom MCP workflow for Claude. Use when deciding whether Zoom MCP fits a task, when planning tool-based AI workflows, or when separating MCP responsi... | [`SKILL.md`](ai-agents/design-mcp-workflow/SKILL.md) |
| **`dynamic-workflow-mode`** | Design task-local harnesses, eval gates, and reusable skill extraction for Claude dynamic workflow mode and other adaptive agent harnesses. | [`SKILL.md`](ai-agents/dynamic-workflow-mode/SKILL.md) |
| **`ecc-guide`** | Guide users through ECC's current agents, skills, commands, hooks, rules, install profiles, and project onboarding by reading the live repository surface bef... | [`SKILL.md`](ai-agents/ecc-guide/SKILL.md) |
| **`ecc-recipes`** | Map a described workflow to the right ECC command-GROUP with run-order and stop condition, and browse all command-group recipe families. Adds a family-groupi... | [`SKILL.md`](ai-agents/ecc-recipes/SKILL.md) |
| **`ecc-tools-cost-audit`** | Evidence-first ECC Tools burn and billing audit workflow. Use when investigating runaway PR creation, quota bypass, premium-model leakage, duplicate jobs, or... | [`SKILL.md`](ai-agents/ecc-tools-cost-audit/SKILL.md) |
| **`enterprise-agent-ops`** | Operate long-lived agent workloads with observability, security boundaries, and lifecycle management. | [`SKILL.md`](ai-agents/enterprise-agent-ops/SKILL.md) |
| **`eval-harness`** | Formal evaluation framework for Claude Code sessions implementing eval-driven development (EDD) principles | [`SKILL.md`](ai-agents/eval-harness/SKILL.md) |
| **`everything-claude-code`** | Development conventions and patterns for everything-claude-code. JavaScript project with conventional commits. | [`SKILL.md`](ai-agents/everything-claude-code/SKILL.md) |
| **`find-skills`** | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express ... | [`SKILL.md`](ai-agents/find-skills/SKILL.md) |
| **`full-output-enforcement`** | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply to any... | [`SKILL.md`](ai-agents/full-output-enforcement/SKILL.md) |
| **`gan-style-harness`** | GAN-inspired Generator-Evaluator agent harness for building high-quality applications autonomously. Based on Anthropic's March 2026 harness design paper. | [`SKILL.md`](ai-agents/gan-style-harness/SKILL.md) |
| **`gateguard`** | Fact-forcing gate that blocks Edit/Write/Bash (including MultiEdit) and demands concrete investigation (importers, data schemas, user instruction) before all... | [`SKILL.md`](ai-agents/gateguard/SKILL.md) |
| **`growth-log`** | Use after a complex task, failure, or when reviewing what was learned. Teaches how to write growth logs that extract reusable patterns — not diary entries. | [`SKILL.md`](ai-agents/growth-log/SKILL.md) |
| **`handoff`** | Compact the current conversation into a handoff document for another agent to pick up. | [`SKILL.md`](ai-agents/handoff/SKILL.md) |
| **`hermes-imports`** | Convert local Hermes operator workflows into sanitized ECC skills and release-pack artifacts. Use when preparing a Hermes workflow for public ECC reuse witho... | [`SKILL.md`](ai-agents/hermes-imports/SKILL.md) |
| **`hook-development`** | This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks... | [`SKILL.md`](ai-agents/hook-development/SKILL.md) |
| **`hookify-rules`** | This skill should be used when the user asks to create a hookify rule, write a hook rule, configure hookify, add a hookify rule, or needs guidance on hookify... | [`SKILL.md`](ai-agents/hookify-rules/SKILL.md) |
| **`iterative-retrieval`** | Pattern for progressively refining context retrieval to solve the subagent context problem | [`SKILL.md`](ai-agents/iterative-retrieval/SKILL.md) |
| **`ito-data-atlas-agent`** | Design background Data Atlas style agents for Itô basket research, market discovery, parameter drafting, and human-in-the-loop editing. Use for architecture ... | [`SKILL.md`](ai-agents/ito-data-atlas-agent/SKILL.md) |
| **`llm-trading-agent-security`** | Security patterns for autonomous trading agents with wallet or transaction authority. Covers prompt injection, spend limits, pre-send simulation, circuit bre... | [`SKILL.md`](ai-agents/llm-trading-agent-security/SKILL.md) |
| **`mcp-builder`** | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use whe... | [`SKILL.md`](ai-agents/mcp-builder/SKILL.md) |
| **`mcp-integration`** | This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol... | [`SKILL.md`](ai-agents/mcp-integration/SKILL.md) |
| **`mcp-server-patterns`** | Build MCP servers with Node/TypeScript SDK — tools, resources, prompts, Zod validation, stdio vs Streamable HTTP. Use Context7 or official MCP docs for lates... | [`SKILL.md`](ai-agents/mcp-server-patterns/SKILL.md) |
| **`nanoclaw-repl`** | Operate and extend NanoClaw v2, ECC's zero-dependency session-aware REPL built on claude -p. | [`SKILL.md`](ai-agents/nanoclaw-repl/SKILL.md) |
| **`openclaw-persona-forge`** | 为 OpenClaw AI Agent 锻造完整的龙虾灵魂方案。根据用户偏好或随机抽卡， 输出身份定位、灵魂描述(SOUL.md)、角色化底线规则、名字和头像生图提示词。 如当前环境提供已审核的生图 skill，可自动生成统一风格头像图片。 当用户需要创建、设计或定制 OpenClaw 龙虾灵魂时使用。 不适用于... | [`SKILL.md`](ai-agents/openclaw-persona-forge/SKILL.md) |
| **`opensource-pipeline`** | Open-source pipeline: fork, sanitize, and package private projects for safe public release. Chains 3 agents (forker, sanitizer, packager). Triggers: '/openso... | [`SKILL.md`](ai-agents/opensource-pipeline/SKILL.md) |
| **`orch-add-feature`** | Orchestrate building a brand-new feature end to end — research, plan, TDD implementation, review, and gated commit — by delegating each phase to the matching... | [`SKILL.md`](ai-agents/orch-add-feature/SKILL.md) |
| **`orch-build-mvp`** | Orchestrate bootstrapping a working MVP from a design or spec document — ingest the doc, plan thin vertical slices, scaffold the first end-to-end slice, then... | [`SKILL.md`](ai-agents/orch-build-mvp/SKILL.md) |
| **`orch-change-feature`** | Orchestrate altering an existing, working feature to new desired behavior — update its tests to the new spec, change the implementation to match, review, and... | [`SKILL.md`](ai-agents/orch-change-feature/SKILL.md) |
| **`orch-fix-defect`** | Orchestrate fixing a bug — reproduce it as a failing regression test, fix to green, review, and gated commit — by delegating each phase to the matching ECC a... | [`SKILL.md`](ai-agents/orch-fix-defect/SKILL.md) |
| **`orch-pipeline`** | Shared orchestration engine for the orch-* skill family. Defines the gated Research-Plan-TDD-Review-Commit pipeline, the size classifier, the agent map, and ... | [`SKILL.md`](ai-agents/orch-pipeline/SKILL.md) |
| **`orch-refine-code`** | Orchestrate a behavior-preserving refactor — confirm tests are green, restructure without changing behavior, keep tests green, review, and gated commit. Use ... | [`SKILL.md`](ai-agents/orch-refine-code/SKILL.md) |
| **`parallel-execution-optimizer`** | Use when the user wants a task done much faster through parallel work, concurrent agents, batched tool calls, isolated worktrees, or many independent verific... | [`SKILL.md`](ai-agents/parallel-execution-optimizer/SKILL.md) |
| **`plan-canvas`** | Open plans and HTML artifacts in a local browser canvas where the human annotates elements, chats, and approves or requests changes without leaving the page.... | [`SKILL.md`](ai-agents/plan-canvas/SKILL.md) |
| **`plan-orchestrate`** | Read a plan document, decompose it into steps, design a per-step agent chain from the ECC catalogue, and emit ready-to-paste /orchestrate custom prompts. Gen... | [`SKILL.md`](ai-agents/plan-orchestrate/SKILL.md) |
| **`plugin-settings`** | This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin st... | [`SKILL.md`](ai-agents/plugin-settings/SKILL.md) |
| **`plugin-structure`** | This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up ... | [`SKILL.md`](ai-agents/plugin-structure/SKILL.md) |
| **`prompt-optimizer`** |  | [`SKILL.md`](ai-agents/prompt-optimizer/SKILL.md) |
| **`ralphinho-rfc-pipeline`** | RFC-driven multi-agent DAG execution pattern with quality gates, merge queues, and work unit orchestration. | [`SKILL.md`](ai-agents/ralphinho-rfc-pipeline/SKILL.md) |
| **`rules-distill`** | Scan skills to extract cross-cutting principles and distill them into rules — append, revise, or create new rule files | [`SKILL.md`](ai-agents/rules-distill/SKILL.md) |
| **`safety-guard`** | Use this skill to prevent destructive operations when working on production systems or running agents autonomously. | [`SKILL.md`](ai-agents/safety-guard/SKILL.md) |
| **`santa-method`** | Multi-agent adversarial verification with convergence loop. Two independent review agents must both pass before output ships. | [`SKILL.md`](ai-agents/santa-method/SKILL.md) |
| **`session-report`** | Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts. | [`SKILL.md`](ai-agents/session-report/SKILL.md) |
| **`setup-matt-pocock-skills`** | Configure this repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the o... | [`SKILL.md`](ai-agents/setup-matt-pocock-skills/SKILL.md) |
| **`skill-comply`** | Visualize whether skills, rules, and agent definitions are actually followed — auto-generates scenarios at 3 prompt strictness levels, runs agents, classifie... | [`SKILL.md`](ai-agents/skill-comply/SKILL.md) |
| **`skill-creator`** | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize a... | [`SKILL.md`](ai-agents/skill-creator/SKILL.md) |
| **`skill-development`** | This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill... | [`SKILL.md`](ai-agents/skill-development/SKILL.md) |
| **`skill-judge`** | Evaluate Agent Skill design quality against official specifications and best practices. Use when reviewing, auditing, or improving SKILL.md files and skill p... | [`SKILL.md`](ai-agents/skill-judge/SKILL.md) |
| **`skill-scout`** | Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. Use when the user wants to create, build, fork, or find a skil... | [`SKILL.md`](ai-agents/skill-scout/SKILL.md) |
| **`skill-stocktake`** | Use when auditing Claude skills and commands for quality. Supports Quick Scan (changed skills only) and Full Stocktake modes with sequential subagent batch e... | [`SKILL.md`](ai-agents/skill-stocktake/SKILL.md) |
| **`strategic-compact`** | Suggests manual context compaction at logical intervals to preserve context through task phases rather than arbitrary auto-compaction. | [`SKILL.md`](ai-agents/strategic-compact/SKILL.md) |
| **`team-agent-orchestration`** | Run team-based orchestration for agent squads using work items, ownership, agent Kanban, merge gates, and control pane handoffs. | [`SKILL.md`](ai-agents/team-agent-orchestration/SKILL.md) |
| **`team-builder`** | Interactive agent picker for composing and dispatching parallel teams | [`SKILL.md`](ai-agents/team-builder/SKILL.md) |
| **`terminal-ops`** | Evidence-first repo execution workflow for ECC. Use when the user wants a command run, a repo checked, a CI failure debugged, or a narrow fix pushed with exa... | [`SKILL.md`](ai-agents/terminal-ops/SKILL.md) |
| **`token-budget-advisor`** |  | [`SKILL.md`](ai-agents/token-budget-advisor/SKILL.md) |
| **`verification-loop`** | A comprehensive verification system for Claude Code sessions. | [`SKILL.md`](ai-agents/verification-loop/SKILL.md) |
| **`workspace-surface-audit`** | Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the highest-value ECC-native skills, hooks, agents, ... | [`SKILL.md`](ai-agents/workspace-surface-audit/SKILL.md) |
| **`writing-great-skills`** | Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable. | [`SKILL.md`](ai-agents/writing-great-skills/SKILL.md) |
| **`writing-hookify-rules`** | This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on... | [`SKILL.md`](ai-agents/writing-hookify-rules/SKILL.md) |

---

<a id="documents-productivity"></a>
### 📄 Documentos & Produtividade (26 skills)

**Caminho no repositório:** [`documents-productivity/`](documents-productivity/)

Manipulação automatizada de documentos de escritório (Word, Excel, PowerPoint, PDF), pesquisa científica, patentes, Obsidian e especificações técnicas.

| Skill | Descrição | Link |
|---|---|:---:|
| **`article-writing`** | Write articles, guides, blog posts, tutorials, newsletter issues, and other long-form content in a distinctive voice derived from supplied examples or brand ... | [`SKILL.md`](documents-productivity/article-writing/SKILL.md) |
| **`deep-research`** | Multi-source deep research using firecrawl and exa MCPs. Searches the web, synthesizes findings, and delivers cited reports with source attribution. Use when... | [`SKILL.md`](documents-productivity/deep-research/SKILL.md) |
| **`doc-coauthoring`** | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision do... | [`SKILL.md`](documents-productivity/doc-coauthoring/SKILL.md) |
| **`documentation`** | Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README", "write a runbook", "onboarding guide", or when... | [`SKILL.md`](documents-productivity/documentation/SKILL.md) |
| **`docx`** | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word ... | [`SKILL.md`](documents-productivity/docx/SKILL.md) |
| **`grill-me`** | A relentless interview to sharpen a plan or design. | [`SKILL.md`](documents-productivity/grill-me/SKILL.md) |
| **`grill-with-docs`** | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. | [`SKILL.md`](documents-productivity/grill-with-docs/SKILL.md) |
| **`humanizer`** |  | [`SKILL.md`](documents-productivity/humanizer/SKILL.md) |
| **`nutrient-document-processing`** | Process, convert, OCR, extract, redact, sign, and fill documents using the Nutrient DWS API. Works with PDFs, DOCX, XLSX, PPTX, HTML, and images. | [`SKILL.md`](documents-productivity/nutrient-document-processing/SKILL.md) |
| **`obsidian-markdown`** | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax. Use when working with .md files ... | [`SKILL.md`](documents-productivity/obsidian-markdown/SKILL.md) |
| **`obsidian-vault`** | Search, create, and manage notes in the Obsidian vault with wikilinks and index notes. Use when user wants to find, create, or organize notes in Obsidian. | [`SKILL.md`](documents-productivity/obsidian-vault/SKILL.md) |
| **`pdf`** | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multipl... | [`SKILL.md`](documents-productivity/pdf/SKILL.md) |
| **`pptx`** | Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; ... | [`SKILL.md`](documents-productivity/pptx/SKILL.md) |
| **`project-artifact`** | Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success criteria, the wo... | [`SKILL.md`](documents-productivity/project-artifact/SKILL.md) |
| **`proposal-writer`** | Create compelling business proposals that win deals and partnerships | [`SKILL.md`](documents-productivity/proposal-writer/SKILL.md) |
| **`research-ops`** | Evidence-first current-state research workflow for ECC. Use when the user wants fresh facts, comparisons, enrichment, or a recommendation built from current ... | [`SKILL.md`](documents-productivity/research-ops/SKILL.md) |
| **`scientific-db-pubmed-database`** | Direct PubMed and NCBI E-utilities search workflows for biomedical literature, MeSH queries, PMID lookup, citation retrieval, and API-backed literature monit... | [`SKILL.md`](documents-productivity/scientific-db-pubmed-database/SKILL.md) |
| **`scientific-db-uspto-database`** | USPTO patent and trademark data workflow for official record lookup, PatentSearch queries, TSDR checks, assignment data, and reproducible IP research logs. | [`SKILL.md`](documents-productivity/scientific-db-uspto-database/SKILL.md) |
| **`scientific-pkg-gget`** | gget CLI and Python workflow for quick genomic database queries, sequence lookup, BLAST-style searches, enrichment checks, and reproducible bioinformatics ev... | [`SKILL.md`](documents-productivity/scientific-pkg-gget/SKILL.md) |
| **`scientific-thinking-literature-review`** | Systematic literature-review workflow for academic, biomedical, technical, and scientific topics, including search planning, source screening, synthesis, cit... | [`SKILL.md`](documents-productivity/scientific-thinking-literature-review/SKILL.md) |
| **`scientific-thinking-scholar-evaluation`** | Structured scholarly-work evaluation for papers, proposals, literature reviews, methods sections, evidence quality, citation support, and research-writing fe... | [`SKILL.md`](documents-productivity/scientific-thinking-scholar-evaluation/SKILL.md) |
| **`search-first`** | Research-before-coding workflow. Search for existing tools, libraries, and patterns before writing custom code. Invokes the researcher agent. | [`SKILL.md`](documents-productivity/search-first/SKILL.md) |
| **`view-pdf`** | Interactive PDF viewer. Use when the user wants to open, show, or view a PDF and collaborate on it visually — annotate, highlight, stamp, fill form fields, p... | [`SKILL.md`](documents-productivity/view-pdf/SKILL.md) |
| **`visa-doc-translate`** | Translate visa application documents (images) to English and create a bilingual PDF with original and translation | [`SKILL.md`](documents-productivity/visa-doc-translate/SKILL.md) |
| **`write-spec`** | Write a feature spec or PRD from a problem statement or feature idea. Use when turning a vague idea or user request into a structured document, scoping a fea... | [`SKILL.md`](documents-productivity/write-spec/SKILL.md) |
| **`xlsx`** | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing ... | [`SKILL.md`](documents-productivity/xlsx/SKILL.md) |

---

<a id="business-management"></a>
### 📊 Gestão & Negócios (43 skills)

**Caminho no repositório:** [`business-management/`](business-management/)

Análise de métricas e KPIs, governança, conformidade regulatória (SOX, HIPAA), supply chain, logística, CRM, faturamento e briefings executivos.

| Skill | Descrição | Link |
|---|---|:---:|
| **`access`** | Manage Discord channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed,... | [`SKILL.md`](business-management/access/SKILL.md) |
| **`analyze`** | Answer data questions -- from quick lookups to full analyses. Use when looking up a single metric, investigating what's driving a trend or drop, comparing se... | [`SKILL.md`](business-management/analyze/SKILL.md) |
| **`audit-support`** | Support SOX 404 compliance with control testing methodology, sample selection, and documentation standards. Use when generating testing workpapers, selecting... | [`SKILL.md`](business-management/audit-support/SKILL.md) |
| **`brief`** | Generate contextual briefings for legal work — daily summary, topic research, or incident response. Use when starting your day and need a scan of legal-relev... | [`SKILL.md`](business-management/brief/SKILL.md) |
| **`capacity-plan`** | Plan resource capacity — workload analysis and utilization forecasting. Use when heading into quarterly planning, the team feels overallocated and you need t... | [`SKILL.md`](business-management/capacity-plan/SKILL.md) |
| **`carrier-relationship-management`** |  | [`SKILL.md`](business-management/carrier-relationship-management/SKILL.md) |
| **`clinical-trial-protocol-skill`** | Generate clinical trial protocols for medical devices or drugs. This skill should be used when users say "Create a clinical trial protocol", "Generate protoc... | [`SKILL.md`](business-management/clinical-trial-protocol-skill/SKILL.md) |
| **`comp-analysis`** | Analyze compensation — benchmarking, band placement, and equity modeling. Trigger with "what should we pay a [role]", "is this offer competitive", "model thi... | [`SKILL.md`](business-management/comp-analysis/SKILL.md) |
| **`configure`** | Set up the Discord channel — save the bot token and review access policy. Use when the user pastes a Discord bot token, asks to configure Discord, asks "how ... | [`SKILL.md`](business-management/configure/SKILL.md) |
| **`customer-billing-ops`** | Operate customer billing workflows such as subscriptions, refunds, churn triage, billing-portal recovery, and plan analysis using connected billing tools lik... | [`SKILL.md`](business-management/customer-billing-ops/SKILL.md) |
| **`customs-trade-compliance`** |  | [`SKILL.md`](business-management/customs-trade-compliance/SKILL.md) |
| **`daily-briefing`** | Start your day with a prioritized sales briefing. Works standalone when you tell me your meetings and priorities, supercharged when you connect your calendar... | [`SKILL.md`](business-management/daily-briefing/SKILL.md) |
| **`data-context-extractor`** |  | [`SKILL.md`](business-management/data-context-extractor/SKILL.md) |
| **`data-visualization`** | Create effective data visualizations with Python (matplotlib, seaborn, plotly). Use when building charts, choosing the right chart type for a dataset, creati... | [`SKILL.md`](business-management/data-visualization/SKILL.md) |
| **`energy-procurement`** |  | [`SKILL.md`](business-management/energy-procurement/SKILL.md) |
| **`finance-billing-ops`** | Evidence-first revenue, pricing, refunds, team-billing, and billing-model truth workflow for ECC. Use when the user wants a sales snapshot, pricing compariso... | [`SKILL.md`](business-management/finance-billing-ops/SKILL.md) |
| **`healthcare-cdss-patterns`** | Clinical Decision Support System (CDSS) development patterns. Drug interaction checking, dose validation, clinical scoring (NEWS2, qSOFA), alert severity cla... | [`SKILL.md`](business-management/healthcare-cdss-patterns/SKILL.md) |
| **`healthcare-emr-patterns`** | EMR/EHR development patterns for healthcare applications. Clinical safety, encounter workflows, prescription generation, clinical decision support integratio... | [`SKILL.md`](business-management/healthcare-emr-patterns/SKILL.md) |
| **`healthcare-eval-harness`** | Patient safety evaluation harness for healthcare application deployments. Automated test suites for CDSS accuracy, PHI exposure, clinical workflow integrity,... | [`SKILL.md`](business-management/healthcare-eval-harness/SKILL.md) |
| **`healthcare-phi-compliance`** | Protected Health Information (PHI) and Personally Identifiable Information (PII) compliance patterns for healthcare applications. Covers data classification,... | [`SKILL.md`](business-management/healthcare-phi-compliance/SKILL.md) |
| **`hipaa-compliance`** | HIPAA-specific entrypoint for healthcare privacy and security work. Use when a task is explicitly framed around HIPAA, PHI handling, covered entities, BAAs, ... | [`SKILL.md`](business-management/hipaa-compliance/SKILL.md) |
| **`inventory-demand-planning`** |  | [`SKILL.md`](business-management/inventory-demand-planning/SKILL.md) |
| **`investor-materials`** | Create and update pitch decks, one-pagers, investor memos, accelerator applications, financial models, and fundraising materials. Use when the user needs inv... | [`SKILL.md`](business-management/investor-materials/SKILL.md) |
| **`investor-outreach`** | Draft cold emails, warm intro blurbs, follow-ups, update emails, and investor communications for fundraising. Use when the user wants outreach to angels, VCs... | [`SKILL.md`](business-management/investor-outreach/SKILL.md) |
| **`ito-basket-compare`** | Compare Itô prediction-market baskets against a user's knowledge base, portfolio notes, financial context, watchlist, or research thesis. Use for read-only b... | [`SKILL.md`](business-management/ito-basket-compare/SKILL.md) |
| **`ito-market-intelligence`** | Research prediction-market events, venues, underliers, liquidity, and news context for Itô basket workflows. Use for read-only market intelligence, API-gated... | [`SKILL.md`](business-management/ito-market-intelligence/SKILL.md) |
| **`ito-trade-planner`** | Build a non-advisory prediction-market trade planning worksheet for Itô or venue workflows. Use to inspect venues, underliers, constraints, order prerequisit... | [`SKILL.md`](business-management/ito-trade-planner/SKILL.md) |
| **`knowledge-ops`** | Knowledge base management, ingestion, sync, and retrieval across multiple storage layers (local files, MCP memory, vector stores, Git repos). Use when the us... | [`SKILL.md`](business-management/knowledge-ops/SKILL.md) |
| **`lead-intelligence`** | AI-native lead intelligence and outreach pipeline. Replaces Apollo, Clay, and ZoomInfo with agent-powered signal scoring, mutual ranking, warm path discovery... | [`SKILL.md`](business-management/lead-intelligence/SKILL.md) |
| **`logistics-exception-management`** |  | [`SKILL.md`](business-management/logistics-exception-management/SKILL.md) |
| **`market-research`** | Conduct market research, competitive analysis, investor due diligence, and industry intelligence with source attribution and decision-oriented summaries. Use... | [`SKILL.md`](business-management/market-research/SKILL.md) |
| **`performance-review`** | Structure a performance review with self-assessment, manager template, and calibration prep. Use when review season kicks off and you need a self-assessment ... | [`SKILL.md`](business-management/performance-review/SKILL.md) |
| **`pipeline-review`** | Analyze pipeline health — prioritize deals, flag risks, get a weekly action plan. Use when running a weekly pipeline review, deciding which deals to focus on... | [`SKILL.md`](business-management/pipeline-review/SKILL.md) |
| **`prediction-market-oracle-research`** | Research prediction markets as data sources or oracle signals for products, agents, dashboards, and corporate decision intelligence. Use for source-grounded ... | [`SKILL.md`](business-management/prediction-market-oracle-research/SKILL.md) |
| **`prediction-market-risk-review`** | Review prediction-market, basket, oracle, and trading-agent workflows for compliance, safety, data-quality, privacy, and execution risk. Use before any workf... | [`SKILL.md`](business-management/prediction-market-risk-review/SKILL.md) |
| **`product-capability`** | Translate PRD intent, roadmap asks, or product discussions into an implementation-ready capability plan that exposes constraints, invariants, interfaces, and... | [`SKILL.md`](business-management/product-capability/SKILL.md) |
| **`product-lens`** | Use this skill to validate the "why" before building, run product diagnostics, and pressure-test product direction before the request becomes an implementati... | [`SKILL.md`](business-management/product-lens/SKILL.md) |
| **`production-scheduling`** |  | [`SKILL.md`](business-management/production-scheduling/SKILL.md) |
| **`project-flow-ops`** | Operate execution flow across GitHub and Linear by triaging issues and pull requests, linking active work, and keeping GitHub public-facing while Linear rema... | [`SKILL.md`](business-management/project-flow-ops/SKILL.md) |
| **`quality-nonconformance`** |  | [`SKILL.md`](business-management/quality-nonconformance/SKILL.md) |
| **`returns-reverse-logistics`** |  | [`SKILL.md`](business-management/returns-reverse-logistics/SKILL.md) |
| **`triage`** | Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if needed, and write agent-ready briefs. | [`SKILL.md`](business-management/triage/SKILL.md) |
| **`unified-notifications-ops`** | Operate notifications as one ECC-native workflow across GitHub, Linear, desktop alerts, hooks, and connected communication surfaces. Use when the real proble... | [`SKILL.md`](business-management/unified-notifications-ops/SKILL.md) |

---

<a id="utilities"></a>
### 🛠️ Utilitários & Otimização (29 skills)

**Caminho no repositório:** [`utilities/`](utilities/)

Modo ultra-conciso (Caveman) para economia massiva de tokens de contexto, web scraping, auditoria de segurança, playbooks interativos e integrações.

| Skill | Descrição | Link |
|---|---|:---:|
| **`ai-music`** |  | [`SKILL.md`](utilities/ai-music/SKILL.md) |
| **`caveman`** |  | [`SKILL.md`](utilities/caveman/SKILL.md) |
| **`caveman-commit`** |  | [`SKILL.md`](utilities/caveman-commit/SKILL.md) |
| **`caveman-compress`** |  | [`SKILL.md`](utilities/caveman-compress/SKILL.md) |
| **`caveman-help`** |  | [`SKILL.md`](utilities/caveman-help/SKILL.md) |
| **`caveman-review`** |  | [`SKILL.md`](utilities/caveman-review/SKILL.md) |
| **`data-scraper-agent`** | Build a fully automated AI-powered data collection agent for any public source — job boards, prices, news, GitHub, sports, anything. Runs on a schedule, enri... | [`SKILL.md`](utilities/data-scraper-agent/SKILL.md) |
| **`email-ops`** | Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC. Use when the user wants to organize email, draft o... | [`SKILL.md`](utilities/email-ops/SKILL.md) |
| **`exa-search`** | Neural search via Exa MCP for web, code, and company research. Use when the user needs web search, code examples, company intel, people lookup, or AI-powered... | [`SKILL.md`](utilities/exa-search/SKILL.md) |
| **`fal-ai-media`** | Unified media generation via fal.ai MCP — image, video, and audio. Covers text-to-image (Nano Banana), text/image-to-video (Seedance, Kling, Veo 3), text-to-... | [`SKILL.md`](utilities/fal-ai-media/SKILL.md) |
| **`firecrawl`** |  | [`SKILL.md`](utilities/firecrawl/SKILL.md) |
| **`google-workspace-ops`** | Operate across Google Drive, Docs, Sheets, and Slides as one workflow surface for plans, trackers, decks, and shared documents. Use when the user needs to fi... | [`SKILL.md`](utilities/google-workspace-ops/SKILL.md) |
| **`image-edit`** |  | [`SKILL.md`](utilities/image-edit/SKILL.md) |
| **`image-to-video`** |  | [`SKILL.md`](utilities/image-to-video/SKILL.md) |
| **`ios-icon-gen`** | Generate iOS app icons as PNG imagesets for Xcode asset catalogs from SF Symbols (5000+ Apple-native) or Iconify API (275k+ open source icons from 200+ colle... | [`SKILL.md`](utilities/ios-icon-gen/SKILL.md) |
| **`jira-integration`** | Use this skill when retrieving Jira tickets, analyzing requirements, updating ticket status, adding comments, or transitioning issues. Provides Jira API patt... | [`SKILL.md`](utilities/jira-integration/SKILL.md) |
| **`lark-mail`** | 飞书邮箱 — draft, compose, send, reply, forward, read, and search emails; manage drafts, folders, labels, contacts, attachments, and mail rules. Use when user me... | [`SKILL.md`](utilities/lark-mail/SKILL.md) |
| **`lark-wiki`** | 飞书知识库：管理知识空间、空间成员和文档节点。创建和查询知识空间、查看和管理空间成员、管理节点层级结构、在知识库中组织文档和快捷方式。当用户需要在知识库中查找或创建文档、浏览知识空间结构、查看或管理空间成员、移动或复制节点时使用。当用户给出 doubao.com 的 /wiki/ URL/token 时，也应直接... | [`SKILL.md`](utilities/lark-wiki/SKILL.md) |
| **`loop-design-check`** | Design a goal-oriented agent loop, and review it for the ways loops go wrong — spinning and burning tokens, Goodhart-gaming the verifier, or running a wrong ... | [`SKILL.md`](utilities/loop-design-check/SKILL.md) |
| **`mailtrap-email-integration`** | Guides agents through integrating transactional email sending via Mailtrap's Email API, including sandbox testing, domain verification, and API authenticatio... | [`SKILL.md`](utilities/mailtrap-email-integration/SKILL.md) |
| **`messages-ops`** | Evidence-first live messaging workflow for ECC. Use when the user wants to read texts or DMs, recover a recent one-time code, inspect a thread before replyin... | [`SKILL.md`](utilities/messages-ops/SKILL.md) |
| **`nano-banana-2`** |  | [`SKILL.md`](utilities/nano-banana-2/SKILL.md) |
| **`nano-banana-edit`** |  | [`SKILL.md`](utilities/nano-banana-edit/SKILL.md) |
| **`playground`** | Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview,... | [`SKILL.md`](utilities/playground/SKILL.md) |
| **`recursive-decision-ledger`** | Use when the user asks for repeated rollouts, marked decision processes, high-dimensional search, stochastic optimization, local-optima exploration, ensemble... | [`SKILL.md`](utilities/recursive-decision-ledger/SKILL.md) |
| **`regex-vs-llm-structured-text`** | Decision framework for choosing between regex and LLM when parsing structured text — start with regex, add LLM only for low-confidence edge cases. | [`SKILL.md`](utilities/regex-vs-llm-structured-text/SKILL.md) |
| **`security-bounty-hunter`** | Hunt for exploitable, bounty-worthy security issues in repositories. Focuses on remotely reachable vulnerabilities that qualify for real reports instead of n... | [`SKILL.md`](utilities/security-bounty-hunter/SKILL.md) |
| **`security-review`** | Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features. Pro... | [`SKILL.md`](utilities/security-review/SKILL.md) |
| **`security-scan`** | Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and injection risks using AgentShield. Checks CLAUD... | [`SKILL.md`](utilities/security-scan/SKILL.md) |

---

## 🤝 Contribuição e Licença

Para adicionar novas skills a este repositório, basta criar uma pasta com o nome da skill dentro da categoria mais adequada contendo seu respectivo `SKILL.md` formatado com frontmatter YAML.

Repositório mantido por [Henrique1601](https://github.com/Henrique1601).
