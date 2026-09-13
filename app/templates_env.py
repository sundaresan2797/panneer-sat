from pathlib import Path
from urllib.parse import quote

from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
templates.env.filters["urlencode"] = lambda s: quote(str(s))


def asset_url(path: str) -> str:
    """Static asset URL with a cache-busting ?v=<mtime> so a browser never
    serves a stale cached CSS/JS file after an edit — no manual hard-refresh
    needed. `path` is relative to /static/, e.g. "css/style.css"."""
    file_path = STATIC_DIR / path
    try:
        version = int(file_path.stat().st_mtime)
    except OSError:
        version = 0
    return f"/static/{path}?v={version}"


templates.env.globals["asset_url"] = asset_url
