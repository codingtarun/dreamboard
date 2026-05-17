# Baagvaani System Architecture

**Idea:** [Baagvaani — Apple Orchard Management Platform](../../ideas/developing/2026-05-16-baagvaani-apple-orchard-management.md)
**Type:** architecture
**Created:** 2026-05-16
**Updated:** 2026-05-17

---

## Description

High-level system architecture showing the React Native mobile app, Laravel backend, database layer, external APIs, consultation services, and admin panel. This represents the actual codebase as it exists today in `baagvaaniworkspace/` plus planned integrations for new features.

---

## Diagram

```mermaid
graph TB
    subgraph "Farmer's Smartphone"
        RN[React Native 0.85 App\nTypeScript + Zustand]
        MMKV[MMKV Local Storage\nOffline Cache]
        PUSH[Push Notifications\nFCM / APNs]
        AGORA_SDK[Agora SDK\nVideo Call]
    end

    subgraph "Mobile App Layers"
        direction TB
        TABS[Bottom Tab Navigator\nHome | Spray | Consult | Shop | Discover | MyOrchard]
        STACKS[Nested Stack Navigators\nPer-tab screen pushes]
        SCREENS[30+ Screens\nAuth | Onboarding | Detail | Lists | Calculators]
        HOOKS[Custom Hooks\nuseVarieties | useDiseases | useBlogs | useConsultation]
        WIDGETS[Mini Widgets\nDosageCalc | FertigationCalc | HDPCalc]
        API_CLIENT[Axios API Client\nBase URL: /api/v1]
    end

    subgraph "Laravel 12 Backend"
        direction TB
        GATEWAY[API Gateway\nRate Limiting | CORS | Localization]
        AUTH[Auth Layer\nSanctum Tokens | Socialite | Phone OTP]
        WEB[Web Routes\nPublic Blog | Admin Panel]
        API[API Controllers\nv1 Namespace | JSON Responses]
        ADMIN[Admin Controllers\nCRUD for all entities]
        SERVICES[Service Layer\nBusiness Logic]
        MODELS[Eloquent Models\n40+ Models | Relationships]
    end

    subgraph "Database & Storage"
        MYSQL[(MySQL\nPrimary Database)]
        REDIS[(Redis\nSessions | Cache)]
        MEDIA[Spatie Media Library\nImages | Documents | Videos]
        S3[Object Storage\nDisease Photos | Blog Images | Spray Videos]
    end

    subgraph "External APIs"
        WEATHER[Weather API\nOpenWeatherMap / IMD]
        MANDI[Mandi Price API\nAgmarknet / Custom Scraper]
        SMS[SMS Gateway\nOTP Delivery]
        FCM[Firebase Cloud Messaging\nPush Notifications]
        AGORA[Agora.io\nVideo / Voice Calls]
        RAZORPAY[Razorpay / PayU\nPayments]
    end

    subgraph "Admin & CMS"
        ADMIN_PANEL[Admin Dashboard\nTailwind CSS + AlpineJS]
        BLOG_CMS[Blog CMS\nPosts | Categories | Tags | Comments]
        USER_MGMT[User Management\nRoles | Permissions | Profiles]
        CONTENT_MGMT[Content Management\nDiseases | Varieties | Chemicals | Spray Schedules]
        CONSULT_MGMT[Consultation Management\nExperts | Sessions | Reviews]
        SHOP_MGMT[Shop Management\nProducts | Orders | Inventory]
    end

    RN --> TABS
    TABS --> STACKS
    STACKS --> SCREENS
    SCREENS --> HOOKS
    SCREENS --> WIDGETS
    HOOKS --> API_CLIENT
    API_CLIENT --> GATEWAY

    RN --> MMKV
    RN --> PUSH
    RN --> AGORA_SDK

    GATEWAY --> AUTH
    AUTH --> API
    AUTH --> WEB
    WEB --> ADMIN_PANEL
    WEB --> BLOG_CMS

    API --> SERVICES
    ADMIN --> SERVICES
    SERVICES --> MODELS

    MODELS --> MYSQL
    MODELS --> REDIS
    MODELS --> MEDIA
    MEDIA --> S3

    API --> WEATHER
    API --> MANDI
    API --> SMS
    API --> FCM
    API --> RAZORPAY
    API --> AGORA

    ADMIN_PANEL --> USER_MGMT
    ADMIN_PANEL --> CONTENT_MGMT
    ADMIN_PANEL --> CONSULT_MGMT
    ADMIN_PANEL --> SHOP_MGMT
```

---

## Key Architecture Decisions

1. **React Native + TypeScript** — Single codebase for Android/iOS, fast iteration
2. **Zustand over Redux** — Lightweight state management, less boilerplate
3. **MMKV over AsyncStorage** — 10-100x faster, synchronous reads, encrypted
4. **Laravel Sanctum** — Simple token-based auth for SPA/mobile
5. **Spatie Media Library** — Handles image conversions, responsive images
6. **Spatie Permission** — Role-based admin access (admin, editor, viewer, expert)
7. **Modular Route Files** — `routes/web/app/*.php` + `routes/web/admin/*.php` for organization
8. **API Versioning** — `/api/v1/` prefix for backward compatibility
9. **Agora for Video** — Most cost-effective for Indian market (~$0.0015/min)
10. **Razorpay for Payments** — Native Indian support, UPI, cards, wallets

---

## New Models (Post-Rename / Post-Roadmap)

| Model | Purpose |
|-------|---------|
| `Consultant` | Expert profiles, credentials, ratings |
| `ConsultationSession` | Booking, timing, status, notes |
| `ConsultationType` | Video / Phone / WhatsApp / Visit definitions |
| `ConsultantAvailability` | Time slots per consultant |
| `ConsultationReview` | Farmer ratings after sessions |
| `OrchardBlock` | Sub-divisions within an orchard |
| `BlockCondition` | Per-block soil, health, age tracking |
| `CompatibilityRule` | Chemical pair compatibility matrix |
| `SprayVideo` | Video content linked to spray stages |
| `RewardTransaction` | Points earned/spent ledger |
| `CommunityPost` | Photo-only community feed |
| `ProductReview` | Farmer product reviews (premium) |
| `LowInputGuide` | Regenerative practice content |
| `GovtScheme` | Government scheme database |
| `CalculatorPreset` | Saved calculator configurations |

---

## Scalability Notes

- **Horizontal:** Laravel apps can scale with load balancers; database can shard by region (HP/UK/JK)
- **Caching:** Redis for spray schedules (rarely change), weather data (TTL 1 hour), variety lists
- **CDN:** CloudFront/Cloudflare for disease photos, blog images, spray videos
- **Offline:** MMKV caches spray schedules, disease library, variety data for 7 days
- **Video:** Agora handles video call scaling; no server infrastructure needed
- **Payments:** Razorpay webhooks for async payment confirmation

---

## Security Considerations

1. **Consultation recordings** — Encrypted storage, farmer consent required
2. **Payment data** — PCI-DSS compliant via Razorpay (no card data on our servers)
3. **Orchard data** — Farmer-owned; explicit consent for aggregated data sales
4. **Expert verification** — KYC + credential verification before onboarding
5. **Community moderation** — Auto + manual moderation for community posts
