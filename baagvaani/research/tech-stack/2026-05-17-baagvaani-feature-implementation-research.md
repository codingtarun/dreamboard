# Feature Implementation Research: Baagvaani

**Project:** Baagvaani (बागवाणी) — Apple Orchard Management App
**Date:** 2026-05-17
**Researcher:** AI Curator
**Focus:** How to implement the new features from the spray schedule product roadmap PDF

---

## Executive Summary

This document provides implementation guidance for 10 major feature categories extracted from the product roadmap PDF. Each feature includes: recommended tech approach, estimated effort, key integrations, and implementation pitfalls to avoid.

---

## 1. Personalized Consultation Module

### Feature Requirements
- Video call, telephone, WhatsApp chat, and on-ground orchard visit consultations
- Expert consultant backend dashboard
- Consultant notes visible on farmer's orchard profile
- Premium pricing (₹30-60/session)

### Recommended Implementation

**Video Calls: Agora.io (Recommended)**
| Aspect | Details |
|--------|---------|
| SDK | `react-native-agora` (npm package) |
| Cost | ~$0.0015/minute ( cheapest for Indian market) |
| Features | HD video, screen sharing, recording, low-bandwidth mode |
| Backend | Laravel generates Agora tokens (RTM + RTC) |
| Alternatives | Twilio Video ($0.004/min), Jitsi (self-hosted, complex) |

**WhatsApp Chat: Twilio WhatsApp Business API or Meta Cloud API**
| Aspect | Details |
|--------|---------|
| Approach | Twilio WhatsApp API for programmatic messaging |
| Cost | ~$0.005-0.02 per message (varies by country) |
| Integration | Laravel sends messages via Twilio REST API |
| Limitation | Requires opt-in; 24-hour session window for free-form messages |
| Alternative | Build in-app chat (Socket.io + Laravel Echo) — cheaper but separate from WhatsApp |

**Telephone: Twilio Voice or Exotel**
| Aspect | Details |
|--------|---------|
| Approach | Masked calling (farmer and expert never see real numbers) |
| Cost | ~$0.02-0.05/minute |
| Integration | Laravel initiates calls via API; both parties receive call |

**Orchard Visit Booking**
| Aspect | Details |
|--------|---------|
| Approach | Simple booking system with calendar + location |
| Tech | Laravel + FullCalendar.js (admin) + react-native-calendars (mobile) |
| Payment | Razorpay checkout before booking confirmation |

**Expert Dashboard**
- Build as a separate Laravel route group: `/expert/`
- Use Spatie Permission: `expert` role
- Show assigned farmers, their orchard profiles, add notes
- Notes stored in `consultation_notes` table, linked to `orchard_id`

### Database Schema
```sql
consultants (id, user_id, credentials, specialization, rating, hourly_rate, is_verified)
consultation_types (id, name, duration_minutes, base_price)
consultation_sessions (id, farmer_user_id, consultant_id, type_id, status, scheduled_at, started_at, ended_at, agora_channel_name, total_cost)
consultation_notes (id, session_id, orchard_id, expert_user_id, notes, recommendations, created_at)
consultant_availability (id, consultant_id, day_of_week, start_time, end_time, is_bookable)
```

### Effort Estimate
| Component | Effort |
|-----------|--------|
| Backend API + models | 4 days |
| Expert dashboard (web) | 3 days |
| Mobile video call integration | 5 days |
| Mobile booking flow | 3 days |
| WhatsApp chat integration | 3 days |
| Payment integration | 2 days |
| **Total** | **~20 days** |

### Pitfalls
- **Bandwidth:** Himalayan farmers have poor connectivity → Agora's "Low Stream" mode essential
- **No-shows:** Require pre-payment; implement cancellation policy with partial refund
- **Liability:** Disclaimers needed; expert advice is "suggestive" not "prescriptive"
- **Language:** Hindi-speaking experts critical; video calls need Hindi UI

---

## 2. Enhanced Spray Intelligence

### 2A. Side Effects & Precautions

**Implementation:**
- Add JSON columns to `chemicals` table:
  ```json
  {
    "side_effects": ["Skin irritation", "Eye damage", "Respiratory issues"],
    "precautions": ["Wear gloves", "Use goggles", "Avoid windy days"],
    "ppe_required": ["Nitrile gloves", "Safety goggles", "N95 mask"],
    "phi_days": 14,
    "re_entry_hours": 24,
    "max_temp_celsius": 30,
    "wind_speed_max_kmh": 15
  }
  ```
