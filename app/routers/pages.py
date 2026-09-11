from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse

from app.config import get_settings
from app.content.data import (
    CAPABILITY_CARDS,
    CORPORATE_REQUIREMENTS,
    CTA_CORPORATE,
    CTA_LOCAL,
    FOOTER,
    INDUSTRY_CARDS,
    NAV,
    PAGES,
    QUOTE_FORM,
    REVIEWS_NOTE,
    SERVICE_CARDS,
    SERVICES_DROPDOWN,
    SITE,
    TRUST_STRIP,
    UI,
    WHATSAPP_MESSAGES,
    WHY_CHOOSE_US,
)
from app.templates_env import templates

router = APIRouter()

LANGS = ("en", "ta")

# slug -> (template file under templates/pages/, content key in PAGES)
PAGE_ROUTES = {
    "about": "about",
    "services": "services",
    "manpower": "manpower",
    "facility-management": "facility-management",
    "transport": "transport",
    "heavy-vehicle-rental": "heavy-vehicle-rental",
    "industries": "industries",
    "gallery": "gallery",
    "reviews": "reviews",
    "contact": "contact",
    "privacy": "privacy",
}


def _other_lang(lang: str) -> str:
    return "ta" if lang == "en" else "en"


def base_context(request: Request, lang: str, slug: str) -> dict:
    settings = get_settings()
    other = _other_lang(lang)
    alt_path = f"/{other}/" if slug == "" else f"/{other}/{slug}"
    canonical_path = f"/{lang}/" if slug == "" else f"/{lang}/{slug}"

    return {
        "request": request,
        "lang": lang,
        "other_lang": other,
        "alt_lang_url": alt_path,
        "canonical_url": f"{settings.site_url}{canonical_path}",
        "site_url": settings.site_url,
        "site": SITE,
        "nav": NAV[lang],
        "services_dropdown": SERVICES_DROPDOWN[lang],
        "ui": UI[lang],
        "footer": FOOTER[lang],
        "whatsapp_messages": WHATSAPP_MESSAGES[lang],
        "whatsapp_number": settings.whatsapp_number,
        "current_slug": slug,
    }


@router.get("/", response_class=HTMLResponse)
def root_redirect(request: Request):
    from fastapi.responses import RedirectResponse

    return RedirectResponse(url="/en/")


@router.get("/{lang}/", response_class=HTMLResponse)
def home(request: Request, lang: str):
    if lang not in LANGS:
        raise HTTPException(status_code=404)

    ctx = base_context(request, lang, "")
    ctx.update(
        {
            "content": PAGES["index"][lang],
            "trust_strip": TRUST_STRIP[lang],
            "service_cards": SERVICE_CARDS[lang],
            "capability_cards": CAPABILITY_CARDS[lang],
            "industry_cards": INDUSTRY_CARDS[lang],
            "why_choose_us": WHY_CHOOSE_US[lang],
            "corporate_requirements": CORPORATE_REQUIREMENTS[lang],
            "cta_corporate": CTA_CORPORATE[lang],
            "cta_local": CTA_LOCAL[lang],
            "reviews_note": REVIEWS_NOTE[lang],
            "quote_form": QUOTE_FORM[lang],
        }
    )
    return templates.TemplateResponse(request, "pages/index.html", ctx)


@router.get("/{lang}/{page}", response_class=HTMLResponse)
def page(request: Request, lang: str, page: str):
    if lang not in LANGS or page not in PAGE_ROUTES:
        raise HTTPException(status_code=404)

    content_key = PAGE_ROUTES[page]
    ctx = base_context(request, lang, page)
    ctx.update({"content": PAGES[content_key][lang]})

    if page == "about":
        ctx.update({"why_choose_us": WHY_CHOOSE_US[lang]})
    if page == "services":
        ctx.update({"service_cards": SERVICE_CARDS[lang]})
    if page == "industries":
        ctx.update({"industry_cards": INDUSTRY_CARDS[lang], "cta_corporate": CTA_CORPORATE[lang]})
    if page == "reviews":
        ctx.update({"reviews_note": REVIEWS_NOTE[lang]})
    if page == "contact":
        ctx.update({"quote_form": QUOTE_FORM[lang]})
    if page in ("manpower", "facility-management", "transport", "heavy-vehicle-rental"):
        ctx.update(
            {
                "cta_corporate": CTA_CORPORATE[lang],
                "cta_local": CTA_LOCAL[lang],
                "quote_form": QUOTE_FORM[lang],
                "why_choose_us": WHY_CHOOSE_US[lang],
            }
        )

    return templates.TemplateResponse(request, f"pages/{content_key}.html", ctx)
