# Baagvaani — AI-Powered Apple Orchard Management Platform

**Status:** developing
**Spark:** 🔥🔥🔥🔥🔥
**Created:** 2026-05-16
**Last Updated:** 2026-05-17
**Tags:** agriculture, ai, mobile-app, react-native, laravel, india, apple-farming, himalayan, b2c, social-impact, consultation, community
**Domain:** baagvaani.app
**Previous Name:** Baagicha (बागीचा)

---

## The Spark

> *"My grandfather was an apple farmer in Himachal. He lost 40% of his crop last year because he sprayed at the wrong time — he didn't know about the weather shift. What if every farmer had an AI in their pocket that knew their orchard's altitude, their variety, and the exact spray schedule?"*

**Baagvaani** (बागवाणी) = "Voice of the Orchard" in Hindi.

An intelligent agricultural platform built specifically for **apple farmers in the Indian Himalayas** — Himachal Pradesh, Uttarakhand, and Jammu & Kashmir. It combines a React Native mobile app for farmers with a Laravel web backend + admin panel, powered by altitude-aware AI recommendations, expert consultation, and a thriving farmer community.

The evolution from "Baagicha" (Orchard) to "Baagvaani" (Voice of the Orchard) reflects our expanded vision: not just managing orchards, but giving farmers a voice through community, expert consultation, knowledge sharing, and data-driven insights.

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

## New Features from Product Roadmap (2026-05-17)

### 1. Personalized Consultation Module (Premium)
Multi-mode expert consultation for farmers:
- **Video Call** — Real-time 1-on-1 with horticulturists (Agora/Twilio integration)
- **Telephone** — Voice consultation for low-bandwidth areas
- **WhatsApp Chat** — Async text + photo sharing with experts
- **Orchard Visit** — On-ground expert visit booking system

Expert consultants get a dedicated backend dashboard where they can view the farmer's saved orchard profile, add suggestions and notes directly to the profile, and the farmer sees these recommendations in their app.

**Pricing:** ₹30-60 per session (Premium feature)

### 2. Enhanced Spray Intelligence
- **Side Effects Library** — Documented side effects for every chemical in the database
- **Spray Precautions** — Pre-spray checklist: PPE requirements, wind speed limits, temperature range, Pre-Harvest Interval (PHI)
- **Compatibility Checker** — Digital "Jar Test" — select multiple chemicals and check tank-mix compatibility before spraying
- **Spray Videos** — Short bilingual (HI/EN) videos explaining each spray schedule stage
- **Yearly Schedule Data** — Complete in-depth annual spray calendar with stage-wise details

### 3. Recommendation Engine
AI-powered suggestions based on:
- User profile (location, farming experience, preferences)
- Orchard profile (altitude, variety mix, block conditions, soil type, age of trees)
- Weather patterns and disease pressure forecasts
- Historical spray performance and outcomes
- Seasonal stage (bud break, flowering, fruit set, harvest)

### 4. Orchard Profile 2.0
- **Multi-orchard support** — One user can manage multiple orchards
- **Block-level management** — Each orchard divided into blocks per variety
- **Per-block suggestions** — Custom spray and nutrient recommendations per block condition
- **Plant tracking** — Track plant diameter, fruit count per plant, yield estimation

### 5. Mini Widgets / Calculators
- **Dosage Calculator** — Chemical quantity based on tank size + orchard area
- **HDP Cost Calculator** — High-Density Plantation setup cost estimator
- **Water Requirement Calculator** — Rootstock-based irrigation needs
- **Fertigation Calculator** — Fertilizer injection rates for drip irrigation systems
- **Fertilizer Calculator** — NPK requirements based on soil test results + crop stage

### 6. Community & Gamification
- **Farmer Community** — Photo-sharing only (peer learning, no text spam)
- **Reward Points** — Earn points for following app recommendations and providing feedback
- **Experience Levels** — User levels/badges based on activity and engagement
- **Redeem Rewards** — Points convert to discounts in the shop

### 7. Shop / Marketplace (Phase 2)
**Categories:**
- Fungicides & Pesticides
- Nutrition & Fertilizers
- Tools & Equipment
- Books & Guides
- Safety Gear (masks, gloves, goggles, spray suits)
- Precision Tools (pH meter, size ring, refractometer, TDS meter)

