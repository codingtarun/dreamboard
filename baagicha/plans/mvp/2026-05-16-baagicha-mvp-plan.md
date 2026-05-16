# MVP Plan: Baagicha — Apple Orchard Management Platform

**Idea:** [Baagicha — Apple Orchard Management Platform](../../ideas/developing/2026-05-16-baagicha-apple-orchard-management.md)
**Date:** 2026-05-16
**Status:** In Development — 70% Complete
**Target Launch:** 6-8 weeks

---

## Executive Summary

The Baagicha MVP is a **React Native mobile app + Laravel backend** that gives Himalayan apple farmers altitude-aware spray schedules, a bilingual disease library, and weather alerts. The codebase is significantly built; this plan defines what's needed to reach a beta-launchable state.

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
| 6 | **My Orchard Profile** — Add/edit orchard details | 🔄 WIP | 3 days | Mobile |
| 7 | **Push Notifications** — Weather alerts, spray reminders | 🔄 WIP | 2 days | Backend + Mobile |
| 8 | **Offline Mode** — Cache spray schedules + disease lib | 🔄 WIP | 4 days | Mobile |
| 9 | **Admin Content Management** — CRUD all entities | ✅ Built | — | Backend |
| 10 | **Bug Fixes + Polish** — Crash fixes, UI refinements | 🔄 WIP | 5 days | Both |

### 🟡 Should Have (Post-MVP, Month 1-2)

| # | Feature | Status | Effort |
|---|---------|--------|--------|
| 11 | **Rootstock Guide** — Full guide in mobile app | ✅ Built | — |
| 12 | **Activity Log** — Track sprays, diseases, harvests | 🔄 WIP | 3 days |
| 13 | **Mandi Price Tracking** — Scraper + display | ❌ Not started | 5 days |
| 14 | **Blog / Knowledge Base** — Mobile reading experience | ✅ Built | — |
| 15 | **Expert Consultation** — Chat with agronomists | ❌ Not started | 7 days |
| 16 | **Test Suite** — Pest PHP + Jest coverage 70%+ | 🔄 WIP | 5 days |

### 🟢 Could Have (Month 3-6)

| # | Feature | Status | Effort |
|---|---------|--------|--------|
| 17 | **Input Marketplace** — Pesticides, fertilizers, tools | ❌ Not started | 3 weeks |
| 18 | **Premium Subscription** — Advanced AI, offline maps | ❌ Not started | 2 weeks |
| 19 | **iOS App** — Port React Native to iOS | ❌ Not started | 1 week |
| 20 | **AI Chat Assistant** — Natural language farming Q&A | ❌ Not started | 2 weeks |
| 21 | **Community Forum** — Farmer Q&A, photo sharing | ❌ Not started | 2 weeks |
| 22 | **Cold Storage Directory** — Map + booking | ❌ Not started | 1 week |

### ⚫ Won't Have (Post-PMF)

| # | Feature | Reason |
|---|---------|--------|
| 23 | **IoT Sensors** — Hardware integration | Too expensive, too complex for MVP |
| 24 | **Drone Mapping** — Aerial orchard analysis | Enterprise feature, not smallholder |
| 25 | **Multi-Crop Support** — Beyond apples | Dilutes focus; apple-only is the moat |
| 26 | **Export Compliance** — International trade docs | B2B feature, not farmer-facing |

---

## User Stories (MVP)

### As a Farmer (Guest)
- [x] I can browse the disease library without registering
- [x] I can view variety guides by altitude
- [x] I can see current weather and spray status
- [x] I can read blog articles about apple farming
- [ ] I can view a generic spray schedule for my altitude range

### As a Farmer (Authenticated)
- [x] I can register with email, phone, or social login
- [x] I can set up my orchard profile (area, altitude, varieties)
- [ ] I can receive personalized spray reminders
- [ ] I can log spray applications with date and chemical used
- [ ] I can receive weather-based disease outbreak alerts
- [ ] I can save articles and varieties for offline reading
- [ ] I can view my spray history and orchard activity log

### As an Admin
- [x] I can CRUD diseases, varieties, chemicals, spray schedules
- [x] I can manage blog posts, categories, tags
- [x] I can view user analytics and activity logs
- [x] I can manage user roles and permissions
- [ ] I can send push notifications to all or segmented users

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
- Focus: Auth flows, crashes, UI bugs
- Feedback channel: WhatsApp group

### Phase 2: KVK Partners (Week 3-4)
- 3 Krishi Vigyan Kendras in Shimla district
- 20 farmers per KVK = 60 total
- Focus: Content accuracy, usability for 50+ year olds
- Incentives: Free premium for 1 year

### Phase 3: Open Beta (Week 5-8)
- Play Store open beta track
- Target: 500 downloads
- Focus: Retention, feature usage analytics
- Feedback: In-app feedback form + Google Play reviews

---

## Success Metrics (MVP)

| Metric | Target | Measurement |
|--------|--------|-------------|
| Beta Downloads | 500 | Play Store console |
| Daily Active Users | 100 | Firebase Analytics |
| Spray Schedule Views | 5+ per user/week | Custom event tracking |
| Disease Library Views | 3+ per user/week | Custom event tracking |
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
- [ ] Domain configured (baagicha.app)
- [ ] Firebase project set up (Analytics, Crashlytics, Messaging)
- [ ] Privacy policy and TOS pages live
- [ ] Support email/ WhatsApp number ready
- [ ] KVK partnership agreements signed
- [ ] Press kit ready (logos, screenshots, founder story)

---

## Timeline

```
Week 1-2:   Complete My Orchard + Push Notifications + Offline Mode
Week 3-4:   Mandi Price + Expert Chat + Testing + Bug Fixes
Week 5-6:   Internal Beta → KVK Beta → Feedback Incorporation
Week 7-8:   Open Beta (500 users) → Analytics Review
Week 9-10:  Polish → Play Store Launch
Week 11-12: Post-launch monitoring + first content update
```

---

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Farmers don't trust app advice | Medium | High | Partner with KVKs for credibility |
| Poor connectivity in mountains | High | Medium | Build robust offline mode |
| Wrong spray advice damages crop | Low | Critical | Vet all content with agronomists |
| Orchard Solutions launches app | Medium | High | Speed to market; community moat |
| Single developer burnout | Medium | High | Scope discipline; open-source help |
| Weather API costs explode | Low | Medium | Cache aggressively; use IMD free tier |

---

*Part of the [DreamBoard MVP Planning System](../../../templates/mvp-template.md).*
