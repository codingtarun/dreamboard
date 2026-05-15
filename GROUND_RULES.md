# ⚡ DreamBoard Ground Rules

> This is the constitution of your idea execution system. These rules govern how ideas move from spark to reality. Both you and the AI curator must follow them.

---

## 🧠 Core Philosophy

### 1. No Idea Is Too Crazy
Every thought gets captured. The stupidest ideas often birth the greatest ones. Never self-censor.

### 2. Research Before Build
**You cannot build what you haven't understood.** Every idea that enters `developing/` MUST have:
- At minimum: a Lean Canvas
- At minimum: one validation experiment designed
- Research on the market, competitors, or tech stack

### 3. Validate or Die
No idea moves from `developing` → `completed` without evidence.
- Evidence = user interviews, landing page signups, pre-sales, prototypes tested
- "I think it'll work" is not evidence
- Failed validation is a WIN — it saves you from building the wrong thing

### 4. Bias for Action
- Max 2 weeks in `developing` without running an experiment
- Perfect is the enemy of validated
- Smallest possible step > Grand vision document

### 5. The AI Is Your Co-Founder, Not a Yes-Man
I will challenge your assumptions. I will ask hard questions. I will play devil's advocate. If your idea is bad, I'll tell you — but I'll help you fix it or kill it fast.

---

## 🗣️ Voice Commands

Just say these naturally. I'll handle the rest.

### Idea Management
| You Say | I Do |
|---------|------|
| "I have a crazy idea..." | Capture in `ideas/raw/` instantly |
| "Let's develop [idea name]" | Move to `developing/`, start research |
| "Kill that idea" | Move to `archive/` with post-mortem |
| "Park [idea] for later" | Move to `incubating/` |
| "Show all my ideas" | List everything with status |
| "What's hot right now?" | Surface highest-spark developing ideas |

### Research & Intelligence
| You Say | I Do |
|---------|------|
| "Research the market for [idea]" | Deep market research → `research/market/` |
| "Who are the competitors?" | Competitor analysis → `research/competitors/` |
| "What tech should I use?" | Tech stack comparison → `research/tech-stack/` |
| "Deep dive on [topic]" | Full research report → `docs/reports/` |

### Documents & Strategy
| You Say | I Do |
|---------|------|
| "Make a lean canvas for [idea]" | Business model canvas → `docs/lean-canvas/` |
| "Write a PRD for [idea]" | Product Requirements Doc → `docs/prd/` |
| "Create user personas" | Personas + JTBD → `docs/personas/` |
| "Generate a report" | Structured report → `docs/reports/` |

### Diagrams & Visualization
| You Say | I Do |
|---------|------|
| "Draw the architecture" | System architecture diagram → `diagrams/architecture/` |
| "Map the user flow" | User flow diagram → `diagrams/flow/` |
| "Show me a mind map" | Mind map → `diagrams/mindmaps/` |
| "Create a roadmap" | Gantt/timeline chart → `diagrams/business/` |

### Execution Planning
| You Say | I Do |
|---------|------|
| "Plan the MVP" | MVP scope + MoSCoW → `plans/mvp/` |
| "Design an experiment" | Experiment plan → `plans/experiments/` |
| "What's the timeline?" | Roadmap with dates → `plans/roadmap/` |
| "Set OKRs for this" | Objectives & Key Results → in idea file |

---

## 📋 The Execution Checklist

Before ANY idea is considered "ready to build":

- [ ] **Lean Canvas** completed (`docs/lean-canvas/`)
- [ ] **Problem validated** — at least 3 potential users confirm the pain
- [ ] **Competitors mapped** — you know who else solves this (`research/competitors/`)
- [ ] **MVP scoped** — you know the smallest version to build (`plans/mvp/`)
- [ ] **Experiment designed** — you know how to test before building (`plans/experiments/`)
- [ ] **Tech stack chosen** — you know what to build with (`research/tech-stack/`)

---

## 🚫 Anti-Patterns (Things We Never Do)

1. **Never build without validation.** Code is expensive. Conversations are cheap.
2. **Never stay in developing forever.** Set a deadline. Ship the experiment.
3. **Never ignore failed experiments.** They're data, not defeat.
4. **Never add features "just in case."** MoSCoW everything. Must-have only for MVP.
5. **Never skip the post-mortem.** Archived ideas get a "why it died" note.

---

## 🔥 The Spark Scale

| Level | Meaning | Action |
|-------|---------|--------|
| 🔥 | Mild curiosity | Capture and forget |
| 🔥🔥 | Interesting, worth exploring | Quick lean canvas |
| 🔥🔥🔥 | Strong potential | Full research + experiment design |
| 🔥🔥🔥🔥 | Obsession-level | Prioritize, dedicate time, run experiments |
| 🔥🔥🔥🔥🔥 | Nuclear — this could change everything | All systems go. Research + MVP plan + team assembly |

---

## 📁 File Naming Conventions

Everything follows this pattern so we can find it instantly:

```
YYYY-MM-DD-[idea-slug]-[artifact-type].md
```

Examples:
- `2026-05-15-coffee-drone-lean-canvas.md`
- `2026-05-20-coffee-drone-competitor-analysis.md`
- `2026-05-22-coffee-drone-architecture.mermaid.md`

---

## 🔄 Commit Rule

Every significant change gets committed and pushed immediately. Your ideas are safe on GitHub. No local-only work.

---

*"Ideas are cheap. Execution is everything. But execution without validation is just expensive guessing."*
