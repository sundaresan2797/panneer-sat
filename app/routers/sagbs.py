from datetime import datetime
import re

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from app.config import get_settings
from app.content.sagbs import COMPANY, ENGAGEMENTS, INDUSTRIES, PAGE_META, PROCESS, PROJECT_MAP, PROJECTS, SERVICE_GROUPS, SERVICE_MAP, SERVICES, TECHNOLOGIES
from app.templates_env import templates

router = APIRouter(prefix="/sagbs", tags=["SAGBS pages"])


def context(request, page="home", title=None, description=None):
    settings = get_settings()
    default_title, default_description = PAGE_META.get(page, PAGE_META["home"])
    phones = [re.sub(r"\D", "", number) for number in (settings.sagbs_whatsapp, settings.sagbs_whatsapp_secondary) if number]
    return {
        "request": request, "company": COMPANY, "services": SERVICES, "industries": INDUSTRIES,
        "process": PROCESS, "engagements": ENGAGEMENTS, "technologies": TECHNOLOGIES, "service_groups": SERVICE_GROUPS,
        "projects": PROJECTS, "page": page, "year": datetime.now().year,
        "title": f"{title or default_title} | SAGBS", "description": description or default_description,
        "canonical_url": settings.site_url + request.url.path.rstrip("/"),
        "site_url": settings.site_url, "email": settings.sagbs_email, "phones": phones,
        "organisation_schema": {
            "@context": "https://schema.org", "@type": "Organization", "name": COMPANY["name"],
            "alternateName": "SAGBS", "url": settings.site_url + "/sagbs",
            "logo": settings.site_url + "/static/images/SAGBS_LOGO.png",
            "email": settings.sagbs_email, "areaServed": ["India", "International"],
            "address": {"@type": "PostalAddress", "addressLocality": "Ranipet / Vellore",
                        "addressRegion": "Tamil Nadu", "addressCountry": "IN"},
        },
    }


@router.get("", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "sagbs/home.html", context(request))


@router.get("/", include_in_schema=False)
def home_slash():
    return RedirectResponse("/sagbs", status_code=308)


@router.get("/services/{slug}", response_class=HTMLResponse)
def service_detail(request: Request, slug: str):
    service = SERVICE_MAP.get(slug)
    if not service:
        raise HTTPException(404)
    ctx = context(request, "services", service["title"], service["summary"] + " Help with one job or regular monthly work from SAGBS.")
    ctx["service"] = service
    ctx["service_schema"] = {
        "@context": "https://schema.org", "@type": "Service", "name": service["title"],
        "description": service["summary"], "url": ctx["canonical_url"],
        "provider": {"@type": "Organization", "name": COMPANY["name"], "url": ctx["site_url"] + "/sagbs"},
        "areaServed": ["India", "International"],
    }
    return templates.TemplateResponse(request, "sagbs/service-detail.html", ctx)


@router.get("/work/{slug}", response_class=HTMLResponse)
def work_detail(request: Request, slug: str):
    project = PROJECT_MAP.get(slug)
    if not project:
        raise HTTPException(404)
    ctx = context(request, "work", project["title"], project["desc"])
    ctx["project"] = project
    return templates.TemplateResponse(request, "sagbs/work-detail.html", ctx)


@router.get("/{page}", response_class=HTMLResponse)
def content_page(request: Request, page: str):
    if page not in PAGE_META or page == "home":
        raise HTTPException(404)
    ctx = context(request, page)
    if page == "services":
        group = SERVICE_GROUPS.get(request.query_params.get("group"))
        ctx["selected_group"] = group
        ctx["listed_services"] = [SERVICE_MAP[slug] for slug in group["slugs"]] if group else SERVICES
    if page in ("contact", "request-quote"):
        selected = request.query_params.get("service", "discuss")
        ctx["selected_service"] = selected if selected in SERVICE_MAP else "discuss"
        mode = request.query_params.get("engagement", "discuss")
        ctx["selected_engagement"] = mode if mode in ("project", "monthly", "dedicated", "maintenance") else "discuss"
        template = "contact"
    else:
        template = page
    return templates.TemplateResponse(request, f"sagbs/{template}.html", ctx)
