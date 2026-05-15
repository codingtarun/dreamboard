# Bhatko User Flow — Surprise Trip Booking

**Idea:** [Bhatko — Spontaneous Travel Platform](../../ideas/developing/2026-05-15-bhatko-spontaneous-travel-platform.md)
**Type:** flow
**Created:** 2026-05-15

---

## Description

Core user flow for booking a surprise trip on Bhatko. From app open to booking confirmation.

## Diagram

```mermaid
flowchart TD
    Start([Open Bhatko App]) --> Onboard{First Time?}
    
    Onboard -->|Yes| Quiz[Bhatko Taste Quiz<br/>• Budget range<br/>• Travel style<br/>• Dietary prefs<br/>• Activity level<br/>• Solo/Group]
    Onboard -->|No| Home[Home Screen]
    
    Quiz --> Profile[Save Taste Profile]
    Profile --> Home
    
    Home --> Action{Choose Action}
    
    Action -->|Surprise Me| Inputs[Set Basic Constraints<br/>• Dates<br/>• Budget<br/>• Max travel time]
    Action -->|Browse| Discover[Discover Feed<br/>Trending destinations]
    Action -->|Groups| GroupFlow[Group Trip Planning]
    
    Inputs --> AI[AI Curation Engine<br/>Matches taste profile]
    AI --> TripCard[Surprise Trip Card<br/>• Mystery destination<br/>• Price breakdown<br/>• Vibe tags<br/>• Teaser images]
    
    TripCard --> Decision{User Action}
    
    Decision -->|Book Now| Checkout[One-Tap Checkout<br/>Apple Pay / UPI / Card]
    Decision -->|Shuffle| AI
    Decision -->|Peek| Reveal[Reveal Destination<br/>Small fee or Premium]
    Decision -->|Save| Saved[Saved Trips]
    
    Reveal --> Checkout
    Saved --> TripCard
    
    Checkout --> Confirm[Booking Confirmed!]
    Confirm --> Itinerary[Dynamic Itinerary<br/>• Day-by-day plan<br/>• Experience vouchers<br/>• Local tips<br/>• Emergency contacts]
    
    Itinerary --> Travel[Travel Period]
    Travel --> Experiences[Unlock Experiences<br/>QR codes / Host contacts]
    
    Experiences --> Share[Share Bhatko Story<br/>Photos / Reels / Review]
    Share --> Rebook[Rebooking Prompt<br/>Discount for next Bhatko]
    Rebook --> Home
    
    Discover --> TripCard
    GroupFlow --> Inputs

    style Start fill:#FFD700
    style Confirm fill:#90EE90
    style Share fill:#87CEEB
```

## Key UX Principles

1. **Speed** — From app open to booking in < 2 minutes
2. **Trust** — Clear price breakdown, flexible cancellation, 24/7 support
3. **Delight** — Mystery destination reveal is a dopamine moment
4. **Social** — Easy sharing creates organic growth
5. **Rebooking** — Post-trip nudge with personalized discount
