# System Architecture - AI Food Ordering

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         END USERS                            │
│                     (300M+ ChatGPT Users)                    │
└────────────────────────────┬────────────────────────────────┘
                             │
                             │ Natural Language
                             │ "I want Indian food"
                             │
┌────────────────────────────▼────────────────────────────────┐
│                    AI PLATFORMS                              │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐             │
│  │ ChatGPT  │    │  Gemini  │    │  Claude  │             │
│  │ Custom   │    │Extensions│    │Tool Use  │             │
│  │   GPT    │    │          │    │          │             │
│  └──────────┘    └──────────┘    └──────────┘             │
└────────────────────────────┬────────────────────────────────┘
                             │
                             │ HTTPS / REST API
                             │ OpenAPI Actions
                             │
┌────────────────────────────▼────────────────────────────────┐
│              BOUNT MIDDLEWARE API (FastAPI)                  │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  API Endpoints                                       │   │
│  │  • POST /api/v1/restaurants/search                  │   │
│  │  • GET  /api/v1/restaurants/{id}                    │   │
│  │  • GET  /api/v1/restaurants/{id}/menu               │   │
│  │  • POST /api/v1/orders/create                       │   │
│  │  • GET  /api/v1/orders/{id}                         │   │
│  │  • POST /api/v1/orders/{id}/payment                 │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Business Logic Layer                                │   │
│  │  • Request validation                                │   │
│  │  • Data transformation                               │   │
│  │  • Error handling                                    │   │
│  │  • Logging & monitoring                              │   │
│  │  • Rate limiting                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Adapter Layer (Nomnom Integration)                  │   │
│  │  • Format translation                                │   │
│  │  • API client management                             │   │
│  │  • Caching strategy                                  │   │
│  │  • Fallback handling                                 │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────────────┬────────────────────────────────┘
                             │
                             │ REST API / GraphQL
                             │ Authentication
                             │
┌────────────────────────────▼────────────────────────────────┐
│                    NOMNOM PLATFORM                           │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Restaurant Management                               │   │
│  │  • Restaurant profiles                               │   │
│  │  • Menu management                                   │   │
│  │  • Availability tracking                             │   │
│  │  • Pricing & promotions                              │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Order Management                                    │   │
│  │  • Order processing                                  │   │
│  │  • Status tracking                                   │   │
│  │  • Payment processing                                │   │
│  │  • Delivery coordination                             │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────────────┬────────────────────────────────┘
                             │
                             │ POS Integration
                             │ Delivery APIs
                             │
┌────────────────────────────▼────────────────────────────────┐
│                 RESTAURANT ECOSYSTEM                         │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │Restaurant│  │   POS    │  │ Payment  │  │ Delivery │   │
│  │ Systems  │  │ Systems  │  │ Gateway  │  │ Services │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow - Complete Order Journey

```
1. DISCOVERY
   User: "I want Indian food"
   ↓
   ChatGPT → searchRestaurants(cuisine="Indian")
   ↓
   Our API → Nomnom API → Restaurant Database
   ↓
   Response: List of Indian restaurants
   ↓
   ChatGPT displays: "Found 3 Indian restaurants..."

2. MENU BROWSING
   User: "Show menu from Taj Palace"
   ↓
   ChatGPT → getRestaurantMenu(id="rest_001")
   ↓
   Our API → Nomnom API → Restaurant Menu System
   ↓
   Response: Complete menu with categories, items, prices
   ↓
   ChatGPT displays formatted menu

3. ORDER COMPOSITION
   User: "I'll have paneer butter masala and garlic naan"
   ↓
   ChatGPT builds order object internally
   ↓
   ChatGPT asks for confirmation and delivery address

4. ORDER PLACEMENT
   User: "123 Main St, SF"
   ↓
   ChatGPT → createOrder({items, address, ...})
   ↓
   Our API validates and transforms request
   ↓
   Nomnom API → Restaurant POS
   ↓
   Response: Order ID, total, estimated delivery
   ↓
   ChatGPT: "Order confirmed! ID: order_0001"

5. PAYMENT
   ChatGPT → processPayment(order_id, payment_method)
   ↓
   Our API → Payment Gateway (Stripe/Square)
   ↓
   Response: Transaction ID, success
   ↓
   ChatGPT: "Payment successful!"

6. TRACKING
   User: "Where's my order?"
   ↓
   ChatGPT → getOrder(order_id)
   ↓
   Our API → Nomnom API → Delivery System
   ↓
   Response: Status, location, ETA
   ↓
   ChatGPT: "Your order is being prepared..."
```

