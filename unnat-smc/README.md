# 🚀 unnat-smc — Smart Content Forge

> **One topic in. Content machine out.**

`unnat-smc` is a content generation module inside your DreamBoard. Give it a topic, and it orchestrates deep research + multi-format content creation for your personal brand.

---

## ✨ What It Creates

| Asset | Specs |
|-------|-------|
| 🔗 **LinkedIn Post** | ~200 words, hook-driven, mobile-formatted, with 5-7 hashtags |
| 📝 **Portfolio Blog** | ~400 words, SEO-optimized (excerpt, tags, keywords, frontmatter) |
| 🎨 **Image Prompts** | 3 detailed prompts for AI image generators (Midjourney / DALL·E / SD) |

All outputs are saved to `outputs/YYYY-MM-DD-topic-slug/` for your review before publishing.

---

## 🛠️ Installation

No dependencies. Just make the script executable (already done):

```bash
chmod +x unnat-smc/create-content
```

---

## 🚀 Usage

### Option A — Interactive Mode
```bash
cd unnat-smc
./create-content
# Then type your topic when prompted
```

### Option B — Direct Topic
```bash
cd unnat-smc
./create-content "How AI is Reshaping Personal Branding"
```

### What Happens Next
1. Creates a workspace: `outputs/2026-05-23-how-ai-is-reshaping-personal-branding/`
2. Generates an AI prompt file: `prompt.md`
3. If `kimi` CLI is installed, offers to auto-run the session
4. Otherwise, prints the manual command

---

## 📁 Output Structure

```
outputs/
└── 2026-05-23-how-ai-is-reshaping-personal-branding/
    ├── prompt.md              # The full AI instruction set
    ├── linkedin.md            # Your LinkedIn post
    ├── blog.md                # SEO-rich blog for unnatdigital_portfolio
    └── image-prompts.md       # 3 AI image prompts
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
| **Images** | Use Prompt 1 (16:9) for blog hero. Use Prompt 2 (1:1) for LinkedIn attachment. |

---

## 🎯 Quick Reference

| Command | Action |
|---------|--------|
| `./create-content` | Interactive topic input |
| `./create-content "Topic"` | Direct topic input |
| `kimi -f prompt.md` | Run the AI session manually |

---

## 📝 Customization

Want to tweak the AI behavior? Edit these files:

- **`create-content`** — Change output directory, date format, or CLI behavior
- **`templates/`** — Update the format references for LinkedIn, blog, or image prompts
- **`prompt.md` (generated)** — Modify the AI instructions before running

---

Built with 🔥 for the DreamBoard.
