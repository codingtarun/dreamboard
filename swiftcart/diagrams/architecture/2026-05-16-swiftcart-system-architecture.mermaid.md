# SwiftCart System Architecture

**Idea:** [SwiftCart — Lightweight Open-Source eCommerce CMS](../../ideas/developing/2026-05-16-swiftcart-lightweight-ecommerce-cms.md)
**Type:** architecture
**Created:** 2026-05-16

---

## Description

High-level architecture of SwiftCart's custom PHP 8.2 MVC framework. Built from scratch with zero external dependencies — no Composer, no npm, no build step. Shows the request lifecycle, core components, theme system, and admin panel.

---

## Diagram

```mermaid
graph TB
    subgraph "Browser / Client"
        STORE[Storefront\nCustomer-facing site]
        ADMIN[Admin Panel\nMerchant dashboard]
        MOBILE[Mobile Browser\nResponsive theme]
    end

    subgraph "Web Server"
        HTACCESS[.htaccess\nRewrite to index.php]
        INDEX[public/index.php\nFront Controller]
    end

    subgraph "Bootstrap Layer"
        BOOTSTRAP[core/bootstrap.php]
        AUTOLOAD[Autoloader.php\nPSR-4 without Composer]
        CONFIG[Config.php\nDot-notation reader]
        HELPERS[helpers.php\ne(), url(), money()]
        ERRORS[ErrorHandler.php\nDebug page + logs]
    end

    subgraph "Application Kernel"
        APP[core/App.php]
        REQUEST[Request.php\nWraps $_GET/$_POST/$_SERVER]
        ROUTER[Router.php\nRegex pattern matching]
        RESPONSE[Response.php\nHTML / JSON / Redirect]
        VIEW[View.php\nTemplate renderer]
    end

    subgraph "Controllers"
        HOMEC[HomeController]
        PRODC[ProductController]
        CARTC[CartController]
        CHECKC[CheckoutController]
        AUTHC[AuthController]
        ACCC[AccountController]
        ADMINC[AdminController]
        STATICC[StaticController]
    end

    subgraph "Middleware"
        CSRF[CsrfMiddleware]
        AUTHM[AuthMiddleware]
        RATE[RateLimitMiddleware]
    end

    subgraph "Models (Phase 5)"
        USERM[UserModel]
        PRODM[ProductModel]
        ORDERM[OrderModel]
        CATM[CategoryModel]
        BASEM[BaseModel\nPDO wrapper]
    end

    subgraph "Database"
        MYSQL[(MySQL 8.0+\nutf8mb4)]
        FILECACHE[(File Cache\nstorage/cache/)]
    end

    subgraph "Theme System"
        THEME[Theme Loader\ntheme.json manifest]
        DEFAULT[Default Theme\nlayouts/ + pages/ + partials/]
        CUSTOM[Custom Themes\nOverride default files]
    end

    subgraph "Admin Assets"
        ADMIN_CSS[admin.css\nCustom styles]
        ADMIN_JS[admin.js\nCharts + interactions]
        CHARTS[charts.js\nSales analytics]
    end

    subgraph "Storefront Assets"
        CSS[style.css\nResponsive styles]
        JS_MODULES[Vanilla JS Modules\ncart.js, modal.js, etc.]
    end

    STORE --> HTACCESS
    ADMIN --> HTACCESS
    MOBILE --> HTACCESS

    HTACCESS --> INDEX
    INDEX --> BOOTSTRAP

    BOOTSTRAP --> AUTOLOAD
    BOOTSTRAP --> CONFIG
    BOOTSTRAP --> HELPERS
    BOOTSTRAP --> ERRORS
    BOOTSTRAP --> APP

    APP --> REQUEST
    APP --> ROUTER
    ROUTER --> CSRF
    CSRF --> AUTHM
    AUTHM --> RATE
    RATE --> HOMEC
    RATE --> PRODC
    RATE --> CARTC
    RATE --> CHECKC
    RATE --> AUTHC
    RATE --> ACCC
    RATE --> ADMINC
    RATE --> STATICC

    HOMEC --> VIEW
    PRODC --> VIEW
    CARTC --> VIEW
    CHECKC --> VIEW
    AUTHC --> VIEW
    ACCC --> VIEW
    ADMINC --> VIEW
    STATICC --> VIEW

    VIEW --> THEME
    THEME --> DEFAULT
    THEME --> CUSTOM

    PRODC --> BASEM
    CARTC --> BASEM
    CHECKC --> BASEM
    AUTHC --> BASEM
    ACCC --> BASEM
    ADMINC --> BASEM

    BASEM --> USERM
    BASEM --> PRODM
    BASEM --> ORDERM
    BASEM --> CATM

    USERM --> MYSQL
    PRODM --> MYSQL
    ORDERM --> MYSQL
    CATM --> MYSQL

    BASEM --> FILECACHE

    ADMIN --> ADMIN_CSS
    ADMIN --> ADMIN_JS
    ADMIN --> CHARTS

    STORE --> CSS
    STORE --> JS_MODULES
```

---

## Key Architecture Decisions

1. **Zero Dependencies** — No Composer means no supply-chain attacks, no version conflicts, no `vendor/` bloat. The entire framework is ~800 lines.
2. **Custom PSR-4 Autoloader** — `spl_autoload_register()` maps namespaces to directories. Understandable in 30 lines.
3. **Native PHP Templating** — No Twig/Smarty compile step. `extract()` + `ob_start()` = template engine in 20 lines.
4. **File-Based Cache** — Works on ₹99 hosting without Redis. Cache files in `storage/cache/` with TTL.
5. **Theme Inheritance** — Custom themes override only the files they need; fall back to default for the rest.
6. **Progressive Enhancement** — PHP renders full HTML. JS modules enhance interactivity. Store works without JavaScript.

---

## Performance Targets

| Metric | Target | How |
|--------|--------|-----|
| TTFB | <200ms | No framework overhead, file cache, minimal autoload |
| Full Page Load | <500ms | No build step, inline critical CSS, lazy images |
| Cart Update | <100ms | Session-based cart, AJAX with JSON response |
| Admin Dashboard | <300ms | File cache for stats, pagination |

---

## Security Model

| Layer | Implementation |
|-------|---------------|
| Passwords | `password_hash()` with bcrypt |
| SQL Injection | PDO prepared statements exclusively |
| XSS | `htmlspecialchars()` via `e()` helper; escape context awareness |
| CSRF | Token per session, validated on POST/PUT/DELETE |
| File Uploads | Real MIME check, random filename, outside doc root |
| Session Fixation | Regenerate ID on privilege change |
| Public Isolation | `public/` is the only web-accessible folder |
