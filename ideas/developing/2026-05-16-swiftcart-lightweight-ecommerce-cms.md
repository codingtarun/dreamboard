# SwiftCart — Lightweight Open-Source eCommerce CMS for Small Business

**Status:** developing
**Spark:** 🔥🔥🔥🔥🔥
**Created:** 2026-05-16
**Last Updated:** 2026-05-16
**Tags:** ecommerce, cms, php, opensource, india, small-business, saas, laravel-like, zero-dependencies, teaching-project
**Domain:** swiftcart.in

---

## The Spark

> *"Every small business owner I meet has the same story: they started on WooCommerce, added 20 plugins, got hacked, got slow, and then got a Shopify bill that eats their margin. What if there was a platform that was actually readable, actually fast on cheap hosting, and actually free without crippleware?"*

**SwiftCart** is a **lightweight, open-source PHP 8.2 eCommerce CMS** built from scratch with **zero external dependencies** — no Composer, no npm, no build step. Designed specifically for small businesses in India who outgrow WooCommerce's complexity but can't afford Shopify's fees.

The project is also a **teaching vehicle** — every line of code is explainable to an intermediate PHP developer learning modern patterns.

---

## What Exists Today (In Development — Phase 1-2)

### Custom PHP Framework (Built From Scratch)

| Component | Status | Details |
|-----------|--------|---------|
| **PSR-4 Autoloader** | ✅ Built | Zero Composer — custom `spl_autoload_register` |
| **Front Controller** | ✅ Built | `public/index.php` + `.htaccess` rewrite |
| **Config System** | ✅ Built | Dot-notation config reader with file caching |
| **Error Handler** | ✅ Built | Catches errors, exceptions, fatal shutdowns; dark debug page |
| **Request Object** | ✅ Built | Wraps `$_GET`, `$_POST`, `$_SERVER`, JSON body, route params |
| **Response Object** | ✅ Built | HTML, JSON, redirects with clean headers |
| **Router** | ✅ Built | Regex pattern matching with named capture groups `{slug}` |
| **View System** | ✅ Built | Template renderer with theme fallback + layout inheritance |
| **BaseController** | ✅ Built | `$this->view()`, `$this->redirect()`, `$this->json()` |
| **Helpers** | ✅ Built | `e()`, `url()`, `money()`, `dd()` globals |
| **App Bootstrap** | ✅ Built | Full request lifecycle: `App::run()` → Router → Controller → View |

### Storefront (Phase 3 Started)

| Page | Status | Template |
|------|--------|----------|
| **Home** | ✅ Built | `themes/default/pages/home.php` |
| **Product List** | ✅ Built | `themes/default/pages/products.php` |
| **Product Detail** | ✅ Built | `themes/default/pages/product.php` |
| **Category List** | ✅ Built | `themes/default/pages/categories.php` |
| **Category Detail** | ✅ Built | `themes/default/pages/category.php` |
| **Cart** | ✅ Built | `themes/default/pages/cart.php` |
| **Checkout** | ✅ Built | `themes/default/pages/checkout.php` |
| **Order Confirmation** | ✅ Built | `themes/default/pages/order-confirmation.php` |
| **Auth (Login/Register)** | ✅ Built | Login, register, forgot-password |
| **Account Dashboard** | ✅ Built | Orders, wishlist, addresses, returns |
| **Static Pages** | ✅ Built | About, contact, FAQ, shipping, returns, privacy, terms, sitemap |
| **Newsletter** | ✅ Built | Subscribe endpoint |

**JS Modules (Vanilla JS, no build step):**
- Cart module (add/remove/update quantities)
- Mobile navigation
- Form validation
- Modal system
- FAQ accordion
- Gallery/lightbox
- Listing filters
- Page loader
- Announcement bar
- Newsletter signup

### Admin Panel (Phase 4 Started)