## Component Architecture

### 1. FastAPI Application (`main.py`)

```
┌─────────────────────────────────────────┐
│         FastAPI Application             │
│                                         │
│  ┌────────────────────────────────┐    │
│  │  Middleware Stack               │    │
│  │  • CORS                         │    │
│  │  • Request Logging              │    │
│  │  • Error Handling               │    │
│  │  • Rate Limiting (future)       │    │
│  └────────────────────────────────┘    │
│                                         │
│  ┌────────────────────────────────┐    │
│  │  Route Handlers                 │    │
│  │  • /restaurants/search          │    │
│  │  • /restaurants/{id}            │    │
│  │  • /restaurants/{id}/menu       │    │
│  │  • /orders/create               │    │
│  │  • /orders/{id}                 │    │
│  │  • /orders/{id}/payment         │    │
│  └────────────────────────────────┘    │
│                                         │
│  ┌────────────────────────────────┐    │
│  │  Pydantic Models                │    │
│  │  • Restaurant                   │    │
│  │  • Menu, MenuItem               │    │
│  │  • Order, OrderItem             │    │
│  │  • Payment                      │    │
│  └────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

### 2. Mock Data Layer (`mock_data.py`)

```
┌─────────────────────────────────────────┐
│         Mock Data Layer                 │
│                                         │
│  ┌────────────────────────────────┐    │
│  │  RESTAURANTS                    │    │
│  │  • 8 restaurants                │    │
│  │  • Multiple cuisines            │    │
│  │  • Location data                │    │
│  │  • Ratings, fees, hours         │    │
│  └────────────────────────────────┘    │
│                                         │
│  ┌────────────────────────────────┐    │
│  │  MENUS                          │    │
│  │  • 50+ menu items               │    │
│  │  • Categorized                  │    │
│  │  • Prices, descriptions         │    │
│  │  • Dietary info                 │    │
│  └────────────────────────────────┘    │
│                                         │
│  ┌────────────────────────────────┐    │
│  │  ORDERS (In-Memory)             │    │
│  │  • Order tracking               │    │
│  │  • Status management            │    │
│  │  • Payment records              │    │
│  └────────────────────────────────┘    │
│                                         │
│  ┌────────────────────────────────┐    │
│  │  Helper Functions               │    │
│  │  • Search/filter                │    │
│  │  • Data transformation          │    │
│  │  • Order calculations           │    │
│  └────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

### 3. Future: Nomnom Adapter

```
┌─────────────────────────────────────────┐
│       Nomnom Adapter Layer              │
│                                         │
│  ┌────────────────────────────────┐    │
│  │  NomNomAdapter Class            │    │
│  │  • Authentication               │    │
│  │  • Session management           │    │
│  │  • Request/response logging     │    │
│  └────────────────────────────────┘    │
│                                         │
│  ┌────────────────────────────────┐    │
│  │  Data Transformers              │    │
│  │  • Nomnom → Our format          │    │
│  │  • Our format → Nomnom          │    │
│  │  • Error mapping                │    │
│  └────────────────────────────────┘    │
│                                         │
│  ┌────────────────────────────────┐    │
│  │  API Methods                    │    │
│  │  • search_restaurants()         │    │
│  │  • get_menu()                   │    │
│  │  • create_order()               │    │
│  │  • track_order()                │    │
│  └────────────────────────────────┘    │
│                                         │
│  ┌────────────────────────────────┐    │
│  │  Caching Layer                  │    │
│  │  • Restaurant cache (5 min)     │    │
│  │  • Menu cache (15 min)          │    │
│  │  • Cache invalidation           │    │
│  └────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

## Deployment Architecture

### Development (Current)

```
┌──────────────────┐
│  Local Machine   │
│                  │
│  ┌────────────┐  │
│  │ FastAPI    │  │
│  │ :8000      │  │
│  └────────────┘  │
│                  │
│  ┌────────────┐  │
│  │ ngrok      │  │
│  │ Tunnel     │  │
│  └────────────┘  │
└────────┬─────────┘
         │
         │ HTTPS
         │
