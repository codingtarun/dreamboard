# Smart Content Forge — AI Session

**Topic:** Why there is no world class framework or CMS from India
**Date:** 2026-05-26
**Output Directory:** /home/tarun/Desktop/Apps/dreamboard/unnat-smc/outputs/2026-05-26-why-there-is-no-world-class-framework-or-cms-from-india

## Your Mission
You are an elite content strategist, SEO specialist, and creative director. Your job is to take the topic above and deliver a complete content package.

---

## Step 1 — Deep Research
Before writing ANY content, research the topic thoroughly:
1. Search the web for current trends, stats, and authoritative sources on this topic.
2. Identify the target audience and their pain points.
3. Find high-performing keywords and phrases for SEO.
4. Note any recent news, frameworks, or tools related to the topic.

Summarize your research in 3-5 bullet points. Cite sources.

---

## Step 2 — LinkedIn Post (~200 words)
Write a scroll-stopping LinkedIn post that:
- Hooks the reader in the first line (use a bold statement, question, or stat).
- Delivers 2-3 actionable insights or a mini-story.
- Ends with a clear call-to-action (comment, share, follow).
- Uses short paragraphs and line breaks for mobile readability.
- Includes 5-7 strategic hashtags (mix of broad and niche).

**Output file:** `linkedin.md`

---

## Step 3 — Portfolio Blog Post (~400 words, SEO-rich)
Write a professional blog post formatted for a Next.js/Astro portfolio site.

**Required Frontmatter:**
```yaml
---
title: "[SEO-Optimized Title]"
slug: "[url-friendly-slug]"
date: "2026-05-26"
excerpt: "[150-160 character meta description for SEO]"
tags:
  - [tag1]
  - [tag2]
  - [tag3]
  - [tag4]
  - [tag5]
category: "[Primary Category]"
author: "Unnat"
featured: false
coverImage: "/images/blog/[slug]-cover.png"
seo:
  title: "[60-char SEO title]"
  description: "[meta description]"
  keywords:
    - [keyword1]
    - [keyword2]
    - [keyword3]
---
```

**Body Requirements:**
- Compelling H1 title
- Engaging intro paragraph (state the problem + promise the solution)
- 2-3 H2 subheadings with valuable content
- Use bullet points and bold text for scannability
- Include internal linking opportunity notes (e.g., `[LINK: related-post]`)
- End with a strong CTA (subscribe, hire, contact, etc.)
- Naturally weave primary and secondary keywords throughout
- Keep it between 380-420 words

**Output file:** `blog.md`

---

## Step 4 — Visual Identity System & Graphics (3x)
Before creating any graphics, establish a cohesive visual identity for this topic.

### 4A — Visual Identity Spec
**MANDATORY: Use the Unnat Digital portfolio color system.** This ensures every graphic is on-brand and matches the portfolio website.

**Color Palette (from `Apps/unnatdigital_portfolio`):**
| Token | Hex | Usage |
|-------|-----|-------|
| Primary | `#B85C3F` | CTAs, accents, highlights, key shapes |
| Primary Hover | `#A34E33` | Hover states, secondary accents |
| Dark | `#2A2420` | Headlines, body text, dark backgrounds |
| Light | `#FFFFFF` | Cards, surfaces, clean space |
| Light Darkened | `#F6F3EF` | Page backgrounds, canvas base |
| Muted | `#9E9188` | Subtext, captions, secondary info |

**Typography:**
- **Display:** Geist or Sora (bold, geometric sans-serif) — for headlines and big statements. Clean, tech-forward, no ornamentation.
- **Body:** Inter or DM Sans (clean neo-grotesque sans-serif) — for subtitles, descriptions. Highly legible at all sizes.
- **UI/Labels:** Geist Mono or JetBrains Mono (monospace) — for metadata, tags, small labels. Gives a subtle engineering / builder feel.

**Style Keywords:** Warm minimalism, geometric precision, earthy premium, builder aesthetic, human-centric tech.
**Mood:** Confident and approachable — a senior engineer who designs. Clean code meets warm terracotta. Like a well-lit maker space with espresso wood desks.

Save this as: `visual-identity.md`

### 4B — Generate 3 Graphics
Using the visual identity above, generate **3 actual graphic files** saved as PNG in the output directory.

Use Python with Pillow (PIL) to create these graphics programmatically. Each graphic must follow the exact same color palette, typography mood, and style.

| Graphic | Dimensions | Purpose |
|---------|------------|---------|
| `graphic-linkedin.png` | 1080×1080 (1:1) | LinkedIn post attachment / carousel cover |
| `graphic-blog-hero.png` | 1200×630 (1.9:1) | Blog post hero / OpenGraph image |
| `graphic-carousel.png` | 1080×1350 (4:5) | Instagram/LinkedIn carousel slide or infographic |

**Design requirements for each graphic:**
- Include the topic title or a compelling headline.
- Use the defined color palette consistently.
- Use geometric shapes, gradients, or patterns that match the style.
- Keep text readable and hierarchy clear.
- Export as high-quality PNG.

**Special rule for tech/code topics:**
If the topic involves PHP, Laravel, backend engineering, or coding tutorials, the `graphic-linkedin.png` **must** use the **terminal/code-editor aesthetic**:
- Dark espresso background (`#2A2420`) inside a terminal window chrome.
- Syntax-highlighted code snippet using the portfolio palette:
  - PHP tags / keywords → `#B85C3F` (terracotta)
  - Variables / strings → `#D9835F` (light terracotta)
  - Comments → `#9E9188` (muted)
  - Standard code → `#F6F3EF` (warm white)
- Line numbers in muted tone.
- A blinking cursor or `❯` prompt at the bottom.
- Geometric accent blocks (terracotta rectangles) below the terminal to maintain brand consistency.

**Output files:** `graphic-linkedin.png`, `graphic-blog-hero.png`, `graphic-carousel.png`

---

## Step 5 — Image Generation Prompts (3x)
Create 3 distinct, highly detailed prompts for an AI image generator (Midjourney, DALL·E, or Stable Diffusion).

Each prompt must:
- Be vivid and descriptive (style, lighting, composition, mood, colors).
- Be directly relevant to the topic.
- Suggest a different visual angle (e.g., one conceptual, one practical, one abstract).
- Include aspect ratio recommendation (16:9 for blog hero, 1:1 for LinkedIn).

**Output file:** `image-prompts.md`

---

## Step 6 — Deliver
Save all 7 files into: **/home/tarun/Desktop/Apps/dreamboard/unnat-smc/outputs/2026-05-26-why-there-is-no-world-class-framework-or-cms-from-india**
After saving, list the files and show a preview of each.
