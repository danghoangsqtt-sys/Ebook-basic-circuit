"""Check summary diagrams, readable SVG bounds and phone layout in Chromium."""

from __future__ import annotations

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
DAYS = (7, 14, 21, 28, 35, 42, 43, 48, 49, 50, 55, 56)


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args: object) -> None:
        pass


def main() -> int:
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    Thread(target=server.serve_forever, daemon=True).start()
    cases = 0
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            try:
                for day in DAYS:
                    asset = f"assets/images/lessons/day{day:02d}-summary.svg"
                    svg_page = browser.new_page()
                    svg_page.goto(f"http://127.0.0.1:{server.server_port}/{asset}")
                    bounds = svg_page.evaluate("""() => {
                      const svg = document.querySelector('svg');
                      const width = svg.viewBox.baseVal.width;
                      const height = svg.viewBox.baseVal.height;
                      return [...svg.querySelectorAll('text')].map(el => {
                        const box = el.getBBox();
                        return {label: el.textContent, x: box.x, y: box.y,
                          right: box.x + box.width, bottom: box.y + box.height,
                          width, height};
                      });
                    }""")
                    assert bounds, f"Day {day}: no SVG labels"
                    for label in bounds:
                        assert label["x"] >= 20 and label["right"] <= label["width"] - 20, (
                            f"Day {day}: clipped label {label}")
                        assert label["y"] >= 0 and label["bottom"] <= label["height"], (
                            f"Day {day}: vertical clipping {label}")
                    svg_page.close()
                    for width in (320, 390, 1280):
                        page = browser.new_page(viewport={"width": width, "height": 900})
                        errors: list[str] = []
                        page.on("pageerror", lambda error: errors.append(str(error)))
                        url = f"week{(day-1)//7+1}/day{day:02d}.html"
                        page.goto(f"http://127.0.0.1:{server.server_port}/{url}")
                        state = page.evaluate("""async () => {
                          const img = document.querySelector('.figure--summary img');
                          if (img) { img.loading = 'eager'; await img.decode().catch(() => {}); }
                          const r = img?.getBoundingClientRect();
                          return {src: img?.getAttribute('src'), alt: img?.alt,
                            loaded: img?.complete && img.naturalWidth > 0,
                            transcript: Boolean(document.querySelector('.summary-transcript ol li')),
                            viewport: document.documentElement.clientWidth,
                            scroll: document.documentElement.scrollWidth,
                            left: r?.left, right: r?.right, imageWidth: r?.width};
                        }""")
                        assert state["src"] == f"../{asset}" and state["alt"], f"{url}: missing summary/alt"
                        assert state["loaded"] and state["transcript"], f"{url}: image/transcript failure"
                        assert state["scroll"] <= state["viewport"] + 1, f"{url} {width}px: overflow"
                        assert state["imageWidth"] > 0 and state["left"] >= -1 and state["right"] <= width + 1, (
                            f"{url} {width}px: image outside viewport")
                        assert not errors, f"{url}: JavaScript error: {errors}"
                        cases += 1
                        page.close()
                print(f"PASS {len(DAYS)} SVG bounds and {cases} lesson/viewport cases (320/390/1280px)")
            finally:
                browser.close()
    finally:
        server.shutdown()
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
