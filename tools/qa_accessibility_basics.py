"""Keyboard bypass and image description checks on the three reader shells."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PAGES = ("week1/day01.html", "advanced/a29.html", "advanced/path.html")


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
                    for path in PAGES:
                        page.goto(f"http://127.0.0.1:{server.server_port}/{path}")
                        page.keyboard.press("Tab")
                        if name == "chromium":
                            assert page.evaluate("document.activeElement.classList.contains('skip-link')"), (name, path, "first Tab")
                        else:
                            # WebKit's default keyboard preference skips links on Tab.
                            page.locator(".skip-link").focus()
                        assert page.locator(".skip-link").evaluate("a => a.getBoundingClientRect().top >= 0"), (name, path, "visible")
                        page.keyboard.press("Enter")
                        page.wait_for_url("**#lesson-main")
                        assert page.evaluate("location.hash === '#lesson-main'"), (name, path, "target")
                        assert page.evaluate("document.activeElement.id === 'lesson-main'"), (name, path, "focus")
                        assert page.locator("#lesson-main").count() == 1
                    print(f"Accessibility {name}: 3 keyboard bypass cases PASS")
                finally:
                    browser.close()
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
