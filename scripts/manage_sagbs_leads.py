"""Private operator commands. Run only in a trusted shell with DB credentials."""

import argparse
import csv
import os
from pathlib import Path

from sqlalchemy import select

from app.schemas.sagbs import SAGBSEnquiryIn
from app.services.sheets_service import append_sagbs_contact_to_sheet
from app.services.sagbs_email import notify_enquiry
from app.services.sagbs_store import database_url, engine_for_url, enquiries, set_notification_status


def export_value(value):
    # Prevent spreadsheet formula evaluation in exported user-supplied text.
    value = str(value)
    return "'" + value if value.lstrip().startswith(("=", "+", "-", "@")) else value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    list_parser = commands.add_parser("list", help="List references/times/status only")
    list_parser.add_argument("--limit", type=int, default=20)
    export_parser = commands.add_parser("export", help="Export lead data to a private CSV")
    export_parser.add_argument("--output", required=True)
    commands.add_parser("retry-notifications", help="Retry pending/failed/unconfigured emails")
    sync_parser = commands.add_parser("sync-contact", help="Copy a saved SAGBS contact to Sheet2 by reference")
    sync_parser.add_argument("reference")
    args = parser.parse_args()
    engine = engine_for_url(database_url())
    if args.command == "sync-contact":
        with engine.connect() as connection:
            row = connection.execute(select(enquiries).where(
                enquiries.c.id == args.reference, enquiries.c.kind == "contact")).mappings().one_or_none()
        if row is None:
            raise SystemExit("No saved contact found for that reference.")
        payload = {key: row[key] for key in SAGBSEnquiryIn.model_fields if key in row}
        enquiry = SAGBSEnquiryIn(**payload, consent=bool(row["consent_at"]))
        if not append_sagbs_contact_to_sheet(enquiry, row["id"], saved_at=row["created_at"]):
            raise SystemExit("Sheet sync failed. The contact is still saved in the database.")
        print("Contact confirmed in Sheet2.")
        return
    if args.command == "list":
        with engine.connect() as connection:
            rows = connection.execute(select(enquiries.c.id, enquiries.c.created_at, enquiries.c.kind,
                enquiries.c.notification_status).order_by(enquiries.c.created_at.desc()).limit(max(1, min(args.limit, 1000))))
            for row in rows:
                print(row.id, row.created_at.isoformat(), row.kind, row.notification_status)
        return
    if args.command == "export":
        path = Path(args.output).expanduser()
        with engine.connect() as connection:
            rows = connection.execute(select(enquiries).order_by(enquiries.c.created_at))
            fields = [column.name for column in enquiries.columns if column.name != "payload_hash"]
            # Refuse to overwrite and create a file readable only by its owner.
            descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(descriptor, "w", newline="", encoding="utf-8-sig") as output:
                writer = csv.DictWriter(output, fieldnames=fields)
                writer.writeheader()
                count = 0
                for row in rows.mappings():
                    writer.writerow({key: export_value(row[key]) for key in fields})
                    count += 1
        print(f"Exported {count} enquiries to the specified private file.")
        return
    with engine.connect() as connection:
        rows = connection.execute(select(enquiries).where(
            enquiries.c.notification_status.in_(["pending", "failed", "unconfigured"]))).mappings().all()
    counts = {"sent": 0, "failed": 0, "unconfigured": 0}
    for row in rows:
        payload = {key: row[key] for key in SAGBSEnquiryIn.model_fields if key in row}
        payload["consent"] = True
        enquiry = SAGBSEnquiryIn(**payload)
        result = notify_enquiry(enquiry, row["id"])
        set_notification_status(row["id"], result)
        counts[result] += 1
    print("Notification results:", counts)


if __name__ == "__main__":
    main()
