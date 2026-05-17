# MVP Plan: Baagvaani — Apple Orchard Management Platform

**Idea:** [Baagvaani — Apple Orchard Management Platform](../../ideas/developing/2026-05-16-baagvaani-apple-orchard-management.md)
**Date:** 2026-05-17
**Status:** In Development — 70% Complete
**Target Launch:** 6-8 weeks
**Previous Name:** Baagicha

---

## Executive Summary

The Baagvaani MVP is a **React Native mobile app + Laravel backend** that gives Himalayan apple farmers altitude-aware spray schedules, a bilingual disease library, weather alerts, and now — enhanced spray intelligence, smart calculators, and the foundation for expert consultation.

The codebase is significantly built; this plan defines what's needed to reach a beta-launchable state, plus the Phase 2 roadmap for the new features from our product planning document.

---

## MoSCoW Prioritization

### 🔴 Must Have (MVP Launch Blockers)

| # | Feature | Status | Effort | Owner |
|---|---------|--------|--------|-------|
| 1 | **Auth System** — Email, Phone OTP, Social, Guest | ✅ Built | — | Backend + Mobile |
| 2 | **Disease Library** — 90+ diseases, bilingual, photos | ✅ Built | — | Backend + Mobile |
| 3 | **Variety Guide** — 50+ varieties, altitude suitability | ✅ Built | — | Backend + Mobile |
| 4 | **Spray Schedule** — Altitude-based templates | ✅ Built | — | Backend + Mobile |
| 5 | **Weather Widget** — Current + forecast on home | ✅ Built | — | Backend + Mobile |
| 6 | **My Orchard Profile** — Multi-orchard + block-level CRUD | 🔄 WIP | 5 days | Mobile |
| 7 | **Push Notifications** — Weather alerts, spray reminders | 🔄 WIP | 2 days | Backend + Mobile |
| 8 | **Offline Mode** — Cache spray schedules + disease lib | 🔄 WIP | 4 days | Mobile |
| 9 | **Admin Content Management** — CRUD all entities | ✅ Built | — | Backend |
| 10 | **Bug Fixes + Polish** — Crash fixes, UI refinements | 🔄 WIP | 5 days | Both |
| 11 | **Spray Side-Effects** — Add to chemical detail screen | 🔄 WIP | 2 days | Backend + Mobile |
| 12 | **Spray Precautions** — Pre-spray checklist per chemical | 🔄 WIP | 2 days | Backend + Mobile |

### 🟡 Should Have (Post-MVP, Month 1-2)

| # | Feature | Status | Effort |
|---|---------|--------|--------|
| 13 | **Rootstock Guide** — Full guide in mobile app | ✅ Built | — |
| 14 | **Activity Log** — Track sprays, diseases, harvests | 🔄 WIP | 3 days |
| 15 | **Mandi Price Tracking** — Scraper + display | ❌ Not started | 5 days |
| 16 | **Blog / Knowledge Base** — Mobile reading experience | ✅ Built | — |
| 17 | **Expert Consultation (Text)** — Chat with agronomists | ❌ Not started | 7 days |
| 18 | **Dosage Calculator** — Tank mix + area calculator | ❌ Not started | 4 days |
| 19 | **Compatibility Checker v1** — 2-chemical compatibility | ❌ Not started | 5 days |
| 20 | **Test Suite** — Pest PHP + Jest coverage 70%+ | 🔄 WIP | 5 days |
| 21 | **Spray Videos** — Bilingual video per spray stage | ❌ Not started | 5 days |

### 🟢 Could Have (Month 3-6)

| # | Feature | Status | Effort |
|---|---------|--------|--------|
| 22 | **Input Marketplace** — Pesticides, fertilizers, tools | ❌ Not started | 3 weeks |
| 23 | **Premium Subscription** — Advanced AI, offline maps, expert chat | ❌ Not started | 2 weeks |
| 24 | **Video Consultation** — Agora/Twilio integration | ❌ Not started | 2 weeks |
| 25 | **AI Chat Assistant** — Natural language farming Q&A | ❌ Not started | 2 weeks |
| 26 | **Community Forum** — Farmer photo sharing + rewards | ❌ Not started | 2 weeks |
| 27 | **Cold Storage Directory** — Map + booking | ❌ Not started | 1 week |
| 28 | **Fertigation Calculator** — Drip fertilizer injection rates | ❌ Not started | 4 days |
| 29 | **HDP Cost Calculator** — High-density plantation estimator | ❌ Not started | 3 days |
| 30 | **Recommendation Engine v1** — Basic rule-based suggestions | ❌ Not started | 2 weeks |
| 31 | **Low Input Practices** — Regenerative ag guides (paid wall) | ❌ Not started | 1 week |
| 32 | **Pear & Plum Content** — Expand beyond apples | ❌ Not started | 1 week |

