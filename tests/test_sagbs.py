import json
import csv
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import urlsplit
from uuid import uuid4

from jinja2 import StrictUndefined
from sqlalchemy import func, select

from app.config import get_settings
from app.content.sagbs import PUBLIC_PATHS, SERVICES
from app.routers import sagbs_enquiry
from app.services.sagbs_store import StorageUnavailable, database_url, engine_for_url, enquiries
from app.templates_env import templates
from scripts.manage_sagbs_leads import main as manage_leads
from test_company_routes import PageLinks, request


class SAGBSPageTests(unittest.IsolatedAsyncioTestCase):
    async def test_all_pages_links_metadata_and_contact_details(self):
        with patch.object(templates.env, "undefined", StrictUndefined):
            for path in PUBLIC_PATHS:
                with self.subTest(path=path):
                    status, _, body = await request(path)
                    self.assertEqual(status, 200)
                    self.assertIn(f'href="{get_settings().site_url}{path}"', body)
                    self.assertIn("sriannamalaiglobal@gmail.com", body)
                    self.assertIn("919345030776", body)
                    self.assertIn("918248454617", body)
                    self.assertNotIn("TO BE CONFIRMED", body)
                    links = PageLinks()
                    links.feed(body)
                    for href in set(links.links):
                        if href == "/sat":
                            continue
                        status, _, _ = await request(href)
                        self.assertEqual(status, 200, (path, href))

    async def test_services_directory_filters_quote_links_by_task(self):
        all_slugs = [service["slug"] for service in SERVICES]
        cases = {
            "": all_slugs,
            "?group=records": ["data-entry", "data-management", "data-analytics"],
            "?group=web": ["website-development", "software-development"],
            "?group=office": ["bpo-services", "business-automation"],
            "?group=unknown": all_slugs,
        }
        prefix = "/sagbs/request-quote?service="
        for query, slugs in cases.items():
            with self.subTest(query=query):
                status, _, body = await request("/sagbs/services" + query)
                self.assertEqual(status, 200)
                links = PageLinks()
                links.feed(body)
                self.assertEqual([url for url in links.links if url.startswith(prefix)],
                                 [prefix + slug for slug in slugs])

    async def test_service_quote_preselection_and_invalid_values(self):
        for service in SERVICES:
            status, _, body = await request(f"/sagbs/request-quote?service={service['slug']}&engagement=monthly")
            self.assertEqual(status, 200)
            self.assertIn(f'<option value="{service["slug"]}" selected>', body)
            self.assertIn('<option value="monthly" selected>', body)
        status, _, body = await request('/sagbs/request-quote?service=unknown&engagement=unknown')
        self.assertEqual(status, 200)
        self.assertIn('<option value="discuss" selected>', body)

    async def test_specialist_ai_and_demo_claims(self):
        _, _, body = await request('/sagbs/services/business-automation')
        self.assertIn('not services we already provide', body)
        _, _, body = await request('/sagbs/work/operations-dashboard')
        self.assertIn('MADE-UP DELIVERY RECORDS', body)
        _, _, body = await request('/sagbs/work/invoice-workflow')
        self.assertIn('no AI is used', body)

    async def test_unknown_service_and_project_return_404(self):
        for path in ('/sagbs/services/missing', '/sagbs/work/missing'):
            status, _, body = await request(path)
            self.assertEqual(status, 404)
            self.assertIn('Sorry, we cannot', body)


class SAGBSEnquiryTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.url = 'sqlite:///' + str(Path(self.directory.name) / 'enquiries.db')
        self.settings = get_settings()
        self.patches = [patch.object(self.settings, 'sagbs_database_url', self.url),
                        patch.object(self.settings, 'app_env', 'development'),
                        patch('app.routers.sagbs_enquiry.notify_enquiry', return_value='unconfigured')]
        self.sheet_append = self.enterContext(patch('app.routers.sagbs_enquiry.append_sagbs_contact_to_sheet', return_value=False))
        for item in self.patches:
            item.start()
        sagbs_enquiry._requests.clear()

    def tearDown(self):
        engine_for_url(self.url).dispose()
        for item in reversed(self.patches):
            item.stop()
        self.directory.cleanup()

    def payload(self, **changes):
        body = {'name': 'Sample Enquirer', 'company_name': 'Example Business',
                'email': 'person@example.com', 'phone': '+91 98765 43210', 'country': 'India',
                'service': 'data-analytics', 'engagement': 'monthly', 'budget': 'discuss',
                'message': 'We need monthly business reports and a new dashboard.', 'consent': True,
                'kind': 'quote', 'submission_id': str(uuid4()), 'website': ''}
        body.update(changes)
        return body

    def count(self):
        with engine_for_url(self.url).connect() as connection:
            return connection.scalar(select(func.count()).select_from(enquiries))

    async def test_saved_even_without_email_and_records_consent(self):
        payload = self.payload(name='  Sample Enquirer  ')
        status, _, body = await request('/sagbs/api/enquiries', 'POST', payload)
        self.assertEqual(status, 201)
        self.assertTrue(json.loads(body)['success'])
        with engine_for_url(self.url).connect() as connection:
            record = connection.execute(select(enquiries)).mappings().one()
        self.assertEqual(record['id'], json.loads(body)['reference'])
        self.assertEqual(record['name'], 'Sample Enquirer')
        self.assertEqual(record['notification_status'], 'unconfigured')
        self.assertIsNotNone(record['consent_at'])

    async def test_delivery_failure_does_not_lose_record(self):
        with patch('app.routers.sagbs_enquiry.notify_enquiry', return_value='failed'):
            status, _, _ = await request('/sagbs/api/enquiries', 'POST', self.payload())
        self.assertEqual(status, 201)
        self.assertEqual(self.count(), 1)

    async def test_retry_is_idempotent_and_changed_payload_conflicts(self):
        payload = self.payload()
        _, _, first = await request('/sagbs/api/enquiries', 'POST', payload)
        status, _, second = await request('/sagbs/api/enquiries', 'POST', payload)
        self.assertEqual(status, 201)
        self.assertEqual(json.loads(first)['reference'], json.loads(second)['reference'])
        self.assertEqual(self.count(), 1)
        payload['message'] = 'A changed requirement with the same submission reference.'
        status, _, _ = await request('/sagbs/api/enquiries', 'POST', payload)
        self.assertEqual(status, 409)
        self.assertEqual(self.count(), 1)

    async def test_contact_appends_once_even_when_sheet_unavailable(self):
        payload = self.payload(kind='contact')
        status, _, body = await request('/sagbs/api/enquiries', 'POST', payload)
        self.assertEqual(status, 201)
        await request('/sagbs/api/enquiries', 'POST', payload)
        await request('/sagbs/api/enquiries', 'POST', self.payload())
        self.sheet_append.assert_called_once()
        contact, reference = self.sheet_append.call_args.args
        self.assertEqual(contact.email, payload['email'])
        self.assertEqual(reference, json.loads(body)['reference'])
        self.assertEqual(self.count(), 2)

    async def test_storage_failure_returns_503_not_success(self):
        with patch('app.routers.sagbs_enquiry.save_enquiry', side_effect=StorageUnavailable):
            status, _, body = await request('/sagbs/api/enquiries', 'POST', self.payload())
        self.assertEqual(status, 503)
        self.assertNotIn('"success":true', body)
        self.assertEqual(self.count(), 0)

    async def test_validation_rejects_blank_fields_phone_and_missing_consent(self):
        for changes in ({'name': '   '}, {'phone': '-------'}, {'country': '  '},
                        {'message': 'too short'}, {'consent': False}, {'service': 'imaginary'},
                        {'email': 'invalid'}, {'engagement': 'free'}, {'budget': 'anything'}):
            with self.subTest(changes=changes):
                # This test concerns validation, not the independent burst guard.
                status, _, body = await request('/sagbs/api/enquiries', 'POST', self.payload(**changes))
                self.assertEqual(status, 422)
                self.assertIn('errors', json.loads(body))
        self.assertEqual(self.count(), 0)

    async def test_honeypot_skips_storage_and_notification(self):
        with patch('app.routers.sagbs_enquiry.notify_enquiry') as notify:
            status, _, _ = await request('/sagbs/api/enquiries', 'POST', self.payload(website='bot.example'))
        self.assertEqual(status, 201)
        self.assertEqual(self.count(), 0)
        notify.assert_not_called()

    async def test_rate_limit(self):
        for _ in range(8):
            status, _, _ = await request('/sagbs/api/enquiries', 'POST', self.payload(website='bot.example'))
            self.assertEqual(status, 201)
        status, headers, _ = await request('/sagbs/api/enquiries', 'POST', self.payload())
        self.assertEqual(status, 429)
        self.assertEqual(headers['retry-after'], '600')

    def test_production_requires_persistent_postgres(self):
        with patch.object(self.settings, 'app_env', 'production'):
            with self.assertRaises(StorageUnavailable):
                database_url()
            with patch.object(self.settings, 'sagbs_database_url', ''):
                with self.assertRaises(StorageUnavailable):
                    database_url()

    async def test_private_export_and_notification_retry(self):
        payload = self.payload(company_name='=HYPERLINK("https://example.com")')
        await request('/sagbs/api/enquiries', 'POST', payload)
        output = Path(self.directory.name) / 'private-export.csv'
        with patch('sys.argv', ['manage_sagbs_leads', 'export', '--output', str(output)]), redirect_stdout(StringIO()):
            manage_leads()
        with output.open(encoding='utf-8-sig', newline='') as source:
            rows = list(csv.DictReader(source))
        self.assertEqual(len(rows), 1)
        self.assertTrue(rows[0]['company_name'].startswith("'="))
        self.assertEqual(output.stat().st_mode & 0o777, 0o600)
        with patch('scripts.manage_sagbs_leads.notify_enquiry', return_value='sent') as notify, \
             patch('sys.argv', ['manage_sagbs_leads', 'retry-notifications']), redirect_stdout(StringIO()):
            manage_leads()
        notify.assert_called_once()
        with engine_for_url(self.url).connect() as connection:
            self.assertEqual(connection.scalar(select(enquiries.c.notification_status)), 'sent')

    def test_postgresql_url_normalization(self):
        with patch.object(self.settings, 'sagbs_database_url', 'postgresql://user:example@localhost/sample'), \
             patch.object(self.settings, 'app_env', 'production'):
            self.assertEqual(database_url(), 'postgresql+psycopg://user:example@localhost/sample')