| Section | Status | Views |
|---------|--------|-------|
| **Admin Login** | ✅ Built | `admin/views/pages/login.php` |
| **Dashboard** | ✅ Built | `admin/views/pages/dashboard.php` |
| **Products** | ✅ Built | `admin/views/pages/products.php` |
| **Catalog** | ✅ Built | `admin/views/pages/catalog.php` |
| **Orders** | ✅ Built | `admin/views/pages/orders.php` |
| **Customers** | ✅ Built | `admin/views/pages/customers.php` |
| **Analytics** | ✅ Built | `admin/views/pages/analytics.php` |
| **Marketing** | ✅ Built | `admin/views/pages/marketing.php` |
| **Extensions** | ✅ Built | `admin/views/pages/extensions.php` |
| **Components Library** | ✅ Built | `admin/views/pages/components.php` + `components/library.php` |
| **Settings** | ✅ Built | General, themes |

**Admin Assets:** Custom CSS + JS (charts.js for analytics, no external UI library)

### Architecture & Design System

- **Database Schema:** Full schema designed (MySQL 8.0+) — users, categories, products, orders, order_items, carts, cart_items, addresses, coupons, reviews, pages, menus, settings, sessions
- **Theme System:** `theme.json` manifest, layout inheritance, component partials
- **Asset Pipeline:** CSS/JS served from `public/assets/` — no build step
- **Security Model:** CSRF tokens, bcrypt passwords, PDO prepared statements, public/ isolation
- **Performance Budget:** TTFB <200ms, full page <500ms, cart update <100ms

---

## The Problem

Small business owners in India face a **trilemma** when choosing eCommerce:

| Platform | Speed | Cost | Ownership |
|----------|-------|------|-----------|
| **WooCommerce** | Slow on cheap hosting | Free core, ₹15-40k/year plugins | WordPress dependency, hacked easily |
| **Shopify** | Fast | ₹8-40k/month + 2% platform fee | Locked in, can't customise deep |
| **OpenCart** | Okay | Free, but extensions expensive | 2010 PHP codebase, museum quality |
| **PrestaShop** | Slow | €70-300/module | Smarty + heavy hooks = bad performance |
| **Magento** | Fast if tuned | ₹50L+ implementation | Requires dev team |

**Top 10 store-owner complaints:**
1. "My store got slower the more I added."
2. "Plugin renewals cost more than hosting."
3. "An update broke my store."
4. "I can't customise X and I don't know why."
5. "I get charged even on failed orders."
6. "Checkout confuses my customers."
7. "I can't export my data without losing something."
8. "Admin is slower than the store."
9. "Gateway fees are invisible until checkout."
10. "I need a developer for things that should be settings."

**Top 10 developer complaints:**
1. "I'm a plugin stitcher, not a developer."
2. "Client updated WP, now I'm on an unpaid emergency call."
3. "I can't sell the same theme twice without rebuilding."
4. "No recurring revenue path from these platforms."
5. "I want a codebase I'd be proud to show a senior engineer."

---

## The Solution

**SwiftCart** — "The readable commerce platform, born in India, built for the real world of small business."

### Core Principles (Never Compromised)

1. **Zero external dependencies** — No Composer, no npm, no build step
2. **PHP renders, JS enhances** — Progressive enhancement always
3. **Runs on ₹99/month shared hosting** — Performance-first
4. **MIT licensed** — Open source core, commercial ecosystem on top
5. **Secure by default** — CSRF, PDO prepared statements, bcrypt, public/ isolation
6. **Readable codebase** — Every file explainable to an intermediate developer

### Key Differentiators

| Feature | SwiftCart | WooCommerce | Shopify |
|---------|-----------|-------------|---------|
| Dependencies | **Zero** | Composer + npm | Closed source |
| Hosting cost | **₹99/mo** | ₹499-999/mo | ₹2,000-15,000/mo |
| Plugin costs | **One-time** | Recurring | Recurring |
| Code ownership | **Full** | GPL | None |
| GST/HSN out-of-box | **Yes** | Plugin needed | Limited |
| Indian gateways | **Free** | Paid plugins | Transaction fees |
| Code readability | **800-line core** | 50K+ files | Black box |
| Setup time | **10 minutes** | 2-4 hours | 15 minutes |

