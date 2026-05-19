# SwiftCart Agency Go-To-Market Strategy

**Idea:** [SwiftCart — Lightweight Open-Source eCommerce CMS](../../ideas/developing/2026-05-16-swiftcart-lightweight-ecommerce-cms.md)  
**Date:** 2026-05-19  
**Status:** Strategy Document — Ready for Execution  
**Research:** [Agency Go-To-Market Research](../../research/market/2026-05-19-swiftcart-agency-go-to-market-research.md)

---

## The Core Insight

> **Don't sell to store owners. Sell to the agencies that build stores for them.**

Small digital marketing and web development agencies in India are your perfect channel. They already have clients, already build eCommerce sites, and are already frustrated with WooCommerce's maintenance burden and Shopify's fees. Give them SwiftCart for free — let them earn from setup, customization, and maintenance. You earn from themes, plugins, and services.

This is the **WordPress model** applied to Indian eCommerce.

---

## Why Agencies Will Say Yes

### Their Current Pain (Validated by Research)

| With WooCommerce | With Shopify |
|---|---|
| Plugin conflicts break client sites | 2% transaction fee ON TOP of gateway fees in India |
| Constant update cycle = unpaid emergency calls | App costs stack to Rs. 3,000–8,000/mo |
| Hidden TCO of Rs. 2–5 lakhs over 24 months | Checkout is locked unless you pay Rs. 1.65L/mo for Plus |
| No recurring revenue from "free" platform | Vendor lock-in — can't migrate easily |
| Client blames agency for platform limits | No true white-label possible |

### What You Offer Them

1. **A platform they can truly white-label** — their clients never see "SwiftCart" if they don't want to
2. **Zero transaction fees** — they can undercut Shopify on TCO by 30–50%
3. **GST, Razorpay, COD native** — no app stacking, no monthly app bills
4. **Readable codebase** — their junior devs can fix things without calling you
5. **Recurring revenue path** — maintenance retainers + your partner commissions
6. **Differentiation** — "We have our own platform" vs. "We use Shopify like everyone else"

---

## The Finish-It-Fast Plan

### Reality Check

Your storefront templates and admin UI are **already built**. What's missing is the *engine* underneath. You don't need to rebuild everything — you need to wire the existing views to real data.

### Aggressive 8-Week Sprint to MVP

#### Week 1–2: Database + Auth (The Foundation)
- [ ] `BaseModel.php` — PDO wrapper with query builder, prepared statements
- [ ] Migration system — ordered PHP scripts (`migrations/001_create_users.php` etc.)
- [ ] Session auth — register, login, logout, bcrypt, remember-me
- [ ] Wire admin login to real database
- [ ] Create all tables from your designed schema

**Why this first:** Everything else depends on this. No shortcuts.

#### Week 3–4: Product + Category CRUD
- [ ] Admin: Add/edit/delete products with image uploads (MIME check, random filename)
- [ ] Admin: Category tree management (nested set or adjacency list)
- [ ] Storefront: Wire product list, product detail, category pages to real DB
- [ ] Search + filters on product listing

#### Week 5–6: Cart + Checkout
- [ ] Session-based cart (add, remove, update qty)
- [ ] Checkout flow: address → shipping → order summary
- [ ] Guest checkout + registered user checkout
- [ ] Order creation + order items in DB
- [ ] Admin: Order list, status updates, order detail view

#### Week 7: Payments (The India-Killer Feature)
- [ ] **Cash on Delivery (COD)** — 1 day, native core
- [ ] **Razorpay integration** — payment, webhook, idempotency key handling
- [ ] Order status flow: Pending → Paid → Processing → Shipped → Delivered
- [ ] Email notifications: order confirmation (simple PHP `mail()` or PHPMailer)

#### Week 8: Installer + Polish
- [ ] Web-based installer wizard: requirements check, DB setup, admin account creation
- [ ] GST invoice generation (basic HSN, inter/intra-state tax calc)
- [ ] Input sanitization + CSRF on all forms
- [ ] File upload validation
- [ ] Error logging to file

**At the end of Week 8, you have a store that can sell products.**

### Post-MVP (Month 3): Agency-Readiness
- [ ] Spreadsheet import (your killer feature) — CSV/XLSX with variants + images
- [ ] Coupon/discount system
- [ ] Basic SEO toolkit (meta tags, sitemap)
- [ ] Email notifications (shipping, order status)
- [ ] Customer reviews
- [ ] Wishlist

---

## The Agency Partner Program

### 3-Tier Structure (Copied from Webflow — Proven Model)

| Tier | Requirements | What They Get | Your Commission to Them |
|------|-------------|---------------|------------------------|
| **Member** (Free) | Sign up, agree to terms | Docs, community access, demo store | 5% on themes/plugins they sell |
| **Certified** | Built 2+ client sites, pass assessment | Directory listing, partner badge, 10% commission, priority support | 10% on all marketplace sales they drive |
| **Premium** | Rs. 50,000+ ARR referred, 5+ sites | Co-marketing, featured directory, 15% commission, dedicated Slack | 15% on all sales + white-label rights |

