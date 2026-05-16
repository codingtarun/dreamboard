# Lean Canvas: SwiftCart — Lightweight Open-Source eCommerce CMS

**Idea:** [SwiftCart — Lightweight Open-Source eCommerce CMS](../../ideas/developing/2026-05-16-swiftcart-lightweight-ecommerce-cms.md)
**Date:** 2026-05-16
**Status:** Developing — Foundation + Core MVC Complete

---

## The Lean Canvas

```
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│  PROBLEM        │  SOLUTION       │  UNIQUE VALUE   │  UNFAIR         │
│                 │                 │  PROPOSITION    │  ADVANTAGE      │
│  1. WooCommerce │  1. Zero-dep    │  "Your store,   │  Readable       │
│     slow on     │     PHP 8.2     │   your code,    │  codebase:      │
│     cheap       │     framework   │   your hosting. │  800-line core  │
│     hosting     │     from scratch│   No plugin tax,│  readable in    │
│  2. Shopify     │  2. One-time    │   no platform   │  one afternoon  │
│     fees eat    │     themes &    │   fees, no      │                 │
│     margins at  │     plugins     │   vendor lock-  │  India-native:  │
│     scale       │     (no subs)   │   in."          │  GST/HSN,       │
│  3. Plugin tax  │  3. GST +       │                 │  pincode COD,   │
│     — ₹15-40k/  │     Indian      │  Runs on ₹99/mo │  Razorpay/PayU  │
│     year on     │     gateways    │  hosting.       │  free, Hindi    │
│     Woo         │     out-of-box  │  Core is free   │                 │
│  4. Stores      │  4. Readable    │  forever.       │  First-mover:   │
│     "stop being │     codebase    │  Every file     │  No zero-dep    │
│     mine" —      │     any dev     │  explainable.   │  eCommerce      │
│     updates,    │     can fix     │                 │  framework      │
│     lock-in     │                 │                 │  exists         │
├─────────────────┴─────────────────┤  High-concept   ├─────────────────┤
│  EXISTING ALTERNATIVES            │  pitch:         │  CHANNELS       │
│                                   │  "Shopify's     │                 │
│  1. WooCommerce — slow, plugin    │   speed +       │  1. GitHub      │
│     tax, WP dependency            │   WooCommerce's │     (open       │
│  2. Shopify — fast but expensive, │   openness,     │     source)     │
│     closed, 2% platform fee       │   minus both    │  2. IndieHackers│
│  3. OpenCart — 2010 PHP, ugly     │   their         │  3. Reddit      │
│     admin, GPL v3 blocks premium  │   problems."    │     r/PHP +     │
│  4. PrestaShop — module costs     │                 │     r/webdev    │
│     €70-300 each, Smarty bloat    │                 │  4. Indian      │
│  5. Magento — enterprise only,    │                 │     freelancer  │
│     ₹50L+ implementations         │                 │     communities │
│                                   │                 │  5. YouTube     │
│                                   │                 │     tutorials   │
├─────────────────┬─────────────────┴─────────────────┴─────────────────┤
│  CUSTOMER       │  EARLY ADOPTERS                                         │
│  SEGMENTS       │                                                         │
│                 │  1. Indian freelance devs building                      │
│  1. Small       │     stores for clients (₹800-6k/mo                     │
│     business    │     hosting budget)                                     │
│     owners in   │  2. WooCommerce store owners hit by                     │
│     India       │     plugin renewals + slowness                          │
│     (₹800-6k/mo │  3. Shopify Lite users who outgrow                    │
│     hosting     │     fees but fear self-hosting                          │
│     budget)     │  4. PHP learners who want to read                       │
│  2. Freelance   │     a real codebase                                     │
│     developers  │  5. Indian agencies needing white-                      │
│     building    │     label eCommerce solution                            │
│     stores for  │                                                         │
│     clients     │                                                         │
│  3. PHP         │                                                         │
│     learners    │                                                         │
│     (teaching   │                                                         │
│     vehicle)    │                                                         │
├─────────────────┼─────────────────────────────────────────────────────────┤
│  KEY METRICS    │  COST STRUCTURE         │  REVENUE STREAMS            │
│                 │                         │                             │
│  1. GitHub      │  1. Developer time      │  Tier 1: Free core (MIT)    │
│     stars       │     (solo, nights/      │  Tier 2: One-time themes    │
│  2. Downloads   │     weekends)           │     ₹1,500-4,000            │
│  3. Active      │  2. Domain + hosting    │  Tier 2: One-time plugins   │
│     installs    │     (dev environment)   │     ₹800-2,500              │
│  4. Theme/      │  3. Payment gateway     │  Tier 3: SwiftCart Cloud    │
│     plugin      │     test accounts       │     ₹399-1,999/mo           │
│     sales       │  4. Content creation    │  Tier 3: Migrations         │
│  5. NPS from    │     (docs, tutorials)   │     ₹15,000-40,000          │
│     devs        │                         │  Tier 3: Support contracts  │
│                 │                         │     ₹1,000-3,000/mo         │
│                 │                         │  Tier 3: White-label        │
│                 │                         │     ₹50,000-2L/year         │
└─────────────────┴─────────────────────────┴─────────────────────────────┘
```

---

## Validation Status

| Assumption | Evidence | Validated? |
|------------|----------|------------|
| Small businesses want cheaper than Shopify | Shopify India complaints = loudest on pricing | ✅ Yes |
| WooCommerce users hate plugin tax | Reddit / forums full of complaints | ✅ Yes |
| Developers want readable codebases | "I want to understand my stack" = common dev sentiment | ✅ Yes |
| India-native GST matters | No open-source platform does GST HSN properly | ✅ Yes |
| One-time pricing beats subscriptions for SMBs | Indian price sensitivity research | ⚠️ Hypothesis |
| Freelancers will build/sell themes | WordPress theme market = proven | ⚠️ Hypothesis |

---

## What's Built vs What's Planned

| Canvas Box | Built? | Notes |
|------------|--------|-------|
| Problem | ✅ | Extensively researched, 10 top complaints documented |
| Solution | 🔄 40% | Core framework done, storefront templates done, no DB yet |
| UVP | ✅ | Clear: ownership + speed + India-native |
| Unfair Advantage | ✅ | Readability + India-focus combo is hard to clone |
| Alternatives | ✅ | 5 competitors analyzed in depth |
| High Concept | ✅ | "Shopify's speed + WooCommerce's openness, minus both their problems" |
| Channels | 🔄 | GitHub presence, no marketing yet |
| Customer Segments | ✅ | Well-defined with price sensitivity map |
| Early Adopters | ✅ | Identified: freelance devs, Woo escapees, learners |
| Key Metrics | ✅ | Tracking plan defined |
| Cost Structure | ✅ | Solo dev, minimal run rate |
| Revenue Streams | 🔄 | Model designed, marketplace not yet built |
