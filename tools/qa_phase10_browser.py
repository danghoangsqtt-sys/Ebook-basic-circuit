"""Check A29–A32 at 24px reader text on mobile in Chromium and WebKit."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


def main():
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    Thread(target=server.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as playwright:
            for name in ("chromium", "webkit"):
                browser = getattr(playwright, name).launch()
                try:
                    page = browser.new_page(viewport={"width": 320, "height": 800})
                    errors = []
                    page.on("pageerror", lambda error: errors.append(str(error)))
                    for number in range(29, 33):
                        for width in (320, 360, 390, 430):
                            page.set_viewport_size({"width": width, "height": 800})
                            page.goto(f"http://127.0.0.1:{server.server_port}/advanced/a{number:02}.html")
                            page.locator(".lesson-title").wait_for()
                            page.evaluate("document.querySelector('.content-area').style.setProperty('--reader-font-size', '24px')")
                            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), (name, number, width, "overflow")
                            assert page.locator(".figure-scroll img").evaluate("img => img.complete && img.naturalWidth > 0"), (name, number, "image")
                            assert page.locator(".summary-transcript").count() == 1
                            page.locator(".answer-toggle").click()
                            page.locator(".answer-content.visible").wait_for(state="visible", timeout=3000)
                            assert not errors, (name, number, errors)
                    for width in (320, 360, 390, 430):
                        page.set_viewport_size({"width": width, "height": 800})
                        page.goto(f"http://127.0.0.1:{server.server_port}/advanced/path.html")
                        page.locator(".lesson-title").wait_for()
                        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), (name, "path", width)
                        assert page.locator('a[href="a32.html"]').count() == 1
                        assert not errors, (name, "path", errors)
                    print(f"Phase 10 {name}: 20 page/viewport cases PASS")
                finally:
                    browser.close()
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