**Premium Features:**
- Additional discounts for paid members
- Product reviews visible only to paid users
- "What other farmers say" social proof on product pages

### 8. Low Input / Regenerative Practices (Paid Wall)
- Regenerative agriculture practices for apple orchards
- Low-cost alternative spray solutions
- Organic spray schedules
- Sustainable orchard management guides
- Integrated Pest Management (IPM) protocols

### 9. Content Expansion
- Blogs for Apple, Pear, Plum, Peach, Apricot, and other temperate fruits
- In-depth data articles and research summaries
- Government scheme guides (Udyam, Startup India, PM-KISAN, subsidies)

### 10. Business Setup Tracker
- Register business checklist
- GST application guide
- Bank account setup (ICICI partner details)
- Government scheme applications:
  - CC Limit / Term Loan
  - 25-35% subsidy tracking
  - Startup India registration
  - Center & State govt. schemes

---

## The Problem

Apple farming in the Himalayas faces **six critical challenges**:

1. **Climate Change** — Declining snowfall reducing chilling hours; Shimla snowfall dropped from 161.7 cm (2021) to 6-9.5 cm (2025)
2. **Pest & Disease** — Apple scab, codling moth, powdery mildew destroy 20-40% of crops
3. **Knowledge Gap** — Farmers unaware of best practices; extension services irregular in mountains
4. **Middlemen Exploitation** — No price transparency; forced distress sales
5. **Counterfeit Inputs** — Fake pesticides, poor-quality saplings
6. **Post-Harvest Loss** — 25-40% losses due to improper handling and no cold storage info

**New Problems Identified:**
7. **No Expert Access** — Small farmers can't afford consultancy fees (₹5,000-50,000)
8. **Chemical Confusion** — Farmers don't know which chemicals are compatible or their side effects
9. **Input Cost Pressure** — Rising costs of fungicides, fertilizers, and equipment
10. **No Peer Learning** — Farmers work in isolation; no platform to share experiences

---

## The Solution

**Baagvaani** puts an AI-powered orchard manager + expert network + farmer community in every farmer's pocket:

- **Altitude-Aware Spray Schedules** — Different recommendations for below 6000ft, 6000-8000ft, above 8000ft
- **Disease Early Warning** — Weather-based disease outbreak predictions
- **Bilingual Knowledge Base** — Hindi + English disease library with photos
- **Variety & Rootstock Database** — Which variety grows best at your altitude
- **Digital Orchard Diary** — Track sprays, diseases, harvests, expenses
- **Mandi Price Tracking** — Real-time apple market prices
- **Expert Consultation** — Affordable access to horticulturists (₹30-60/session)
- **Chemical Safety Tools** — Side effects, precautions, compatibility checker
- **Smart Calculators** — Dosage, fertigation, HDP cost, water requirements
- **Farmer Community** — Photo-based peer learning + reward points
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
| **SOM** (Year 1) | ~25,000-50,000 users (HP focus) |

**No direct competitor** exists for Himalayan apple farmers with this comprehensive feature set.

---

## Revenue Model (Phase 2+)

| Stream | Description | Year 3 Est. |
|--------|-------------|-------------|
| Input Marketplace | Commission on pesticides, fertilizers, saplings | ₹2.25 Crores |
| Premium Subscriptions | Advanced AI, offline maps, expert chat, calculators | ₹75 Lakhs |
| Expert Consultation | Commission on paid sessions (20-30%) | ₹30 Lakhs |
| B2B Mandi Data | Sell price trend data to traders | ₹30 Lakhs |
| Cold Storage Directory | Listing fees + booking commission | ₹15 Lakhs |
| Sponsored Content | Agrochemical company educational content | ₹20 Lakhs |
| **Total Year 3** | | **₹3.95 Crores** |

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
│  ┌────┴───────────┴───────────┴───────────┴───────────┴──┐  │
│  │  Mini Widgets │ Community │ Consultation │ Calculators │  │
│  └─────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
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
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐   │
│  │ Agora/Twilio │  │   Firebase   │  │   Mandi API     │   │
│  │ (Video Call) │  │  (Push/Auth) │  │  (Price Data)   │   │
│  └──────────────┘  └──────────────┘  └─────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Metrics

