import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse, Response
from fastapi.staticfiles import StaticFiles

from app.config import get_settings
from app.content.data import PAGES
from app.routers import companies, enquiry, pages, sagbs, sagbs_enquiry
from app.content.sagbs import PUBLIC_PATHS
from app.routers.pages import PAGE_ROUTES, base_context
from app.templates_env import templates

logging.basicConfig(level=logging.INFO)

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(title="SAT & SAGBS Websites")

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

app.include_router(companies.router)
app.include_router(enquiry.router, prefix="/sat")
app.include_router(enquiry.router, include_in_schema=False)
app.include_router(pages.router)
app.include_router(sagbs_enquiry.router)
app.include_router(sagbs.router)

PAGE_PRIORITY = {"": "1.0", "contact": "0.9", "manpower": "0.9", "facility-management": "0.9", "transport": "0.9", "heavy-vehicle-rental": "0.9"}


@app.get("/robots.txt", response_class=PlainTextResponse)
def robots_txt():
    settings = get_settings()
    return (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /docs\n"
        "Disallow: /redoc\n"
        "Disallow: /openapi.json\n"
        "Disallow: /api/\n"
        "Disallow: /sat/api/\n"
        "Disallow: /sagbs/api/\n\n"
        f"Sitemap: {settings.site_url}/sitemap.xml\n"
    )


@app.get("/sitemap.xml")
def sitemap_xml():
    settings = get_settings()
    slugs = [""] + list(PAGE_ROUTES.keys())
    urls = [f"  <url><loc>{settings.site_url}/</loc><priority>1.0</priority></url>"]
    for lang in ("en", "ta"):
        for slug in slugs:
            path = f"/sat/{lang}/" if slug == "" else f"/sat/{lang}/{slug}"
            other_lang = "ta" if lang == "en" else "en"
            other_path = f"/sat/{other_lang}/" if slug == "" else f"/sat/{other_lang}/{slug}"
            priority = PAGE_PRIORITY.get(slug, "0.7")
            urls.append(
                "  <url>\n"
                f"    <loc>{settings.site_url}{path}</loc>\n"
                f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{settings.site_url}{path}" />\n'
                f'    <xhtml:link rel="alternate" hreflang="{other_lang}" href="{settings.site_url}{other_path}" />\n'
                f"    <priority>{priority}</priority>\n"
                "  </url>"
            )
    for path in PUBLIC_PATHS:
        urls.append(f"  <url><loc>{settings.site_url}{path}</loc><priority>0.8</priority></url>")
    body = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls)
        + "\n</urlset>"
    )
    return Response(content=body, media_type="application/xml")


@app.exception_handler(404)
async def not_found_handler(request: Request, exc: HTTPException):
    lang = "en"
    path_parts = request.url.path.strip("/").split("/")
    if path_parts[0] == "sagbs":
        ctx = sagbs.context(request, title="Page not found")
        return templates.TemplateResponse(request, "sagbs/404.html", ctx, status_code=404)
    if path_parts[0] == "sat":
        path_parts = path_parts[1:]
    else:
        return templates.TemplateResponse(request, "companies/not-found.html", {}, status_code=404)
    if path_parts and path_parts[0] in ("en", "ta"):
        lang = path_parts[0]

    ctx = base_context(request, lang, "404")
    ctx.update({"content": PAGES["404"][lang]})
    return templates.TemplateResponse(request, "pages/404.html", ctx, status_code=404)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = [err.get("msg", "Invalid input") for err in exc.errors()]
    body = {"success": False, "message": "; ".join(errors) or "Invalid input."}
    if request.url.path.startswith("/sagbs/api/"):
        body["errors"] = {str(err["loc"][-1]): err["msg"] for err in exc.errors() if err["loc"]}
    return JSONResponse(status_code=422, content=body)


@app.exception_handler(500)
async def server_error_handler(request: Request, exc: Exception):
    logging.getLogger("sat.error").exception("Unhandled server error")
    return JSONResponse(status_code=500, content={"success": False, "message": "Something went wrong. Please try again or call us directly."})