### ⚫ Won't Have (Post-PMF)

| # | Feature | Reason |
|---|---------|--------|
| 33 | **IoT Sensors** — Hardware integration | Too expensive, too complex for MVP |
| 34 | **Drone Mapping** — Aerial orchard analysis | Enterprise feature, not smallholder |
| 35 | **Multi-Crop Support** — Beyond temperate fruits | Dilutes focus; apple-first is the moat |
| 36 | **Export Compliance** — International trade docs | B2B feature, not farmer-facing |
| 37 | **Telephone Consultation** — PSTN integration | Low priority; WhatsApp + video sufficient |

---

## User Stories (MVP)

### As a Farmer (Guest)
- [x] I can browse the disease library without registering
- [x] I can view variety guides by altitude
- [x] I can see current weather and spray status
- [x] I can read blog articles about apple farming
- [ ] I can view a generic spray schedule for my altitude range
- [ ] I can use the Dosage Calculator without registering
- [ ] I can check chemical compatibility before mixing

### As a Farmer (Authenticated)
- [x] I can register with email, phone, or social login
- [x] I can set up my orchard profile (area, altitude, varieties)
- [ ] I can manage multiple orchards with block-level detail
- [ ] I can receive personalized spray reminders
- [ ] I can log spray applications with date and chemical used
- [ ] I can receive weather-based disease outbreak alerts
- [ ] I can save articles and varieties for offline reading
- [ ] I can view my spray history and orchard activity log
- [ ] I can see chemical side-effects and precautions before spraying
- [ ] I can watch short videos explaining each spray stage
- [ ] I can chat with an expert (text/WhatsApp style)

### As a Premium Subscriber
- [ ] I can book video consultations with horticulturists
- [ ] I can access advanced AI recommendations for my orchard
- [ ] I can use all calculators (fertigation, HDP cost, water needs)
- [ ] I get additional discounts in the marketplace
- [ ] I can see farmer reviews on product pages
- [ ] I can access low-input / regenerative practice guides

### As an Admin
- [x] I can CRUD diseases, varieties, chemicals, spray schedules
- [x] I can manage blog posts, categories, tags
- [x] I can view user analytics and activity logs
- [x] I can manage user roles and permissions
- [ ] I can send push notifications to all or segmented users
- [ ] I can manage expert consultants and their availability
- [ ] I can approve community posts and moderate content

### As an Expert Consultant
- [ ] I can view assigned farmer orchard profiles
- [ ] I can add recommendations/notes to farmer profiles
- [ ] I can set my availability for consultations
- [ ] I can view my earnings and consultation history

---

## New Feature Implementation Notes

### Personalized Consultation Module

**Architecture:**
```
Mobile App → Laravel API → Consultation Booking Service
                          → Agora/Twilio SDK (video)
                          → Twilio (WhatsApp Business API)
                          → FCM (call notifications)
```

**Models needed:** `Consultant`, `ConsultationSession`, `ConsultationType`, `ConsultantAvailability`, `ConsultationReview`

**Pricing tiers:**
| Type | Duration | Price |
|------|----------|-------|
| WhatsApp Chat | 30 min | ₹30 |
| Video Call | 20 min | ₹60 |
| Telephone | 15 min | ₹45 |
| Orchard Visit | 1-2 hrs | ₹500+ |

**Payment:** Razorpay / PayU integration

### Enhanced Spray Intelligence

**Side Effects & Precautions:**
- Add `side_effects` (JSON), `precautions` (JSON), `ppe_required` (JSON) fields to `chemicals` table
- Mobile: Pre-spray checklist screen before logging spray
- Push notification: "Check wind speed before spraying Mancozeb"

**Compatibility Checker:**
- Data source: `chemical_compatibility_rules` table (matrix of compatible/incompatible/conditional pairs)
- Algorithm: User selects 2-5 chemicals → check all pairs against matrix → show result with warnings
- Jar Test integration: Link to video showing physical compatibility test

**Spray Videos:**
- Host on YouTube / CloudFront CDN
- 60-90 seconds per spray stage
- Bilingual audio tracks or separate videos

### Mini Widgets

**Dosage Calculator:**
```
Inputs: Tank capacity (L), Chemical concentration (%), Area (kanals/bighas), Recommended dose (ml/L)
Output: Total chemical needed (ml), Number of tanks required
```

**Fertigation Calculator:**
```
Inputs: Fertilizer NPK grade, Target ppm, Drip flow rate, Area, Irrigation time
Output: Fertilizer quantity per tank (g), Injection rate (L/hr)
```

**HDP Cost Calculator:**
```
Inputs: Area (acres), Plant spacing, Rootstock type, Trellis type, Drip irrigation (yes/no)
Output: Total plants, Sapling cost, Infrastructure cost, Total investment
```

### Community & Gamification

