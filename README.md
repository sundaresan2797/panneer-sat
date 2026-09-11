# Sri Annamalayar Transport & Logistics — Website

FastAPI + Jinja2 + Bootstrap 5 corporate website, bilingual (English / Tamil),
built for deployment on Vercel's free plan.

## Architecture

- **Backend:** FastAPI, routes in `app/routers/`, Pydantic validation in
  `app/schemas/`, email sending in `app/services/`.
- **Content:** All English/Tamil copy lives in one place —
  `app/content/data.py` — rather than being duplicated across separate
  `templates/en/*.html` and `templates/ta/*.html` files. Each page type has
  **one** Jinja template under `templates/pages/`, rendered twice (once per
  language) with the matching content pulled from `data.py`. This keeps the
  markup DRY while still producing fully separate, real `/en/...` and
  `/ta/...` URLs with correct hreflang/canonical tags. (Deviates slightly
  from a literal `templates/en/` + `templates/ta/` folder split for that
  reason — the routing, URLs and SEO behaviour are unaffected.)
- **Frontend:** Bootstrap 5 (grid/navbar/accordion/modal primitives only) +
  custom CSS in `static/css/style.css` (design system, mobile-first) and
  `static/css/responsive.css` (breakpoint overrides). Vanilla JS in
  `static/js/` — no jQuery, no build step.

## Local development

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env
# edit .env — at minimum set SITE_URL=http://127.0.0.1:8000

uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000` (redirects to `/en/`).

## Testing the enquiry form

With `.env` SMTP fields left blank, submitting the quote form on `/en/contact`
or `/ta/contact` still succeeds — the enquiry is logged to the server console
instead of emailed, so you can verify the flow works end-to-end before SMTP
is configured. Fill in `SMTP_HOST` / `SMTP_PORT` / `SMTP_USERNAME` /
`SMTP_PASSWORD` / `CONTACT_EMAIL` to actually receive enquiries by email.

Every enquiry is also logged as a row in a Google Sheet (see
`BUSINESS_DETAILS_TO_CONFIRM.md` → "Enquiry logging to Google Sheets" for the
one manual step still needed — sharing a sheet with the service account and
giving its Sheet ID). The service-account key lives at
`secrets/google-service-account.json` (gitignored) for local dev; set
`GOOGLE_APPLICATION_CREDENTIALS` to that path locally, or
`GOOGLE_SERVICE_ACCOUNT_JSON` (the file's full contents) on Vercel.

## Deploying to Vercel (free plan)

1. Push this project to a GitHub repository.
2. In Vercel, **Add New Project** → import the repository.
3. Vercel will detect `vercel.json` (Python runtime via `api/index.py`) —
   no build command is needed.
4. Under **Environment Variables**, add everything from `.env.example`
   (`SITE_URL` should be the final production URL, e.g.
   `https://www.sriannamalayar.com`).
5. Deploy.
6. Once live, open `/robots.txt` and `/sitemap.xml` to confirm they resolve
   against the production domain.
7. In **Google Search Console**, add the property and submit
   `https://<your-domain>/sitemap.xml`.
8. To connect a custom domain: Vercel project → **Settings → Domains** → add
   the domain and follow the DNS instructions, then update `SITE_URL` in the
   environment variables to match.

## Before going live

Several facts (WhatsApp number, official email, whether the Mahindra name
can be used publicly, customer testimonials, real photographs, etc.) were
not supplied and must not be invented. See **`BUSINESS_DETAILS_TO_CONFIRM.md`**
for the full list and exactly which file/env var each one plugs into.

## Project structure

```
app/
  main.py            FastAPI app, static mount, sitemap/robots, error handlers
  config.py          Settings from environment variables
  content/data.py    All bilingual (EN/TA) page copy
  routers/
    pages.py         /{lang}/ and /{lang}/{page} routes
    enquiry.py        POST /api/enquiry
  schemas/enquiry.py  Pydantic request/response models
  services/email_service.py   SMTP sending (safe no-op if unconfigured)
templates/
  base.html
  components/        navbar, footer, whatsapp button, mobile action bar,
                      quote form, and reusable Jinja macros
  pages/             one template per page type (index, about, manpower, ...)
static/
  css/, js/, images/
api/index.py          Vercel entrypoint (imports app.main:app)
vercel.json
requirements.txt
.env.example
BUSINESS_DETAILS_TO_CONFIRM.md
```
