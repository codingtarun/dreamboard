# 🧠 DreamBoard Memory

This is the long-term memory for the DreamBoard agent.
Curated wisdom, decisions, and context that should survive across sessions.

## Active Context

- **Current Focus:** SwiftCart MVP sprint (paused), Offline Music Player idea (raw/researched)
- **Last Session Date:** 2026-05-21
- **Open Decisions:**
  - Whether to move Offline Music Player from `raw` → `developing` (user said "not now")
  - SwiftCart 8-week MVP execution (pending user return)

## Key Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-05-19 | Agency-first GTM for SwiftCart | Agencies already have clients and are frustrated with WooCommerce/Shopify. Free core + paid themes/plugins is the WordPress model. |
| 2026-05-19 | Core value prop = cheap hosting, not "zero deps" | User clarified: the real customer-facing benefit is running on ₹99/month shared hosting. "Zero dependencies" is just the mechanism. |

## Lessons Learned

- The user repeatedly refines toward simplicity and accessibility. When they clarify, listen — it's usually the real insight.
- "Lightweight" is a developer feature. "Saves you ₹1,500/month on hosting" is a business outcome. Always pitch the outcome.
- SwiftCart's competitive moat is not features — it's TCO (Total Cost of Ownership) for Indian small businesses.

- 

## Preferences

- 

## People & Relationships

- 

---

## SwiftCart Agency Go-To-Market Strategy — 2026-05-19

**Context:** User decided on an agency-first go-to-market for SwiftCart. Instead of selling directly to merchants, give the CMS for free to small digital marketing/web development agencies in India. Agencies earn from setup, customization, and maintenance. User earns from premium themes, plugins, and custom development.

**Key decisions recorded:**
- Target channel: Small Indian agencies (2–10 people) doing WooCommerce/Shopify work
- Core stays free forever. No "Pro" edition.
- Payment gateway plugins always free.
- One-time purchases for themes/plugins (Indian market hates subscriptions).
- 3-tier partner program: Member → Certified → Premium (10–15% commission).
- 8-week MVP sprint defined: DB+Auth → Products → Cart+Checkout → Payments → Installer.
- "Spreadsheet-to-catalogue import" remains the #1 killer feature.

**Research sources stored:** `research/market/2026-05-19-swiftcart-agency-go-to-market-research.md`
**Strategy doc stored:** `swiftcart/plans/2026-05-19-agency-go-to-market-strategy.md`

**Next actions when user returns:**
1. Execute the 8-week MVP sprint (starting with BaseModel.php)
2. Build demo store + agency pitch deck
3. Identify and approach 5 pilot agencies
4. Create 2 premium starter themes (fashion + electronics)

**User's exact words:** *"I have an idea, to finish this project as soon as possible and then approach some small Digital marketing companies and give them this product for free to implement for their clients, I can earn money by providing extra themes and creating custom themes for this CMS or plugin etc..."*

---

## SwiftCart Core Philosophy — 2026-05-19 (Clarified by User)

**The fundamental insight the user keeps coming back to:**

> When a small business sets up an eCommerce store, they are forced into one of two bad choices:
> 1. **WordPress + WooCommerce + 20 plugins** — heavy, slow, plugin conflicts, needs mid-range hosting
> 2. **OpenCart / Magento / Shopify** — either outdated, overkill, or expensive with lock-in
>
> **SwiftCart fixes this by being a truly lightweight eCommerce CMS with ZERO dependencies.**
> No Composer packages. No npm. No build step. No 3rd party plugins needed for basic functionality.
> Just pure PHP 8.2 + Alpine JS (or vanilla JS) + CSS.
>
> **The real win:** Because it's so light, a small business can run their entire store on the
> **cheapest shared hosting** (₹99–300/month) instead of being forced to upgrade to
> VPS/cloud hosting (₹1,000–5,000/month).
>
> This is not just about "no dependencies" as a developer preference — it's about
> **democratizing eCommerce for the smallest businesses** who can't afford server costs.

**Key phrases to use when pitching:**
- "Runs on ₹99/month hosting"
- "No plugin tax, no build step, no dependency hell"
- "Your store loads in under 500ms even on cheap shared hosting"
- "One afternoon to read the entire codebase"
- "No vendor lock-in — you own every file"

**This is the emotional hook for agencies:**
Tell their clients: *"We can build you a store that costs ₹99/month to host instead of ₹2,000/month — and it will be faster."*
