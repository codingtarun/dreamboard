# Baagvaani User Flow — Farmer Journey

**Idea:** [Baagvaani — Apple Orchard Management Platform](../../ideas/developing/2026-05-16-baagvaani-apple-orchard-management.md)
**Type:** flow
**Created:** 2026-05-16
**Updated:** 2026-05-17

---

## Description

Complete user flow from first app open to daily usage, covering onboarding, authentication, core features, consultation, community, calculators, and return visits. Based on the actual React Native navigation structure + new features from product roadmap.

---

## Diagram

```mermaid
flowchart TD
    START([App Launch]) --> ONBOARDING{First Launch?}

    ONBOARDING -->|Yes| WELCOME[Welcome Screen\nBrand intro in Hindi]
    WELCOME --> LOC_PERM[Location Permission\nGPS for altitude detection]
    LOC_PERM --> NOTIF_PERM[Notification Permission\nWeather & spray alerts]
    NOTIF_PERM --> AUTH_CHOICE{Choose Auth Method}

    ONBOARDING -->|No| MAIN_TABS[Main Tabs\nBottom Navigation]

    AUTH_CHOICE -->|Email| EMAIL_REG[Email Register\nName + Email + Password]
    AUTH_CHOICE -->|Phone| PHONE_AUTH[Phone Auth\nMobile + OTP]
    AUTH_CHOICE -->|Social| SOCIAL_AUTH[Social Login\nGoogle / Facebook]
    AUTH_CHOICE -->|Skip| GUEST_MODE[Guest Mode\nLimited features]

    EMAIL_REG --> VERIFY_EMAIL[Email Verification]
    PHONE_AUTH --> VERIFY_OTP[OTP Verification]
    SOCIAL_AUTH --> PROFILE_SETUP[Profile Setup\nName + Location + Experience Level]
    GUEST_MODE --> MAIN_TABS

    VERIFY_EMAIL --> PROFILE_SETUP
    VERIFY_OTP --> PROFILE_SETUP

    PROFILE_SETUP --> ORCHARD_SETUP[Orchard Setup\nArea + Altitude + Varieties + Blocks]
    ORCHARD_SETUP --> MAIN_TABS

    subgraph "Home Tab"
        HOME[Home Dashboard]
        HOME --> WEATHER[Weather Widget\nCurrent + 7-day forecast]
        HOME --> SPRAY_STATUS[Spray Status\nSafe to spray / Warning]
        HOME --> MANDI_TREND[Mandi Trend\nToday's apple price]
        HOME --> PENDING_SPRAYS[Pending Sprays\nThis week's schedule]
        HOME --> ALERTS[Disease Alerts\nWeather-based warnings]
        HOME --> CALC_WIDGETS[Mini Widgets\nDosage | Fertigation | HDP]
        HOME --> REWARDS[My Rewards\nPoints + Level + Badges]
    end

    subgraph "Spray Tab"
        SPRAY[Spray Calendar]
        SPRAY --> STAGE_VIEW[Stage View\nBud break → Harvest]
        SPRAY --> CHEM_REC[Chemical Recommendation\nFor current stage + altitude]
        SPRAY --> SPRAY_LOG[Log Spray\nDate + Chemical + Quantity]
        SPRAY --> SPRAY_HISTORY[Spray History\nPast applications]
        SPRAY --> SPRAY_VIDEOS[Spray Videos\nBilingual video guides]
        SPRAY --> SIDE_EFFECTS[Side Effects\nPer chemical details]
        SPRAY --> PRECAUTIONS[Precautions\nPPE + Weather checklist]
        SPRAY --> COMPAT_CHECK[Compatibility Checker\nTank-mix validation]
    end

    subgraph "Consult Tab"
        CONSULT[Consultation\nNew Tab]
        CONSULT --> CONSULT_TYPES[Consultation Types\nVideo | Phone | WhatsApp | Visit]
        CONSULT --> EXPERT_LIST[Expert List\nHorticulturists by specialty]
        CONSULT --> BOOKING[Book Session\nSelect time + type + pay]
        CONSULT --> MY_SESSIONS[My Sessions\nUpcoming + History]
        CONSULT --> CONSULT_NOTES[Expert Notes\nRecommendations on my orchard]
        BOOKING --> PAYMENT[Payment\nRazorpay / PayU]
        PAYMENT --> VIDEO_CALL[Agora Video Room\nConsultation in progress]
        PAYMENT --> WHATSAPP_CHAT[WhatsApp Chat\nAsync consultation]
    end

    subgraph "Shop Tab"
        SHOP[Input Marketplace\nPhase 2]
        SHOP --> CATALOG[Product Catalog\nPesticides | Fertilizers | Tools | Safety]
        SHOP --> PRODUCT_DETAIL[Product Detail\nPrice | Reviews | Farmer Says]
        SHOP --> CART[Shopping Cart]
        SHOP --> ORDERS[Order History]
        SHOP --> CATEGORIES[Categories\nFungicides | Nutrition | Tools | Books | Safety Gear | Precision Tools]
    end

    subgraph "Discover Tab"
        DISCOVER[Discover / Learn]
        DISCOVER --> DISEASE_LIB[Disease Library\n90+ diseases with photos]
        DISCOVER --> VARIETY_GUIDE[Variety Guide\n50+ varieties by altitude]
        DISCOVER --> ROOTSTOCK_GUIDE[Rootstock Guide\nCompatibility matrix]
        DISCOVER --> BLOG[Knowledge Base\nArticles | Videos | Tips]
        DISCOVER --> SEARCH[Search\nDiseases | Varieties | Chemicals]
        DISCOVER --> COMMUNITY[Community\nFarmer Photo Feed]
        DISCOVER --> LOW_INPUT[Low Input Practices\nRegenerative | Organic | Paid Wall]
        DISCOVER --> SCHEMES[Govt Schemes\nSubsidies | Loans | Udyam]

        DISEASE_LIB --> DISEASE_DETAIL[Disease Detail\nSymptoms | Treatment | Prevention]
        VARIETY_GUIDE --> VARIETY_DETAIL[Variety Detail\nClimate | Disease resistance | Yield]
        BLOG --> BLOG_DETAIL[Article Detail\nRelated posts | Share | Save]
        COMMUNITY --> POST_DETAIL[Post Detail\nPhoto | Likes | Comments]
    end

    subgraph "My Orchard Tab"
        MY_ORCHARD[My Orchard]
        MY_ORCHARD --> ORCHARD_LIST[My Orchards\nMultiple orchards]
        ORCHARD_LIST --> ORCHARD_PROFILE[Orchard Profile\nArea | Altitude | Varieties | Blocks]
        ORCHARD_PROFILE --> BLOCK_DETAIL[Block Detail\nVariety | Age | Plant count | Condition]
        MY_ORCHARD --> ACTIVITY_LOG[Activity Log\nSprays | Diseases | Harvests]
        MY_ORCHARD --> SAVED[Saved Content\nArticles | Varieties | Diseases]
        MY_ORCHARD --> SETTINGS[Settings\nLanguage | Notifications | Units]
        MY_ORCHARD --> REWARD_HISTORY[Reward History\nPoints earned | Redeemed]
    end

    MAIN_TABS --> HOME
    MAIN_TABS --> SPRAY
    MAIN_TABS --> CONSULT
    MAIN_TABS --> SHOP
    MAIN_TABS --> DISCOVER
    MAIN_TABS --> MY_ORCHARD

    HOME --> DISEASE_DETAIL
    HOME --> SPRAY
    HOME --> CALC_WIDGETS
    ALERTS --> DISEASE_DETAIL

    PROFILE_SETUP --> SETTINGS
```

