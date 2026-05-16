# Baagicha User Flow — Farmer Journey

**Idea:** [Baagicha — Apple Orchard Management Platform](../../ideas/developing/2026-05-16-baagicha-apple-orchard-management.md)
**Type:** flow
**Created:** 2026-05-16

---

## Description

Complete user flow from first app open to daily usage, covering onboarding, authentication, core features, and return visits. Based on the actual React Native navigation structure.

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
    SOCIAL_AUTH --> PROFILE_SETUP[Profile Setup\nName + Location + Orchard Details]
    GUEST_MODE --> MAIN_TABS

    VERIFY_EMAIL --> PROFILE_SETUP
    VERIFY_OTP --> PROFILE_SETUP

    PROFILE_SETUP --> ORCHARD_SETUP[Orchard Setup\nArea + Altitude + Varieties]
    ORCHARD_SETUP --> MAIN_TABS

    subgraph "Home Tab"
        HOME[Home Dashboard]
        HOME --> WEATHER[Weather Widget\nCurrent + 7-day forecast]
        HOME --> SPRAY_STATUS[Spray Status\nSafe to spray / Warning]
        HOME --> MANDI_TREND[Mandi Trend\nToday's apple price]
        HOME --> PENDING_SPRAYS[Pending Sprays\nThis week's schedule]
        HOME --> ALERTS[Disease Alerts\nWeather-based warnings]
    end

    subgraph "Spray Tab"
        SPRAY[Spray Calendar]
        SPRAY --> STAGE_VIEW[Stage View\nBud break → Harvest]
        SPRAY --> CHEM_REC[Chemical Recommendation\nFor current stage + altitude]
        SPRAY --> SPRAY_LOG[Log Spray\nDate + Chemical + Quantity]
        SPRAY --> SPRAY_HISTORY[Spray History\nPast applications]
    end

    subgraph "Shop Tab"
        SHOP[Input Marketplace\nPhase 2]
        SHOP --> CATALOG[Product Catalog\nPesticides | Fertilizers | Tools]
        SHOP --> PRODUCT_DETAIL[Product Detail\nPrice | Reviews | Verified]
        SHOP --> CART[Shopping Cart]
        SHOP --> ORDERS[Order History]
    end

    subgraph "Discover Tab"
        DISCOVER[Discover / Learn]
        DISCOVER --> DISEASE_LIB[Disease Library\n90+ diseases with photos]
        DISCOVER --> VARIETY_GUIDE[Variety Guide\n50+ varieties by altitude]
        DISCOVER --> ROOTSTOCK_GUIDE[Rootstock Guide\nCompatibility matrix]
        DISCOVER --> BLOG[Knowledge Base\nArticles | Videos | Tips]
        DISCOVER --> SEARCH[Search\nDiseases | Varieties | Chemicals]

        DISEASE_LIB --> DISEASE_DETAIL[Disease Detail\nSymptoms | Treatment | Prevention]
        VARIETY_GUIDE --> VARIETY_DETAIL[Variety Detail\nClimate | Disease resistance | Yield]
        BLOG --> BLOG_DETAIL[Article Detail\nRelated posts | Share | Save]
    end

    subgraph "My Orchard Tab"
        MY_ORCHARD[My Orchard]
        MY_ORCHARD --> ORCHARD_PROFILE[Orchard Profile\nArea | Altitude | Varieties]
        MY_ORCHARD --> ACTIVITY_LOG[Activity Log\nSprays | Diseases | Harvests]
        MY_ORCHARD --> SAVED[Saved Content\nArticles | Varieties | Diseases]
        MY_ORCHARD --> SETTINGS[Settings\nLanguage | Notifications | Units]
    end

    MAIN_TABS --> HOME
    MAIN_TABS --> SPRAY
    MAIN_TABS --> SHOP
    MAIN_TABS --> DISCOVER
    MAIN_TABS --> MY_ORCHARD

    HOME --> DISEASE_DETAIL
    HOME --> SPRAY
    ALERTS --> DISEASE_DETAIL

    PROFILE_SETUP --> SETTINGS
```

---

## Guest vs Authenticated Feature Matrix

| Feature | Guest | Authenticated |
|---------|-------|---------------|
| Disease Library | ✅ | ✅ |
| Variety Guide | ✅ | ✅ |
| Weather | ✅ | ✅ |
| Spray Schedule | ✅ (generic) | ✅ (personalized) |
| Blog | ✅ | ✅ |
| My Orchard | ❌ | ✅ |
| Activity Log | ❌ | ✅ |
| Push Alerts | ❌ | ✅ |
| Saved Content | ❌ | ✅ |
| Shop / Orders | ❌ | ✅ |

---

## Key UX Decisions

1. **Guest mode** — Farmers can explore before committing to registration
2. **Bottom tabs** — 5 tabs modeled after successful Indian apps (PhonePe, Krishi Network)
3. **Bilingual** — All content in Hindi + English; UI language switch in settings
4. **Altitude-first** — Spray schedules auto-adjust based on GPS-detected altitude
5. **Offline-first** — Core content cached locally; sync when connected
