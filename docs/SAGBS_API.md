# SAGBS enquiry API

`POST /sagbs/api/enquiries` accepts `application/json`. A successful request is
stored before the response is sent. Notification email is best-effort after
storage; response success does not claim that an email was delivered.

## Request

```json
{
  "name": "Sample Enquirer",
  "company_name": "Example Business",
  "email": "person@example.com",
  "phone": "+91 98765 43210",
  "country": "India",
  "service": "data-analytics",
  "engagement": "monthly",
  "budget": "discuss",
  "message": "We need a monthly reporting dashboard for our operations.",
  "consent": true,
  "kind": "quote",
  "submission_id": "1e416c2e-c689-4ac3-b1db-8811fe91930e",
  "website": ""
}
```

| Field | Rules |
| --- | --- |
| `name` | Required, 2–100 characters after trimming |
| `company_name` | Optional, at most 150 characters |
| `email` | Required, valid email, at most 254 characters |
| `phone` | Required, 7–15 digits; `+`, spaces, parentheses, periods and hyphens allowed |
| `country` | Required, 2–100 characters |
| `service` | Required; one of the service slugs below or `discuss` |
| `engagement` | `project`, `monthly`, `dedicated`, `maintenance`, `discuss` (default) |
| `budget` | Optional: empty, `under-25k`, `25k-75k`, `75k-2l`, `2l-plus`, `discuss`; INR bands |
| `message` | Required, 20–5,000 characters after trimming |
| `consent` | Required, must be `true` |
| `kind` | `contact` (default) or `quote` |
| `submission_id` | UUID; generated server-side if absent; reuse for same-payload retries |
| `website` | Honeypot: leave empty; maximum 200 characters |

Services: `data-entry`, `data-management`, `data-analytics`, `bpo-services`,
`website-development`, `software-development`, `business-automation`.
Extra fields are rejected. Whitespace is trimmed before length validation.

## Responses

HTTP 201, saved successfully (including an unchanged idempotent retry):

```json
{
  "success": true,
  "message": "Thank you. Your message has been saved for our team to read.",
  "reference": "c53b8943-e8aa-4cc6-932b-66d97cc118d5"
}
```

The honeypot deliberately returns 201 without saving or notifying and with a
null reference. Do not treat a filled honeypot as a real enquiry.

HTTP 422, invalid input:

```json
{
  "success": false,
  "message": "String should have at least 2 characters",
  "errors": {"name": "String should have at least 2 characters"}
}
```

HTTP 409, reused submission identity with changed data:

```json
{"detail": "This message number was already used. Please reload the page to send a new message."}
```

HTTP 429, more than eight valid requests per client address in ten minutes:

```json
{"detail": "You have sent several messages. Please wait 10 minutes before trying again, or email us."}
```

Includes `Retry-After: 600`. This is a bounded in-process burst guard, not a
distributed rate limit; configure hosting/edge controls in production.

HTTP 503, record not stored:

```json
{"detail": "We could not save your message. Please try again or email us."}
```

The browser must not show success for 503. A network timeout is ambiguous:
retry the unchanged payload with the same `submission_id` to avoid duplicates.

## Local example

Run against your development server only; this creates a real local record:

```bash
curl http://127.0.0.1:8000/sagbs/api/enquiries \
  -H 'Content-Type: application/json' \
  --data '{"name":"Local Test","email":"test@example.com","phone":"+91 9876543210","country":"India","service":"discuss","message":"This is a local development test enquiry.","consent":true}'
```

Open `/docs` for generated models and interactive examples. Private operator
commands are documented in the repository README. No public lead retrieval or
administration API is exposed.
