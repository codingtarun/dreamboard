# Lean Canvas: Baagvaani — AI-Powered Apple Orchard Management

**Idea:** [Baagvaani — Apple Orchard Management Platform](../../ideas/developing/2026-05-16-baagvaani-apple-orchard-management.md)
**Date:** 2026-05-17
**Status:** Developing — Codebase 70% complete
**Previous Name:** Baagicha

---

## The Lean Canvas

```
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│  PROBLEM        │  SOLUTION       │  UNIQUE VALUE   │  UNFAIR         │
│                 │                 │  PROPOSITION    │  ADVANTAGE      │
│  1. Climate     │  1. Altitude-   │  "Your AI orchard│  Deep domain    │
│     change      │     aware spray │   manager +     │  expertise:     │
│     destroying  │     schedules   │   expert        │  lived apple    │
│     crops —     │     (GPS-based) │   network in    │  farming        │
│     reduced     │  2. Weather-    │   your pocket.  │  heritage       │
│     chilling    │     based       │                 │                 │
│     hours       │     disease     │  Altitude-aware │  First-mover    │
│  2. Farmers     │     outbreak    │  AI + Bilingual │  in Himalayan   │
│     spray       │     predictions │  (Hindi+English)│  apple-specific │
│     blindly —   │  3. Bilingual   │  + Expert       │  app space      │
│     wrong       │     disease     │  Consultation   │                 │
│     timing/     │     library     │  + Community    │  Community      │
│     chemicals   │     (90+ diseases│  + Smart       │  trust from     │
│  3. No price    │     with photos)│  Calculators    │  grandfather's  │
│     transparency│  4. Digital     │                 │  generation     │
│     — middlemen │     orchard     │                 │                 │
│     exploit     │     diary       │                 │                 │
│  4. Knowledge   │  5. Mandi price │                 │                 │
│     gap — no    │     tracking    │                 │                 │
│     extension   │  6. Expert      │                 │                 │
│     services    │     consultation│                 │                 │
│     in mountains│     (₹30-60)    │                 │                 │
│  5. No peer     │  7. Community   │                 │                 │
│     learning    │     + rewards   │                 │                 │
│  6. Chemical    │  8. Smart       │                 │                 │
│     confusion   │     calculators │                 │                 │
├─────────────────┴─────────────────┤  High-concept   ├─────────────────┤
│  EXISTING ALTERNATIVES            │  pitch:         │  CHANNELS       │
│                                   │                 │                 │
│  1. Orchard Solutions —           │  "Duolingo for  │  1. KVKs        │
│     consultancy, expensive        │   apple farming │     (Krishi     │
│  2. IFFCO Kisan — generic,        │   + Your        │     Vigyan      │
│     not apple-specific            │   personal      │     Kendras)    │
│  3. YouTube / WhatsApp —          │   agri-expert"  │  2. Apple mandi │
│     unreliable, unverified        │                 │     QR codes    │
│  4. Government extension —        │                 │  3. Farmer      │
│     irregular, understaffed       │                 │     WhatsApp    │
│  5. Agrochemical dealers —        │                 │     groups      │
│     biased advice                 │                 │  4. Local agro  │
│  6. Local agri-apps — no          │                 │     shops       │
│     consultation, no community    │                 │  5. Play Store  │
│                                   │                 │     + word of   │
│                                   │                 │     mouth       │
│                                   │                 │  6. Expert      │
│                                   │                 │     referrals   │
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
│     (5-20 acres)│  5. Farmers seeking affordable expert                   │
│  3. Orchard     │     advice (₹30-60 vs ₹5,000+)                          │
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
│  3. Disease     │  5. Content creation    │    - Expert consultation    │
│     library     │     (bilingual docs)    │      commission (20-30%)    │
│     views       │  6. Developer time      │    - B2B mandi data sales   │
│  4. Mandi       │     (solo founder)      │    - Sponsored content      │
│     price       │  7. Video/API costs     │    - Cold storage directory │
│     checks      │     (Agora/Twilio)      │                             │
│  5. Orchard     │  8. Expert payouts      │                             │
│     profiles    │     (consultation rev)  │                             │
│  6. Consultation│                         │                             │
│     bookings    │                         │                             │
│  7. Calculator  │                         │                             │
│     uses        │                         │                             │
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
| Farmers want affordable consultation | Existing consultancy costs ₹5,000-50,000 | ✅ Strong demand signal |
| Community/peer learning valued | WhatsApp groups very active among farmers | ✅ Yes |

---

## What's Built vs What's Planned

| Canvas Box | Built? | Notes |
|------------|--------|-------|
| Problem | ✅ | Extensively researched, farmer interviews |
| Solution | 🔄 70% | Mobile app + backend coded, new features planned |
| UVP | ✅ | Clear and validated with farmer feedback |
| Unfair Advantage | ✅ | Domain expertise + first-mover + community |
| Alternatives | ✅ | 8 competitors analyzed |
| High Concept | ✅ | "Duolingo for apple farming + your personal agri-expert" |
| Channels | 🔄 | KVK partnerships in progress |
| Customer Segments | ✅ | Well-defined with personas |
| Early Adopters | ✅ | Identified Shimla/Kullu farmers |
| Key Metrics | ✅ | Tracking plan defined |
| Cost Structure | ✅ | Estimated ₹3-5L/year run rate + expert payouts |
| Revenue Streams | 🔄 | Model designed, consultation added as new stream |

---

## New Revenue Stream: Expert Consultation

| Metric | Value |
|--------|-------|
| Target consultation price | ₹30-60 per session |
| Platform commission | 20-30% |
| Expert payout | ₹21-42 per session |
| Target monthly sessions (Year 2) | 500 |
| Monthly commission revenue | ₹3,000-9,000 |
| Annual commission revenue | ₹36,000-1,08,000 |

This is small initially but builds trust and differentiates from competitors. Scales with user base.

---

*Part of the [DreamBoard Lean Canvas System](../../../templates/lean-canvas-template.md).*
