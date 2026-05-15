# Bhatko Business Model Flow

**Idea:** [Bhatko — Spontaneous Travel Platform](../../ideas/developing/2026-05-15-bhatko-spontaneous-travel-platform.md)
**Type:** business
**Created:** 2026-05-15

---

## Description

Visual flow of how Bhatko creates and captures value. Shows the user journey, revenue streams, and key partnerships.

## Diagram

```mermaid
flowchart TD
    subgraph "Discovery"
        A[Social Media / SEO / Ads] --> B[Downloads App / Visits Web]
        B --> C[Takes Bhatko Quiz<br/>Budget + Dates + Vibe]
    end

    subgraph "Curation"
        C --> D[AI Curation Engine<br/>Analyzes Taste Profile]
        D --> E[Surprise Trip Generated<br/>Flights + Stay + Experiences]
        E --> F{User Approves?}
        F -->|Yes| G[One-Tap Booking]
        F -->|No| H[Adjust Preferences]<-->D
        F -->|Shuffle| D
    end

    subgraph "Booking & Travel"
        G --> I[Payment Processed]
        I --> J[Itinerary Generated]
        J --> K[Travel Period]
        K --> L[Experiences Unlocked]
        L --> M[User Shares Story]
    end

    subgraph "Revenue Streams"
        G --> N[Commission<br/>8-15% on bookings]
        G --> O[Bhatko Premium<br/>$9/month subscription]
        L --> P[Experience Fees<br/>10-20% on local experiences]
        M --> Q[Affiliate Revenue<br/>Referral commissions]
        O --> R[B2B White-Label<br/>Corporate retreats]
    end

    subgraph "Key Partners"
        S[Hotels / Hostels]
        T[Airlines / Railways]
        U[Local Experience Hosts]
        V[Payment Processors]
        W[Influencers / Affiliates]
    end

    I --> V
    G --> S
    G --> T
    L --> U
    A --> W

    style N fill:#90EE90
    style O fill:#90EE90
    style P fill:#90EE90
    style Q fill:#90EE90
    style R fill:#90EE90
```

## Revenue Model Summary

| Stream | Description | Margin | Volume |
|--------|-------------|--------|--------|
| Booking Commission | % of flight/hotel/experience bookings | 8-15% | High |
| Bhatko Premium | Monthly subscription for advanced AI, perks | $9/mo | Medium |
| Experience Fees | % of local experience bookings | 10-20% | Medium |
| Affiliate Revenue | Referral fees from partners | 3-8% | Medium |
| B2B White-Label | Corporate retreat planning tool | Custom | Low |

## Unit Economics (Target)

- **Average Booking Value**: $300
- **Commission per Booking**: $30 (10%)
- **Customer Acquisition Cost**: $15
- **Lifetime Value**: $150 (5 rebookings)
- **LTV:CAC Ratio**: 10:1 ✓
