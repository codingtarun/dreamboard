# SwiftCart Request Lifecycle

**Idea:** [SwiftCart — Lightweight Open-Source eCommerce CMS](../../ideas/developing/2026-05-16-swiftcart-lightweight-ecommerce-cms.md)
**Type:** flow
**Created:** 2026-05-16

---

## Description

Every HTTP request in SwiftCart follows this exact path — from browser through `.htaccess`, front controller, bootstrap, application kernel, router, middleware, controller, and finally to view rendering or JSON response.

---

## Diagram

```mermaid
flowchart TD
    BROWSER[Browser Request\nGET /product/iphone-case]

    BROWSER --> HTACCESS[.htaccess\nRewriteRule → index.php]

    HTACCESS --> INDEX[public/index.php\n1. Define ROOT, APP, CORE constants\n2. require core/bootstrap.php]

    INDEX --> BOOTSTRAP[core/bootstrap.php\nBoot Sequence:]

    subgraph "Bootstrap Phase"
        direction TB
        AUTOLOAD[1. Autoloader::register()\nspl_autoload_register PSR-4]
        HELPERS[2. require helpers.php\ne(), url(), money(), dd()]
        CONFIG[3. Config::load(config/)\napp.php + store.php]
        ERRORS[4. ErrorHandler::register()\nset_error_handler + exception + shutdown]
        APPRUN[5. App::run()]
    end

    BOOTSTRAP --> AUTOLOAD --> HELPERS --> CONFIG --> ERRORS --> APPRUN

    APPRUN --> APP[core/App.php]

    APP --> REQUEST[Request.php\nnew Request\n$_GET, $_POST, $_SERVER, JSON body]
    APP --> ROUTER[Router.php\nnew Router]
    APP --> ROUTES[require routes/web.php\nRegister URL patterns]

    ROUTES --> DISPATCH[Router::dispatch\nMatch URI to pattern]

    DISPATCH --> MATCH{Route Match?}

    MATCH -->|No| FOUR04[Response::error\n404 Not Found]
    MATCH -->|Yes| PARAMS[Extract {params}\nNamed capture groups]

    PARAMS --> MIDDLEWARE[Middleware Stack\nOnion pattern]

    subgraph "Middleware Onion"
        direction TB
        CSRF[CsrfMiddleware\nValidate token]
        AUTH[AuthMiddleware\nCheck session/login]
        RATE[RateLimitMiddleware\nThrottle requests]
    end

    MIDDLEWARE --> CSRF --> AUTH --> RATE

    CSRF -->|Invalid| CSRF_ERR[Response::error\n403 Forbidden]
    AUTH -->|Not logged in| AUTH_RED[Response::redirect\n/login]

    RATE --> CONTROLLER[Controller@method\nProductController@show]

    CONTROLLER --> VALIDATE[Validate Input\nSanitize + type check]
    VALIDATE --> MODEL[Model Query\nProductModel::findBySlug]
    MODEL --> DB[(MySQL via PDO\nPrepared statements)]
    DB --> DATA[Data Array\nProduct + related]

    DATA --> OUTPUT{Response Type?}

    OUTPUT -->|HTML| VIEW[View::render\nTemplate + Layout]
    OUTPUT -->|JSON| JSON[Response::json\nAPI / AJAX]
    OUTPUT -->|Redirect| REDIR[Response::redirect\n302 Location]

    VIEW --> THEME[Theme Resolution\ndefault/ + custom fallback]
    THEME --> PAGE[Render Page Template\nob_start + extract + include]
    PAGE --> LAYOUT[Render Layout\nWrap $content in main.php]
    LAYOUT --> HTML[Send HTML\nheader + echo]

    JSON --> API_RESP[Send JSON\nContent-Type: application/json]
    REDIR --> REDIR_RESP[Send Redirect\nheader Location + exit]

    HTML --> BROWSER_RESP[Browser Renders Page]
    API_RESP --> BROWSER_RESP
    REDIR_RESP --> BROWSER_RESP
```

---

## Lifecycle Timing Breakdown (Target)

| Stage | Target Time | Notes |
|-------|-------------|-------|
| `.htaccess` → `index.php` | <1ms | Apache rewrite |
| Bootstrap (autoload + config + helpers) | <5ms | File reads, no network |
| Router dispatch + match | <2ms | Regex on URI string |
| Middleware stack | <5ms | Session read, CSRF check |
| Controller logic | <10ms | Input validation, model calls |
| Database query (cached) | <5ms | File cache hits |
| Database query (uncached) | <50ms | PDO prepared statement |
| View rendering | <10ms | Native PHP `include` |
| **Total TTFB** | **<100ms** | **Best case with cache** |
| **Total TTFB** | **<200ms** | **Worst case without cache** |

---

## Two Output Paths

### HTML Response (Page Load)
```
Controller → View::render('pages/product', $data)
  → find template file
  → ob_start()
  → include page template (product.php)
  → $content = ob_get_clean()
  → include layout (main.php) with $content
  → echo complete HTML
```

### JSON Response (AJAX / API)
```
Controller → Response::json(['success' => true, 'cart' => $cart])
  → header('Content-Type: application/json')
  → echo json_encode($data)
  → exit
```
