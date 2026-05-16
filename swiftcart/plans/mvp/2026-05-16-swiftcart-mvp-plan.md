# MVP Plan: SwiftCart — Lightweight Open-Source eCommerce CMS

**Idea:** [SwiftCart — Lightweight Open-Source eCommerce CMS](../../ideas/developing/2026-05-16-swiftcart-lightweight-ecommerce-cms.md)
**Date:** 2026-05-16
**Status:** Foundation + Core MVC Complete
**Target Launch:** 4-6 months
**Realistic Timeline:** 12-18 months (nights/weekends)

---

## Executive Summary

SwiftCart's MVP is a **self-hosted PHP 8.2 eCommerce store** that a small business can install in 10 minutes, load products via spreadsheet import, and start selling with Razorpay or COD. The custom MVC framework is complete; the next milestones are database layer, payment integration, and installer.

---

## MoSCoW Prioritization

### 🔴 Must Have (MVP Launch Blockers)

| # | Feature | Status | Effort | Notes |
|---|---------|--------|--------|-------|
| 1 | **Custom MVC Framework** | ✅ Complete | — | Autoloader, Router, Request, Response, View, Config, ErrorHandler |
| 2 | **Storefront Pages** | ✅ Complete | — | Home, products, categories, cart, checkout, auth, account, static |
| 3 | **Admin Panel UI** | ✅ Complete | — | Login, dashboard, products, orders, customers, settings views |
| 4 | **Database Layer** | 🔄 Next | 1 week | BaseModel + PDO + migrations |
| 5 | **User Auth** | 🔄 Next | 3 days | Registration, login, logout, sessions, bcrypt |
| 6 | **Product CRUD** | ⏳ Pending | 3 days | Admin: add/edit/delete products with images |
| 7 | **Category Management** | ⏳ Pending | 2 days | Nested categories, tree view |
| 8 | **Cart System** | ⏳ Pending | 3 days | Session-based cart, add/remove/update qty |
| 9 | **Checkout Flow** | ⏳ Pending | 4 days | Address, shipping, order summary |
| 10 | **Razorpay Integration** | ⏳ Pending | 3 days | Payment, webhook, idempotency |
| 11 | **COD Support** | ⏳ Pending | 1 day | Cash on delivery option |
| 12 | **Order Management** | ⏳ Pending | 3 days | Admin order list, status updates, email notifications |
| 13 | **GST-Compliant Invoicing** | ⏳ Pending | 4 days | HSN codes, inter/intra-state, correct rounding |
| 14 | **Installer Wizard** | ⏳ Pending | 1 week | Web-based setup, requirements check, DB creation |
| 15 | **Spreadsheet Import** | ⏳ Pending | 3 days | CSV/XLSX product import with variants + images |

### 🟡 Should Have (Post-MVP, Month 2-3)

| # | Feature | Status | Effort |
|---|---------|--------|--------|
| 16 | **Theme System** | 🔄 Partial | 1 week | Theme.json, override fallback, custom themes |
| 17 | **Coupon/Discount System** | ⏳ Pending | 3 days |
| 18 | **Customer Reviews** | ⏳ Pending | 2 days |
| 19 | **Wishlist** | ⏳ Pending | 2 days |
| 20 | **SEO Toolkit** | ⏳ Pending | 3 days | Meta tags, sitemap, structured data |
| 21 | **Basic Analytics** | 🔄 Partial | 2 days | Sales chart, top products |
| 22 | **Email Notifications** | ⏳ Pending | 3 days | Order confirmations, shipping |
| 23 | **Multi-language (HI)** | ⏳ Pending | 1 week | Hindi UI + content |

### 🟢 Could Have (Month 4-6)

| # | Feature | Status | Effort |
|---|---------|--------|--------|
| 24 | **Plugin System** | ⏳ Pending | 2 weeks | Hooks, filters, plugin loader |
| 25 | **Theme Marketplace** | ⏳ Pending | 2 weeks |
| 26 | **Abandoned Cart Recovery** | ⏳ Pending | 3 days |
| 27 | **Advanced Shipping** | ⏳ Pending | 3 days | Pincode-based, weight-based, free threshold |
| 28 | **Inventory Management** | ⏳ Pending | 3 days | Stock alerts, low-stock notifications |
| 29 | **Multi-vendor (Phase 2)** | ⏳ Pending | 1 month |
| 30 | **SwiftCart Cloud** | ⏳ Pending | 2 months | Hosted version, one-click export |

### ⚫ Won't Have (Post-PMF)

| # | Feature | Reason |
|---|---------|--------|
| 31 | **Multi-currency** | India-first; add after local dominance |
| 32 | **Subscription billing** | Complex; plugin territory |
| 33 | **POS integration** | Hardware-dependent; enterprise feature |
| 34 | **AI product recommendations** | Overkill for MVP; plugin later |

---

## User Stories (MVP)

### As a Store Owner
- [ ] I can install SwiftCart in 10 minutes without terminal access
- [ ] I can import my products from a spreadsheet on the first try
- [ ] I can add/edit products with images in the admin panel
- [ ] I can accept payments via Razorpay and COD
- [ ] I can view orders and update their status
- [ ] I can generate GST-compliant invoices automatically
- [ ] I can customize my store's logo and colors
- [ ] I can view basic sales analytics