### Partner Benefits You Offer

1. **Free core forever** — they never pay to use SwiftCart
2. **White-label license** — they can rebrand admin, remove SwiftCart branding
3. **Demo stores** — pre-built demo they can show clients in 10 minutes
4. **Sales deck** — co-branded PPT they can use in client pitches
5. **Commission on ecosystem** — they earn when clients buy themes/plugins
6. **No platform fees** — unlike Shopify, you don't take a cut of sales

### Revenue Share Mechanics

Agency builds store for Client X using SwiftCart.
Client X buys Premium Theme from you: Rs. 5,000
→ Agency gets 10–15% = Rs. 500–750

Client X buys 3 plugins: Rs. 6,000 total
→ Agency gets 10–15% = Rs. 600–900

Client X pays Agency monthly maintenance: Rs. 8,000/mo
→ Agency keeps 100% (your platform is free)

**The agency wins twice:** they charge for the build + maintenance, AND they earn passive income from your marketplace.

---

## Your Revenue Model

### Stream 1: Premium Themes (Primary)

| Theme Type | Price | Target |
|---|---|---|
| Starter (fashion, electronics, grocery) | Rs. 1,500–3,000 | First-time store owners |
| Professional (high-conversion, mobile-first) | Rs. 5,000–10,000 | Growing businesses |
| Custom theme development (by you) | Rs. 25,000–75,000 | Agency referrals |

**Why themes first:** Every agency needs multiple themes. One theme can sell 100+ times. Build 5 good themes = Rs. 5–10L potential.

### Stream 2: Premium Plugins

| Plugin | Price | Why Agencies Buy It |
|---|---|---|
| Advanced SEO Toolkit | Rs. 1,500 | Meta templates, schema markup, sitemap automation |
| Abandoned Cart Recovery | Rs. 2,000 | Email sequences, WhatsApp notifications |
| Advanced Shipping | Rs. 1,500 | Pincode-based rates, weight-based, free threshold |
| Bundle Builder | Rs. 2,500 | Product bundles, "frequently bought together" |
| Multi-language (Hindi, Gujarati, etc.) | Rs. 2,000 | Regional stores |
| GST Advanced | Rs. 3,000 | E-invoicing, GSTR reports, automated filing prep |

**Rule:** Payment gateway plugins (Razorpay, PayU, Stripe, PhonePe) are **always free**.

### Stream 3: Custom Development

When agencies need something bespoke, you build it:
- Custom theme: Rs. 30,000–2,50,000
- Custom plugin: Rs. 15,000–1,00,000
- Migration from WooCommerce: Rs. 50,000–2,00,000

### Stream 4: Support Contracts (Future)

Once you have 10+ agency partners:
- Priority support for partners: Rs. 2,000–5,000/month
- Partner directory listing fee: Rs. 3,600/year

### Stream 5: SwiftCart Cloud (Year 2)

Hosted, white-label version agencies can resell:
- Starter: Rs. 399/month (they charge client Rs. 799, keep Rs. 400)
- Business: Rs. 999/month (they charge client Rs. 1,999, keep Rs. 1,000)
- Agency Reseller: Rs. 4,999/month for unlimited stores

---

## How to Find and Approach Agencies

### Where They Are

1. **LinkedIn** — Search: "eCommerce developer India", "Shopify expert India", "WooCommerce agency Ahmedabad/Mumbai/Delhi"
2. **Instagram/Facebook** — Small agencies market heavily here
3. **JustDial / IndiaMART** — Search "website development" in your city
4. **Freelancer platforms** — Upwork, Fiverr Indian agencies doing WooCommerce work
5. **Local tech meetups** — PHP meetups, WordPress meetups

### The Pitch Sequence

#### Step 1: The Hook (LinkedIn DM / Email)

Subject: Are your clients paying Shopify's 2% fee + app costs?

Hi [Name],

I noticed [Agency Name] builds eCommerce stores for [industry].
Quick question: Are your clients happy with their monthly platform bills?

I built SwiftCart — an open-source eCommerce platform specifically
for Indian small businesses. Zero transaction fees, GST + Razorpay
native, and agencies keep 100% of maintenance revenue.

No platform cuts into your margins.

Worth a 15-min call? I can show you a live demo.

[Your name]

#### Step 2: The Demo (15-Minute Call)

1. **Share screen** → Open your demo store
2. **Show admin** → "This is what your clients will see. Clean, fast, no branding."
3. **Show TCO comparison** → "Your client pays Rs. 0 platform fee vs. Shopify's 2% + apps"
4. **Show white-label** → "You can rebrand this as [Agency Name] Commerce"
5. **Close** → "Want me to set up a sandbox for your team to play with?"

#### Step 3: The Sandbox

Give them:
- A live test store (subdomain: `agencyname.swiftcart.in`)
- Admin login
- A 1-page "Getting Started" guide
- Your WhatsApp number for questions

#### Step 4: The First Client

Offer to **co-build the first client store together**:
- You handle technical setup
- They handle client relationship + design
- Split revenue 50/50 on the build
- They keep 100% of maintenance

