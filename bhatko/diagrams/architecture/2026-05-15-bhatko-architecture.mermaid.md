# Bhatko System Architecture

**Idea:** [Bhatko — Spontaneous Travel Platform](../../ideas/developing/2026-05-15-bhatko-spontaneous-travel-platform.md)
**Type:** architecture
**Created:** 2026-05-15

---

## Description

High-level system architecture for the Bhatko spontaneous travel platform. Shows the mobile app, backend services, AI curation engine, and third-party integrations.

## Diagram

```mermaid
graph TB
    subgraph "User Layer"
        MA[Mobile App<br/>React Native / Flutter]
        WA[Web App<br/>Next.js]
    end

    subgraph "API Gateway"
        GW[API Gateway<br/>Rate Limiting / Auth]
    end

    subgraph "Core Services"
        US[User Service<br/>Profiles / Preferences]
        TS[Trip Service<br/>Booking / Itinerary]
        PS[Payment Service<br/>UPI / Cards / Wallets]
        NS[Notification Service<br/>Push / Email / SMS]
        SS[Search Service<br/>Elasticsearch]
    end

    subgraph "AI / ML Layer"
        CE[Curation Engine<br/>Trip Recommendation]
        TP[Taste Profile<br/>User Preference Learning]
        PP[Pricing Engine<br/>Dynamic Deals]
        NL[Natural Language<br/>Chat Interface]
    end

    subgraph "External APIs"
        AM[Amadeus / Sabre<br/>Flights]
        BK[Booking.com API<br/>Hotels]
        AB[Airbnb API<br/>Stays / Experiences]
        IR[IRCTC API<br/>Indian Railways]
        GP[Google Places<br/>Local Data]
    end

    subgraph "Data Layer"
        PG[(PostgreSQL<br/>Primary DB)]
        RD[(Redis<br/>Cache / Sessions)]
        MG[(MongoDB<br/>Logs / Analytics)]
        S3[Object Storage<br/>Images / Docs]
    end

    MA --> GW
    WA --> GW
    GW --> US
    GW --> TS
    GW --> PS
    GW --> NS
    GW --> SS

    US --> PG
    TS --> PG
    PS --> PG
    NS --> RD
    SS --> RD

    CE --> TP
    CE --> PP
    CE --> NL
    CE --> SS

    TS --> AM
    TS --> BK
    TS --> AB
    TS --> IR
    TS --> GP

    US --> S3
    TS --> S3
    PG --> MG
```

## Notes

- **Mobile-first** — React Native or Flutter for iOS + Android
- **AI Curation Engine** — Core differentiator. Python/TensorFlow or use OpenAI API
- **External APIs** — Start with Booking.com Affiliate + Amadeus. Add others later.
- **IRCTC** — Critical for India market (8B passengers/year)
- **Payments** — Must support UPI, Paytm, PhonePe for India
- **Caching** — Redis for session management and frequent queries
- **Scalability** — Services are decoupled; can scale independently
