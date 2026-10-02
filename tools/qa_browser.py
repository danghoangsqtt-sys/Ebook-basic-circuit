"""End-to-end checks for the static reader, served over a local HTTP origin.

Requires the optional Playwright Python package and Chromium or WebKit browser.
Run ``python tools/qa_browser.py`` or ``python tools/qa_browser.py --quick --browser webkit``.
"""

from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parent.parent
LESSONS = [f"week{(day - 1) // 7 + 1}/day{day:02}.html" for day in range(1, 57)]
SAMPLES = ["week1/day01.html", "week4/day28.html", "week8/day56.html"]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args: object) -> None:
        pass


def page_url(server: ThreadingHTTPServer, path: str) -> str:
    return f"http://127.0.0.1:{server.server_port}/{path}"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def select_prose(page) -> None:
    page.evaluate("""() => {
      const p = document.querySelector('.content-area .lesson-subtitle');
      if (!p) throw new Error('No selectable prose');
      const range = document.createRange();
      range.setStart(p.firstChild, 0);
      range.setEnd(p.firstChild, 24);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
    }""")


def check_home(browser, server: ThreadingHTTPServer) -> int:
    page = browser.new_page(viewport={"width": 390, "height": 800})
    errors: list[str] = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    for width in (320, 360, 390, 430):
        page.set_viewport_size({"width": width, "height": 800})
        page.goto(page_url(server, "index.html"))
        page.locator("#full-catalog a").first.wait_for(state="attached")
        check(page.evaluate("document.documentElement.scrollWidth <= innerWidth"), f"Home overflows at {width}")
        check(page.locator(".roadmap article").count() == 8, "Home must show 8 weeks")
        links = page.locator("#full-catalog a")
        check(links.count() == 56, "Home must expose 56 lessons")
        check(len(set(links.evaluate_all("nodes => nodes.map(node => node.pathname)"))) == 56,
              "Home lesson URLs must be unique")
        check(page.locator("h1").count() == 1, "Home must have one h1")
    check(not errors, f"Home JavaScript errors: {errors}")
    page.close()
    return 4


def check_layout(browser, server: ThreadingHTTPServer, quick: bool) -> int:
    page = browser.new_page(viewport={"width": 320, "height": 800})
    errors: list[str] = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    paths = SAMPLES if quick else LESSONS
    count = 0
    for path in paths:
        page.goto(page_url(server, path))
        page.locator(".ebook-search-trigger").wait_for()
        width = page.evaluate("document.documentElement.scrollWidth")
        check(width <= 320, f"{path} overflows at 320px: {width}px")
        check(page.locator(".sidebar-lesson").count() == 56, f"{path} sidebar has != 56 lessons")
        count += 1
    for path in SAMPLES:
        for width in (360, 390, 430, 160, 180, 195, 215):
            page.set_viewport_size({"width": width, "height": 800})
            page.goto(page_url(server, path))
            page.locator("#reader-font-size").fill("24")
            actual = page.evaluate("document.documentElement.scrollWidth")
            check(actual <= width, f"{path} at 24px font overflows {width}px: {actual}px")
            count += 1
    check(not errors, f"Lesson JavaScript errors: {errors[:3]}")
    page.close()
    return count


