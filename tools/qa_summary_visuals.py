"""Check summary diagrams, readable SVG bounds and phone layout in Chromium."""

from __future__ import annotations

import argparse
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--browser", choices=("chromium", "webkit"), default="chromium")
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    Thread(target=server.serve_forever, daemon=True).start()
    cases = 0
    try:
        with sync_playwright() as playwright:
            browser = getattr(playwright, args.browser).launch()
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
                        page.locator("#reader-font-size").fill("24")
                        page.locator(".summary-transcript summary").click()
                        state = page.evaluate("""async () => {
                          const img = document.querySelector('.figure--summary img');
                          if (img) { img.loading = 'eager'; await img.decode().catch(() => {}); }
                          const r = img?.getBoundingClientRect();
                          return {src: img?.getAttribute('src'), alt: img?.alt,
                            loaded: img?.complete && img.naturalWidth > 0,
                            transcript: Boolean(document.querySelector('.summary-transcript ol li')),
                            viewport: document.documentElement.clientWidth,
                            scroll: document.documentElement.scrollWidth,
                            scrollX: window.scrollX,
                            boxes: ['body','.content-area','.table-wrap','pre','.summary-transcript'].map(s => {
                              const e=document.querySelector(s), r=e?.getBoundingClientRect();
                              return {s,left:r?.left,right:r?.right,width:r?.width,
                                scroll:e?.scrollWidth,client:e?.clientWidth,
                                overflow:e && getComputedStyle(e).overflowX};
                            }),
                            overflowBoxes: [...document.querySelectorAll('body *')].filter(e =>
                              e.scrollWidth > e.clientWidth+1 &&
                              getComputedStyle(e).overflowX === 'visible').slice(0,15).map(e =>
                              ({tag:e.tagName,cls:e.className,client:e.clientWidth,scroll:e.scrollWidth,
                                text:e.textContent.trim().slice(0,100)})),
                            offenders: [...document.querySelectorAll('body *')]
                              .filter(el => {
                                const box = el.closest('.table-wrap,.code-block,.circuit-ascii,.figure,pre');
                                return el.getBoundingClientRect().right > innerWidth + 1 &&
                                  (!box || box === el);
                              })
                              .slice(0, 15).map(el => ({tag: el.tagName, className: el.className,
                                text: el.textContent.trim().slice(0, 60),
                                right: Math.round(el.getBoundingClientRect().right)})),
                            left: r?.left, right: r?.right, imageWidth: r?.width};
                        }""")
                        assert state["src"] == f"../{asset}" and state["alt"], f"{url}: missing summary/alt"
                        assert state["loaded"] and state["transcript"], f"{url}: image/transcript failure"
                        assert state["scroll"] <= state["viewport"] + 1, (
                            f"{url} {width}px: overflow to {state['scroll']}px; scrollX={state['scrollX']}; {state['boxes']}; {state['overflowBoxes']}; {state['offenders']}")
                        assert state["imageWidth"] > 0 and state["left"] >= -1 and state["right"] <= width + 1, (
                            f"{url} {width}px: image outside viewport")
                        assert not errors, f"{url}: JavaScript error: {errors}"
                        cases += 1
                        page.close()
                print(f"PASS ({args.browser}) {len(DAYS)} SVG bounds and {cases} lesson/viewport cases (320/390/1280px, 24px font)")
            finally:
                browser.close()
    finally:
        server.shutdown()
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
