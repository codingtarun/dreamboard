# Lean Canvas: Simple Offline Music Player for Android

**Idea:** [Simple Offline Music Player for Android](../ideas/raw/2026-05-21-simple-offline-music-player-android.md)
**Date:** 2026-05-21
**Status:** Draft

---

## The Lean Canvas

```
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│  PROBLEM        │  SOLUTION       │  UNIQUE VALUE   │  UNFAIR         │
│                 │                 │  PROPOSITION    │  ADVANTAGE      │
│  Top 3 problems │  Top 3 features │  Single, clear, │  Can't be       │
│                 │                 │  compelling     │  easily copied  │
│  1. Existing    │  1. Zero-setup  │  message        │                 │
│     offline     │     launch —    │                 │                 │
│     players     │     music is    │  "Your music,   │  Founder is the │
│     bombard     │     just THERE  │   your way,     │  target user;   │
│     users with  │  2. Single-     │   instantly.    │  dogfooding     │
│     ads         │     tap play    │   No ads. No    │  from day one   │
│  2. UI/UX is    │     from any    │   clutter. No   │                 │
│     cluttered   │     screen      │   learning      │  Open-source    │
│     and         │  3. True        │   curve."       │  community can  │
│     confusing   │     offline —   │                 │  build loyalty  │
│  3. Apps are    │     zero net    │  High-level     │  & contributions│
│     bloated     │     permission  │  concept        │                 │
│     and slow    │                 │                 │                 │
├─────────────────┴─────────────────┤                 ├─────────────────┤
│  EXISTING ALTERNATIVES            │                 │  CHANNELS       │
│                                   │                 │                 │
│  How do people solve this now?    │                 │  Path to        │
│                                   │                 │  customers      │
│  1. Musicolet — free, no ads,    │                 │                 │
│     but utilitarian UI            │                 │  1. Google Play │
│  2. Poweramp — powerful but       │                 │     Store (free)│
│     overwhelming & paid           │                 │  2. Reddit /    │
│  3. BlackPlayer — freemium,       │                 │     r/android   │
│     ads in free tier              │                 │  3. F-Droid     │
│  4. Pulsar — free, clean but      │                 │     (privacy    │
│     basic; premium for EQ         │                 │     conscious)  │
│  5. Oto Music — free, open-       │                 │  4. YouTube /   │
│     source, but niche             │                 │     tech blogs  │
├─────────────────┬─────────────────┴─────────────────┴─────────────────┤
│  CUSTOMER       │  EARLY ADOPTERS                                         │
│  SEGMENTS       │                                                         │
│                 │  Who feels the pain MOST acutely?                       │
│  Target         │                                                         │
│  customers      │  • Spotify quitters who want local playback             │
│                 │  • Privacy-conscious users who want zero net            │
│                 │    permissions                                          │
│                 │  • Users on budget/older Android phones                 │
│                 │    (need lightweight)                                   │
│                 │  • Audiophiles with local FLAC libraries                │
│                 │  • Open-source enthusiasts & F-Droid users              │
├─────────────────┼─────────────────────────────────────────────────────────┤
│  KEY METRICS    │  COST STRUCTURE         │  REVENUE STREAMS            │
│                 │                         │                             │
│  How do you     │  Fixed & variable costs │  Pricing model              │
│  measure        │                         │                             │
│  success?       │  1. Developer time      │  1. Free core app           │
│                 │     (your own hours)    │     + "Pro" one-time        │
│  1. Downloads   │  2. Google Play dev fee │     purchase (~$2-5)        │
│     (target     │     ($25 one-time)      │     for themes, advanced    │
│     10K in      │  3. Domain / website    │     EQ, widgets             │
│     6 months)   │     (negligible)        │  2. GitHub Sponsors /       │
│  2. DAU / MAU   │  4. F-Droid hosting     │     donations (optional)    │
│  3. Play Store  │     (free)              │  3. White-label licensing   │
│     rating      │                         │     to OEMs (long shot)     │
│     (target     │                         │                             │
│     4.5+)       │                         │  Lifetime value: Low        │
│  4. Pro         │                         │  (~$0-5 per user), but      │
│     conversion  │                         │  zero marginal cost         │
│     rate        │                         │                             │
└─────────────────┴─────────────────────────┴─────────────────────────────┘
```

---

## Validation Status

| Assumption | Evidence | Validated? |
|------------|----------|------------|
| Problem exists | 43% of users prefer offline music; Play Store reviews full of "too many ads" complaints | ✅ Strong |
| Solution is desirable | Musicolet has 5M+ downloads despite utilitarian UI; "minimalist music player" is a search term | ✅ Strong |
| Customer segment is reachable | F-Droid, r/android, Play Store feature as indie app | ⚠️ Moderate |
| Revenue model is viable | One-time purchase is hard at scale; donations are unpredictable | ❌ Weak |

## Next Experiments
1. **Reddit Validation** — Post a mockup/screenshot concept to r/android and r/androidapps to gauge interest
2. **Play Store Review Mining** — Systematically analyze 1-star reviews of top 5 competitors for recurring complaints
3. **MVP Build** — Build a functional prototype with just folder browsing + playback, test with 5 real users
