# Open-Source YouTube to MP3 Desktop App

**Status:** archive
**Spark:** 🔥🔥🔥
**Created:** 2026-05-20
**Last Updated:** 2026-05-20
**Tags:** opensource, desktop-app, media-converter, youtube, audio, video

## The Spark
User recently built a YouTube-to-MP3 converter and wants to package it as downloadable open-source desktop software. Users would install the app on their desktop and download YouTube videos as MP3 (audio) or video files locally.

## Details
- Desktop application (cross-platform? Windows/Mac/Linux?)
- Open-source on GitHub
- Converts YouTube URLs → MP3 or video formats
- User downloads and installs as local software

## Why It Excites Me
- Already built the core converter — low effort to productize
- Open-source gets community contributions and visibility
- Desktop app = no hosting costs, no server infrastructure
- Useful utility with broad appeal

## Potential Obstacles
**🚨 LEGAL — This is the #1 killer:**
- YouTube's Terms of Service **explicitly prohibit** downloading content
- **RIAA DMCA takedown risk** — In 2020, the RIAA issued a DMCA takedown against `youtube-dl` on GitHub (later reversed, but the legal threat remains)
- Copyright infringement liability for enabling downloads of copyrighted content
- GitHub/Microsoft could remove the repo under DMCA
- In some jurisdictions, distributing tools that circumvent access controls is illegal
- Even open-source projects face legal action (see `yt-dlp` forks ongoing cat-and-mouse)

**Technical:**
- YouTube changes their obfuscation regularly — requires constant maintenance
- Competing with mature projects like `yt-dlp`, `youtube-dl`, `4K Video Downloader`
- Desktop packaging (electron, Tauri, native) adds complexity

**Market:**
- Extremely saturated space
- Hard to monetize ethically/legally
- Users who want this already know `yt-dlp`

## Next Steps
- **Assess legal risk tolerance** — This is make-or-break before any code is written
- Research specific jurisdiction's laws on downloading tools (e.g., India?)
- Consider pivot to a broader "media toolkit" that supports public domain / Creative Commons sources explicitly
- Design an experiment: Can we get 100 GitHub stars on a README before writing code?

## Related Ideas
- [None yet]

## Post-Mortem
**Why it died:** Legal risk outweighed utility.
- YouTube ToS explicitly prohibits downloading
- RIAA DMCA takedown precedent (`youtube-dl`, 2020)
- Saturated market with mature alternatives (`yt-dlp`, `4K Video Downloader`)
- Solo maintainer would lose cat-and-mouse game against YouTube's obfuscation changes
- No clear ethical monetization path

**Lesson:** Legal due diligence *before* excitement. A working prototype does not equal a shippable product.

## Notes Log
- 2026-05-20 — Idea captured. Strong legal concerns flagged immediately. This idea is high-risk.
- 2026-05-20 — Archived by user decision after legal challenge.
