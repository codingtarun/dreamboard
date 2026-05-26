# 🚀 unnat-smc — Smart Content Forge

> **One topic in. Content machine out.**

`unnat-smc` is a content generation module inside your DreamBoard. It has two modes:
- **General content** — research-driven LinkedIn + blog + graphics package
- **Code content** — developer-focused LinkedIn post + topic graphic + terminal code graphic

Both modes use the **locked Unnat Digital portfolio visual identity** (warm terracotta + espresso + tech typography).

---

## ✨ Two Commands

### 1. `create-content` — Full Content Package
For general topics, thought leadership, and SEO blog posts.

| Asset | Specs |
|-------|-------|
| 🔗 **LinkedIn Post** | ~200 words, hook-driven, mobile-formatted, 5-7 hashtags |
| 📝 **Portfolio Blog** | ~400 words, SEO-optimized (excerpt, tags, keywords, frontmatter) |
| 🎨 **3 Branded Graphics** | LinkedIn (1:1), Blog Hero (1.9:1), Carousel (4:5) — unified palette |
| 🎨 **Image Prompts** | 3 detailed prompts for Midjourney / DALL·E / Stable Diffusion |
| 🎨 **Visual Identity** | Locked portfolio palette, font pairings, mood spec |

### 2. `create-code-content` — Code Snippet Package
For PHP, Laravel, backend patterns, and developer tips.

| Asset | Specs |
|-------|-------|
| 🔗 **LinkedIn Post** | ~180-220 words, developer-focused, code teaser + CTA |
| 🎨 **Topic Highlight Graphic** | 1080×1080 — bold headline + concept, no code |
| 🎨 **Terminal Code Graphic** | 1080×1080 — syntax-highlighted code in a terminal window |
| 🎨 **Visual Identity** | Locked portfolio palette, font pairings, mood spec |

**Terminal graphic features:**
- Dark espresso (`#2A2420`) background with chrome bar
- Syntax highlighting using portfolio terracotta tones
- Line numbers + `❯` prompt or blinking cursor
- Geometric terracotta blocks below for brand consistency

---

## 🛠️ Installation

No dependencies. Just make the scripts executable (already done):

```bash
chmod +x unnat-smc/create-content
chmod +x unnat-smc/create-code-content
```

---

## 🚀 Usage

### General Content
```bash
cd unnat-smc
./create-content "How AI is Reshaping Personal Branding"
```

### Code Content
```bash
cd unnat-smc
./create-code-content "PHP Pipeline Pattern"
# or paste a raw snippet:
./create-code-content "class Pipeline { public function handle($request) { ... } }"
```

### Interactive Mode
Run either script without arguments to enter interactive mode:
```bash
./create-content
./create-code-content
```

### What Happens Next
1. Creates a workspace: `outputs/2026-05-23-topic-slug/`
2. Generates an AI prompt file: `prompt.md`
3. If `kimi` CLI is installed, offers to auto-run the session
4. Otherwise, prints the manual command

---

## 📁 Output Structure

### `create-content` output:
```
outputs/
└── 2026-05-23-how-ai-is-reshaping-personal-branding/
    ├── prompt.md                   # The full AI instruction set
    ├── linkedin.md                 # Your LinkedIn post
    ├── blog.md                     # SEO-rich blog for unnatdigital_portfolio
    ├── visual-identity.md          # Locked portfolio palette, fonts, mood
    ├── graphic-linkedin.png        # 1080×1080 branded social graphic
    ├── graphic-blog-hero.png       # 1200×630 branded blog hero / OG image
    ├── graphic-carousel.png        # 1080×1350 branded carousel / infographic
    └── image-prompts.md            # 3 AI image prompts
```

### `create-code-content` output:
```
outputs/
└── 2026-05-23-php-pipeline-pattern/
    ├── prompt.md                   # The full AI instruction set
    ├── linkedin.md                 # Developer-focused LinkedIn post
    ├── visual-identity.md          # Locked portfolio palette, fonts, mood
    ├── graphic-topic-highlight.png # 1080×1080 bold concept graphic
    └── graphic-code-example.png    # 1080×1080 terminal code snippet
```

---

## 🔗 Portfolio Integration

Your portfolio lives at: `Apps/unnatdigital_portfolio`

After reviewing the generated `blog.md`:
1. Copy the frontmatter + body into your portfolio's content directory
2. Drop the generated hero image into `/public/images/blog/`
3. Update the `coverImage` path in frontmatter

The blog template uses **generic YAML frontmatter** compatible with:
- Next.js (Contentlayer, MDX)
- Astro (Content Collections)
- Gatsby
- Jekyll

---

## 🧠 Workflow Tips

| Stage | Tip |
|-------|-----|
| **Research** | The AI searches current web data. Always verify stats before publishing. |
| **LinkedIn** | Post during Tue-Thu, 8-10 AM IST for best Indian professional engagement. |
| **Blog** | Wait 24h after LinkedIn, then publish the long-form blog + cross-link back. |
| **Code Posts** | Post the terminal graphic as the main image. Tease the code in the caption. |
| **Images** | Use generated branded graphics for immediate posting. Use AI prompts for custom hero art. |

---

## 🎯 Quick Reference

| Command | Action |
|---------|--------|
| `./create-content` | Interactive general topic input |
| `./create-content "Topic"` | Direct general topic input |
| `./create-code-content` | Interactive code topic input |
| `./create-code-content "Code / Topic"` | Direct code topic or raw snippet input |
| `kimi -f prompt.md` | Run the AI session manually |

---

## 📝 Customization

Want to tweak the AI behavior? Edit these files:

- **`create-content`** — General content workflow, output directory, CLI behavior
- **`create-code-content`** — Code content workflow, terminal graphic specs
- **`templates/`** — Update format references for LinkedIn, blog, or image prompts
- **`prompt.md` (generated)** — Modify the AI instructions before running

---

Built with 🔥 for the DreamBoard.
