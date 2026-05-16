# Baagicha — AI-Powered Apple Orchard Management Platform

**Status:** developing
**Spark:** 🔥🔥🔥🔥🔥
**Created:** 2026-05-16
**Last Updated:** 2026-05-16
**Tags:** agriculture, ai, mobile-app, react-native, laravel, india, apple-farming, himalayan, b2c, social-impact
**Domain:** baagicha.app

---

## The Spark

> *"My grandfather was an apple farmer in Himachal. He lost 40% of his crop last year because he sprayed at the wrong time — he didn't know about the weather shift. What if every farmer had an AI in their pocket that knew their orchard's altitude, their variety, and the exact spray schedule?"*

**Baagicha** (बागीचा) = "The Orchard" in Hindi.

An intelligent agricultural platform built specifically for **apple farmers in the Indian Himalayas** — Himachal Pradesh, Uttarakhand, and Jammu & Kashmir. It combines a React Native mobile app for farmers with a Laravel web backend + admin panel, powered by altitude-aware AI recommendations.

---

## What Exists Today (In Development)

### Mobile App (React Native 0.85 + TypeScript)

| Feature | Status | Screens |
|---------|--------|---------|
| **Auth System** | ✅ Built | Email/Password, Phone OTP, Social (Google, Facebook), Guest mode |
| **Onboarding Flow** | ✅ Built | Welcome → Location Permission → Notification Permission → Auth/Guest |
| **Home Dashboard** | ✅ Built | Weather widget, spray status, mandi trends, pending sprays, auth prompt |
| **Spray Schedule** | ✅ Built | Altitude-based spray calendar (below 6000ft / 6000-8000ft / above 8000ft) |
| **Disease Library** | ✅ Built | 90+ diseases with bilingual (EN/HI) descriptions, photos, treatments |
| **Variety Guide** | ✅ Built | 50+ apple varieties with altitude suitability, climate reqs, disease resistance |
| **Rootstock Guide** | ✅ Built | Rootstock database with compatibility, vigor, disease resistance |
| **Discover / Learn** | ✅ Built | Blog/Knowledge base with categories, tags, search |
| **Weather** | ✅ Built | Current weather, forecasts, spray advisories |
| **My Orchard** | 🔄 WIP | Orchard profile, activity log, variety tracking |
| **Shop** | 🔄 WIP | Input marketplace placeholder (Phase 2) |
| **Profile** | ✅ Built | Edit profile, preferences, saved content, notifications |

**Tech:** React Native 0.85, TypeScript, Zustand (state), React Navigation v7 (bottom tabs + stacks), MMKV (local storage), Axios

### Web Backend (Laravel 12 + PHP 8.2)

| Module | Status | Key Features |
|--------|--------|-------------|
| **API (v1)** | ✅ Built | RESTful JSON API for mobile app, Sanctum auth |
| **Auth** | ✅ Built | Email + Phone OTP + Social OAuth + Password reset |
| **Disease Management** | ✅ Built | 90+ diseases, bilingual content, media (photos) |
| **Variety Management** | ✅ Built | 50+ varieties, altitude ranges, disease resistance matrix |
| **Rootstock Management** | ✅ Built | Rootstock DB with compatibility rules |
| **Spray Schedule Engine** | ✅ Built | Templates by altitude, stage-based chemical recommendations |
| **Chemical DB** | ✅ Built | Pesticides, fungicides, compatibility rules, brands |
| **Blog / CMS** | ✅ Built | Categories, tags, comments, revisions, related posts |
| **Weather Integration** | ✅ Built | Weather data + alert rules |
| **Admin Panel** | ✅ Built | Full CRUD for all entities, role-based access (Spatie Permission) |
| **Notifications** | ✅ Built | Push notifications via device tokens |
| **Activity Logs** | ✅ Built | User action tracking |
| **Media Library** | ✅ Built | Spatie Media Library for images |
| **SEO Tools** | ✅ Built | Artesaos SEOTools, sitemap generation |
| **Localization** | ✅ Built | English + Hindi (mcamara/laravel-localization) |