| Metric | Current | Target (MVP Launch) |
|--------|---------|---------------------|
| Backend Models | 30+ | 40+ |
| API Endpoints | 25+ | 50+ |
| Mobile Screens | 20+ | 35+ |
| Diseases Documented | 90+ | 100+ |
| Varieties Documented | 50+ | 75+ |
| Admin Modules | 12 | 18 |
| Test Coverage | Basic | 70%+ |

---

## Potential Obstacles

1. **Connectivity** — Himalayan network is unreliable; offline mode is critical
2. **Trust-building** — Older farmers may resist digital tools; need KVK partnerships
3. **Data accuracy** — Wrong spray advice = crop damage = trust destroyed forever
4. **Single developer bandwidth** — Mobile + Backend + Content = lot of work
5. **Orchard Solutions** — Established consultancy with same vision; potential competitor/partner
6. **Government apps** — IFFCO Kisan could add apple module overnight
7. **Consultation quality** — Need verified horticulturists; bad advice = liability
8. **Marketplace logistics** — Delivery to remote villages is challenging

---

## Next Steps

### Immediate (This Week)
- [ ] Complete "My Orchard" screen with multi-orchard + block-level CRUD
- [ ] Integrate weather API for disease prediction alerts
- [ ] Add offline mode for spray schedules and disease library
- [ ] Complete push notification setup

### Short Term (This Month)
- [ ] Beta test with 10 farmers in Shimla district
- [ ] Add expert consultation chat feature architecture
- [ ] Build mandi price scraper/aggregator
- [ ] Write comprehensive test suite (Pest PHP + Jest)
- [ ] Add spray side-effects + precautions to chemical detail

### Medium Term (3 Months)
- [ ] Launch on Play Store (Android first)
- [ ] Partner with 3 KVKs (Krishi Vigyan Kendras)
- [ ] Onboard 500 beta users
- [ ] Build input marketplace MVP
- [ ] Launch Dosage Calculator widget
- [ ] Add Compatibility Checker (v1)

### Long Term (6-12 Months)
- [ ] iOS App Store launch
- [ ] Launch Premium Consultation Module (Agora video)
- [ ] Build Recommendation Engine v1
- [ ] Launch Community (photo sharing + rewards)
- [ ] Expand to Pear & Plum content
- [ ] 10,000 active users
- [ ] First revenue from marketplace + consultation

---

## Related Artifacts

- [Lean Canvas](../baagvaani/docs/lean-canvas/2026-05-16-baagvaani-lean-canvas.md)
- [System Architecture](../baagvaani/diagrams/architecture/2026-05-16-baagvaani-system-architecture.mermaid.md)
- [User Flow](../baagvaani/diagrams/flow/2026-05-16-baagvaani-user-flow.mermaid.md)
- [MVP Plan](../baagvaani/plans/mvp/2026-05-16-baagvaani-mvp-plan.md)
- [Competitor Analysis](../baagvaani/research/competitors/2026-05-15-baagvaani-competitor-analysis.md)
- [Market Research](../baagvaani/research/market/2026-05-15-apple-orchard-market-india.md)
- [Revenue Model](../baagvaani/research/revenue-model/2026-05-15-baagvaani-revenue-model-analysis.md)
- [Feature Implementation Research](../baagvaani/research/tech-stack/2026-05-17-baagvaani-feature-implementation-research.md)
- [Mobile Feature Suggestions](../baagvaani/research/tech-stack/2026-05-17-baagvaani-mobile-feature-suggestions.md)
- [Prediction Engine — Global DSS Landscape](../baagvaani/research/competitors/2026-05-20-apple-dss-global-landscape.md)
- [Prediction Engine — Technical Architecture](../baagvaani/research/tech-stack/2026-05-20-baagvaani-prediction-engine-architecture.md)

---

## Notes Log

- **2026-05-16** — Moved from raw → developing. Comprehensive codebase audit complete. Laravel backend (30+ models, admin panel, REST API) and React Native app (20+ screens, Zustand state, tab navigation) both significantly built. Ready for MVP polish and farmer beta testing.
- **2026-05-17** — Rebranded from Baagicha to Baagvaani. Integrated product roadmap from spray schedule PDF. Added: Consultation Module, Enhanced Spray Intelligence, Recommendation Engine, Orchard Profile 2.0, Mini Widgets, Community & Gamification, Shop expansion, Low Input Practices, Content expansion, Business Setup Tracker.