┌────────▼─────────┐
│   ChatGPT        │
│   Custom GPT     │
└──────────────────┘
```

### Production (Target)

```
┌──────────────────────────────────────────┐
│         Cloud Provider                    │
│         (Railway/Heroku/AWS)              │
│                                           │
│  ┌────────────────────────────────────┐  │
│  │  Load Balancer                     │  │
│  │  • SSL Termination                 │  │
│  │  • Rate Limiting                   │  │
│  └──────────┬─────────────────────────┘  │
│             │                             │
│  ┌──────────▼─────────────────────────┐  │
│  │  API Instances (Auto-scaling)      │  │
│  │  ┌─────────┐  ┌─────────┐         │  │
│  │  │FastAPI 1│  │FastAPI 2│  ...    │  │
│  │  └─────────┘  └─────────┘         │  │
│  └──────────┬─────────────────────────┘  │
│             │                             │
│  ┌──────────▼─────────────────────────┐  │
│  │  Redis Cache                       │  │
│  │  • Restaurant data                 │  │
│  │  • Menu data                       │  │
│  │  • Session data                    │  │
│  └────────────────────────────────────┘  │
│                                           │
│  ┌────────────────────────────────────┐  │
│  │  PostgreSQL Database               │  │
│  │  • Order history                   │  │
│  │  • User preferences                │  │
│  │  • Analytics                       │  │
│  └────────────────────────────────────┘  │
│                                           │
│  ┌────────────────────────────────────┐  │
│  │  Monitoring & Logging              │  │
│  │  • Sentry (errors)                 │  │
│  │  • CloudWatch (metrics)            │  │
│  │  • ELK Stack (logs)                │  │
│  └────────────────────────────────────┘  │
└───────────────────────────────────────────┘
```

## Security Architecture

```
┌─────────────────────────────────────────┐
│         Security Layers                  │
│                                          │
│  1. API Authentication                   │
│     • API Key (X-API-Key header)        │
│     • Rate limiting per key             │
│     • IP whitelisting (optional)        │
│                                          │
│  2. Request Validation                   │
│     • Pydantic models                   │
│     • Input sanitization                │
│     • SQL injection prevention          │
│                                          │
│  3. Payment Security                     │
│     • PCI DSS compliance                │
│     • Tokenized payments                │
│     • No card data storage              │
│                                          │
│  4. Data Protection                      │
│     • HTTPS only                        │
│     • Encrypted at rest                 │
│     • Encrypted in transit              │
│                                          │
│  5. Access Control                       │
│     • Role-based access                 │
│     • Restaurant-level permissions      │
│     • Admin vs user separation          │
│                                          │
│  6. Monitoring                           │
│     • Anomaly detection                 │
│     • Failed auth attempts              │
│     • Suspicious patterns               │
└─────────────────────────────────────────┘
```

## Scaling Strategy

### Phase 1: MVP (0-1K orders/day)
- Single server
- In-memory caching
- Simple logging
- Manual monitoring

### Phase 2: Growth (1K-10K orders/day)
- Multiple servers
- Redis caching
- Database for persistence
- Automated monitoring

### Phase 3: Scale (10K-100K orders/day)
- Auto-scaling
- CDN for static content
- Database read replicas
- Advanced caching
- Queue-based processing

### Phase 4: Enterprise (100K+ orders/day)
- Multi-region deployment
- Microservices architecture
- Event-driven design
- Real-time analytics
- ML-powered recommendations

## Technology Stack

```
┌─────────────────────────────────────────┐
│         Technology Stack                 │
│                                          │
│  Backend                                 │
│  • Python 3.11+                         │
│  • FastAPI (web framework)              │
│  • Uvicorn (ASGI server)                │
│  • Pydantic (data validation)           │
│                                          │
│  Database (Future)                       │
│  • PostgreSQL (primary)                 │
│  • Redis (caching)                      │
│                                          │
│  AI Integration                          │
│  • OpenAI Custom GPT                    │
│  • Google Gemini Extensions             │
│  • Anthropic Claude Tool Use            │
│                                          │
│  External Services                       │
│  • Nomnom API (restaurant platform)     │
│  • Stripe/Square (payments)             │
│  • Twilio (notifications)               │
│                                          │
│  DevOps                                  │
│  • Docker (containerization)            │
│  • GitHub Actions (CI/CD)               │
│  • Railway/Heroku (hosting)             │
│  • Sentry (error tracking)              │
│                                          │
│  Monitoring                              │
│  • Prometheus (metrics)                 │
│  • Grafana (dashboards)                 │
│  • ELK Stack (logging)                  │
└─────────────────────────────────────────┘
```

## API Request Flow Example

```
1. User Input
   "I want Indian food"
   
