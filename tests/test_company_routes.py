"""Routing migration checks, with no network calls or additional dependencies."""

import asyncio
import json
import unittest
from html.parser import HTMLParser
from unittest.mock import patch
from urllib.parse import urlsplit
from xml.etree import ElementTree

from app.config import get_settings
from app.main import app
from app.routers.pages import PAGE_ROUTES
from app.content.sagbs import PUBLIC_PATHS


async def request(url, method="GET", payload=None):
    parsed = urlsplit(url)
    data = json.dumps(payload).encode() if payload is not None else b""
    messages = []
    sent = False

    async def receive():
        nonlocal sent
        if not sent:
            sent = True
            return {"type": "http.request", "body": data, "more_body": False}
        await asyncio.Event().wait()

    async def send(message):
        messages.append(message)

    await app({
        "type": "http", "asgi": {"version": "3.0"}, "http_version": "1.1",
        "method": method, "scheme": "http", "path": parsed.path,
        "raw_path": parsed.path.encode(), "query_string": parsed.query.encode(),
        "root_path": "", "headers": [(b"host", b"testserver"),
        (b"content-type", b"application/json")],
        "client": ("127.0.0.1", 1000), "server": ("testserver", 80),
    }, receive, send)
    start = next(m for m in messages if m["type"] == "http.response.start")
    headers = {k.decode(): v.decode() for k, v in start["headers"]}
    body = b"".join(m.get("body", b"") for m in messages if m["type"] == "http.response.body")
    return start["status"], headers, body.decode()


class PageLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        href = dict(attrs).get("href", "")
        if tag == "a" and href.startswith("/"):
            self.links.append(href)


class CompanyRoutesTest(unittest.IsolatedAsyncioTestCase):
    async def test_root_is_selection_even_after_a_company_visit(self):
        await request("/sat/en/")
        status, headers, body = await request("/")
        self.assertEqual(status, 200)
        self.assertNotIn("location", headers)
        self.assertIn('href="/sat"', body)
        self.assertIn('href="/sagbs"', body)
        self.assertNotIn("enquiryForm", body)

    async def test_sat_entrypoints(self):
        for path in ("/sat", "/sat/"):
            status, headers, _ = await request(path)
            self.assertEqual(status, 307)
            self.assertEqual(headers["location"], "/sat/en/")

    async def test_all_sat_pages_and_links(self):
        for lang in ("en", "ta"):
            for slug in ("", *PAGE_ROUTES):
                path = f"/sat/{lang}/{slug}"
                with self.subTest(path=path):
                    status, _, body = await request(path)
                    self.assertEqual(status, 200)
                    self.assertIn(f'<html lang="{lang}"', body)
                    self.assertIn(f'href="{get_settings().site_url}{path}"', body)
                    other = "ta" if lang == "en" else "en"
                    self.assertIn(f'href="/sat/{other}/{slug}"', body)
                    links = PageLinks()
                    links.feed(body)
                    for href in links.links:
                        self.assertTrue(href == "/" or href.startswith("/sat/"), href)
                        linked_status, _, _ = await request(href)
                        self.assertEqual(linked_status, 200, href)

    async def test_legacy_urls_preserve_page_and_query(self):
        for lang in ("en", "ta"):
            for slug in ("", *PAGE_ROUTES):
                status, headers, _ = await request(f"/{lang}/{slug}?source=bookmark")
                self.assertEqual(status, 308)
                self.assertEqual(headers["location"], f"/sat/{lang}/{slug}?source=bookmark")
            status, headers, _ = await request(f"/{lang}")
            self.assertEqual(status, 308)
            self.assertEqual(headers["location"], f"/sat/{lang}/")

    async def test_sagbs_company_entrypoint(self):
        status, _, body = await request("/sagbs")
        self.assertEqual(status, 200)
        self.assertIn("Sri Annamalai Global Business Solutions", body)
        self.assertIn('href="/sagbs/services"', body)
        status, headers, _ = await request("/sagbs/")
        self.assertEqual(status, 308)
        self.assertEqual(headers["location"], "/sagbs")

    async def test_sitemap_uses_new_urls(self):
        status, _, body = await request("/sitemap.xml")
        self.assertEqual(status, 200)
        tree = ElementTree.fromstring(body)
        locations = [el.text for el in tree.findall("{*}url/{*}loc")]
        self.assertEqual(len(locations), 25 + len(PUBLIC_PATHS))
        self.assertIn(get_settings().site_url + "/", locations)
        self.assertTrue(all(url == get_settings().site_url + "/" or "/sat/" in url or "/sagbs" in url for url in locations))
        self.assertIn(get_settings().site_url + "/sagbs", locations)

    async def test_company_specific_404(self):
        status, _, body = await request("/missing")
        self.assertEqual(status, 404)
        self.assertIn("Back to company selection", body)
        status, _, body = await request("/sagbs/missing")
        self.assertEqual(status, 404)
        self.assertIn('href="/sagbs"', body)
        status, _, body = await request("/sat/ta/missing")
        self.assertEqual(status, 404)
        self.assertIn('<html lang="ta"', body)
        self.assertIn('href="/sat/ta/"', body)

    async def test_sat_and_legacy_enquiry_api(self):
        payload = {"name": "Routing Test", "phone": "9876543210", "location": "Ranipet",
                   "service": "Manpower", "message": "Test requirement", "language": "ta"}
        with patch("app.routers.enquiry.send_enquiry_email", return_value=True) as email, \
             patch("app.routers.enquiry.append_enquiry_to_sheet", return_value=True) as sheet:
            for path in ("/sat/api/enquiry", "/api/enquiry"):
                status, _, body = await request(path, "POST", payload)
                self.assertEqual(status, 200)
                self.assertTrue(json.loads(body)["success"])
            self.assertEqual(email.call_count, 2)
            self.assertEqual(sheet.call_count, 2)
        status, _, _ = await request("/sat/api/enquiry", "POST", {})
        self.assertEqual(status, 422)


if __name__ == "__main__":
    unittest.main()
