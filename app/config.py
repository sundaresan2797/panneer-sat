import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Local dev only — on Vercel, env vars are injected by the platform and this
# is a silent no-op since no .env file exists there.
load_dotenv(BASE_DIR / ".env")


def _resolve_path(value: str) -> str:
    """Resolve a possibly-relative .env path against the project root, so it
    works from any working directory and on any machine/clone — not just the
    one where an absolute path happened to be written down."""
    if not value:
        return value
    path = Path(value)
    return str(path if path.is_absolute() else BASE_DIR / path)


class Settings:
    app_env: str = os.getenv("APP_ENV", "development")

    smtp_host: str = os.getenv("SMTP_HOST", "")
    smtp_port: int = int(os.getenv("SMTP_PORT", "587"))
    smtp_username: str = os.getenv("SMTP_USERNAME", "")
    smtp_password: str = os.getenv("SMTP_PASSWORD", "")

    contact_email: str = os.getenv("CONTACT_EMAIL", "")
    whatsapp_number: str = os.getenv("WHATSAPP_NUMBER", "")

    site_url: str = os.getenv("SITE_URL", "http://127.0.0.1:8000")

    # Google Sheets logging for quote-form enquiries. Either set
    # GOOGLE_SERVICE_ACCOUNT_JSON (the full key file content, e.g. on Vercel)
    # or GOOGLE_APPLICATION_CREDENTIALS (a local file path, for dev).
    google_service_account_json: str = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    google_application_credentials: str = _resolve_path(os.getenv("GOOGLE_APPLICATION_CREDENTIALS", ""))
    google_sheet_id: str = os.getenv("GOOGLE_SHEET_ID", "")
    google_sheet_tab: str = os.getenv("GOOGLE_SHEET_TAB", "Enquiries")

    @property
    def email_configured(self) -> bool:
        return bool(self.smtp_host and self.smtp_username and self.smtp_password and self.contact_email)

    @property
    def sheets_configured(self) -> bool:
        has_credentials = bool(self.google_service_account_json or self.google_application_credentials)
        return bool(has_credentials and self.google_sheet_id)


@lru_cache
def get_settings() -> Settings:
    return Settings()
