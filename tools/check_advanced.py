"""Check published advanced lessons, their editable figures and source records."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]


class Lesson(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.h1 = 0
        self.images: list[dict[str, str]] = []
        self.classes: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "h1":
            self.h1 += 1
        if tag == "img":
            self.images.append(values)
        self.classes.extend(values.get("class", "").split())


def main() -> int:
    pages = sorted((ROOT / "advanced").glob("a[0-9][0-9].html"))
    ids = [page.stem for page in pages]
    errors: list[str] = []
    if ids and ids != [f"a{number:02}" for number in range(1, len(ids) + 1)]:
        errors.append(f"Advanced pages are not contiguous: {ids}")
    registry = ROOT / "assets/images/advanced/SOURCES.md"
    source_text = registry.read_text(encoding="utf-8") if registry.is_file() else ""
    for page in pages:
        html = page.read_text(encoding="utf-8")
        parser = Lesson()
        parser.feed(html)
        image_name = f"{page.stem}.svg"
        image = ROOT / "assets/images/advanced" / image_name
        if parser.h1 != 1 or "objectives-list" not in parser.classes:
            errors.append(f"{page.name}: expected one h1 and objectives-list")
        if not any(img.get("src", "").endswith(image_name) and img.get("alt", "").strip()
                   and img.get("width", "").isdigit() and img.get("height", "").isdigit()
                   for img in parser.images):
            errors.append(f"{page.name}: missing labeled SVG {image_name}")
        for required in ("figure-caption", "figure-source", "summary-transcript", "exercise-section",
                         "answer-content", "checklist"):
            if required not in parser.classes:
                errors.append(f"{page.name}: missing {required}")
        if f"renderSidebar('{page.stem}.html')" not in html:
            errors.append(f"{page.name}: sidebar active page mismatch")
        if len(re.findall(r'href="https://', html)) < 1:
            errors.append(f"{page.name}: no primary source link")
        if not image.is_file():
            errors.append(f"{page.name}: missing {image_name}")
        else:
            try:
                svg = ElementTree.parse(image).getroot()
                tags = {child.tag.rsplit("}", 1)[-1] for child in svg}
                if not svg.tag.endswith("svg") or not {"title", "desc"} <= tags:
                    errors.append(f"{image_name}: missing SVG title/desc")
            except ElementTree.ParseError:
                errors.append(f"{image_name}: invalid XML")
        if f"`{image_name}`" not in source_text:
            errors.append(f"{image_name}: no source record")
    if pages and not registry.is_file():
        errors.append("assets/images/advanced/SOURCES.md missing")
    print(f"Advanced lessons: {len(pages)}; errors: {len(errors)}")
    for error in errors:
        print(error)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