2. ChatGPT Processing
   Intent: Search restaurants
   Parameters: cuisine="Indian"
   
3. API Call
   GET /api/v1/restaurants/search?cuisine=Indian
   
4. Middleware
   • Log request
   • Validate parameters
   • Check rate limit
   
5. Business Logic
   • Parse cuisine parameter
   • Apply filters
   • Get user location (if available)
   
6. Data Layer
   Mock: Query RESTAURANTS dict
   Future: Call Nomnom API
   
7. Data Transformation
   • Format response
   • Add computed fields
   • Filter sensitive data
   
8. Response
   {
     "restaurants": [
       {
         "id": "rest_001",
         "name": "Taj Palace",
         "cuisine": "Indian",
         ...
       }
     ]
   }
   
9. Middleware
   • Log response
   • Add headers
   • Track metrics
   
10. ChatGPT Processing
    • Parse response
    • Format for user
    • Generate natural language
    
11. User Output
    "I found 1 Indian restaurant near you:
     Taj Palace - 4.5⭐ - 30-45 min - $3.99 delivery"
```

## Error Handling Flow

```
┌─────────────────────────────────────────┐
│         Error Handling Strategy          │
│                                          │
│  1. Validation Errors (400)              │
│     • Missing parameters                 │
│     • Invalid format                     │
│     • Out of range values                │
│     → Return clear error message         │
│                                          │
│  2. Not Found Errors (404)               │
│     • Restaurant not found               │
│     • Order not found                    │
│     → Suggest alternatives               │
│                                          │
│  3. Business Logic Errors (422)          │
│     • Restaurant closed                  │
│     • Item unavailable                   │
│     • Delivery area not covered          │
│     → Explain reason, offer options      │
│                                          │
│  4. External API Errors (502/503)        │
│     • Nomnom API down                    │
│     • Payment gateway timeout            │
│     → Retry logic, fallback, notify      │
│                                          │
│  5. Internal Errors (500)                │
│     • Unexpected exceptions              │
│     • Database errors                    │
│     → Log, alert, graceful degradation   │
└─────────────────────────────────────────┘
```

## Performance Optimization

```
┌─────────────────────────────────────────┐
│      Performance Optimization            │
│                                          │
│  1. Caching Strategy                     │
│     • Restaurant data: 5 min TTL        │
│     • Menu data: 15 min TTL             │
│     • User preferences: 1 hour TTL      │
│                                          │
│  2. Database Optimization                │
│     • Indexed queries                   │
│     • Connection pooling                │
│     • Read replicas                     │
│                                          │
│  3. API Optimization                     │
│     • Response compression (gzip)       │
│     • Pagination for large results      │
│     • Partial responses                 │
│                                          │
│  4. Network Optimization                 │
│     • CDN for static content            │
│     • HTTP/2                            │
│     • Connection keep-alive             │
│                                          │
│  5. Code Optimization                    │
│     • Async/await                       │
│     • Lazy loading                      │
│     • Efficient algorithms              │
└─────────────────────────────────────────┘
```

## Monitoring & Observability

```
┌─────────────────────────────────────────┐
│      Monitoring Dashboard                │
│                                          │
│  Key Metrics                             │
│  • Requests per minute                  │
│  • Average response time                │
│  • Error rate                           │
│  • Success rate                         │
│  • Active orders                        │
│                                          │
│  Business Metrics                        │
│  • Orders per hour                      │
│  • Average order value                  │
│  • Restaurant utilization               │
│  • User retention                       │
│                                          │
│  Technical Metrics                       │
│  • CPU usage                            │
│  • Memory usage                         │
│  • Database connections                 │
│  • Cache hit rate                       │
│                                          │
│  Alerts                                  │
│  • Error rate > 5%                      │
│  • Response time > 2s                   │
│  • API downtime                         │
│  • Payment failures                     │
└─────────────────────────────────────────┘
```

This architecture is designed to:
- ✅ Scale from POC to production
- ✅ Handle millions of requests
- ✅ Maintain <2s response times
- ✅ Ensure 99.9% uptime
- ✅ Support multiple AI platforms
- ✅ Easy Nomnom integration
- ✅ Secure and compliant

