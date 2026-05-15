# 🧠 DreamBoard — Your Idea Execution Engine

Welcome to your personal **brain-to-build command center**. This is where **no idea is too crazy** — and where crazy ideas get the research, strategy, and execution plans they need to become real.

## What This Is

DreamBoard is not just an idea notebook. It's a **full AI-powered execution system** that manages your ideas through their entire lifecycle:

```
SPARK → RESEARCH → VALIDATION → PLAN → BUILD → LAUNCH
```

Your AI co-founder (me) handles the heavy lifting: market research, competitor analysis, diagramming, PRDs, MVP planning, experiment design, and more.

---

## How to Use

### 1. Brain-Dump Freely
Just tell me your idea. I'll capture it instantly in `ideas/raw/`.

### 2. Say the Magic Words
I respond to natural voice commands:

| You Say | I Do |
|---------|------|
| **"Research the market"** | Deep market research → `research/market/` |
| **"Who are my competitors?"** | Competitor battlecard → `research/competitors/` |
| **"Make a lean canvas"** | Business model canvas → `docs/lean-canvas/` |
| **"Write a PRD"** | Product Requirements Doc → `docs/prd/` |
| **"Draw the architecture"** | Mermaid diagram → `diagrams/architecture/` |
| **"Plan the MVP"** | MVP scope + roadmap → `plans/mvp/` |
| **"Design an experiment"** | Validation experiment → `plans/experiments/` |
| **"Generate a report"** | Structured research report → `docs/reports/` |

### 3. Let the System Work
Every idea follows a validated path. I enforce the rules in `GROUND_RULES.md`:
- Research before building
- Validate or die
- Bias for action
- No idea rots in development forever

---

## Directory Map

```
dreamboard/
├── 📄 README.md              ← You are here
├── 📄 GROUND_RULES.md        ← The constitution. Read this.
├── 📄 AGENTS.md              ← My playbook. How I operate.
├── 📄 IDEA-INDEX.md          ← Dashboard of all ideas
│
├── 🌱 ideas/                 ← Your idea repository
│   ├── raw/                  ← Fresh brain-dumps
│   ├── developing/           ← Active research & planning
│   ├── incubating/           ← On hold
│   └── completed/            ← Done!
│
├── 🔬 research/              ← All intelligence
│   ├── market/               ← Market research, TAM/SAM/SOM
│   ├── competitors/          ← Competitor analysis
│   ├── tech-stack/           ← Technical research
│   └── trends/               ← Industry trends
│
├── 📑 docs/                  ← Structured documents
│   ├── lean-canvas/          ← Business model canvases
│   ├── prd/                  ← Product Requirements Docs
│   ├── personas/             ← User personas & JTBD
│   └── reports/              ← Generated research reports
│
├── 📊 diagrams/              ← Visual artifacts (all Mermaid)
│   ├── architecture/         ← System architecture
│   ├── flow/                 ← User flows & processes
│   ├── business/             ← Business model diagrams
│   └── mindmaps/             ← Idea mind maps
│
├── 🗺️ plans/                 ← Execution plans
│   ├── mvp/                  ← MVP scopes & feature lists
│   ├── roadmap/              ← Timelines & Gantt charts
│   └── experiments/          ← Validation experiments
│
├── 📁 archive/               ← Dead ideas (with post-mortems)
│
└── 📋 templates/             ← All templates
```

---

## Idea Lifecycle

```
[RAW] → [DEVELOPING] → [COMPLETED]
   ↓         ↓
[ARCHIVE] [INCUBATING]
```

| Status | Meaning | Exit Criteria |
|--------|---------|---------------|
| **Raw** | Fresh brain-dump. Unfiltered, chaotic, pure energy. | User asks to develop it |
| **Developing** | Being researched, validated, and planned. | Lean Canvas + Experiment + MVP plan |
| **Incubating** | Good idea, wrong timing. Let it sit. | User reactivates |
| **Completed** | Done! Built, launched, or achieved. | Evidence of completion |
| **Archive** | Killed or merged. Lessons learned. | Post-mortem written |

---

## The Execution Checklist

Before ANY idea is "ready to build":

- [ ] **Lean Canvas** completed
- [ ] **Problem validated** — at least 3 users confirm the pain
- [ ] **Competitors mapped** — you know the landscape
- [ ] **MVP scoped** — smallest version defined
- [ ] **Experiment designed** — you know how to test
- [ ] **Tech stack chosen** — you know what to build with

---

## Quick Start

**New to DreamBoard?** Start here:

1. Read `GROUND_RULES.md` — understand the system
2. Dump your first idea: *"I have a crazy idea..."*
3. Pick one developing idea and say: *"Make a lean canvas for [idea]"*
4. Then: *"Research the market for [idea]"*
5. Then: *"Plan the MVP for [idea]"*

Watch your idea transform from a spark into an executable plan.

---

## Why Mermaid for Diagrams?

All diagrams use **Mermaid** syntax — a text-based diagram language that:
- Renders automatically on GitHub
- Is version-controlled (it's just text)
- Requires zero tools or subscriptions
- Works in VS Code, Notion, and any markdown viewer

Need a PNG/SVG? Paste the code into [mermaid.live](https://mermaid.live).

---

## Ground Rules

See `GROUND_RULES.md` for the full constitution, but the highlights are:

1. **No idea is too crazy** — capture everything
2. **Research before build** — never code without validation
3. **Validate or die** — evidence required, not opinions
4. **Bias for action** — max 2 weeks in developing without an experiment
5. **The AI is your co-founder** — I challenge assumptions, not just agree

---

*"Ideas are cheap. Execution is everything. But execution without validation is just expensive guessing."*

**Ready? Hit me with your craziest idea.** 🚀