**Reward Points System:**
| Action | Points |
|--------|--------|
| Follow spray schedule for a week | 50 pts |
| Log spray application | 20 pts |
| Submit feedback after spray | 30 pts |
| Share photo in community | 10 pts |
| Complete profile setup | 100 pts |

**Levels:**
| Level | Name | Points Required |
|-------|------|-----------------|
| 1 | Sprout | 0 |
| 2 | Sapling | 200 |
| 3 | Grower | 500 |
| 4 | Expert | 1,000 |
| 5 | Master Farmer | 2,500 |

**Redemption:** 100 pts = ₹10 shop discount

---

## Technical Debt to Clear Before Launch

| Item | Priority | Effort | Impact |
|------|----------|--------|--------|
| Add Laravel Pest tests (Feature + Unit) | High | 3 days | Prevents regressions |
| Add React Native Jest tests | High | 2 days | Mobile stability |
| API rate limiting | Medium | 1 day | Security |
| Input sanitization on all forms | Medium | 1 day | Security |
| Image optimization (WebP, responsive) | Medium | 1 day | Performance |
| Error boundary + crash reporting | Medium | 1 day | Reliability |
| App store assets (screenshots, description) | Low | 1 day | Marketing |

---

## Beta Testing Plan

### Phase 1: Internal (Week 1-2)
- 5 friends/family test on Android
- Focus: Auth flows, crashes, UI bugs, calculator accuracy
- Feedback channel: WhatsApp group

### Phase 2: KVK Partners (Week 3-4)
- 3 Krishi Vigyan Kendras in Shimla district
- 20 farmers per KVK = 60 total
- Focus: Content accuracy, usability for 50+ year olds, calculator usefulness
- Incentives: Free premium for 1 year

### Phase 3: Open Beta (Week 5-8)
- Play Store open beta track
- Target: 500 downloads
- Focus: Retention, feature usage analytics, consultation demand
- Feedback: In-app feedback form + Google Play reviews

---

## Success Metrics (MVP)

| Metric | Target | Measurement |
|--------|--------|-------------|
| Beta Downloads | 500 | Play Store console |
| Daily Active Users | 100 | Firebase Analytics |
| Spray Schedule Views | 5+ per user/week | Custom event tracking |
| Disease Library Views | 3+ per user/week | Custom event tracking |
| Calculator Uses | 2+ per user/week | Custom event tracking |
| Push Notification CTR | 15%+ | Firebase Messaging |
| Crash-Free Sessions | 99%+ | Firebase Crashlytics |
| User Retention (D7) | 40%+ | Firebase Analytics |
| NPS Score | 50+ | In-app survey |

---

## Launch Checklist

- [ ] All Must-Haves complete and tested
- [ ] Beta testing complete with farmer feedback incorporated
- [ ] Play Store listing ready (screenshots, description, privacy policy)
- [ ] Backend deployed to production server with SSL
- [ ] Domain configured (baagvaani.app)
- [ ] Firebase project set up (Analytics, Crashlytics, Messaging)
- [ ] Privacy policy and TOS pages live
- [ ] Support email/ WhatsApp number ready
- [ ] KVK partnership agreements signed
- [ ] Press kit ready (logos, screenshots, founder story)
- [ ] Consultation expert network (minimum 3 horticulturists) onboarded

---

## Timeline

```
Week 1-2:   Complete My Orchard (multi-orchard) + Push Notifications + Offline Mode
Week 3-4:   Mandi Price + Dosage Calculator + Compatibility Checker + Testing
Week 5-6:   Internal Beta → KVK Beta → Feedback Incorporation
Week 7-8:   Open Beta (500 users) + Expert Consultation (text) soft launch
Week 9-10:  Polish → Play Store Launch
Week 11-12: Post-launch monitoring + first content update + Community v1

Month 4-6:  Premium subscriptions + Video consultation + Recommendation Engine
Month 7-9:  Marketplace MVP + Full community + Reward points
Month 10-12: Expand to Pear/Plum + iOS launch + B2B data services
```

---

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Farmers don't trust app advice | Medium | High | Partner with KVKs for credibility; show expert credentials |
| Poor connectivity in mountains | High | Medium | Build robust offline mode; SMS fallback for alerts |
| Wrong spray advice damages crop | Low | Critical | Vet all content with agronomists; liability disclaimer |
| Orchard Solutions launches app | Medium | High | Speed to market; community moat; consultation differentiation |
| Single developer burnout | Medium | High | Scope discipline; open-source help; defer non-core features |
| Weather API costs explode | Low | Medium | Cache aggressively; use IMD free tier |
| Consultation no-shows | Medium | Medium | Pre-payment requirement; cancellation policy; backup experts |
| Marketplace delivery issues | Medium | High | Partner with existing dealer networks; don't build logistics |

---

*Part of the [DreamBoard MVP Planning System](../../../templates/mvp-template.md).*
