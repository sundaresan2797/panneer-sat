# Business details to confirm before launch

The website is built and functional, but the items below were **not**
provided in the original brief and must not be guessed. Placeholders in the
code are marked `[TO BE CONFIRMED]`, driven by empty environment variables,
or use safe generic copy until these are filled in.

```
[TO BE CONFIRMED]

Official registered company name:
Owner/founder name:
Official email:
WhatsApp number:                      -> ✅ done — 919344354617, set in .env
Website domain:                       -> set SITE_URL in .env
Exact establishment year:
Exact service locations:
Approved client names:
Permission to display client logos:
Number of employees:
Number of vehicles:
Exact fleet:
Vehicle availability:
Vehicle rental pricing:
Certifications:
Licenses:
Insurance:
ESI/PF:
MSME/Udyam:
Social media links:
Google Business Profile:
Verified customer testimonials (names, ratings, dates, and permission to publish):
Business hours — please confirm Mon–Sat 9:00 AM–9:00 PM / Sunday closed / lunch 1–2 PM is correct
Google Sheet ID for enquiry logging:   -> set GOOGLE_SHEET_ID in .env (see below)
```

## Where these plug in once confirmed

| Item | File |
|---|---|
| WhatsApp number | ✅ Done — `919344354617`, set in `.env`. Still needed for **production**: also set `WHATSAPP_NUMBER` on Vercel. |
| Contact email | `.env` → `CONTACT_EMAIL` |
| SMTP credentials (to actually send enquiry emails) | `.env` → `SMTP_HOST` / `SMTP_PORT` / `SMTP_USERNAME` / `SMTP_PASSWORD` |
| Site domain | `.env` → `SITE_URL` |
| Company email / official name / GSTIN / addresses | `app/content/data.py` → `SITE` dict |
| Client logos (Mahindra etc.) | Only add once the client has given written permission to display their name/logo publicly. Until then the site uses "Serving Leading Industrial & Corporate Clients." |
| Customer reviews | `app/content/data.py` — do not publish names, ratings or quotes without the customer's and owner's permission |
| Real photographs (~15–20 images) | `static/images/` — see `static/images/README.md` for exact filenames expected by the templates |
| Logo | ✅ Done — real logo supplied and wired into the navbar, footer, 404 page, favicons, apple-touch-icon and social-share (OG) image. |
| Google Sheet for enquiries | ✅ Done — `SAT_QUOTA` sheet confirmed shared and working end-to-end (see below). Still needed only for **production**: set `GOOGLE_SERVICE_ACCOUNT_JSON` on Vercel. |

Nothing above blocks a technical deployment — the site works end-to-end with
sensible defaults (enquiries are received and logged even without SMTP
configured; before the WhatsApp number was set, those buttons fell back to a
phone call instead of a dead `wa.me/` link).
But **do not go live publicly** until the client-facing claims (Mahindra,
testimonials, fleet size, pricing) are confirmed by the business owner.

## Enquiry logging to Google Sheets

Every quote-form submission is now also appended as a row to a Google Sheet
(in addition to email), so there's a durable record even if an email
bounces. This was built using the service-account key you supplied
(`sat-72@spironova-ai.iam.gserviceaccount.com`, project `spironova-ai`) —
it's stored at `secrets/google-service-account.json`, which is gitignored
and must **never** be committed or pasted anywhere public.

**Status: working end-to-end.** Sheet `SAT_QUOTA`
(`1j9bTe2iSV2jPdKxkEhHe2fdOBQtn755FWhp3ffq5aOE`, tab `Sheet1`) is shared with
the service account, has a bolded header row
(`Submitted At | Name | Company | Phone | Email | Location | Service | Workers / Vehicles | Requirement | Language`),
and two live test submissions were confirmed to land correctly (then
removed, so the sheet only has real leads from here on).

`.env` (gitignored, local only) now has `GOOGLE_SHEET_ID`,
`GOOGLE_SHEET_TAB=Sheet1`, and `GOOGLE_APPLICATION_CREDENTIALS` pointing at
`secrets/google-service-account.json` already filled in.

**One remaining step for production:** on Vercel, set
`GOOGLE_SERVICE_ACCOUNT_JSON` (Project → Settings → Environment Variables)
to the full contents of `secrets/google-service-account.json` pasted as one
line, plus `GOOGLE_SHEET_ID=1j9bTe2iSV2jPdKxkEhHe2fdOBQtn755FWhp3ffq5aOE` and
`GOOGLE_SHEET_TAB=Sheet1`. The key file itself never gets deployed — only
these three environment variables need to be set there.
