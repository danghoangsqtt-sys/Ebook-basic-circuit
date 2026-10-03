"""Check local href/src targets and static HTML fragments in site pages.

Usage: python tools/check_links.py [--root PATH] [--verbose]
Remote URLs, query-only links, and anchors created by JavaScript are not checked.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class References(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.items: list[tuple[int, str, str]] = []
        self.anchors: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.anchors.add(attributes["id"])
        if tag == "a" and attributes.get("name"):
            self.anchors.add(attributes["name"])
        for name, value in attrs:
            if name in {"href", "src"} and value:
                self.items.append((self.getpos()[0], name, value))

    handle_startendtag = handle_starttag


def pages(root: Path) -> list[Path]:
    lessons = sorted(root.glob("week*/day*.html"))
    expected = {
        root / f"week{(day - 1) // 7 + 1}" / f"day{day:02}.html"
        for day in range(1, 57)
    }
    actual = set(lessons)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing or extra:
        details = ["Lesson inventory differs from the expected 56 pages:"]
        details += [f"  missing: {p.relative_to(root).as_posix()}" for p in missing]
        details += [f"  extra: {p.relative_to(root).as_posix()}" for p in extra]
        raise ValueError("\n".join(details))
    if not (root / "index.html").is_file():
        raise ValueError("Missing index.html")
    other_pages = sorted(path for path in root.glob("*.html") if path.name != "index.html")
    advanced = sorted(root.glob("advanced/a[0-9][0-9].html"))
    return [root / "index.html", *other_pages, *lessons, *advanced]


def local_target(root: Path, source: Path, value: str) -> Path | None:
    parsed = urlsplit(value.strip())
    if parsed.scheme or parsed.netloc or (not parsed.path and parsed.query):
        return None
    path = unquote(parsed.path).replace("\\", "/")
    if not path:
        return source if parsed.fragment else None
    if path.startswith("/"):
        target = root / path.lstrip("/")
    else:
        target = source.parent / path
    target = target.resolve()
    if target.is_dir():
        target = target / "index.html"
    return target


def label(root: Path, target: Path) -> str:
    try:
        return target.relative_to(root).as_posix()
    except ValueError:
        return str(target)


def check(root: Path) -> tuple[
    int, int, dict[Path, list[str]], dict[tuple[Path, str], list[str]], dict[Path, list[str]]
]:
    checked_pages = pages(root)
    broken_files: dict[Path, list[str]] = defaultdict(list)
    broken_fragments: dict[tuple[Path, str], list[str]] = defaultdict(list)
    escaping: dict[Path, list[str]] = defaultdict(list)
    parsed_html: dict[Path, References] = {}
    local_count = 0

    def parse_html(path: Path) -> References:
        if path not in parsed_html:
            parser = References()
            parser.feed(path.read_text(encoding="utf-8"))
            parsed_html[path] = parser
        return parsed_html[path]

    for source in checked_pages:
        parser = parse_html(source)
        for line, attr, value in parser.items:
            target = local_target(root, source, value)
            if target is None:
                continue
            local_count += 1
            reference = f"{source.relative_to(root).as_posix()}:{line} {attr}={value}"
            if not target.is_relative_to(root):
                escaping[target].append(reference)
                continue
            if not target.is_file():
                broken_files[target].append(reference)
                continue
            fragment = unquote(urlsplit(value.strip()).fragment)
            if attr == "href" and fragment and target.suffix.lower() in {".html", ".htm"}:
                if fragment not in parse_html(target).anchors:
                    broken_fragments[(target, fragment)].append(reference)
    return len(checked_pages), local_count, broken_files, broken_fragments, escaping


def main() -> int:
    argp = argparse.ArgumentParser(description=__doc__)
    argp.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    argp.add_argument("--verbose", action="store_true", help="show every broken reference")
    args = argp.parse_args()
    root = args.root.resolve()
    try:
        page_count, local_count, broken_files, broken_fragments, escaping = check(root)
    except (OSError, ValueError) as exc:
        argp.exit(2, f"check_links: {exc}\n")

    broken_count = sum(map(len, broken_files.values())) + sum(map(len, broken_fragments.values())) + sum(map(len, escaping.values()))
    print(f"Pages: {page_count}; local references: {local_count}")
    print(f"Broken references: {broken_count}; missing targets: {len(broken_files)}; missing fragments: {len(broken_fragments)}; escaping paths: {len(escaping)}")

    def show(references: list[str]) -> None:
        shown = references if args.verbose else references[:3]
        for reference in shown:
            print(f"    {reference}")
        if len(shown) < len(references):
            print(f"    ... {len(references) - len(shown)} more (use --verbose)")

    for target, references in sorted(broken_files.items(), key=lambda item: label(root, item[0])):
        print(f"  {label(root, target)}: {len(references)} reference(s)")
        show(references)
    for (target, fragment), references in sorted(broken_fragments.items(), key=lambda item: (label(root, item[0][0]), item[0][1])):
        print(f"  {label(root, target)}#{fragment}: {len(references)} reference(s) [missing fragment]")
        show(references)
    for target, references in sorted(escaping.items(), key=lambda item: label(root, item[0])):
        print(f"  {label(root, target)}: {len(references)} reference(s) [escapes root]")
        show(references)
    return 1 if broken_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
