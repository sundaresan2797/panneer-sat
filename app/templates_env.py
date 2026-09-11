from pathlib import Path
from urllib.parse import quote

from fastapi.templating import Jinja2Templates

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
templates.env.filters["urlencode"] = lambda s: quote(str(s))
