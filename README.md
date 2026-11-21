# SAT & SAGBS — Company Websites

Two independent company websites in one Python application. `/` always opens
company selection. SAT retains its English/Tamil website under `/sat`; SAGBS
has a complete corporate website under `/sagbs`.

## Stack and architecture

- **Server:** Python 3.11+, FastAPI, Jinja2, Pydantic. No Node build step.
- **SAT:** existing Bootstrap 5 / custom CSS / vanilla JavaScript website,
  bilingual content, SMTP notifications and optional Google Sheets logging.
- **SAGBS:** HTML5, CSS3, ES6 JavaScript, locally served Bootstrap 5 and
  Bootstrap Icons. GSAP + ScrollTrigger reveals, desktop Lenis scrolling,
  and an original lightweight Lottie illustration. Reduced-motion preferences
  disable animated enhancement; page content remains available without it.
- **SAGBS enquiries:** SQLAlchemy with SQLite locally and persistent
  PostgreSQL in production. Validated input is committed before success;
  SMTP notification is a separate, optional step. SAT enquiries keep their
  original integrations and are not written to SAGBS's database.
- **Deployment:** existing Vercel Python entrypoint and static routing.

```text
Browser
  /                   Company selection
  /sat                Redirect → /sat/en/ (existing bilingual site)
  /sagbs              SAGBS corporate website
                          │
                          └─ POST /sagbs/api/enquiries
                               Validate + burst guard + honeypot
                               → Commit database row
                               → Attempt SMTP notification
                               → Return saved enquiry reference
```

## Sitemap

| URL | Purpose |
| --- | --- |
| `/` | Company selection |
| `/sat` | SAT entrypoint → `/sat/en/` |
| `/sat/en/`, `/sat/ta/` | SAT homepages |
| `/sat/{lang}/{page}` | Existing SAT pages in English or Tamil |
| `/sagbs` | SAGBS homepage |
| `/sagbs/about` | Company, mission, vision, values and approach |
| `/sagbs/services` | All seven service divisions |
| `/sagbs/services/data-entry` | Data Entry Services |
| `/sagbs/services/data-management` | Data Processing & Data Management |
| `/sagbs/services/data-analytics` | Data Analytics & Business Intelligence |
| `/sagbs/services/bpo-services` | Back-Office & BPO Services |
| `/sagbs/services/website-development` | Website Development & Digital Solutions |
| `/sagbs/services/software-development` | Software & Web Application Development |
| `/sagbs/services/business-automation` | Business Automation & Reporting |
| `/sagbs/industries` | Nine industry-specific solutions |
| `/sagbs/technology` | Platforms, tools and project selection approach |
| `/sagbs/work` | Filterable portfolio and demonstrations |
| `/sagbs/work/operations-dashboard` | Interactive fictional logistics dashboard |
| `/sagbs/work/invoice-workflow` | Sample rule-based invoice validation + CSV export |
| `/sagbs/work/corporate-website` | This site's implementation example |
| `/sagbs/contact` | Contact information and enquiry form |
| `/sagbs/request-quote` | Dedicated quotation enquiry form |
| `/sagbs/privacy` | Enquiry data/privacy notice |
| `/robots.txt`, `/sitemap.xml` | Shared crawl configuration and 44 public URLs |
| `/docs`, `/openapi.json` | Interactive API documentation and schema |

`/sagbs/` permanently redirects to canonical `/sagbs`. Existing `/en/...`
and `/ta/...` URLs permanently redirect to `/sat/en/...` and `/sat/ta/...`,
preserving query strings. `/api/enquiry` remains compatible with the original
SAT API; new SAT forms use `/sat/api/enquiry`.

## Project structure

