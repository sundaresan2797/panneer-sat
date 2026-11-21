"""Company entry points, kept separate from each company's website."""

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from app.config import get_settings
from app.templates_env import templates

router = APIRouter()


@router.get("/")
def company_selection(request: Request):
    return templates.TemplateResponse(request, "companies/selection.html", {
        "site_url": get_settings().site_url.rstrip("/"),
    })


@router.get("/sat", include_in_schema=False)
@router.get("/sat/", include_in_schema=False)
def sat_entry():
    return RedirectResponse("/sat/en/", status_code=307)


# Preserve existing bookmarks and search results after moving SAT under /sat.
@router.get("/en", include_in_schema=False)
@router.get("/ta", include_in_schema=False)
@router.get("/en/{path:path}", include_in_schema=False)
@router.get("/ta/{path:path}", include_in_schema=False)
def legacy_sat_redirect(request: Request, path: str = ""):
    lang = request.url.path.split("/")[1]
    destination = f"/sat/{lang}/{path}"
    if request.url.query:
        destination += f"?{request.url.query}"
    return RedirectResponse(destination, status_code=308)