**Models:** 30+ Eloquent models including User, UserProfile, UserPreference, UserOrchard, OrchardVariety, Disease, DiseaseReport, Variety, Rootstock, Chemical, ChemicalBrand, ChemicalCompatRule, SprayScheduleTemplate, SprayScheduleStage, SprayStageChemical, SprayStageDisease, SprayStageTip, NutrientTimingRule, Weather, WeatherAlertRule, OrchardActivity, BlogPost, BlogCategory, BlogTag, Comment, Notification, ActivityLog, SavedContent, DeviceToken, PhoneVerification, SocialAccount

**Tech:** Laravel 12, Sanctum, Spatie Permission, Spatie Media Library, Spatie Sluggable, Socialite, Tailwind CSS v4, Bootstrap 5, Vite, AlpineJS

---

## The Problem

Apple farming in the Himalayas faces **six critical challenges**:

1. **Climate Change** — Declining snowfall reducing chilling hours; Shimla snowfall dropped from 161.7 cm (2021) to 6-9.5 cm (2025)
2. **Pest & Disease** — Apple scab, codling moth, powdery mildew destroy 20-40% of crops
3. **Knowledge Gap** — Farmers unaware of best practices; extension services irregular in mountains
4. **Middlemen Exploitation** — No price transparency; forced distress sales
5. **Counterfeit Inputs** — Fake pesticides, poor-quality saplings
6. **Post-Harvest Loss** — 25-40% losses due to improper handling and no cold storage info

---

## The Solution

**Baagicha** puts an AI-powered orchard manager in every farmer's pocket:

- **Altitude-Aware Spray Schedules** — Different recommendations for below 6000ft, 6000-8000ft, above 8000ft
- **Disease Early Warning** — Weather-based disease outbreak predictions
- **Bilingual Knowledge Base** — Hindi + English disease library with photos
- **Variety & Rootstock Database** — Which variety grows best at your altitude
- **Digital Orchard Diary** — Track sprays, diseases, harvests, expenses
- **Mandi Price Tracking** — Real-time apple market prices
- **Input Marketplace** — Verified seeds, chemicals, equipment (Phase 2)

---

## Market Opportunity

| Metric | Value |
|--------|-------|
| India Annual Apple Production | ~2.5-3 Million Tonnes |
| Families Dependent (HP alone) | ~250,000 (~1.2-1.5M people) |
| Smartphone Farmers (under 40) | 72% use for agri-decisions weekly |
| Agri-Apps Market | $4.2B → $11.8B by 2034 (12.2% CAGR) |
| **TAM** | ~4-5 lakh apple-farming families |
| **SAM** | ~2.5-3 lakh smartphone-owning, under-50 farmers |
| **SOM (Year 1)** | ~25,000-50,000 users (HP focus) |

**No direct competitor** exists for Himalayan apple farmers.

---

## Revenue Model (Phase 2+)

| Stream | Description | Year 3 Est. |
|--------|-------------|-------------|
| Input Marketplace | Commission on pesticides, fertilizers, saplings | ₹2.25 Crores |
| Premium Subscriptions | Advanced AI, offline maps, expert chat | ₹75 Lakhs |
| B2B Mandi Data | Sell price trend data to traders | ₹30 Lakhs |
| Cold Storage Directory | Listing fees + booking commission | ₹15 Lakhs |
| Sponsored Content | Agrochemical company educational content | ₹20 Lakhs |
| **Total Year 3** | | **₹3.65 Crores** |

---

## Tech Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    REACT NATIVE MOBILE APP                   │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│  │  Home   │ │  Spray  │ │  Shop   │ │Discover │ │MyOrchard│
│  │  Tab    │ │  Tab    │ │  Tab    │ │  Tab    │ │  Tab    │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘
│       │           │           │           │           │     │
│  Zustand State │ MMKV Cache │ Axios API Client          │
│       │           │           │           │           │     │
└───────┼───────────┼───────────┼───────────┼───────────┼─────┘
        │           │           │           │           │
        └───────────┴───────────┴─────┬─────┴───────────┘
                                      │ HTTPS / JSON
                                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    LARAVEL 12 BACKEND                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │  API v1     │  │  Web Admin  │  │  Blog/CMS   │         │
