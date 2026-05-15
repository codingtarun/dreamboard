# Diagram Standards

> All visual artifacts in DreamBoard use **Mermaid** syntax. This ensures they render natively on GitHub, in VS Code, in any markdown viewer, and require zero external tools.

## Why Mermaid?

- ✅ Renders on GitHub automatically
- ✅ Version-controllable (it's just text)
- ✅ Editable by both you and AI
- ✅ No build step, no dependencies
- ✅ Exportable to PNG/SVG when needed via GitHub or Mermaid Live Editor

## File Naming

```
YYYY-MM-DD-[idea-slug]-[diagram-type].mermaid.md
```

Examples:
- `2026-05-15-coffee-drone-architecture.mermaid.md`
- `2026-05-15-coffee-drone-user-flow.mermaid.md`
- `2026-05-15-coffee-drone-roadmap.mermaid.md`

## Diagram Types Reference

### 1. System Architecture
```mermaid
graph TB
    User[User] -->|HTTP| LB[Load Balancer]
    LB --> API[API Server]
    API --> DB[(Database)]
    API --> Cache[Redis Cache]
```

### 2. User Flow
```mermaid
flowchart TD
    Start([Start]) --> Login{Logged In?}
    Login -->|Yes| Dashboard[Dashboard]
    Login -->|No| Auth[Auth Screen]
    Auth --> Dashboard
    Dashboard --> Action[Core Action]
    Action --> Success([Success])
```

### 3. Sequence Diagram
```mermaid
sequenceDiagram
    actor U as User
    participant A as App
    participant S as Server
    U->>A: Click button
    A->>S: POST /api/action
    S-->>A: 200 OK
    A-->>U: Show success
```

### 4. Entity Relationship
```mermaid
erDiagram
    USER ||--o{ ORDER : places
    USER {
        int id PK
        string email
        string name
    }
    ORDER {
        int id PK
        int user_id FK
        float total
    }
```

### 5. Gantt Chart (Roadmap)
```mermaid
gantt
    title MVP Roadmap
    dateFormat  YYYY-MM-DD
    section Research
    Market Research      :a1, 2026-05-15, 7d
    section Build
    Core Features        :a2, after a1, 14d
    section Launch
    Beta Release         :a3, after a2, 3d
```

### 6. Mind Map
```mermaid
mindmap
  root((Idea))
    Feature A
      Sub-feature 1
      Sub-feature 2
    Feature B
    Feature C
```

### 7. State Diagram
```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Review: Submit
    Review --> Approved: Pass
    Review --> Draft: Revisions
    Approved --> [*]
```

## Styling Guidelines

- Use clear, descriptive node names
- Group related components with `subgraph`
- Add direction hints (`TB`, `LR`, `RL`, `BT`) for clarity
- Keep diagrams focused — one concept per diagram
- For complex systems, break into multiple diagrams

## Rendering Tips

- On GitHub: Mermaid renders automatically in markdown files
- In VS Code: Install "Markdown Preview Mermaid Support" extension
- Online editor: https://mermaid.live
- Export: Use Mermaid Live Editor to export PNG/SVG when needed