### The Core Philosophy (User's Words)

> *"What if we have a lightweight ecommerce CMS with no dependencies, no 3rd party plugins, no npm — just pure PHP + JS + CSS? The user can run it on the cheapest shared hosting instead of being forced into mid-range servers. That's the whole point."*
>
> **This is not about developer preferences. This is about democratizing eCommerce for the smallest businesses who can't afford server costs.**
>
> A store owner paying ₹99/month for hosting should still have a fast, beautiful, fully-functional online store. SwiftCart makes that possible.

---

## Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| Language | PHP 8.2 | `strict_types`, modern features, ubiquitous hosting |
| Framework | **Custom MVC** (no Laravel/Symfony) | Teaching vehicle; zero deps; total control |
| Database | MySQL 8.0+ / MariaDB 10.6+ | Standard on all shared hosting |
| Frontend | Vanilla JS + CSS | No build step; progressive enhancement |
| Templating | Native PHP + `e()` helper | No Twig/Smarty compile latency |
| Session | File-based + cookie flags | Works everywhere |
| Cache | File cache (built-in) | No Redis dependency on cheap hosting |
| Assets | Direct CSS/JS files | No Vite/Webpack complexity |

### Custom Core (No Framework)

```
core/
├── Autoloader.php      ← PSR-4 autoloading without Composer
├── bootstrap.php       ← Boot sequence
├── Config.php          ← Dot-notation config reader
├── ErrorHandler.php    ← Debug page + logging
├── helpers.php         ← Global helper functions
├── Request.php         ← HTTP request wrapper
├── Response.php        ← HTTP response builder
├── Router.php          ← Regex-based routing
├── View.php            ← Template renderer
└── App.php             ← Application kernel
```

**Total core: ~800 lines of PHP.** A senior developer can read and understand the entire framework in one afternoon.

---

## Market Opportunity

| Segment | Monthly Spend | Current Platform | SwiftCart Fit |
|---------|--------------|------------------|---------------|
| Hobby | ₹200-600 | Free Woo + cheap hosting | ✅ Better performance, zero plugin tax |
| Serious small | ₹800-2,500 | Woo + Elementor OR Shopify Lite | ✅ One-time costs, no recurring fees |
| Growing small | ₹2,500-6,000 | Shopify Basic OR Woo + paid plugins | ✅ India-native, GST ready, readable |
| Established | ₹6,000-20,000 | Shopify Standard + apps | ✅ Customisable, data ownership |

**Beachhead:** ₹800–6,000 tier — ~2-3 million businesses in India. Too big for free WooCommerce, too small for Shopify Basic plus apps.

---

## Revenue Model (Post-Launch)

### Tier 1 — Free Core (MIT License)
- Full store functionality: catalogue, cart, checkout, orders, GST tax, coupons, accounts, shipping, COD
- One starter theme, plugin system, installer, admin, basic analytics
- **A real store can run on free core forever**

### Tier 2 — One-Time Paid Themes & Plugins
- Premium themes: ₹1,500–4,000 (lifetime for major version)
- Premium plugins: ₹800–2,500 (invoice PDF, abandoned cart, advanced shipping, SEO toolkit, bundle builder)
- **Payment gateway plugins: ALWAYS FREE** (Razorpay, PayU, Stripe, Paytm, PhonePe)

### Tier 3 — Recurring Services
- SwiftCart Cloud (hosted): ₹399 / ₹899 / ₹1,999 monthly
- Migration services: ₹15,000–40,000 per store
- Certified partner directory: ₹2,000–5,000/year
- Priority support: ₹1,000–3,000/month
- White-label for agencies: ₹50,000–2,00,000/year

**GST HSN Plugin** = the killer niche premium plugin. No existing open-source platform does GST-compliant invoicing with HSN codes, e-invoicing thresholds, and inter-state correctness properly for India.

---

## Development Phases

