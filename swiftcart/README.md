# 🛒 SwiftCart — Lightweight Open-Source eCommerce CMS

> **Name:** SwiftCart  
> **Target:** Small businesses in India who outgrew WooCommerce but can't afford Shopify  
> **Status:** Developing — Foundation + Core MVC Complete  
> **Domain:** swiftcart.in

---

## What is SwiftCart?

**SwiftCart** is a **lightweight, open-source PHP 8.2 eCommerce CMS** built from scratch with **zero external dependencies** — no Composer, no npm, no build step. Designed for small businesses in India who need a fast, ownable, affordable online store.

**Core principle:** *"You own your store. You understand your store. Your store won't mysteriously break."*

---

## Live Codebase

Full development is happening in `../../swiftcartworkspace/SwiftCart/`:

```
SwiftCart/
├── core/                   ← Custom MVC framework (~800 lines)
│   ├── Autoloader.php      ← PSR-4 without Composer
│   ├── Router.php          ← Regex-based routing
│   ├── Request.php         ← HTTP request wrapper
│   ├── Response.php        ← HTML/JSON/Redirect builder
│   ├── View.php            ← Template renderer
│   ├── Config.php          ← Dot-notation config reader
│   ├── ErrorHandler.php    ← Debug page + logging
│   ├── helpers.php         ← Global helper functions
│   └── App.php             ← Application kernel
│
├── app/Controllers/        ← 10 controllers
├── app/Middleware/         ← CSRF, Auth, RateLimit
├── themes/default/         ← Storefront theme
│   ├── layouts/main.php    ← Master layout
│   ├── pages/*.php         ← 15+ page templates
│   └── partials/           ← Reusable components
│
├── admin/                  ← Admin panel (separate entry)
│   ├── views/pages/        ← 10 admin views
│   └── assets/             ← Custom CSS + JS
│
├── config/                 ← app.php + store.php
├── routes/                 ← web.php + api.php
└── public/                 ← Web root only
    ├── index.php           ← Front controller
    └── assets/             ← CSS + JS modules
```

---

## Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| Language | PHP 8.2 | Modern features, ubiquitous hosting |
| Framework | **Custom MVC** (no Laravel/Symfony) | Zero deps, total control, teaching vehicle |
| Database | MySQL 8.0+ / MariaDB 10.6+ | Standard on all shared hosting |
| Frontend | Vanilla JS + CSS | No build step, progressive enhancement |
| Templating | Native PHP + `e()` helper | No compile latency |
| Cache | File-based (built-in) | Works on ₹99 hosting |

---

## Key Features (Built)

### Custom PHP Framework
- ✅ PSR-4 Autoloader (zero Composer)
- ✅ Front Controller + `.htaccess` routing
- ✅ Config system with dot-notation
- ✅ Error handler with debug page
- ✅ Request/Response wrappers
- ✅ Regex router with named params
- ✅ View system with theme fallback
- ✅ Global helper functions

### Storefront
- ✅ Home, products, categories pages
- ✅ Product detail + category detail
- ✅ Cart + checkout + order confirmation
- ✅ Auth (login, register, forgot password)
- ✅ Account dashboard (orders, wishlist, addresses)
- ✅ Static pages (about, contact, FAQ, etc.)
- ✅ Newsletter subscription
- ✅ 10 vanilla JS modules (cart, modal, gallery, etc.)

### Admin Panel
- ✅ Login + logout
- ✅ Dashboard
- ✅ Products, catalog, orders, customers
- ✅ Analytics, marketing, extensions
- ✅ Components library
- ✅ Settings (general, themes)

---

## Artifacts

| Document | Purpose |
|----------|---------|
| [Main Idea](../ideas/developing/2026-05-16-swiftcart-lightweight-ecommerce-cms.md) | Full concept, problem, solution, revenue model |
| [Lean Canvas](docs/lean-canvas/2026-05-16-swiftcart-lean-canvas.md) | 9-box business model canvas |
| [System Architecture](diagrams/architecture/2026-05-16-swiftcart-system-architecture.mermaid.md) | Laravel-like custom framework architecture |
| [Request Lifecycle](diagrams/flow/2026-05-16-swiftcart-request-lifecycle.mermaid.md) | HTTP request path from browser to response |
| [MVP Plan](plans/mvp/2026-05-16-swiftcart-mvp-plan.md) | MoSCoW prioritization, user stories, launch checklist |

---

## Market Position

| Platform | Speed | Cost | Ownership | India-Native |
|----------|-------|------|-----------|--------------|
| **SwiftCart** | Fast | Free core | Full | ✅ GST, COD, Razorpay |
| WooCommerce | Slow | ₹15-40k/yr plugins | GPL | ❌ Plugin needed |
| Shopify | Fast | ₹8-40k/mo | None | ⚠️ 2% platform fee |
| OpenCart | Okay | Free | GPL v3 | ❌ Outdated |

**Beachhead:** ₹800–6,000/month hosting budget — ~2-3 million businesses in India.

---

## Revenue Model

| Tier | Description | Price |
|------|-------------|-------|
| **Core** | Full store functionality, MIT license | Free forever |
| **Themes** | Premium storefront themes | ₹1,500–4,000 (one-time) |
| **Plugins** | Premium utilities (SEO, bundles, etc.) | ₹800–2,500 (one-time) |
| **Gateways** | Razorpay, PayU, Stripe, Paytm | Always free |
| **Cloud** | Hosted version (v2+) | ₹399–1,999/mo |
| **Services** | Migrations, support, white-label | ₹15,000–2,00,000 |

**Hard Rule:** Never charge for payment gateway plugins. Never create a "Pro" edition.

---

## Next Steps

### This Week
- [ ] Build `BaseModel.php` — PDO wrapper with prepared statements
- [ ] Create migration system — ordered PHP scripts
- [ ] Implement session-based authentication

### This Month
- [ ] Product CRUD in admin with image uploads
- [ ] Cart functionality with session persistence
- [ ] Checkout flow with address management

### 3 Months
- [ ] Razorpay + COD payment integration
- [ ] GST-compliant invoice generation
- [ ] Admin dashboard with sales analytics

### 6 Months
- [ ] Plugin system with hooks and filters
- [ ] Theme marketplace
- [ ] Installer wizard
- [ ] v1.0.0 release

---

*Part of the [DreamBoard](../README.md) execution system.*
