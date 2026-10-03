"""Targeted Phase 9 mobile/zoom/browser check for published A17–A24."""

from __future__ import annotations

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
PAGES = [f"a{number:02}.html" for number in range(17, 25)]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args: object) -> None:
        pass


def main() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        with sync_playwright() as playwright:
            for name in ("chromium", "webkit"):
                browser = getattr(playwright, name).launch()
                try:
                    page = browser.new_page(viewport={"width": 320, "height": 800})
                    errors: list[str] = []
                    page.on("pageerror", lambda error: errors.append(str(error)))
                    for filename in PAGES:
                        for width in (320, 390, 430):
                            page.set_viewport_size({"width": width, "height": 800})
                            page.goto(f"http://127.0.0.1:{server.server_port}/advanced/{filename}")
                            page.locator(".lesson-title").wait_for()
                            page.evaluate("document.querySelector('.content-area').style.setProperty('--reader-font-size', '24px')")
                            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), (name, filename, width, "overflow")
                            assert page.locator(".figure-scroll img").evaluate("img => img.complete && img.naturalWidth > 0"), (name, filename, "image")
                            assert page.locator(".summary-transcript").count() == 1
                            assert page.locator(".answer-toggle").count() == 1
                            page.locator(".answer-toggle").click()
                            page.locator(".answer-content.visible").wait_for(state="visible", timeout=3000)
                            assert not errors, (name, filename, errors)
                    print(f"Phase 9 advanced {name}: {len(PAGES) * 3} page/viewport cases PASS")
                finally:
                    browser.close()
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
