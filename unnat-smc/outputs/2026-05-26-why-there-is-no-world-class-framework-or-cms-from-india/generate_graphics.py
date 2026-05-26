#!/usr/bin/env python3
"""Generate branded graphics for the content package."""

from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Color Palette ───────────────────────────────────────────────
PRIMARY = "#B85C3F"
PRIMARY_HOVER = "#A34E33"
DARK = "#2A2420"
LIGHT = "#FFFFFF"
LIGHT_DARKENED = "#F6F3EF"
MUTED = "#9E9188"

# ── Fonts ───────────────────────────────────────────────────────
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
FONT_BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
FONT_REG = os.path.join(FONT_DIR, "DejaVuSans.ttf")
FONT_MONO = os.path.join(FONT_DIR, "DejaVuSansMono-Bold.ttf")

# ── Helpers ─────────────────────────────────────────────────────
def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def draw_rounded_rect(draw, xy, radius, fill):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill)

def wrap_text(text, font, max_width, draw):
    """Simple word wrap."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = current + (" " if current else "") + word
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

# ════════════════════════════════════════════════════════════════
#  Graphic 1 — LinkedIn (1080×1080)
# ════════════════════════════════════════════════════════════════
def make_linkedin():
    W, H = 1080, 1080
    img = Image.new("RGB", (W, H), hex_to_rgb(LIGHT_DARKENED))
    d = ImageDraw.Draw(img)

    # Background dark overlay at top
    d.rectangle([0, 0, W, H], fill=hex_to_rgb(DARK))

    # Geometric terracotta accent blocks at bottom
    block_h = 120
    d.rectangle([0, H - block_h, W, H], fill=hex_to_rgb(PRIMARY))
    # Sub-block
    d.rectangle([0, H - block_h, W // 3, H], fill=hex_to_rgb(PRIMARY_HOVER))

    # Small geometric shapes as decoration
    d.rectangle([80, 80, 180, 180], fill=hex_to_rgb(PRIMARY))
    d.rectangle([900, 200, 1000, 300], fill=hex_to_rgb(PRIMARY_HOVER))

    # Title
    title_font = ImageFont.truetype(FONT_BOLD, 68)
    subtitle_font = ImageFont.truetype(FONT_REG, 36)
    tag_font = ImageFont.truetype(FONT_MONO, 22)

    title_text = "Why Hasn't India\\nBuilt a World-Class\\nFramework or CMS?"
    title_lines = title_text.split("\\n")
    y = 260
    for line in title_lines:
        d.text((80, y), line, font=title_font, fill=hex_to_rgb(LIGHT))
        y += 88

    # Subtitle
    sub = "A deep dive into the mindset, ecosystem,\\nand the builders changing the narrative."
    sub_lines = sub.split("\\n")
    y += 20
    for line in sub_lines:
        d.text((80, y), line, font=subtitle_font, fill=hex_to_rgb(MUTED))
        y += 50

    # Tag
    d.text((80, H - block_h + 45), "UNNAT DIGITAL  ·  TECH DEEP DIVE", font=tag_font, fill=hex_to_rgb(LIGHT))

    out = os.path.join(OUTPUT_DIR, "graphic-linkedin.png")
    img.save(out, "PNG")
    print(f"✅ Saved: {out}")

# ════════════════════════════════════════════════════════════════
#  Graphic 2 — Blog Hero (1200×630)
# ════════════════════════════════════════════════════════════════
def make_blog_hero():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), hex_to_rgb(LIGHT_DARKENED))
    d = ImageDraw.Draw(img)

    # Split layout: left dark, right light
    split = 520
    d.rectangle([0, 0, split, H], fill=hex_to_rgb(DARK))
    d.rectangle([split, 0, W, H], fill=hex_to_rgb(LIGHT_DARKENED))

    # Geometric terracotta blocks on right
    d.rectangle([split, H - 80, W, H], fill=hex_to_rgb(PRIMARY))
    d.rectangle([split, H - 80, split + 300, H], fill=hex_to_rgb(PRIMARY_HOVER))

    # Small accent shapes
    d.rectangle([split + 40, 40, split + 100, 100], fill=hex_to_rgb(PRIMARY))

    # Title on dark side
    title_font = ImageFont.truetype(FONT_BOLD, 52)
    body_font = ImageFont.truetype(FONT_REG, 24)
    tag_font = ImageFont.truetype(FONT_MONO, 18)

    title = "Why India Hasn't\\nBuilt a World-Class\\nFramework or CMS"
    y = 140
    for line in title.split("\\n"):
        d.text((60, y), line, font=title_font, fill=hex_to_rgb(LIGHT))
        y += 68

    # Body teaser
    y += 20
    teaser = "1.5M+ engineers. Zero global frameworks.\\nHere's what changed — and what's next."
    for line in teaser.split("\\n"):
        d.text((60, y), line, font=body_font, fill=hex_to_rgb(MUTED))
        y += 38

    # Date & tag on light side bottom
    d.text((split + 40, H - 60), "26 MAY 2026  ·  UNNAT DIGITAL", font=tag_font, fill=hex_to_rgb(DARK))

    # Decorative code-like lines on right
    mono_small = ImageFont.truetype(FONT_MONO, 16)
    code_lines = [
        "<?php",
        "  // India builds the world...",
        "  // but who builds for India?",
        "  class Ecosystem {",
        "    public function change() {",
        "      return new Builders();",
        "    }",
        "  }",
    ]
    y = 120
    for cl in code_lines:
        d.text((split + 60, y), cl, font=mono_small, fill=hex_to_rgb(MUTED))
        y += 28

    out = os.path.join(OUTPUT_DIR, "graphic-blog-hero.png")
    img.save(out, "PNG")
    print(f"✅ Saved: {out}")

# ════════════════════════════════════════════════════════════════
#  Graphic 3 — Carousel (1080×1350)
# ════════════════════════════════════════════════════════════════
def make_carousel():
    W, H = 1080, 1350
    img = Image.new("RGB", (W, H), hex_to_rgb(LIGHT))
    d = ImageDraw.Draw(img)

    # Header bar
    d.rectangle([0, 0, W, 12], fill=hex_to_rgb(PRIMARY))

    # Bottom terracotta anchor
    d.rectangle([0, H - 160, W, H], fill=hex_to_rgb(PRIMARY))
    d.rectangle([0, H - 160, 360, H], fill=hex_to_rgb(PRIMARY_HOVER))

    # Title
    title_font = ImageFont.truetype(FONT_BOLD, 64)
    h2_font = ImageFont.truetype(FONT_BOLD, 38)
    body_font = ImageFont.truetype(FONT_REG, 30)
    mono_font = ImageFont.truetype(FONT_MONO, 22)

    y = 80
    d.text((80, y), "The Framework Gap:", font=title_font, fill=hex_to_rgb(DARK))
    y += 90
    d.text((80, y), "Why India? Why Now?", font=title_font, fill=hex_to_rgb(PRIMARY))
    y += 120

    # Divider
    d.rectangle([80, y, 300, y + 6], fill=hex_to_rgb(PRIMARY))
    y += 50

    # Sections
    sections = [
        ("1. SERVICES MINDSET", "IT culture rewarded billable hours, not product bets."),
        ("2. RISK AVERSION", "No patient capital for 5–10 year open-source plays."),
        ("3. BRAIN DRAIN", "Best builders left for Silicon Valley."),
        ("4. THE TURN", "Hoppscotch, ERPNext, Bagisto — proof it's changing."),
    ]

    for heading, body in sections:
        d.text((80, y), heading, font=h2_font, fill=hex_to_rgb(DARK))
        y += 56
        # Wrap body
        words = body.split()
        line = ""
        for word in words:
            test = line + (" " if line else "") + word
            bbox = d.textbbox((0, 0), test, font=body_font)
            if bbox[2] - bbox[0] <= W - 160:
                line = test
            else:
                d.text((80, y), line, font=body_font, fill=hex_to_rgb(MUTED))
                y += 44
                line = word
        if line:
            d.text((80, y), line, font=body_font, fill=hex_to_rgb(MUTED))
            y += 44
        y += 30

    # CTA
    y += 20
    d.text((80, y), "→ Read the full analysis on unnatdigital.com", font=mono_font, fill=hex_to_rgb(PRIMARY))

    # Tag
    d.text((80, H - 100), "UNNAT DIGITAL  ·  TECH ECOSYSTEM", font=mono_font, fill=hex_to_rgb(LIGHT))

    out = os.path.join(OUTPUT_DIR, "graphic-carousel.png")
    img.save(out, "PNG")
    print(f"✅ Saved: {out}")

# ════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    make_linkedin()
    make_blog_hero()
    make_carousel()
    print("\n🎨 All 3 graphics generated successfully!")
