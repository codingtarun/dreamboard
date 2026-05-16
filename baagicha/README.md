# 🍎 Baagicha — AI-Powered Apple Orchard Management Platform

> **Name:** बागीचा (Baagicha = "The Orchard")  
> **Target:** Himalayan apple farmers (Himachal Pradesh, Uttarakhand, J&K)  
> **Status:** Developing — Codebase 70% complete  
> **Domain:** baagicha.app

---

## What is Baagicha?

**Baagicha** is an intelligent agricultural management platform built specifically for **apple farmers in the Indian Himalayas**. It combines a React Native mobile app for farmers with a Laravel web backend + admin panel, powered by altitude-aware AI recommendations.

The name "Baagicha" (बाग़िचा) means "orchard" in Hindi, reflecting the platform's core purpose: empowering orchardists with modern technology.

---

## Live Codebase

Full development is happening in `../../baagichaworkspace/`:

```
baagichaworkspace/
├── web_baagicha/          ← Laravel 12 backend + admin panel
│   ├── app/Models/         ← 30+ Eloquent models
│   ├── app/Http/Controllers/Api/  ← REST API (v1)
│   ├── app/Http/Controllers/Admin/ ← Admin CRUD
│   ├── routes/api.php      ← 25+ API endpoints
│   ├── routes/web/admin/   ← Admin routes
│   └── resources/views/    ← Tailwind + AlpineJS admin
│
└── baagichaApp/           ← React Native 0.85 mobile app
    ├── src/screens/        ← 20+ screens
    ├── src/navigation/     ← Tab + Stack navigators
    ├── src/store/          ← Zustand state management
    ├── src/services/       ← API service layer
    └── src/hooks/          ← Custom data hooks
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Mobile App | React Native 0.85 + TypeScript |
| State Management | Zustand |
| Local Storage | MMKV |
| Navigation | React Navigation v7 |
| Web Backend | Laravel 12 + PHP 8.2 |
| Auth | Laravel Sanctum + Socialite |
| Admin Panel | Tailwind CSS v4 + AlpineJS |
| Database | MySQL |
| Cache | Redis |
| Media | Spatie Media Library |
| Permissions | Spatie Permission |
| Localization | English + Hindi |
| Build | Vite |

---

## Key Features (Built)

### Mobile App
- ✅ Multi-auth (Email / Phone OTP / Google / Facebook / Guest)
- ✅ Onboarding flow (Welcome → Permissions → Auth)
- ✅ Home dashboard (Weather, Spray Status, Mandi Trends)
- ✅ Spray Schedule (Altitude-aware: <6000ft / 6000-8000ft / >8000ft)
- ✅ Disease Library (90+ diseases, bilingual EN/HI, photos)
- ✅ Variety Guide (50+ varieties with altitude suitability)
- ✅ Rootstock Guide (Compatibility matrix)
- ✅ Blog / Knowledge Base (Categories, tags, search)
- ✅ Weather (Current + forecast, spray advisories)
- ✅ Profile & Settings

### Web Backend
- ✅ REST API v1 (JSON for mobile app)
- ✅ Full admin panel (CRUD all entities)
- ✅ Role-based access control
- ✅ Blog CMS with revisions
- ✅ SEO tools + sitemap generation
- ✅ Push notification system
- ✅ Activity logging
- ✅ Media library with image conversions

---

## Artifacts

| Document | Purpose |
|----------|---------|
| [Main Idea](../../ideas/developing/2026-05-16-baagicha-apple-orchard-management.md) | Full concept, problem, solution, metrics |
| [Lean Canvas](docs/lean-canvas/2026-05-16-baagicha-lean-canvas.md) | 9-box business model canvas |
| [System Architecture](diagrams/architecture/2026-05-16-baagicha-system-architecture.mermaid.md) | Laravel + React Native architecture diagram |
| [User Flow](diagrams/flow/2026-05-16-baagicha-user-flow.mermaid.md) | Complete farmer journey flowchart |
| [MVP Plan](plans/mvp/2026-05-16-baagicha-mvp-plan.md) | MoSCoW prioritization, user stories, launch checklist |
| [Competitor Analysis](research/competitors/2026-05-15-baagicha-competitor-analysis.md) | 8 competitors, feature matrix, SWOT |
| [Market Research](research/market/2026-05-15-apple-orchard-market-india.md) | Production stats, TAM/SAM/SOM, climate data |
| [Revenue Model](research/revenue-model/2026-05-15-baagicha-revenue-model-analysis.md) | 8 revenue streams, unit economics |

---

## Quick Stats

| Metric | Value |
|--------|-------|
| India Annual Apple Production | ~2.5-3 Million Tonnes |
| J&K Share | ~75% of India's output |
| HP Share | ~20% (6,47,000 tonnes in 2025-26) |
| Families Dependent (HP alone) | ~250,000 (~1.2-1.5M people) |
| Smartphone Farmers (under 40) | 72% use for agri-decisions weekly |
| Agri-Apps Market | $4.2B → $11.8B by 2034 |
| Post-Harvest Losses | 25-40% |
| Projected Year 3 Revenue | ₹3.65 Crores |

---

## Next Steps

### This Week
- [ ] Complete "My Orchard" screen with orchard CRUD
- [ ] Integrate push notifications for weather alerts
- [ ] Add offline mode for core content

### This Month
- [ ] Beta test with 10 farmers in Shimla district
- [ ] Build mandi price scraper
- [ ] Write comprehensive test suite

### 3 Months
- [ ] Play Store launch (Android)
- [ ] Partner with 3 KVKs
- [ ] Onboard 500 beta users

---

*Part of the [DreamBoard](../../README.md) execution system.*
