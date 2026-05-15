# MVP Plan: Bhatko — Weekend Surprise Trips (India)

**Idea:** [Bhatko — Spontaneous Travel Platform](../../ideas/developing/2026-05-15-bhatko-spontaneous-travel-platform.md)
**Date:** 2026-05-15
**Version:** 1.0

---

## MVP Vision

> The smallest version of Bhatko that delivers core value: **A user can open the app, set a budget and dates, and book a complete surprise weekend trip in under 2 minutes.**

**Scope**: Weekend getaways within India, 2-3 days, budget range ₹3,000-₹25,000.

---

## What We're NOT Building (Yet)

- International trips
- Flight bookings (start with train + bus + self-drive)
- Group trip planning (solo/couple only for MVP)
- AI taste profile learning (manual preference form for MVP)
- Local experience marketplace (partner with 1-2 curated hosts)
- Premium subscription
- Offline mode
- Social features

---

## Feature Prioritization (MoSCoW)

### Must-Have (Launch Blockers)

| # | Feature | User Story | Est. Effort | Why Critical |
|---|---------|------------|-------------|--------------|
| 1 | **User Auth** | As a user, I can sign up/login with phone/email | 2 days | Can't book without identity |
| 2 | **Preference Form** | As a user, I can set budget, dates, vibe, dietary prefs | 2 days | Core input for curation |
| 3 | **Surprise Trip Generator** | As a user, I get a curated surprise trip with stay + transport | 5 days | THE core feature |
| 4 | **Trip Card UI** | As a user, I see a beautiful card with teaser info, price, vibe | 3 days | Conversion moment |
| 5 | **One-Tap Booking** | As a user, I can book with UPI/Card in one tap | 4 days | Revenue moment |
| 6 | **Booking Confirmation** | As a user, I receive confirmation + itinerary via email/SMS | 2 days | Trust & fulfillment |
| 7 | **Admin Dashboard** | As an admin, I can manage trips, bookings, and inventory | 4 days | Operations |

### Should-Have (V1.1 — Week 3-4)

| # | Feature | User Story | Est. Effort |
|---|---------|------------|-------------|
| 1 | **Shuffle Trips** | As a user, I can shuffle for another surprise trip | 1 day |
| 2 | **Basic Cancellation** | As a user, I can cancel within 24hrs for full refund | 2 days |
| 3 | **Trip Reveal** | As a user, I can pay a small fee to see destination before booking | 2 days |
| 4 | **Push Notifications** | As a user, I get booking updates and trip reminders | 1 day |

### Could-Have (V1.2 — Month 2)

| # | Feature | User Story | Est. Effort |
|---|---------|------------|-------------|
| 1 | **Saved Trips** | As a user, I can save trips for later | 1 day |
| 2 | **Referral Code** | As a user, I can invite friends for discounts | 2 days |
| 3 | **Trip Rating** | As a user, I can rate my trip after completion | 1 day |

### Won't-Have (Explicit Exclusions)

| # | Feature | Reason |
|---|---------|--------|
| 1 | AI/ML curation | Manual curation for MVP; AI comes after validation |
| 2 | International trips | Focus on India first |
| 3 | Flight bookings | Trains + buses cover most weekend trips; flights add complexity |
| 4 | Group planning | Single user focus for MVP |
| 5 | iOS app | Android first (India market); iOS later |
| 6 | Experience marketplace | Partner with 2-3 hosts manually |

---

## Technical Approach

### Stack

| Layer | Technology | Reason |
|-------|-----------|--------|
| Mobile App | Flutter | Single codebase, fast, beautiful UI |
| Backend | Node.js + Express | Fast to build, great API ecosystem |
| Database | PostgreSQL | Reliable, relational data |
| Cache | Redis | Session + frequent queries |
| AI (V2) | OpenAI API + Python | Start with GPT for curation |
| Payments | Razorpay | Best for India (UPI, cards, wallets) |
| Hosting | AWS / DigitalOcean | Cost-effective, scalable |
| Notifications | Firebase | Push + SMS |

### Architecture
[See full architecture diagram](../../diagrams/architecture/2026-05-15-bhatko-architecture.mermaid.md)

### External APIs (MVP)
- **Booking.com Affiliate API** — Hotel inventory
- **IRCTC API / RailRider** — Train bookings
- **RedBus API** — Bus bookings
- **Google Places API** — Location data

---

## Success Metrics for MVP

| Metric | Definition | Target (Month 1) | Target (Month 3) |
|--------|------------|------------------|------------------|
| App Downloads | Unique installs | 500 | 5,000 |
| Quiz Completions | Users who finish preference form | 300 | 3,000 |
| Surprise Trip Views | Users who see a trip card | 200 | 2,000 |
| Booking Conversion | % of trip views that book | 5% | 8% |
| NPS Score | User satisfaction | >30 | >50 |
| Rebooking Rate | % of users who book again | 10% | 25% |
| CAC | Cost to acquire a booking user | <₹500 | <₹300 |
| Gross Revenue | Total booking value | ₹2L | ₹25L |

---

## Launch Checklist

### Pre-Launch (Week -2)
- [ ] App on Play Store (internal testing)
- [ ] 10 curated weekend trip packages ready
- [ ] 5 hotel partnerships confirmed
- [ ] 2 local experience hosts onboarded
- [ ] Payment gateway (Razorpay) integrated
- [ ] Terms of Service + Privacy Policy
- [ ] Customer support channel (WhatsApp)

### Launch (Week 0)
- [ ] Social media pages live (Instagram, TikTok)
- [ ] Launch post + reels
- [ ] Influencer outreach (5 micro-influencers)
- [ ] Reddit/IndieHackers launch post
- [ ] Friends & family beta

### Post-Launch (Week 1-4)
- [ ] Daily booking monitoring
- [ ] User interview every 3 bookings
- [ ] Bug fixes within 24 hours
- [ ] Content creation (1 reel/day)
- [ ] Iterate based on feedback

---

## Post-Launch Plan

**Month 1**: Prove demand — 50 bookings, measure NPS  
**Month 2**: Improve conversion — A/B test trip cards, pricing  
**Month 3**: Add Should-Haves — shuffle, cancellation, reveal  
**Month 4**: Expand inventory — more cities, more hotel partners  
**Month 5-6**: AI curation V1 — taste profile learning  
**Month 6+**: Raise pre-seed / seed based on metrics

---

## Budget Estimate (MVP)

| Item | Cost (₹) | Cost ($) |
|------|----------|----------|
| Developer (freelance, 2 months) | ₹3,00,000 | $3,500 |
| Flutter dev (freelance, 1 month) | ₹1,50,000 | $1,750 |
| Design (Figma, freelancer) | ₹50,000 | $600 |
| AWS/Hosting (2 months) | ₹20,000 | $250 |
| APIs + Razorpay (transactional) | ₹10,000 | $120 |
| Marketing (ads + influencers) | ₹50,000 | $600 |
| Legal + Compliance | ₹20,000 | $250 |
| **Total** | **₹6,00,000** | **~$7,000** |

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| No bookings | Start with "Concierge MVP" — manually curate first 50 trips |
| Bad trip experience | Over-communicate with hotels, 24/7 WhatsApp support, easy refunds |
| Hotel partners ghost | Have 2x backup options for every destination |
| Payment failures | Razorpay + Cash on Delivery fallback |
| App store rejection | Follow guidelines, submit early, have backup APK distribution |
