# 🧠 DreamBoard — Your Idea Execution Engine

Welcome to your personal **brain-to-build command center**. This is where **no idea is too crazy** — and where crazy ideas get the research, strategy, and execution plans they need to become real.

---

## Workspace Structure

```
dreamboard/
├── README.md                    ← You are here (master index)
├── GROUND_RULES.md              ← The constitution. Read this.
├── AGENTS.md                    ← My playbook. How I operate.
├── IDEA-INDEX.md                ← Dashboard of all ideas (auto-updated)
│
├── bin/
│   └── dbpulse                  ← CLI automation tool
├── scripts/
│   └── lib.sh                   ← Pulse engine core
├── memory/
│   ├── MEMORY.md                ← Long-term curated context
│   └── daily/                   ← Auto-generated daily digests
│
├── ideas/                       ← Core idea repository
│   ├── raw/                     ← Fresh brain-dumps
│   ├── developing/              ← Active research & planning
│   ├── incubating/              ← On hold
│   └── completed/               ← Done!
├── templates/                   ← All templates (lean canvas, PRD, etc.)
├── research/                    ← General research archive
├── docs/                        ← General documents
├── diagrams/                    ← Visual artifacts
├── plans/                       ← Execution plans
├── archive/                     ← Dead ideas
│
├── bhatko/                      ← ACTIVE: Spontaneous Travel Platform
├── baagvaani/                   ← ACTIVE: Apple Orchard Management App (renamed from Baagicha)
│
└── .git/                        ← Everything tracked on GitHub
```

---

## Active Projects

| Project | Domain | Status | Spark |
|---------|--------|--------|-------|
| **[Bhatko](bhatko/README.md)** | bhatko.com | Developing | 🔥🔥🔥🔥🔥 |
| **[Baagvaani](baagvaani/README.md)** | (App) | Developing | 🔥🔥🔥🔥🔥 |

---

## How to Use

### 1. Let the Board Run Itself (Pulse Automation)
DreamBoard has a built-in heartbeat system inspired by `.openclaw`:

```bash
# Add to PATH
export PATH="$PWD/bin:$PATH"

# Check board health anytime
dbpulse status
dbpulse check

# Generate today's digest + auto-update index
dbpulse daily

# Quick capture a note
dbpulse note "Had a breakthrough on Bhatko pricing"

# Set up daily 9 AM automation
dbpulse init
```

**What runs automatically:**
- Daily digest in `memory/daily/YYYY-MM-DD.md`
- Auto-updated `IDEA-INDEX.md` (no more manual upkeep)
- Stale idea alerts (developing >14 days, raw >30 days)
- Missing artifact detection (lean canvas, experiments)
- Orphaned doc detection

**Memory System:**
- `memory/MEMORY.md` — Curated long-term context (decisions, lessons)
- `memory/daily/` — Raw daily logs & digests

### 2. Brain-Dump Freely
Just tell me your idea. I'll capture it instantly in `ideas/raw/`.

### 3. Say the Magic Words
I respond to natural voice commands:

| You Say | I Do |
|---------|------|
| **"Research the market"** | Deep market research |
| **"Who are my competitors?"** | Competitor battlecard |
| **"Make a lean canvas"** | Business model canvas |
| **"Write a PRD"** | Product Requirements Doc |
| **"Draw the architecture"** | Mermaid diagram |
| **"Plan the MVP"** | MVP scope + roadmap |
| **"Design an experiment"** | Validation experiment |
| **"Generate a report"** | Structured research report |

### 4. Projects Get Their Own Workspace
When an idea moves to `developing`, it gets a dedicated folder under `projects/` with its own:
- `ideas/` — All related concepts
- `research/` — Market, competitor, tech research
- `docs/` — Lean canvas, PRD, personas
- `diagrams/` — Architecture, flows, business models
- `plans/` — MVP, experiments, roadmaps

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