### As a Customer
- [ ] I can browse products by category
- [ ] I can add products to cart and checkout
- [ ] I can pay via Razorpay (card/UPI/netbanking) or COD
- [ ] I receive email confirmation after placing an order
- [ ] I can track my order status

### As a Developer
- [ ] I can read and understand the entire framework in one afternoon
- [ ] I can create a custom theme by overriding default files
- [ ] I can fix bugs without Composer/npm dependency hell
- [ ] I can sell a premium theme without GPL viral licensing

---

## The Unglamorous Killer Feature

**Spreadsheet-to-catalogue import that works on the first try** — including variants and images referenced by filename from a zip.

Every platform has CSV import; every single one is broken in some way. Getting this right makes the product sell itself. It's the #1 requested feature in migration projects and the biggest time-saver for store setup.

**Priority:** Above drag-drop page builders, above AI features, above social integrations.

---

## Technical Debt to Clear Before Launch

| Item | Priority | Effort | Impact |
|------|----------|--------|--------|
| Write BaseModel + PDO layer | Critical | 1 week | Blocks all data features |
| Create migration system | Critical | 3 days | Database schema versioning |
| CSRF protection on all forms | Critical | 2 days | Security |
| Input sanitization | High | 2 days | Security |
| File upload validation | High | 1 day | Security |
| PHPUnit test suite | High | 1 week | Prevents regressions |
| Error logging to file | Medium | 1 day | Debugging |
| Rate limiting | Medium | 1 day | Security |
| Docker setup | Low | 2 days | Dev onboarding |

---

## Beta Testing Plan

### Phase 1: Dogfood (Week 1-2)
- Build a real store for a friend's business
- Use the spreadsheet import for their actual products
- Document every friction point

### Phase 2: Developer Friends (Week 3-4)
- 5 PHP developers install and review the codebase
- Focus: readability, bug reports, feature gaps
- Feedback channel: GitHub issues

### Phase 3: Real Stores (Week 5-8)
- 3 small businesses migrate from WooCommerce
- Free migration + setup assistance
- Focus: installer experience, payment flow, admin usability

### Phase 4: Open Beta (Week 9-12)
- GitHub release + Reddit/IndieHackers announcement
- Target: 50 real installs
- Focus: stability, documentation gaps, community feedback

---

## Success Metrics (MVP)

| Metric | Target | Measurement |
|--------|--------|-------------|
| GitHub Stars | 500+ | GitHub API |
| Installs (tracked) | 50+ | Installer ping (opt-in) |
| Active Stores (30d) | 20+ | Admin dashboard analytics |
| Theme/Plugin Sales | 10+ | Gumroad/Stripe |
| Average Install Time | <10 min | Installer logs |
| Spreadsheet Import Success | 90%+ | Import logs |
| NPS (Developers) | 50+ | GitHub discussions survey |
| Critical Bugs (open) | 0 | GitHub issues |

---

## Launch Checklist

- [ ] All Must-Haves complete and tested
- [ ] Installer wizard tested on 3 different hosting providers
- [ ] Spreadsheet import tested with 5 real product catalogs
- [ ] Razorpay webhooks handling idempotency correctly
- [ ] GST invoice format validated by 2 accountants
- [ ] Documentation complete (install, theme dev, plugin dev)
- [ ] GitHub repo public with README, LICENSE (MIT), CONTRIBUTING
- [ ] Demo store live with sample data
- [ ] 1 premium theme + 1 premium plugin ready for sale
- [ ] Pricing page live (free core + paid ecosystem)
- [ ] Community channel ready (Discord / GitHub Discussions)

---

## Timeline

```
Month 1:   Database layer + models + auth + product CRUD
Month 2:   Cart + checkout + Razorpay + COD + orders
Month 3:   GST invoicing + email + installer + spreadsheet import
Month 4:   Polish + testing + docs + beta with real stores
Month 5:   Theme system + first premium theme + plugin system
Month 6:   Plugin marketplace + community + v1.0.0 release
```

---

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| "Custom framework" scares developers | High | High | Publish core file walkthrough videos; prove readability |
| Solo dev burnout | Medium | Critical | Scope discipline; community contributions |
| WooCommerce ecosystem too strong | Medium | Medium | Target the "I outgrew Woo" segment specifically |
| Shopify launches cheaper India plan | Low | High | Differentiate on ownership + readability |
| Payment gateway API changes | Medium | Medium | Gateway plugins always free + community-maintained |
| No plugin ecosystem at launch | High | Medium | Ship with 5 essential plugins built-in |
| Hosting support gaps | Medium | Medium | Test on GoDaddy, Hostinger, Bluehost India |

---

## Hard Rules (Never Break)

1. **No "SwiftCart Pro" edition** — Free core must run a real store forever
2. **Never charge for payment gateway plugins** — #1 OpenCart complaint
3. **One-time purchases for themes/plugins** — No subscriptions for Tier 2
4. **No publisher fee for third-party marketplace** — Curate, don't tollgate
5. **Core must stay readable** — Every file explainable to an intermediate dev

---

*Part of the [DreamBoard MVP Planning System](../../../templates/mvp-template.md).*