```text
api/index.py                       Vercel entrypoint
app/
  main.py                          App, shared sitemap/robots/error handling
  config.py                        Environment settings; separate company contact data
  templates_env.py                 Jinja environment and cache-busted asset URLs
  content/
    data.py                        SAT bilingual copy and gallery metadata
    sagbs.py                       SAGBS catalogue, industries, technology, project content
  routers/
    companies.py                   Selection, SAT entrypoint, legacy redirects
    pages.py                       Existing SAT page routes
    enquiry.py                     Existing SAT enquiry API
    sagbs.py                       SAGBS page routes and template context
    sagbs_enquiry.py                SAGBS enquiry API and per-process burst guard
  schemas/
    enquiry.py                     Existing SAT validation
    sagbs.py                       SAGBS form input/output models
  services/
    email_service.py               SAT SMTP notification
    sheets_service.py              SAT Google Sheets integration
    sagbs_store.py                 Database table, connections, idempotent inserts
    sagbs_email.py                 SAGBS SMTP notification
  ...                              Python package markers
templates/
  companies/                       Selection and neutral 404
  base.html, pages/, components/    Existing SAT templates
  sagbs/
    base.html                      SAGBS metadata, shared layout, script loading
    components/                    Header, footer and reusable macros
    home.html, about.html, services.html, service-detail.html
    industries.html, technology.html, work.html, work-detail.html
    contact.html, privacy.html, 404.html
static/
  css/, js/, images/, videos/       Existing SAT / selection assets
  sagbs/                           SAGBS CSS, JS, SVG identity, Lottie JSON, social image
  vendor/                          Pinned browser dependencies + license notices
scripts/init_sagbs_db.py            Repeatable schema setup
scripts/manage_sagbs_leads.py        Private operator listing, export and notification retry
database/sagbs_schema.sql           Initial PostgreSQL schema, for inspection/manual setup
tests/                             Company routing + SAGBS integration regression checks
data/sagbs.db                      Local enquiry data (generated, ignored, never deployed)
design-source/                     Original SAT image sources (not deployed)
requirements.txt, .env.example, vercel.json
```

## Local setup

```bash
python3.11 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Set `SITE_URL=http://127.0.0.1:8000` and `APP_ENV=development` in `.env`.
`SITE_URL` is the shared origin only: do not append `/sat` or `/sagbs`.

```bash
python -m scripts.init_sagbs_db
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000`. Choose SAGBS, or open `/sagbs` directly.
No database server, SMTP credentials or Google credentials are needed for
local SAGBS development. A local enquiry is actually saved even without SMTP.
SQLite's schema is also created on first local enquiry if setup was skipped.

## Contact settings and content

Confirmed SAGBS details:

- Email: `sriannamalaiglobal@gmail.com`
- WhatsApp: `+91 93450 30776`, `+91 82484 54617`
- Business base: Ranipet and Vellore, Tamil Nadu, India.

Override with `SAGBS_EMAIL`, `SAGBS_WHATSAPP`, and
`SAGBS_WHATSAPP_SECONDARY`. WhatsApp values use international digits only.
Company/service copy lives in `app/content/sagbs.py`. SAT contact settings
and `app/content/data.py` remain independent.

Portfolio records are explicitly fictional demonstrations. The corporate
website example describes this implementation; it is not an invented client
project. No fabricated customer names, testimonials, certifications or
business results are published. AI document processing and AI workflow
integration are clearly described as specialist options requiring separate
feasibility assessment, not standard implemented offerings.

## Database setup and operations

Local development defaults to `data/sagbs.db`. For local PostgreSQL or production,
set the secret `SAGBS_DATABASE_URL` in your environment. Supported forms:

```text
postgresql+psycopg://user:password@host/database?sslmode=require
postgresql://user:password@host/database?sslmode=require
```

Ordinary `postgresql://` / `postgres://` URLs are normalised to psycopg 3.
Use your provider's TLS settings. Initialise before enabling the form:

```bash
python -m scripts.init_sagbs_db
```

This creates missing tables/indexes; it does not delete data or migrate
existing columns. Future schema changes need a versioned migration.
`database/sagbs_schema.sql` contains the initial PostgreSQL table/index DDL.

The `sagbs_enquiries` table contains:

| Fields | Meaning |
| --- | --- |
| `id` | Public enquiry reference, UUID |
| `submission_id`, `payload_hash` | Unique submission identity and content fingerprint |
| `created_at`, `consent_at` | UTC timestamps for storage and consent |
| `kind` | `contact` or `quote` |
| `name`, `company_name`, `email`, `phone`, `country` | Contact information |
| `service`, `engagement`, `budget`, `message` | Requested scope |
| `notification_status` | `pending`, `sent`, `failed`, or `unconfigured` |

Private operator commands run in a trusted shell with database credentials;
there is intentionally no public endpoint exposing leads:

```bash
python -m scripts.manage_sagbs_leads list
python -m scripts.manage_sagbs_leads export --output /secure/path/enquiries.csv
python -m scripts.manage_sagbs_leads retry-notifications
```

The list command prints references/status, not messages or contact data.
Exported CSVs contain personal information; store them privately and remove
them when no longer needed. Set a database backup and retention policy for
production, and restrict database access to the application and operators.

## Notifications and enquiry behaviour

Use `SMTP_HOST`, `SMTP_PORT` (587 with STARTTLS), `SMTP_USERNAME` and
`SMTP_PASSWORD` to enable notifications. SAGBS notifications go to
`SAGBS_EMAIL`; SAT notifications use `CONTACT_EMAIL`.