│  │ (Sanctum)   │  │  (Breeze)   │  │  (Public)   │         │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘         │
│         │                │                │                │
│  ┌──────┴────────────────┴────────────────┴──────┐         │
│  │  Controllers → Services → Eloquent Models      │         │
│  │  30+ models │ Spatie Media │ Spatie Permission │         │
│  └────────────────────────────────────────────────┘         │
│         │                                                   │
│  ┌──────┴──────┐  ┌──────────────┐  ┌─────────────────┐    │
│  │  MySQL DB   │  │  Redis Cache │  │  Weather API    │    │
│  │  (Primary)  │  │  (Sessions)  │  │  (External)     │    │
│  └─────────────┘  └──────────────┘  └─────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Metrics

| Metric | Current | Target (MVP Launch) |
|--------|---------|---------------------|
| Backend Models | 30+ | 30+ |
| API Endpoints | 25+ | 40+ |
| Mobile Screens | 20+ | 25+ |
| Diseases Documented | 90+ | 100+ |
| Varieties Documented | 50+ | 75+ |
| Admin Modules | 12 | 15 |
| Test Coverage | Basic | 70%+ |

---

## Potential Obstacles

1. **Connectivity** — Himalayan network is unreliable; offline mode is critical
2. **Trust-building** — Older farmers may resist digital tools; need KVK partnerships
3. **Data accuracy** — Wrong spray advice = crop damage = trust destroyed forever
4. **Single developer bandwidth** — Mobile + Backend + Content = lot of work
5. **Orchard Solutions** — Established consultancy with same vision; potential competitor/partner
6. **Government apps** — IFFCO Kisan could add apple module overnight

---

## Next Steps

### Immediate (This Week)
- [ ] Complete "My Orchard" screen with orchard CRUD
- [ ] Integrate weather API for disease prediction alerts
- [ ] Add offline mode for spray schedules and disease library
- [ ] Complete push notification setup

### Short Term (This Month)
- [ ] Beta test with 10 farmers in Shimla district
- [ ] Add expert consultation chat feature
- [ ] Build mandi price scraper/aggregator
- [ ] Write comprehensive test suite (Pest PHP + Jest)

### Medium Term (3 Months)
- [ ] Launch on Play Store (Android first)
- [ ] Partner with 3 KVKs (Krishi Vigyan Kendras)
- [ ] Onboard 500 beta users
- [ ] Build input marketplace MVP

### Long Term (6-12 Months)
- [ ] iOS App Store launch
- [ ] 10,000 active users
- [ ] First revenue from marketplace
- [ ] Expand to Uttarakhand and J&K

---

## Related Artifacts

- [Lean Canvas](../baagicha/docs/lean-canvas/2026-05-16-baagicha-lean-canvas.md)
- [System Architecture](../baagicha/diagrams/architecture/2026-05-16-baagicha-system-architecture.mermaid.md)
- [User Flow](../baagicha/diagrams/flow/2026-05-16-baagicha-user-flow.mermaid.md)
- [MVP Plan](../baagicha/plans/mvp/2026-05-16-baagicha-mvp-plan.md)
- [Competitor Analysis](../baagicha/research/competitors/2026-05-15-baagicha-competitor-analysis.md)
- [Market Research](../baagicha/research/market/2026-05-15-apple-orchard-market-india.md)
- [Revenue Model](../baagicha/research/revenue-model/2026-05-15-baagicha-revenue-model-analysis.md)

---

## Notes Log

- **2026-05-16** — Moved from raw → developing. Comprehensive codebase audit complete. Laravel backend (30+ models, admin panel, REST API) and React Native app (20+ screens, Zustand state, tab navigation) both significantly built. Ready for MVP polish and farmer beta testing.