This removes their risk completely.

---

## The 90-Day Launch Timeline

```
Week 1–4:   FINISH MVP (database → auth → products → cart → checkout)
Week 5–6:   Payments + installer + GST invoices
Week 7–8:   Polish + bug fixes + spreadsheet import
Week 9:     Build 2 premium themes (fashion + electronics)
Week 10:    Build demo store + agency pitch deck + partner page
Week 11:    Reach out to 20 agencies (LinkedIn + email)
Week 12:    Onboard first 3 pilot partners + build their first stores
Month 4–6:  Launch marketplace with 5 themes + 5 plugins
Month 6–9:  Scale to 20+ agency partners + certification program
Month 9–12: Launch SwiftCart Cloud (white-label hosting)
```

---

## What You Need to Build for Agencies

### Immediate (Before First Pitch)

| Asset | Why It Matters | Effort |
|---|---|---|
| **Live demo store** | Agencies need to see and touch | 2–3 days |
| **Admin demo login** | They need to show clients the backend | Included above |
| **1-page TCO comparison** | "Why SwiftCart vs. Shopify/WooCommerce" | 1 day |
| **Agency pitch deck (10 slides)** | They can use it in client pitches | 2–3 days |
| **Getting Started guide** | How to install, theme, deploy | 2–3 days |

### Short-Term (Month 2–3)

| Asset | Why It Matters | Effort |
|---|---|---|
| **Theme development guide** | Agencies will want custom themes | 3–5 days |
| **Plugin development guide** | Eventually they'll build their own | 3–5 days |
| **Partner portal** (simple) | Track commissions, download resources | 1 week |
| **Certification quiz** | Creates social proof + quality filter | 2–3 days |

---

## The Numbers That Matter

### Agency Economics (Why This Works)

**Typical small agency in India:**
- Builds 2–4 eCommerce stores per month
- Charges Rs. 40,000–1,50,000 per store
- Has 10–20 active maintenance clients at Rs. 5,000–15,000/mo

**With SwiftCart instead of WooCommerce/Shopify:**
- Lower setup time (your installer + spreadsheet import)
- Lower maintenance burden (no plugin conflicts, no core updates breaking things)
- Higher margins (no platform fees, no app costs passed to client)
- Recurring marketplace commissions (passive income for them)

### Your Economics (Why This Works for You)

| Milestone | Agencies | Monthly Theme/Plugin Sales | Your Monthly Revenue |
|---|---|---|---|
| Month 3 | 3 pilot | 5 sales x Rs. 2,500 avg | ~Rs. 12,500 |
| Month 6 | 10 partners | 30 sales x Rs. 2,500 avg | ~Rs. 75,000 |
| Month 12 | 25 partners | 100 sales x Rs. 2,500 avg | ~Rs. 2,50,000 |
| Month 18 | 50 partners | 250 sales x Rs. 2,500 avg | ~Rs. 6,25,000 |

**Note:** This is marketplace revenue ONLY. Add custom development, support contracts, and cloud hosting on top.

---

## Risks and Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Agencies don't want to learn a new platform | High | Offer to co-build first store free. Make onboarding frictionless. |
| Custom framework scares developers | Medium | Emphasize readability. Publish "Understand SwiftCart in 1 hour" guide. |
| No plugin ecosystem at launch | High | Ship with 5 essential plugins built-in. Build 5 yourself. |
| Support burden crushes you | Medium | Only offer priority support to Certified+ partners. Community for rest. |
| Pricing pressure from "free" alternatives | Medium | Compete on TCO + India-native features, not price alone. |
| Shopify launches cheaper India plan | Low | Differentiate on ownership + white-label + zero transaction fees. |

---

## The One-Sentence Pitch for Agencies

> **"Use SwiftCart — build stores faster, charge clients less in monthly fees, and keep 100% of your maintenance revenue. Plus earn commissions on themes and plugins."**

---

## Next Actions — What to Do Today

1. [ ] **Set a launch deadline.** Pick a date 8 weeks from now. Write it down.
2. [ ] **Block 2 hours every single day** for SwiftCart development. No exceptions.
3. [ ] **Start with BaseModel.php.** It's the foundation everything else sits on.
4. [ ] **Create a simple Trello/Notion board** with the 8-week sprint tasks.
5. [ ] **Identify 5 agencies in your city** doing WooCommerce work. Save their LinkedIn profiles.
6. [ ] **Prepare your demo environment.** You'll need a live store running by Week 6.

---

## Hard Rules (Never Break)

1. **Core stays free forever.** No "Pro" edition. No feature-gating.
2. **Payment gateway plugins always free.** #1 complaint against OpenCart.
3. **One-time purchases for themes/plugins.** Indian market hates subscriptions.
4. **Agencies keep 100% of build + maintenance fees.** You only earn from your marketplace.
5. **Every file stays readable.** Don't sacrifice simplicity for features.

---

*Part of the [SwiftCart Execution Plan](mvp/2026-05-16-swiftcart-mvp-plan.md).*