| Phase | Description | Status |
|---|---|---|
| 1 | Foundation — autoloader, bootstrap, helpers, error handler | ✅ Complete |
| 2 | Core MVC — Router, Request, Response, Controllers, Views | ✅ Complete |
| 3 | Storefront — default theme, pages, partials, JS modules | 🔄 In Progress |
| 4 | Admin Panel — dashboard, product/order/customer manager | 🔄 In Progress |
| 5 | Database & Models — PDO, BaseModel, migrations | ⏳ Next |
| 6 | Payments & Orders — Stripe, Razorpay, COD, email, invoices | ⏳ Pending |
| 7 | Plugin & Theme System — hooks, plugin loader, theme override | ⏳ Pending |
| 8 | Installer — web wizard, requirements checker, migrations | ⏳ Pending |
| 9 | Polish & Launch — docs, Docker, CI, security audit, v1.0.0 | ⏳ Pending |

---

## Key Metrics

| Metric | Current | Target (MVP Launch) |
|--------|---------|---------------------|
| Core PHP files | ~15 | ~25 |
| Core lines of code | ~800 | ~1,500 |
| Storefront pages | 15+ | 20+ |
| Admin pages | 10+ | 15+ |
| JS modules | 10 | 15 |
| Controllers | 10 | 15 |
| Database tables | 0 (schema designed) | 15+ |
| Test coverage | 0% | 70%+ |

---

## Potential Obstacles

1. **Single developer bandwidth** — Learning project = slower than a team
2. **Ecosystem gap** — No plugin marketplace yet; early adopters get less
3. **Trust building** — "Custom framework" sounds risky to developers
4. **Shopify's convenience** — 15-min setup vs. 10-min self-hosted setup is close
5. **Hosting knowledge gap** — Small business owners fear server management
6. **Payment gateway complexity** — Webhook handling, idempotency, retries
7. **SEO parity** — WooCommerce has 15 years of SEO plugin evolution

---

## Next Steps

### Immediate (This Week)
- [ ] Build `BaseModel.php` — PDO wrapper with prepared statements
- [ ] Create migration system — ordered PHP scripts, not SQL files
- [ ] Implement user authentication (session-based, bcrypt)
- [ ] Wire admin login to real database

### Short Term (This Month)
- [ ] Product CRUD in admin with image uploads
- [ ] Category tree management
- [ ] Cart functionality with session persistence
- [ ] Checkout flow with address management

### Medium Term (3 Months)
- [ ] Razorpay + COD payment integration
- [ ] Order management + email notifications
- [ ] GST-compliant invoice generation
- [ ] Admin dashboard with sales analytics

### Long Term (6-12 Months)
- [ ] Plugin system with hooks and filters
- [ ] Theme marketplace
- [ ] Installer wizard
- [ ] Docker + GitHub Actions CI
- [ ] v1.0.0 release on GitHub

---

## Related Artifacts

- [Lean Canvas](../swiftcart/docs/lean-canvas/2026-05-16-swiftcart-lean-canvas.md)
- [System Architecture](../swiftcart/diagrams/architecture/2026-05-16-swiftcart-system-architecture.mermaid.md)
- [Request Lifecycle](../swiftcart/diagrams/flow/2026-05-16-swiftcart-request-lifecycle.mermaid.md)
- [MVP Plan](../swiftcart/plans/mvp/2026-05-16-swiftcart-mvp-plan.md)
- [Agency Go-To-Market Strategy](../swiftcart/plans/2026-05-19-agency-go-to-market-strategy.md)
- [Agency Go-To-Market Research](../research/market/2026-05-19-swiftcart-agency-go-to-market-research.md)

---

## Notes Log

- **2026-05-16** — Added to DreamBoard as developing. Foundation (Phase 1) and Core MVC (Phase 2) complete. Storefront templates and admin panel views built. Next critical milestone: database layer + models.
- **2026-05-19** — Agency-first go-to-market strategy defined. Research validates: Indian agencies are frustrated with WooCommerce maintenance and Shopify fees. Decision: sell through agencies (free core + theme/plugin marketplace), not direct to merchants. 8-week MVP sprint + 90-day agency onboarding plan created.
