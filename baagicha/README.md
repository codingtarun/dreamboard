# 🍎 Baagicha — Apple Orchard Management App

> **Name:** बागीचा (Baagicha = "The Orchard")  
> **Target:** Himalayan apple farmers (Himachal Pradesh, Uttarakhand, J&K)  
> **Status:** Research complete, Development in progress

---

## What is Baagicha?

Baagicha is a **React Native mobile app + Laravel web backend** designed specifically for apple orchard farmers in the Indian Himalayas.

It provides:
- Altitude-aware spray schedules (below 6000ft / 6000-8000ft / above 8000ft)
- Apple-specific disease library with photos & Hindi descriptions
- Weather-based disease outbreak alerts
- Apple variety & rootstock database
- Mandi price tracking
- Digital orchard record-keeping

---

## Folder Structure

```
baagicha/
├── README.md                    ← You are here
└── research/
    ├── market/                  ← Apple production stats, TAM/SAM/SOM, climate data
    ├── competitors/             ← Agri-tech competitor landscape
    └── revenue-model/           ← 8 revenue streams, unit economics
```

---

## Quick Stats

| Metric | Value |
|--------|-------|
| India Annual Apple Production | ~2.5-3 Million Tonnes |
| J&K Share | ~75% of India's output |
| HP Share | ~20% (6,47,000 tonnes in 2025-26) |
| Families Dependent (HP alone) | ~250,000 |
| Agri-Apps Market | $4.2B → $11.8B by 2034 |
| Smartphone Farmers (under 40) | 72% use for agri-decisions |
| Post-Harvest Losses | 25-40% |
| Projected Year 3 Revenue | ₹3.65 Crores |

---

## Key Documents

| Document | Purpose |
|----------|---------|
| [Market Research](research/market/2026-05-15-apple-orchard-market-india.md) | Production data, state-wise breakdown, climate crisis analysis |
| [Competitor Analysis](research/competitors/2026-05-15-baagicha-competitor-analysis.md) | 8 competitors analyzed, feature matrix, SWOT |
| [Revenue Model](research/revenue-model/2026-05-15-baagicha-revenue-model-analysis.md) | 8 streams: marketplace, premium, B2B, data, grants |

---

## Key Challenges Addressed

1. **Climate Change** — Declining snowfall, reduced chilling hours
2. **Pest & Disease** — Apple scab, codling moth, powdery mildew
3. **Knowledge Gap** — Farmers unaware of best practices
4. **Middlemen Exploitation** — No price transparency
5. **Input Quality** — Counterfeit pesticides, poor saplings
6. **Post-Harvest Loss** — 25-40% loss due to no cold storage info

---

## Revenue Potential

| Stream | Year 3 Estimate |
|--------|----------------|
| Input Marketplace (commission) | ₹2.25 Crores |
| Premium Subscriptions | ₹75 Lakhs |
| B2B Mandi Price Data | ₹30 Lakhs |
| Cold Storage Directory | ₹15 Lakhs |
| Sponsored Content | ₹20 Lakhs |
| **Total** | **₹3.65 Crores** |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Mobile App | React Native 0.85 + TypeScript |
| Web Backend | Laravel 12 + PHP |
| Styling | Tailwind CSS + Bootstrap |
| Build | Vite |
| Database | (Configured in Laravel) |

> Full development is happening in `../../baagichaworkspace/`  
> This folder contains the **strategy & research** artifacts.

---

## Next Steps

- [ ] Complete React Native app screens
- [ ] Integrate Laravel backend API
- [ ] Add weather API for disease prediction
- [ ] Partner with KVKs (Krishi Vigyan Kendras)
- [ ] Pilot with 100 farmers in Shimla district

---

*Part of the [DreamBoard](../README.md) execution system.*