SAGBS returns success **after committing** a database record. A missing or
failed SMTP setup does not discard it; the notification status is stored for
operator follow-up. Notification retries are an explicit operator action,
not an automatically scheduled job. Concurrent retry commands should not be
run; a crash between email delivery and status update can cause a retry email.

If storage is unavailable, the API returns 503 and the form offers retry/email.
Repeating an unchanged `submission_id` is safe and returns the original reference.
Reusing that ID for changed details returns 409. The browser generates a fresh
ID when the requirement changes, and keeps it for a same-payload retry.

Validation trims before checking lengths, validates phone digits, enforces
known service/engagement choices, and requires consent. An offscreen honeypot
skips storage and email for filled bot submissions. A bounded per-process
burst guard allows eight valid requests per address per ten minutes. On
multi-worker/serverless hosting, add a shared/edge limit: in-memory state is
not a global abuse control. Restrict direct origin access and configure
trusted proxy handling appropriately for your hosting setup.

SAT keeps its original enquiry behaviour; see `BUSINESS_DETAILS_TO_CONFIRM.md`
for its original launch information. That older document describes a previous
machine's Google Sheets setup and does not establish that this checkout has
credentials or a local `.env` file.

## API

See [`docs/SAGBS_API.md`](docs/SAGBS_API.md) for the request, response and error
contract. FastAPI also generates `/docs`, `/redoc`, and `/openapi.json`.
The form posts JSON to `POST /sagbs/api/enquiries`; no authentication is required
to submit an enquiry. There is no public list/read/delete-leads API.

## Verification

```bash
python -m unittest discover -s tests -v
python -m pip check
node --check static/sagbs/site.js
node --check static/sagbs/enquiry.js
node --check static/sagbs/demos.js
```

Node is optional and only needed for these JS syntax checks. Python tests use
isolated temporary SQLite files and mocked notification calls; they do not
send email or write to Google Sheets. Checks cover both companies, all SAGBS
page routes/navigation, strict template rendering, preselection, 404s,
validation, consent, persistence, idempotency, failure paths and burst limiting.

Browser checks should cover mobile navigation, keyboard workspace tabs,
portfolio filters, the dashboard period selector, invoice workflow/export,
form validation and submission, 320px widths and reduced-motion behaviour.

## Production deployment

The existing `vercel.json` sends `/static/**` to static hosting and other
requests to `api/index.py`. Jinja templates and static assets are included in
the Python bundle so FastAPI's static mount can also initialise there.
This is a Python server application, not a static HTML export.

1. Install requirements with the production Python runtime.
2. Provision a persistent PostgreSQL database. Add `SAGBS_DATABASE_URL` to the
   deployment's secret environment variables; never commit it.
3. Set `APP_ENV=production`, `SITE_URL` to the final shared HTTPS origin, the
   SAGBS contact settings, and SMTP settings if notifications are required.
   Keep SAT's independent WhatsApp/email/Sheets variables as needed.
4. From a trusted shell using that database URL, run
   `python -m scripts.init_sagbs_db` once before accepting enquiries.
5. Deploy the repository to Vercel using the existing entrypoint/configuration,
   or run `uvicorn app.main:app --host 0.0.0.0 --port 8000` behind an HTTPS proxy
   on a Python host. Verify provider outbound SMTP support if using email.
6. Check company selection, both sites, `/sitemap.xml`, canonical tags and a
   controlled enquiry. Confirm the saved row and notification status, then
   remove only your test record. Configure backups and edge abuse limits.
7. Submit the sitemap to your search console after the production origin is set.

With `APP_ENV=production` or `VERCEL` set, the SAGBS API refuses SQLite or a
missing database URL. This prevents apparent success backed by an ephemeral
serverless file. Public pages still render; enquiry submission returns 503
until persistent storage is configured. Production credentials and an external
PostgreSQL instance are not included in this repository.

No production deployment is performed by local development commands.

## Reference documentation

- [FastAPI on Vercel](https://vercel.com/docs/frameworks/backend/fastapi)
- [SQLAlchemy engines](https://docs.sqlalchemy.org/en/20/core/engines.html)
- [SQLAlchemy psycopg dialect](https://docs.sqlalchemy.org/en/20/dialects/postgresql.html#module-sqlalchemy.dialects.postgresql.psycopg)
- [GSAP responsive/reduced-motion animation](https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/)
- [Lenis setup and ScrollTrigger integration](https://github.com/darkroomengineering/lenis)