def check_reader_flow(browser, server: ThreadingHTTPServer) -> None:
    page = browser.new_page(viewport={"width": 390, "height": 800})
    errors: list[str] = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto(page_url(server, "week1/day01.html"))
    page.locator("[data-action=highlight]").wait_for(state="attached")

    # Menu and basic settings survive keyboard use and reload.
    menu = page.locator(".btn-menu")
    menu.click()
    check(menu.get_attribute("aria-expanded") == "true", "Lesson menu did not open")
    page.keyboard.press("Escape")
    check(menu.get_attribute("aria-expanded") == "false", "Escape did not close lesson menu")
    check(menu.evaluate("el => document.activeElement === el"), "Menu focus not returned")
    slider = page.locator("#reader-font-size")
    slider.fill("24")
    check(page.locator(".content-area p.lesson-subtitle").evaluate("el => getComputedStyle(el).fontSize") == "24px",
          "Font slider did not affect prose")
    slider.focus()
    slider.press("ArrowLeft")
    check(slider.input_value() == "23", "Font slider keyboard failed")
    page.reload()
    check(page.locator("#reader-font-size").input_value() == "23", "Font size not persisted")
    page.locator(".reader-font-controls button").click()
    check(page.locator("#reader-font-size").input_value() == "16", "Font reset failed")

    check(page.locator(".progress-label").inner_text().startswith("1/56"), "Visit progress not recorded")
    checklist = page.locator('.checklist-item input[type="checkbox"]').first
    checklist.check()
    page.reload()
    check(page.locator('.checklist-item input[type="checkbox"]').first.is_checked(), "Checklist not persisted")
    answer = page.locator(".answer-toggle").first
    answer.click()
    check(answer.locator("xpath=following-sibling::*[1]").evaluate("el => el.classList.contains('visible')"),
          "Answer did not open")
    page.emulate_media(media="print")
    check(page.locator(".site-header").evaluate("el => getComputedStyle(el).display") == "none",
          "Header appears in print layout")
    check(page.locator(".content-area").evaluate("el => getComputedStyle(el).display") != "none",
          "Lesson missing from print layout")
    page.emulate_media(media="screen")

    page.locator(".ebook-search-trigger").wait_for()
    page.locator(".ebook-search-trigger").click()
    query = page.locator("#ebook-search-input")
    query.fill("dien ap")
    check("day01.html" in page.locator(".ebook-search-results a").first.get_attribute("href"),
          "Accent-free search did not rank Bài 1 first")
    page.keyboard.press("Escape")

    select_prose(page)
    page.locator(".ebook-selection-trigger").click()
    page.locator("[data-action=related]").click()
    check(bool(page.locator("#ebook-search-input").input_value()), "Related search got no selected text")
    page.keyboard.press("Escape")

    select_prose(page)
    page.locator(".ebook-selection-trigger").click()
    page.locator("[data-action=highlight]").click()
    check(page.locator("mark[data-ebook-highlight-id]").count() > 0, "No visible highlight")
    check(len(page.evaluate("EbookHighlights.getAll()")) == 1, "Highlight not saved")
    page.reload()
    page.locator("mark[data-ebook-highlight-id]").first.wait_for()
    page.locator(".ebook-highlights-panel").evaluate("el => el.open = true")
    page.locator(".ebook-highlights-controls button").first.click()
    check(page.locator("mark[data-ebook-highlight-id]").first.evaluate("el => document.activeElement === el"),
          "Jump did not focus highlight")
    page.locator(".ebook-highlights-controls button").nth(1).click()
    check(len(page.evaluate("EbookHighlights.getAll()")) == 0, "Highlight not removed")

    theme = page.locator(".a11y-btn-theme")
    initial_theme = page.locator("html").get_attribute("data-theme")
    theme.click()
    check(page.locator("html").get_attribute("data-theme") != initial_theme, "Theme toggle failed")
    check(not errors, f"Reader JavaScript errors: {errors[:3]}")
    page.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quick", action="store_true", help="scan 3 lessons instead of all 56")
    parser.add_argument("--browser", choices=("chromium", "webkit"), default="chromium")
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        with sync_playwright() as playwright:
            browser = getattr(playwright, args.browser).launch()
            try:
                home = check_home(browser, server)
                lessons = check_layout(browser, server, args.quick)
                check_reader_flow(browser, server)
            finally:
                browser.close()
    finally:
        server.shutdown()
        thread.join(timeout=5)
    print(f"QA PASS ({args.browser}): {home} home viewports, {lessons} lesson/viewport checks, reader flow")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