---

## Guest vs Authenticated Feature Matrix

| Feature | Guest | Authenticated | Premium |
|---------|-------|---------------|---------|
| Disease Library | ✅ | ✅ | ✅ |
| Variety Guide | ✅ | ✅ | ✅ |
| Weather | ✅ | ✅ | ✅ |
| Spray Schedule | ✅ (generic) | ✅ (personalized) | ✅ (advanced) |
| Blog | ✅ | ✅ | ✅ |
| Dosage Calculator | ✅ | ✅ | ✅ |
| Compatibility Checker | ✅ (2 chem) | ✅ (5 chem) | ✅ (unlimited) |
| My Orchard | ❌ | ✅ | ✅ (unlimited) |
| Activity Log | ❌ | ✅ | ✅ |
| Push Alerts | ❌ | ✅ | ✅ (hyperlocal) |
| Saved Content | ❌ | ✅ | ✅ |
| Shop / Orders | ❌ | ✅ | ✅ + discounts |
| Expert Consultation | ❌ | ❌ | ✅ |
| Video Call | ❌ | ❌ | ✅ |
| Community Posting | ❌ | ✅ | ✅ |
| Reward Points | ❌ | ✅ | ✅ (2x multiplier) |
| Low Input Practices | ❌ | ❌ | ✅ |
| Fertigation Calculator | ❌ | ❌ | ✅ |
| HDP Cost Calculator | ❌ | ❌ | ✅ |
| Product Reviews | ❌ | ❌ | ✅ |

---

## Key UX Decisions

1. **Guest mode** — Farmers can explore before committing to registration
2. **Bottom tabs** — 6 tabs: Home | Spray | Consult | Shop | Discover | MyOrchard
3. **Bilingual** — All content in Hindi + English; UI language switch in settings
4. **Altitude-first** — Spray schedules auto-adjust based on GPS-detected altitude
5. **Offline-first** — Core content cached locally; sync when connected
6. **Consultation tab** — Prominent placement because it's a key differentiator
7. **Mini widgets on home** — One-tap access to most-used calculators
8. **Photo-only community** — Reduces spam, focuses on visual learning

---

## New Navigation Elements (Post-Rename)

| Element | Type | Description |
|---------|------|-------------|
| Consult Tab | Bottom Tab | New primary tab for expert access |
| Compatibility Checker | Spray Sub-screen | Tank-mix validation tool |
| Spray Videos | Spray Sub-screen | Bilingual video guides |
| Mini Widgets | Home Widgets | Dosage, Fertigation, HDP calculators |
| Community | Discover Sub-screen | Photo-based farmer feed |
| Low Input Practices | Discover Sub-screen | Regenerative ag guides (premium) |
| Govt Schemes | Discover Sub-screen | Subsidy and loan guides |
| Reward History | My Orchard Sub-screen | Points tracking |
| Block Detail | My Orchard Sub-screen | Per-block orchard management |
