"""Durable SAGBS enquiries. SQLite locally, PostgreSQL in production."""

import hashlib
import json
import os
from datetime import datetime, timezone
from functools import lru_cache
from uuid import uuid4

from sqlalchemy import Column, DateTime, MetaData, String, Table, Text, create_engine, insert, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.pool import NullPool

from app.config import BASE_DIR, get_settings

metadata = MetaData()
enquiries = Table(
    "sagbs_enquiries", metadata,
    Column("id", String(36), primary_key=True),
    Column("submission_id", String(36), nullable=False, unique=True),
    Column("payload_hash", String(64), nullable=False),
    Column("created_at", DateTime(timezone=True), nullable=False, index=True),
    Column("kind", String(10), nullable=False),
    Column("name", String(100), nullable=False),
    Column("company_name", String(150), nullable=False),
    Column("email", String(254), nullable=False),
    Column("phone", String(25), nullable=False),
    Column("country", String(100), nullable=False),
    Column("service", String(100), nullable=False),
    Column("engagement", String(20), nullable=False),
    Column("budget", String(20), nullable=False),
    Column("message", Text, nullable=False),
    Column("consent_at", DateTime(timezone=True), nullable=False),
    Column("notification_status", String(20), nullable=False, server_default="pending"),
)


class StorageUnavailable(RuntimeError):
    pass


class SubmissionConflict(ValueError):
    pass


def database_url():
    settings = get_settings()
    value = settings.sagbs_database_url
    production = settings.app_env == "production" or bool(os.getenv("VERCEL"))
    if not value:
        if production:
            raise StorageUnavailable("SAGBS_DATABASE_URL is required in production.")
        directory = BASE_DIR / "data"
        directory.mkdir(exist_ok=True)
        value = f"sqlite:///{directory / 'sagbs.db'}"
    if value.startswith(("postgres://", "postgresql://")):
        value = "postgresql+psycopg://" + value.split("://", 1)[1]
    if production and not value.startswith("postgresql+psycopg://"):
        raise StorageUnavailable("Use a persistent PostgreSQL database in production.")
    if not value.startswith(("sqlite:///", "postgresql+psycopg://")):
        raise StorageUnavailable("Unsupported SAGBS database URL.")
    return value


@lru_cache(maxsize=4)
def engine_for_url(url):
    args = {"check_same_thread": False, "timeout": 5} if url.startswith("sqlite:") else {"connect_timeout": 5}
    engine = create_engine(url, poolclass=NullPool, connect_args=args, hide_parameters=True)
    if url.startswith("sqlite:"):
        metadata.create_all(engine)
    return engine


def init_database():
    engine = engine_for_url(database_url())
    metadata.create_all(engine)
    for index in enquiries.indexes:
        index.create(engine, checkfirst=True)


def save_enquiry(enquiry):
    payload = enquiry.model_dump(mode="json", exclude={"website", "submission_id"})
    digest = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    engine = engine_for_url(database_url())
    now = datetime.now(timezone.utc)
    record = {key: value for key, value in payload.items() if key != "consent"}
    record.update(id=str(uuid4()), submission_id=str(enquiry.submission_id), payload_hash=digest,
                  created_at=now, consent_at=now, notification_status="pending")
    try:
        with engine.begin() as connection:
            connection.execute(insert(enquiries).values(**record))
        return record["id"], True
    except IntegrityError:
        with engine.connect() as connection:
            existing = connection.execute(select(enquiries.c.id, enquiries.c.payload_hash).where(
                enquiries.c.submission_id == str(enquiry.submission_id))).first()
        if existing is None:
            raise
        if existing.payload_hash != digest:
            raise SubmissionConflict("This message number was already used. Please reload the page to send a new message.")
        return existing.id, False


def set_notification_status(reference, status):
    with engine_for_url(database_url()).begin() as connection:
        connection.execute(update(enquiries).where(enquiries.c.id == reference).values(notification_status=status))
