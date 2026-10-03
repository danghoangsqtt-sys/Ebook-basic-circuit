"""Check sidebar entries against foundation and advanced lesson headings.

Use --fix after editing a lesson heading to refresh sidebar labels. URLs remain
stable; the homepage reads the same CURRICULUM data.
"""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SIDEBAR = ROOT / "assets/js/sidebar-data.js"
ENTRY = re.compile(
    r"(\{\s*day:\s*(\d+),\s*title:\s*')([^']+)(',\s*file:\s*')([^']+)('\s*\})"
)
ADV_ENTRY = re.compile(
    r"\{\s*id:\s*'(a\d{2})',\s*number:\s*'(A\d{2})',\s*title:\s*'([^']+)',\s*file:\s*'([^']+)'\s*\}"
)


class Heading(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.inside = False
        self.parts: list[str] = []
        self.headings: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "h1":
            self.inside = True
            self.parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "h1" and self.inside:
            self.headings.append(" ".join("".join(self.parts).split()))
            self.inside = False

    def handle_data(self, data: str) -> None:
        if self.inside:
            self.parts.append(data)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fix", action="store_true")
    args = parser.parse_args()
    source = SIDEBAR.read_text(encoding="utf-8")
    matches = list(ENTRY.finditer(source))
    if len(matches) != 56:
        print(f"Expected 56 menu entries, found {len(matches)}")
        return 1
    expected_days = list(range(1, 57))
    actual_days = [int(match.group(2)) for match in matches]
    if actual_days != expected_days:
        print("Menu entries must enumerate days 1–56 exactly once in order")
        return 1

    mismatches: list[str] = []

    def replace(match: re.Match[str]) -> str:
        day = int(match.group(2))
        expected_path = f"../week{(day - 1) // 7 + 1}/day{day:02}.html"
        if match.group(5) != expected_path:
            mismatches.append(f"D{day:02}: bad URL {match.group(5)!r}")
        lesson = ROOT / expected_path.removeprefix("../")
        if not lesson.is_file():
            mismatches.append(f"D{day:02}: missing lesson {lesson}")
            return match.group(0)
        heading = Heading()
        heading.feed(lesson.read_text(encoding="utf-8"))
        if len(heading.headings) != 1 or not heading.headings[0]:
            mismatches.append(f"D{day:02}: expected one nonempty h1")
            return match.group(0)
        title = heading.headings[0]
        if match.group(3) != title:
            mismatches.append(f"D{day:02}: {match.group(3)!r} != {title!r}")
        if "'" in title:
            mismatches.append(f"D{day:02}: apostrophe in h1 needs JS escaping")
            return match.group(0)
        return match.group(1) + title + match.group(4) + match.group(5) + match.group(6)

    updated = ENTRY.sub(replace, source)
    advanced_files = sorted((ROOT / "advanced").glob("a[0-9][0-9].html"))
    advanced_matches = list(ADV_ENTRY.finditer(source))
    if [match.group(1) for match in advanced_matches] != [path.stem for path in advanced_files]:
        mismatches.append("Advanced menu entries must match published aNN pages in order")
    for match in advanced_matches:
        lesson_id, number, title, url = match.groups()
        expected_path = f"../advanced/{lesson_id}.html"
        if number != lesson_id.upper() or url != expected_path:
            mismatches.append(f"{lesson_id}: bad number or URL")
            continue
        lesson = ROOT / "advanced" / f"{lesson_id}.html"
        if not lesson.is_file():
            mismatches.append(f"{lesson_id}: missing lesson")
            continue
        heading = Heading()
        heading.feed(lesson.read_text(encoding="utf-8"))
        if heading.headings != [title]:
            mismatches.append(f"{lesson_id}: sidebar title does not match h1")
    if args.fix and not any("bad URL" in item or "missing lesson" in item or "expected one" in item for item in mismatches):
        SIDEBAR.write_text(updated, encoding="utf-8", newline="\n")
        print(f"Updated {len(mismatches)} title(s); 56 URLs preserved")
        return 0
    if mismatches:
        print("\n".join(mismatches))
        return 1
    print(f"Navigation matches 56 foundation and {len(advanced_matches)} advanced lesson headings and URLs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
