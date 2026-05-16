# Baagicha System Architecture

**Idea:** [Baagicha — Apple Orchard Management Platform](../../ideas/developing/2026-05-16-baagicha-apple-orchard-management.md)
**Type:** architecture
**Created:** 2026-05-16

---

## Description

High-level system architecture showing the React Native mobile app, Laravel backend, database layer, external APIs, and admin panel. This represents the actual codebase as it exists today in `baagichaworkspace/`.

---

## Diagram

```mermaid
graph TB
    subgraph "Farmer's Smartphone"
        RN[React Native 0.85 App\nTypeScript + Zustand]
        MMKV[MMKV Local Storage\nOffline Cache]
        PUSH[Push Notifications\nFCM / APNs]
    end

    subgraph "Mobile App Layers"
        direction TB
        TABS[Bottom Tab Navigator\nHome | Spray | Shop | Discover | MyOrchard]
        STACKS[Nested Stack Navigators\nPer-tab screen pushes]
        SCREENS[20+ Screens\nAuth | Onboarding | Detail | Lists]
        HOOKS[Custom Hooks\nuseVarieties | useDiseases | useBlogs]
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
        MODELS[Eloquent Models\n30+ Models | Relationships]
    end

    subgraph "Database & Storage"
        MYSQL[(MySQL\nPrimary Database)]
        REDIS[(Redis\nSessions | Cache)]
        MEDIA[Spatie Media Library\nImages | Documents]
        S3[Object Storage\nDisease Photos | Blog Images]
    end

    subgraph "External APIs"
        WEATHER[Weather API\nOpenWeatherMap / IMD]
        MANDI[Mandi Price API\nAgmarknet / Custom Scraper]
        SMS[SMS Gateway\nOTP Delivery]
        FCM[Firebase Cloud Messaging\nPush Notifications]
    end

    subgraph "Admin & CMS"
        ADMIN_PANEL[Admin Dashboard\nTailwind CSS + AlpineJS]
        BLOG_CMS[Blog CMS\nPosts | Categories | Tags | Comments]
        USER_MGMT[User Management\nRoles | Permissions | Profiles]
        CONTENT_MGMT[Content Management\nDiseases | Varieties | Chemicals | Spray Schedules]
    end

    RN --> TABS
    TABS --> STACKS
    STACKS --> SCREENS
    SCREENS --> HOOKS
    HOOKS --> API_CLIENT
    API_CLIENT --> GATEWAY

    RN --> MMKV
    RN --> PUSH

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

    ADMIN_PANEL --> USER_MGMT
    ADMIN_PANEL --> CONTENT_MGMT
```

---

## Key Architecture Decisions

1. **React Native + TypeScript** — Single codebase for Android/iOS, fast iteration
2. **Zustand over Redux** — Lightweight state management, less boilerplate
3. **MMKV over AsyncStorage** — 10-100x faster, synchronous reads, encrypted
4. **Laravel Sanctum** — Simple token-based auth for SPA/mobile
5. **Spatie Media Library** — Handles image conversions, responsive images
6. **Spatie Permission** — Role-based admin access (admin, editor, viewer)
7. **Modular Route Files** — `routes/web/app/*.php` + `routes/web/admin/*.php` for organization
8. **API Versioning** — `/api/v1/` prefix for backward compatibility

---

## Scalability Notes

- **Horizontal:** Laravel apps can scale with load balancers; database can shard by region (HP/UK/JK)
- **Caching:** Redis for spray schedules (rarely change), weather data (TTL 1 hour), variety lists
- **CDN:** CloudFront/Cloudflare for disease photos and blog images
- **Offline:** MMKV caches spray schedules, disease library, variety data for 7 days
