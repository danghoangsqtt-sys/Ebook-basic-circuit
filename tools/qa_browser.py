"""End-to-end checks for the static reader, served over a local HTTP origin.

Requires the optional Playwright Python package and Chromium or WebKit browser.
Run ``python tools/qa_browser.py`` or ``python tools/qa_browser.py --quick --browser webkit``.
"""

from __future__ import annotations

import argparse
import json
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parent.parent
LESSONS = [f"week{(day - 1) // 7 + 1}/day{day:02}.html" for day in range(1, 57)]
ADVANCED = [f"advanced/{path.name}" for path in sorted((ROOT / "advanced").glob("a[0-9][0-9].html"))]
LESSONS.extend(ADVANCED)
SAMPLES = ["week1/day01.html", "week4/day28.html", "week8/day56.html", *ADVANCED]
TOTAL_LESSONS = len(LESSONS)
TOTAL_GROUPS = 8 + int(bool(ADVANCED))


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
        check(page.locator(".roadmap article").count() == TOTAL_GROUPS, "Home roadmap group count mismatch")
        links = page.locator("#full-catalog a")
        check(links.count() == TOTAL_LESSONS, "Home lesson count mismatch")
        check(len(set(links.evaluate_all("nodes => nodes.map(node => node.pathname)"))) == TOTAL_LESSONS,
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
        check(page.locator(".sidebar-lesson").count() == TOTAL_LESSONS, f"{path} sidebar lesson count mismatch")
        if path in SAMPLES:
            for query, expected in (("điện áp", {"day01"}), ("dien ap", {"day01"}),
                                    ("voltage", {"day01"}), ("resistor", {"day03", "a01", "a02"}),
                                    ("capacitor", {"day08", "a03", "a04"}), ("sensor", {"day27"}),
                                    ("pcb", {"day33"})):
                first = page.evaluate("q => EbookSearch.search(q)[0]", query)
                check(first and first["id"] in expected and first["snippet"] and first["heading"]
                      and "�" not in first["snippet"] and "�" not in first["heading"],
                      f"Search quality failed for {query} on {path}: {first}")
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

    progress_label = page.locator(".progress-label").inner_text()
    check(progress_label.startswith(f"1/{TOTAL_LESSONS}"), f"Visit progress not recorded: {progress_label}")
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


def check_library_flow(browser, server: ThreadingHTTPServer) -> None:
    page = browser.new_page(viewport={"width": 390, "height": 800})
    errors: list[str] = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    for path in ("week1/day01.html", "week4/day28.html"):
        page.goto(page_url(server, path))
        page.locator("[data-action=highlight]").wait_for(state="attached")
        select_prose(page)
        page.locator(".ebook-selection-trigger").click()
        page.locator("[data-action=highlight]").click()
        check(page.locator("mark[data-ebook-highlight-id]").count() > 0, f"No mark in {path}")
    page.goto(page_url(server, "highlights.html"))
    page.locator(".highlight-state[data-state=anchored]").first.wait_for()
    check(page.locator(".highlight-item").count() == 2, "Library did not show 2 lessons")
    for width in (320, 360, 390, 430):
        page.set_viewport_size({"width": width, "height": 800})
        check(page.evaluate("document.documentElement.scrollWidth <= innerWidth"),
              f"Library overflows at {width}px")
    page.locator("#highlight-lesson").select_option("day28")
    check(page.locator(".highlight-item").count() == 1, "Lesson filter failed")
    page.locator("#highlight-lesson").select_option("")
    page.locator("#highlight-query").fill("Tổng hợp")
    check(page.locator(".highlight-item").count() == 1, "Quote filter failed")
    page.locator("#highlight-query").fill("")
    page.evaluate("""() => {
      const all = JSON.parse(localStorage.getItem('ebook-highlights-v1'));
      const orphan = structuredClone(all[0]);
      orphan.id = 'qa-orphan';
      orphan.quote = 'Đoạn không còn trong bài này';
      localStorage.setItem('ebook-highlights-v1', JSON.stringify([...all, orphan]));
    }""")
    page.reload()
    page.locator(".highlight-state[data-state=orphan]").wait_for()
    orphan = page.locator(".highlight-item").filter(has_text="Đoạn không còn trong bài này")
    check("highlight=" not in orphan.locator("a").get_attribute("href"),
          "Orphan link must not jump to an uncertain position")
    page.locator("#highlight-state").select_option("orphan")
    check(page.locator(".highlight-item").count() == 1, "Anchor-state filter failed")
    page.locator("#highlight-state").select_option("")
    page.locator(".highlight-item").filter(has_text="Đoạn không còn trong bài này").locator("button").click()
    check(page.locator(".highlight-item").count() == 2, "Deleting one mark affected others")
    page.locator(".highlight-item").first.locator("a").click()
    page.locator("mark[data-ebook-highlight-id]").first.wait_for()
    check(not errors, f"Library JavaScript errors: {errors[:3]}")
    page.close()


def check_reader_data_flow(browser, server: ThreadingHTTPServer) -> None:
    page = browser.new_page(viewport={"width": 390, "height": 800}, accept_downloads=True)
    errors: list[str] = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto(page_url(server, "week1/day01.html"))
    page.locator("[data-action=highlight]").wait_for(state="attached")
    select_prose(page)
    page.locator(".ebook-selection-trigger").click()
    page.locator("[data-action=highlight]").click()
    page.locator("#reader-font-size").fill("21")
    page.locator(".checklist-item input[type=checkbox]").first.check()
    page.locator(".a11y-btn-theme").click()
    page.locator(".reader-data-link").click()
    check(page.url.endswith("reader-data.html"), "Lesson backup link failed")
    page.evaluate("""() => {
      localStorage.removeItem('ebook-fontsize-px');
      localStorage.setItem('ebook-fontsize', '4');
    }""")
    check(page.evaluate("ReaderData.readCurrent().settings.fontSizePx") == 20,
          "Legacy font setting was not included in backup")
    page.evaluate("""() => {
      localStorage.setItem('ebook-fontsize-px', '21');
      localStorage.removeItem('ebook-fontsize');
    }""")
    for width in (320, 360, 390, 430):
        page.set_viewport_size({"width": width, "height": 800})
        check(page.evaluate("document.documentElement.scrollWidth <= innerWidth"),
              f"Reader data page overflows at {width}px")
    with page.expect_download() as info:
        page.locator("#export-button").click()
    exported = json.loads(Path(info.value.path()).read_text(encoding="utf-8"))
    check(len(exported["data"]["highlights"]) == 1, "Export missed highlight")
    check(exported["data"]["settings"]["fontSizePx"] == 21, "Export missed font size")
    check(exported["data"]["checklists"].get("day01", {}).get("0") is True,
          "Export missed checklist")
    backup_bytes = json.dumps(exported, ensure_ascii=False).encode("utf-8")
    original_quote = exported["data"]["highlights"][0]["quote"]
    page.evaluate("""() => {
      for (const key of Object.keys(localStorage)) {
        if (key.startsWith('checklist_') || ['ebook-highlights-v1','lessonProgress','ebook-fontsize-px','ebook-theme','weekStates'].includes(key)) localStorage.removeItem(key);
      }
    }""")

    def upload(data: bytes) -> None:
        page.locator("#import-file").set_input_files({"name": "reader.json", "mimeType": "application/json", "buffer": data})

    upload(b"{broken")
    check("JSON không hợp lệ" in page.locator("#import-status").inner_text(), "Invalid JSON accepted")
    invalid = json.loads(json.dumps(exported))
    del invalid["data"]["settings"]
    upload(json.dumps(invalid).encode())
    check(page.locator("#import-preview").is_hidden(), "Missing settings accepted")
    invalid = json.loads(json.dumps(exported))
    invalid["version"] = 0
    upload(json.dumps(invalid).encode())
    check(page.locator("#import-preview").is_hidden(), "Old version accepted")
    invalid = json.loads(json.dumps(exported))
    invalid["exportedAt"] = "1"
    upload(json.dumps(invalid).encode())
    check(page.locator("#import-preview").is_hidden(), "Invalid date accepted")
    invalid["exportedAt"] = "2026-02-31T00:00:00Z"
    upload(json.dumps(invalid).encode())
    check(page.locator("#import-preview").is_hidden(), "Impossible calendar date accepted")
    invalid = json.loads(json.dumps(exported))
    invalid["data"]["highlights"][0]["quote"] = "x" * 1001
    upload(json.dumps(invalid).encode())
    check(page.locator("#import-preview").is_hidden(), "Oversize quote accepted")
    check(page.evaluate("localStorage.getItem('ebook-highlights-v1')") is None,
          "Invalid import modified existing data")

    upload(backup_bytes)
    page.locator("#import-preview").wait_for(state="visible")
    check("1 dấu trong tệp" in page.locator("#preview-summary").inner_text(), "Preview count wrong")
    page.locator("input[value=replace]").check()
    page.locator("#import-button").click()
    restored = page.evaluate("ReaderData.readCurrent()")
    check(len(restored["highlights"]) == 1 and restored["highlights"][0]["quote"] == original_quote,
          "Round trip lost highlight")
    check(restored["settings"]["fontSizePx"] == 21 and restored["settings"]["theme"] == "light",
          "Round trip lost settings")
    check(restored["progress"].get("day01") is True and restored["checklists"]["day01"]["0"] is True,
          "Round trip lost progress or checklist")

    conflict = json.loads(json.dumps(exported))
    conflict["data"]["highlights"][0]["quote"] = "Khác nội dung cùng ID"
    upload(json.dumps(conflict, ensure_ascii=False).encode("utf-8"))
    page.locator("#import-preview").wait_for(state="visible")
    check("1 xung đột" in page.locator("#preview-summary").inner_text(), "Conflict not reported")
    page.locator("input[value=merge]").check()
    page.locator("#import-button").click()
    check(page.evaluate("ReaderData.readCurrent().highlights[0].quote") == original_quote,
          "Merge overwrote conflicting mark")

    upload(backup_bytes)
    page.locator("#import-preview").wait_for(state="visible")
    before_failure = page.evaluate("JSON.stringify(ReaderData.readCurrent())")
    page.evaluate("""() => {
      const old = Storage.prototype.setItem;
      let writes = 0;
      Storage.prototype.setItem = function(...args) {
        writes += 1;
        if (writes === 2) throw new Error('simulated storage error');
        return old.apply(this, args);
      };
    }""")
    page.locator("#import-button").click()
    check("Lưu thất bại" in page.locator("#import-status").inner_text(), "Storage failure not reported")
    check(page.evaluate("JSON.stringify(ReaderData.readCurrent())") == before_failure,
          "Storage failure changed existing data")
    check(not errors, f"Reader data JavaScript errors: {errors[:3]}")
    page.close()


def check_advanced_reader_flow(browser, server: ThreadingHTTPServer) -> None:
    if not ADVANCED:
        return
    page = browser.new_page(viewport={"width": 390, "height": 800}, accept_downloads=True)
    errors: list[str] = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto(page_url(server, ADVANCED[0]))
    page.locator("[data-action=highlight]").wait_for(state="attached")
    check(page.locator(".progress-label").inner_text().startswith(f"1/{TOTAL_LESSONS}"),
          "Advanced visit progress not recorded")
    page.locator(".checklist-item input[type=checkbox]").first.check()
    select_prose(page)
    page.locator(".ebook-selection-trigger").click()
    page.locator("[data-action=highlight]").click()
    check(page.evaluate("EbookHighlights.getAll()[0]?.lessonId") == "a01", "Advanced highlight ID mismatch")
    page.goto(page_url(server, "highlights.html"))
    page.locator(".highlight-state[data-state=anchored]").first.wait_for()
    check(page.locator(".highlight-item").count() == 1, "Advanced highlight missing from library")
    check("advanced/a01.html" in page.locator(".highlight-item a").first.get_attribute("href"),
          "Advanced highlight link points to wrong page")
    page.goto(page_url(server, "reader-data.html"))
    current = page.evaluate("ReaderData.readCurrent()")
    check(current["progress"].get("a01") is True, "Advanced progress missing from backup")
    check(current["checklists"].get("a01", {}).get("0") is True, "Advanced checklist missing from backup")
    check(current["highlights"][0]["lessonId"] == "a01", "Advanced highlight missing from backup")
    check(not errors, f"Advanced reader JavaScript errors: {errors[:3]}")
    page.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quick", action="store_true", help="scan foundation samples and published advanced lessons")
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
                check_library_flow(browser, server)
                check_reader_data_flow(browser, server)
                check_advanced_reader_flow(browser, server)
            finally:
                browser.close()
    finally:
        server.shutdown()
        thread.join(timeout=5)
    print(f"QA PASS ({args.browser}): {home} home viewports, {lessons} lesson/viewport checks, reader, library and backup flows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
