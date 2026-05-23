# 🍎 Baagvaani — AI-Powered Apple Orchard Management Platform

> **Name:** बागवाणी (Baagvaani = "Voice of the Orchard")  
> **Previously:** Baagicha (बागीचा) — "The Orchard"  
> **Target:** Himalayan apple farmers (Himachal Pradesh, Uttarakhand, J&K)  
> **Status:** Developing — Codebase 70% complete  
> **Domain:** baagvaani.app

---

## What is Baagvaani?

**Baagvaani** (बागवाणी) is an intelligent agricultural management platform built specifically for **apple farmers in the Indian Himalayas**. It combines a React Native mobile app for farmers with a Laravel web backend + admin panel, powered by altitude-aware AI recommendations.

The evolution from "Baagicha" (Orchard) to "Baagvaani" (Voice of the Orchard) reflects the platform's expanded vision: not just managing orchards, but giving farmers a voice through community, expert consultation, knowledge sharing, and data-driven insights.

---

## Live Codebase

Full development is happening in `../../baagichaworkspace/` (will be renamed to `baagvaaniworkspace`):

```
baagvaaniworkspace/
├── web_baagvaani/          ← Laravel 12 backend + admin panel
│   ├── app/Models/         ← 30+ Eloquent models
│   ├── app/Http/Controllers/Api/  ← REST API (v1)
│   ├── app/Http/Controllers/Admin/ ← Admin CRUD
│   ├── routes/api.php      ← 25+ API endpoints
│   ├── routes/web/admin/   ← Admin routes
│   └── resources/views/    ← Tailwind + AlpineJS admin
│
└── baagvaaniApp/           ← React Native 0.85 mobile app
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
| Video Calls | Agora / Twilio (planned) |
| Push Notifications | Firebase Cloud Messaging |

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

## New Features from Product Roadmap (PDF Integration)

### 🆕 Personalized Consultation Module (Premium)
| Mode | Description | Pricing |
|------|-------------|---------|
| Video Call | 1-on-1 with horticulturist | ₹30-60/session |
| Telephone | Voice consultation | ₹30-60/session |
| WhatsApp Chat | Async text + photo advice | ₹30-60/session |
| Orchard Visit | On-ground expert visit | Premium pricing |

- Expert consultants get backend dashboard to view user's orchard profile
- Consultants add suggestions/notes directly to user's orchard profile
- Users view recommendations in their profile (covered in consultancy fee)

### 🆕 Enhanced Spray Intelligence
| Feature | Description |
|---------|-------------|
| Side Effects Library | Documented side effects for every chemical |
| Spray Precautions | Pre-spray checklist: PPE, wind speed, temperature, PHI |
| Compatibility Checker | Tank-mix compatibility before spraying (Jar Test digital) |
| Spray Videos | Short bilingual videos explaining each spray schedule |
| Yearly Schedule Data | Complete annual spray calendar with in-depth stage data |

### 🆕 Recommendation Engine
- AI-powered suggestions based on:
  - User profile (location, experience level)
  - Orchard profile (altitude, variety, block conditions, soil type)
  - Weather patterns and disease pressure
  - Historical spray performance

### 🆕 Orchard Profile 2.0
- **Multi-orchard support**: One user can manage multiple orchards
- **Block-level management**: Each orchard divided into blocks per variety
- **Per-block suggestions**: Custom recommendations per block condition
- **Plant tracking**: Plant diameter, fruit count per plant

### 🆕 Mini Widgets / Calculators
| Widget | Purpose |
|--------|---------|
| Dosage Calculator | Chemical quantity based on tank size + area |
| HDP Cost Calculator | High-Density Plantation setup cost estimator |
| Water Requirement Calculator | Rootstock-based irrigation needs |
| Fertigation Calculator | Fertilizer injection rates for drip systems |
| Fertilizer Calculator | NPK requirements based on soil test + crop stage |

### 🆕 Community & Gamification
| Feature | Description |
|---------|-------------|
| Farmer Community | Photo-sharing only (peer learning) |
| Reward Points | Points for following app recommendations + feedback |
| Experience Levels | User levels based on activity and engagement |
| Redeem Rewards | Points convert to shop discounts |

### 🆕 Shop / Marketplace (Phase 2)
**Categories:**
- Fungicides & Pesticides
- Nutrition & Fertilizers
- Tools & Equipment
- Books & Guides
- Safety Gear (masks, gloves, goggles)
- Precision Tools (pH meter, size ring, refractometer)

**Premium Features:**
- Additional discounts for paid members
- Product reviews visible only to paid users
- "What other farmers say" on product pages

### 🆕 Low Input / Regenerative Practices (Paid Wall)
- Regenerative agriculture practices
- Low-cost alternative solutions
- Organic spray schedules
- Sustainable orchard management guides

### 🆕 Content Expansion
- Blogs for Apple, Pear, Plum, and other temperate fruits
- In-depth data articles
- Government scheme guides (Udyam, Startup India, subsidies)

### 🆕 Business Setup Tracker
- Register business checklist
- GST application guide
- Bank account setup (ICICI partner details)
- Government scheme applications:
  - CC Limit / Term Loan
  - 25-35% subsidy tracking
  - Startup India registration
  - Center & State govt. schemes

---

## Artifacts

| Document | Purpose |
|----------|---------|
| [Main Idea](../../ideas/developing/2026-05-16-baagvaani-apple-orchard-management.md) | Full concept, problem, solution, metrics |
| [Lean Canvas](docs/lean-canvas/2026-05-16-baagvaani-lean-canvas.md) | 9-box business model canvas |
| [System Architecture](diagrams/architecture/2026-05-16-baagvaani-system-architecture.mermaid.md) | Laravel + React Native architecture diagram |
| [User Flow](diagrams/flow/2026-05-16-baagvaani-user-flow.mermaid.md) | Complete farmer journey flowchart |
| [MVP Plan](plans/mvp/2026-05-16-baagvaani-mvp-plan.md) | MoSCoW prioritization, user stories, launch checklist |
| [Competitor Analysis](research/competitors/2026-05-15-baagvaani-competitor-analysis.md) | 8 competitors, feature matrix, SWOT |
| [Market Research](research/market/2026-05-15-apple-orchard-market-india.md) | Production stats, TAM/SAM/SOM, climate data |
| [Revenue Model](research/revenue-model/2026-05-15-baagvaani-revenue-model-analysis.md) | 8 revenue streams, unit economics |
| [Feature Implementation Research](research/tech-stack/2026-05-17-baagvaani-feature-implementation-research.md) | How to build new features from PDF roadmap |
| [Mobile App Feature Suggestions](research/tech-stack/2026-05-17-baagvaani-mobile-feature-suggestions.md) | Additional mobile app features & ideas |
| [Prediction Engine Architecture](research/tech-stack/2026-05-20-baagvaani-prediction-engine-architecture.md) | Technical blueprint with pseudocode |
| **[Implementation Guide](../../baagichaworkspace/research/prediction-engine/00_INDEX.md)** | **Production-ready code for Laravel + React Native** |

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
- [ ] Complete "My Orchard" screen with multi-orchard + block-level CRUD
- [ ] Integrate push notifications for weather alerts
- [ ] Add offline mode for core content

### This Month
- [ ] Beta test with 10 farmers in Shimla district
- [ ] Build mandi price scraper
- [ ] Write comprehensive test suite
- [ ] Add spray side-effects + precautions to chemical detail

### 3 Months
- [ ] Play Store launch (Android)
- [ ] Partner with 3 KVKs
- [ ] Onboard 500 beta users
- [ ] Launch Dosage Calculator widget
- [ ] Add Compatibility Checker (v1)

### 6 Months
- [ ] Launch Premium Consultation Module (Agora video)
- [ ] Build Recommendation Engine v1
- [ ] Launch Community (photo sharing + rewards)
- [ ] Expand to Pear & Plum content

---

*Part of the [DreamBoard](../../README.md) execution system.*
