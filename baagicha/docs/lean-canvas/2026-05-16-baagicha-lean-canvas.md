# Lean Canvas: Baagicha — AI-Powered Apple Orchard Management

**Idea:** [Baagicha — Apple Orchard Management Platform](../../ideas/developing/2026-05-16-baagicha-apple-orchard-management.md)
**Date:** 2026-05-16
**Status:** Developing — Codebase 70% complete

---

## The Lean Canvas

```
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│  PROBLEM        │  SOLUTION       │  UNIQUE VALUE   │  UNFAIR         │
│                 │                 │  PROPOSITION    │  ADVANTAGE      │
│  1. Climate     │  1. Altitude-   │  "Your AI orchard│  Deep domain    │
│     change      │     aware spray │   manager in     │  expertise:     │
│     destroying  │     schedules   │   your pocket.   │  lived apple    │
│     crops —     │     (GPS-based) │   Know exactly   │  farming        │
│     reduced     │  2. Weather-    │   when, what,    │  heritage       │
│     chilling    │     based       │   and how much   │                 │
│     hours       │     disease     │   to spray."     │  First-mover    │
│  2. Farmers     │     outbreak    │                  │  in Himalayan   │
│     spray       │     predictions │  Altitude-aware  │  apple-specific │
│     blindly —   │  3. Bilingual   │  AI + Bilingual  │  app space      │
│     wrong       │     disease     │  (Hindi+English) │                 │
│     timing/     │     library     │  + No hardware   │  Community      │
│     chemicals   │     (90+ diseases│  required        │  trust from     │
│  3. No price    │     with photos)│                  │  grandfather's  │
│     transparency│  4. Digital     │                  │  generation     │
│     — middlemen │     orchard     │                  │                 │
│     exploit     │     diary       │                  │                 │
│  4. Knowledge   │  5. Mandi price │                  │                 │
│     gap — no    │     tracking    │                  │                 │
│     extension   │                 │                  │                 │
│     services    │                 │                  │                 │
│     in mountains│                 │                  │                 │
├─────────────────┴─────────────────┤  High-concept   ├─────────────────┤
│  EXISTING ALTERNATIVES            │  pitch:         │  CHANNELS       │
│                                   │  "Duolingo for   │                 │
│  1. Orchard Solutions —           │   apple farming"│  1. KVKs        │
│     consultancy, expensive        │                 │     (Krishi      │
│  2. IFFCO Kisan — generic,        │                 │     Vigyan      │
│     not apple-specific            │                 │     Kendras)    │
│  3. YouTube / WhatsApp —          │                 │  2. Apple mandi │
│     unreliable, unverified        │                 │     QR codes    │
│  4. Government extension —        │                 │  3. Farmer      │
│     irregular, understaffed       │                 │     WhatsApp    │
│  5. Agrochemical dealers —        │                 │     groups      │
│     biased advice                 │                 │  4. Local agro  │
│                                   │                 │     shops       │
│                                   │                 │  5. Play Store  │
│                                   │                 │     + word of   │
│                                   │                 │     mouth       │
├─────────────────┬─────────────────┴─────────────────┴─────────────────┤
│  CUSTOMER       │  EARLY ADOPTERS                                         │
│  SEGMENTS       │                                                         │
│                 │  1. Apple farmers aged 25-45 with                       │
│  1. Smallholder │     smartphones in Shimla/Kullu                         │
│     apple       │  2. Young farmers taking over family                    │
│     farmers     │     orchards (digital-native)                           │
│     (1-5 acres) │  3. Progressive farmers already using                   │
│     in HP/UK/JK │     WhatsApp/YouTube for farming info                   │
│  2. Medium      │  4. KVK-trained farmers seeking                         │
│     orchards    │     structured digital guidance                         │
│     (5-20 acres)│                                                         │
│  3. Orchard     │                                                         │
│     consultants │                                                         │
│     & KVKs      │                                                         │
├─────────────────┼─────────────────────────────────────────────────────────┤
│  KEY METRICS    │  COST STRUCTURE         │  REVENUE STREAMS            │
│                 │                         │                             │
│  1. Monthly     │  1. API/Server costs    │  Year 1: Free (acquisition) │
│     Active      │     (Laravel + MySQL)   │  Year 2+:                   │
│     Users (MAU) │  2. Weather API         │    - Input marketplace      │
│  2. Spray       │  3. SMS/OTP costs       │      commission (8-15%)     │
│     schedule    │  4. Push notification     │    - Premium subscriptions  │
│     completions │     service (FCM)       │      (₹99/mo)               │
│  3. Disease     │  5. Content creation    │    - B2B mandi data sales   │
│     library     │     (bilingual docs)    │    - Sponsored content      │
│     views       │  6. Developer time      │    - Cold storage directory │
│  4. Mandi       │     (solo founder)      │                             │
│     price       │                         │                             │
│     checks      │                         │                             │
│  5. Orchard     │                         │                             │
│     profiles    │                         │                             │
│     created     │                         │                             │
└─────────────────┴─────────────────────────┴─────────────────────────────┘
```

---

## Validation Status

| Assumption | Evidence | Validated? |
|------------|----------|------------|
| Farmers want digital spray schedules | 72% of under-40 farmers use smartphones for agri-decisions | ✅ Yes |
| Altitude matters for spray timing | Horticulture research confirms different schedules by elevation | ✅ Yes |
| Hindi language is critical | 70%+ farmers in target regions prefer Hindi | ✅ Yes |
| Farmers will trust app over dealer | Unknown — needs beta testing | ⚠️ Hypothesis |
| Marketplace commission model works | Amazon/Krishi Network prove model in India | ⚠️ Hypothesis |
| Free app can convert to paid | Typical freemium: 2-5% conversion | ⚠️ Hypothesis |

---

## What's Built vs What's Planned

| Canvas Box | Built? | Notes |
|------------|--------|-------|
| Problem | ✅ | Extensively researched, farmer interviews |
| Solution | 🔄 70% | Mobile app + backend coded, needs polish |
| UVP | ✅ | Clear and validated with farmer feedback |
| Unfair Advantage | ✅ | Domain expertise + first-mover |
| Alternatives | ✅ | 8 competitors analyzed |
| High Concept | ✅ | "Duolingo for apple farming" |
| Channels | 🔄 | KVK partnerships in progress |
| Customer Segments | ✅ | Well-defined with personas |
| Early Adopters | ✅ | Identified Shimla/Kullu farmers |
| Key Metrics | ✅ | Tracking plan defined |
| Cost Structure | ✅ | Estimated ₹3-5L/year run rate |
| Revenue Streams | 🔄 | Model designed, not yet live |
