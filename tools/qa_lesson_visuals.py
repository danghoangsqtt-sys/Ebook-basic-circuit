"""Check lesson figures on phone and desktop viewports using Chromium.

Usage: python tools/qa_lesson_visuals.py --start 1 --end 14
"""

from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args: object) -> None:
        pass


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=56)
    parser.add_argument("--widths", nargs="+", type=int, default=[320, 360, 390, 430, 1280])
    args = parser.parse_args()
    if not 1 <= args.start <= args.end <= 56:
        raise ValueError("Invalid lesson range")
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    cases = 0
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            try:
                for width in args.widths:
                    page = browser.new_page(viewport={"width": width, "height": 900})
                    errors: list[str] = []
                    page.on("pageerror", lambda error: errors.append(str(error)))
                    for day in range(args.start, args.end + 1):
                        path = f"week{(day - 1) // 7 + 1}/day{day:02}.html"
                        page.goto(f"http://127.0.0.1:{server.server_port}/{path}", wait_until="load")
                        state = page.evaluate("""async () => {
                          const image = document.querySelector('.figure--overview img');
                          const all = [...document.querySelectorAll('.content-area .figure img')];
                          await Promise.all(all.map(async img => {
                            img.loading = 'eager';
                            await img.decode().catch(() => {});
                          }));
                          return {
                            viewport: document.documentElement.clientWidth,
                            scroll: document.documentElement.scrollWidth,
                            overview: Boolean(image),
                            expected: image?.getAttribute('src').split('/').at(-1),
                            captions: [...document.querySelectorAll('.content-area .figure')].
                              filter(fig => fig.querySelector('img')).
                              every(fig => fig.querySelector('.figure-caption') &&
                                fig.querySelector('.figure-source')?.textContent.trim()),
                            images: all.map(img => ({src: img.getAttribute('src'),
                              loaded: img.complete && img.naturalWidth > 0,
                              alt: Boolean(img.alt.trim()),
                              width: img.getBoundingClientRect().width,
                              x: img.getBoundingClientRect().x}))
                          };
                        }""")
                        assert state["overview"], f"{path}: no overview image"
                        assert state["captions"], f"{path}: missing figure caption/source"
                        assert state["expected"] == f"day{day:02}-overview.svg", f"{path}: wrong image"
                        assert state["scroll"] <= state["viewport"] + 1, f"{path} {width}px: horizontal overflow"
                        for image in state["images"]:
                            assert image["loaded"] and image["alt"], f"{path}: broken/unlabelled {image['src']}"
                            assert image["width"] > 0 and image["x"] >= -1, f"{path}: hidden image {image['src']}"
                            assert image["x"] + image["width"] <= width + 1, f"{path}: image crosses viewport"
                        assert not errors, f"{path}: JavaScript error: {errors}"
                        cases += 1
                    page.close()
                print(f"PASS {cases} lesson/viewport checks; days {args.start:02}–{args.end:02}; widths {'/'.join(map(str,args.widths))}px")
            finally:
                browser.close()
    finally:
        server.shutdown()
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
