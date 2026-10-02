"""Check local href/src targets in the home page and all 56 lessons.

Usage: python tools/check_links.py [--root PATH] [--verbose]
Only file existence is checked; fragment identifiers and remote URLs are not.
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

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
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
    return [root / "index.html", *lessons]


def local_target(root: Path, source: Path, value: str) -> Path | None:
    parsed = urlsplit(value.strip())
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    path = unquote(parsed.path).replace("\\", "/")
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


def check(root: Path) -> tuple[int, int, dict[Path, list[str]]]:
    checked_pages = pages(root)
    broken: dict[Path, list[str]] = defaultdict(list)
    local_count = 0
    for source in checked_pages:
        parser = References()
        parser.feed(source.read_text(encoding="utf-8"))
        for line, attr, value in parser.items:
            target = local_target(root, source, value)
            if target is None:
                continue
            local_count += 1
            if not target.is_file():
                broken[target].append(
                    f"{source.relative_to(root).as_posix()}:{line} {attr}={value}"
                )
    return len(checked_pages), local_count, broken


def main() -> int:
    argp = argparse.ArgumentParser(description=__doc__)
    argp.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    argp.add_argument("--verbose", action="store_true", help="show every broken reference")
    args = argp.parse_args()
    root = args.root.resolve()
    try:
        page_count, local_count, broken = check(root)
    except (OSError, ValueError) as exc:
        argp.exit(2, f"check_links: {exc}\n")

    broken_count = sum(map(len, broken.values()))
    print(f"Pages: {page_count}; local references: {local_count}")
    print(f"Broken references: {broken_count}; missing targets: {len(broken)}")
    for target, references in sorted(broken.items(), key=lambda item: label(root, item[0])):
        print(f"  {label(root, target)}: {len(references)} reference(s)")
        shown = references if args.verbose else references[:3]
        for reference in shown:
            print(f"    {reference}")
        if len(shown) < len(references):
            print(f"    ... {len(references) - len(shown)} more (use --verbose)")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