- Mobile: Show as expandable cards on chemical detail screen
- Pre-spray checklist: Generate dynamic checklist based on selected chemical + weather

**Effort:** 2-3 days (backend + mobile)

### 2B. Compatibility Checker

**Implementation:**
- Create `chemical_compatibility_rules` table:
  ```sql
  chemical_a_id, chemical_b_id, status, notes
  -- status: compatible, incompatible, conditional
  ```
- Algorithm: Farmer selects chemicals → check all pairwise combinations → return matrix result
- UI: Color-coded grid (green = compatible, red = incompatible, yellow = conditional with notes)

**Data Sources:**
- Primary: University extension data (e.g., [Jar Test Method](https://www.uaex.uada.edu/publications/pdf/FSA-2166.pdf))
- Secondary: Agrochemical manufacturer compatibility charts
- Community: Flag incompatible mixes reported by farmers

**Reference Apps:**
- [Mix Tank by Precision Labs](https://www.precisionlab.com/news-resources/mix-tank-app/) — tank mixing sequence app
- [Koppert One Compatibility Database](https://naturalenemies.com/pesticide-compatibility-database/) — biological compatibility

**Effort:** 5-7 days (data entry will take longer than code)

### 2C. Spray Videos

**Implementation:**
- Host on YouTube (free CDN, works on low bandwidth with quality selection)
- Embed using `react-native-youtube-iframe` or WebView
- Or: Host on CloudFront/S3 with HLS streaming for better control
- Keep videos 60-90 seconds max
- Separate audio tracks for Hindi/English, or separate video files

**Effort:** 3 days (code) + ongoing (content production)

---

## 3. Recommendation Engine

### Approach: Rule-Based + Simple ML Hybrid

**Phase 1 (Immediate): Rule-Based Engine**
```
IF altitude < 6000ft AND month == March AND stage == "Bud Break"
  → Recommend: Copper Oxychloride spray
  → Warn: Check for scab pressure if humidity > 70%
  → Suggest: Fertilizer: Calcium Nitrate 2kg/acre

IF orchard_age < 3 years AND rootstock == "M9"
  → Recommend: Higher nitrogen schedule
  → Warn: Monitor for fire blight in warm springs
```

**Tech:**
- Laravel: Rule engine service class
- Store rules as JSON in database (admins can edit without deploy)
- No ML needed initially — rules are deterministic and explainable

**Phase 2 (3-6 months): Simple ML**
- Use farmer feedback on recommendations to improve
- Collaborative filtering: "Farmers with similar orchards used..."
- Can be implemented with simple Python script + Laravel queue jobs

**Data Inputs:**
| Input | Source |
|-------|--------|
| Altitude | GPS / User input |
| Variety | Orchard profile |
| Stage | Calendar + user logs |
| Weather | Weather API |
| Historical sprays | Activity log |
| Disease reports | User submissions |
| Soil type | User input (future: soil test integration) |

**Effort:**
| Phase | Effort |
|-------|--------|
| Rule engine v1 | 5 days |
| Admin rule editor | 2 days |
| Mobile recommendation UI | 3 days |
| ML upgrade (Phase 2) | 2 weeks |

---

## 4. Orchard Profile 2.0 (Multi-Orchard + Blocks)

**Schema Changes:**
```sql
-- Existing: user_orchards table
-- New: orchard_blocks table
orchard_blocks (
  id,
  orchard_id,
  name,              -- e.g., "Block A", "Upper Slope"
  variety_id,
  rootstock_id,
  area_kanal,        -- or acres
  plant_count,
  tree_age_years,
  spacing_meters,
  soil_type,         -- loam, clay, sandy
  soil_ph,
  irrigation_type,   -- drip, sprinkler, flood
  created_at
)
```

**Mobile UI:**
- Orchard list screen (tap to expand)
- Each orchard shows blocks as cards
- Per-block: quick stats + "Get Recommendations" button
- Spray log asks: "Which block?" before logging

**Effort:** 4-5 days

---

## 5. Mini Widgets / Calculators

### 5A. Dosage Calculator

**Formula:**
```
Tank Capacity (L) × Recommended Dose (ml/L) = Chemical per Tank (ml)
Orchard Area (acres) ÷ Spray Coverage per Tank (acres) = Tanks Needed
Total Chemical = Chemical per Tank × Tanks Needed
```

**Mobile:** Simple form with unit converters (kanals ↔ acres, liters ↔ gallons)

**Effort:** 2 days

### 5B. Fertigation Calculator

**Reference Implementation:**
- [Clemson Drip Fertigation Calculator](https://news.clemson.edu/clemson-extension-researchers-develop-new-technology-to-help-vegetable-growers/) — open-source logic
- [Haifa FertiMatch App](https://www.haifa-group.com/fertimatch%E2%84%A2-your-assistant-fertigation-calculations) — industry standard

**Formula:**
```
Injection Rate (L/hr) = (Fertilizer Rate kg/ha × Area ha) ÷ (Fertigation Events × Concentration g/L)
```

**Inputs:** Fertilizer NPK grade, target ppm, drip flow rate, area, irrigation time
**Output:** Fertilizer quantity per tank (g), injection rate (L/hr), schedule

**Effort:** 3-4 days

### 5C. HDP Cost Calculator

**Inputs:**
- Area (acres)
- Plant spacing (m × m)
- Rootstock type (M9, MM106, etc.)
- Trellis type (vertical axis, spindle, etc.)
- Drip irrigation (yes/no)

**Outputs:**
- Total plants needed
- Sapling cost
- Trellis/material cost
- Drip system cost
- Total investment
- Break-even estimate

**Effort:** 3 days

### 5D. Water Requirement Calculator

**Based on:** Rootstock type + tree age + weather + soil type
**Reference:** [Clemson Precision Ag Calculators](https://www.clemson.edu/extension/precision-agriculture/calculators/)

**Effort:** 2-3 days

---

## 6. Community & Gamification

### Community (Photo-Only)

**Why photo-only?**
- Reduces text spam and misinformation
- Visual learning is powerful for farmers
- Easier moderation
- Lower barrier (take a photo vs write a post)

**Implementation:**
- `community_posts` table: `id, user_id, image_url, caption, likes_count, created_at`
- Comments: Simple text, max 200 chars, flagged words filter
- Like system: `community_likes` table
- Feed: Infinite scroll, chronological (start) → algorithmic later

**Tech:**
- Image upload: React Native Image Picker + Laravel Spatie Media
- Feed pagination: Cursor-based (performance)
- Moderation: Auto-flag + manual admin review

### Gamification / Reward Points

**Point System:**
| Action | Points |
|--------|--------|
| Follow spray schedule for a week | 50 |
| Log spray application | 20 |
| Submit feedback after spray | 30 |
| Share photo in community | 10 |
| Complete profile setup | 100 |
| First consultation | 50 |
| Read 5 blog articles | 25 |

**Levels:**
| Level | Name | Points | Benefit |
|-------|------|--------|---------|
| 1 | Sprout | 0 | — |
| 2 | Sapling | 200 | 5% shop discount |
| 3 | Grower | 500 | 10% shop discount |
| 4 | Expert | 1,000 | 15% shop discount + badge |
| 5 | Master Farmer | 2,500 | 20% shop discount + premium feature trial |

**Redemption:**
- 100 points = ₹10 shop discount
- Discounts applied at checkout via coupon code generation

**Effort:**
| Component | Effort |
|-----------|--------|
| Community backend | 3 days |
| Community mobile UI | 3 days |
| Points system backend | 2 days |
| Levels + badges UI | 2 days |
| Redemption integration | 2 days |
| **Total** | **~12 days** |

---

## 7. Shop / Marketplace

### Product Categories
| Category | Examples |
|----------|----------|
| Fungicides | Mancozeb, Carbendazim, Difenoconazole |
| Pesticides | Chlorpyriphos, Acetamiprid, Spinosad |
| Nutrition | NPK 20-20-20, Calcium Nitrate, Boron |
| Tools | Pruners, Sprayers, Ladders |
| Books | Apple cultivation guides, HP Govt manuals |
| Safety Gear | N95 masks, chemical gloves, goggles, spray suits |
| Precision Tools | pH meter, refractometer (Brix), size ring, TDS meter |

### Implementation

**Option A: Simple Affiliate/Lead Model (Recommended for MVP)**
- Don't handle inventory or delivery
- Product listings link to partner websites (Amazon, AgriMart, local dealers)
- Earn affiliate commission (1-5%)
- Much lower operational complexity

**Option B: Full Marketplace (Phase 2)**
- Sellers register, list products
- Baagvaani handles payments (Razorpay)
- Delivery via tie-up with local courier / dealer network
- Commission: 8-15%

**Premium Features:**
- "What other farmers say" — reviews table, visible only to premium users
- Additional discount for paid members — coupon system

**Effort:**
| Approach | Effort |
|----------|--------|
| Affiliate model | 5 days |
| Full marketplace | 3-4 weeks |

---

## 8. Low Input / Regenerative Practices (Paid Wall)

**Content Types:**
- Organic spray schedules (neem, cow urine, bio-pesticides)
- Regenerative practices (cover cropping, composting, mulching)
- Low-cost alternatives to expensive chemicals
- IPM (Integrated Pest Management) protocols

**Implementation:**
- `low_input_guides` table: `id, title, content, category, is_premium, video_url`
- Access control: Middleware checks subscription status
- Mobile: Blurred preview with "Unlock with Premium" CTA

**Effort:** 3 days (code) + ongoing (content)

---

## 9. Content Expansion (Pear, Plum, etc.)

**Implementation:**
- Add `crop_type` enum to varieties, diseases, blogs: `['apple', 'pear', 'plum', 'peach', 'apricot']`
- Filter all queries by user's selected crop types
- Default to apple for existing users

**Content Strategy:**
| Crop | HP Suitability | Priority |
|------|---------------|----------|
| Pear | High (Nashpati) | High |
| Plum | Medium (Aloo Bukhara) | High |
| Peach | Medium | Medium |
| Apricot | High (Ladakh/Kinnaur) | Medium |
| Cherry | Emerging | Low |

**Effort:** 2 days (code) + content creation time

---

## 10. Business Setup Tracker

**Features:**
- Checklist: Register business → GST → Bank account → Udyam → Schemes
- Each item has: description, required documents, apply link, status tracker
- Links to official government portals
- Reminder notifications for pending steps

**Scheme Database:**
| Scheme | Type | Link |
|--------|------|------|
| Udyam Registration | MSME | udyamregistration.gov.in |
| Startup India | Startup | startupindia.gov.in |
| PM-KISAN | Farmer Benefit | pmkisan.gov.in |
| NABARD Subsidy | Loan/Subsidy | nabard.org |
| State Horticulture Mission | State | State-specific |

**Implementation:**
- `govt_schemes` table with scheme details
- `user_business_setup` table tracks user progress
- Simple checklist UI with progress bar

**Effort:** 3-4 days

---

## Implementation Priority Matrix

| Feature | User Impact | Effort | Revenue Potential | Priority |
|---------|-------------|--------|-------------------|----------|
| Side Effects & Precautions | High | Low | Low | **P1** |
| Dosage Calculator | High | Low | Low | **P1** |
| Multi-Orchard + Blocks | High | Medium | Medium | **P1** |
| Compatibility Checker | High | Medium | Low | **P2** |
| Spray Videos | Medium | Low | Low | **P2** |
| Expert Consultation (text) | High | Medium | High | **P2** |
| Community + Rewards | Medium | Medium | Medium | **P3** |
| Fertigation Calculator | Medium | Medium | Low | **P3** |
| Recommendation Engine | High | High | High | **P3** |
| Video Consultation | Medium | Medium | High | **P3** |
| Marketplace (affiliate) | Medium | Low | Medium | **P3** |
| Low Input Practices | Medium | Low | High (premium) | **P4** |
| HDP Calculator | Low | Low | Low | **P4** |
| Govt Schemes Tracker | Medium | Low | Low | **P4** |
| Full Marketplace | High | High | High | **P5** |

---

## Sources

1. [Agora.io Pricing](https://www.agora.io/en/pricing/) — 2026
2. [Twilio Video Pricing](https://www.twilio.com/en-us/video/pricing) — 2026
3. [Razorpay Documentation](https://razorpay.com/docs/) — 2026
4. [Jar Test for Pesticide Compatibility](https://www.uaex.uada.edu/publications/pdf/FSA-2166.pdf) — University of Arkansas
5. [Mix Tank App — Precision Labs](https://www.precisionlab.com/news-resources/mix-tank-app/) — 2026
6. [Clemson Drip Fertigation Calculator](https://news.clemson.edu/clemson-extension-researchers-develop-new-technology-to-help-vegetable-growers/) — 2021
7. [Haifa FertiMatch App](https://www.haifa-group.com/fertimatch%E2%84%A2-your-assistant-fertigation-calculations) — Industry reference
8. [Smart Spray App — UC Davis](https://www.mdpi.com/2077-0472/11/10/916) — 2021
9. [Gamification in Agriculture](https://agrospheresmagazine.vitalbiotech.org/aadmin/articles/Agrospheres-2025-6-9-29-32.pdf) — 2025
