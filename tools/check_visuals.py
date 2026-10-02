"""Check locally stored lesson illustrations and their source records.

Usage: python tools/check_visuals.py [--require-all] [--json] [--root PATH]
The default permits lessons that are still awaiting illustrations in Phase 4/5.
"""

from __future__ import annotations

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree


LESSON_COUNT = 56
MAX_RASTER_BYTES = 800_000


class Images(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.items: list[tuple[int, str, dict[str, str]]] = []
        self.ascii_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "img" or (tag == "source" and values.get("srcset")):
            self.items.append((self.getpos()[0], tag, values))
        if "circuit-ascii" in values.get("class", "").split():
            self.ascii_count += 1

    handle_startendtag = handle_starttag


def is_valid_asset(path: Path) -> bool:
    if path.suffix.lower() == ".svg":
        try:
            root = ElementTree.parse(path).getroot()
        except ElementTree.ParseError:
            return False
        return root.tag.endswith("svg")
    with path.open("rb") as handle:
        header = handle.read(16)
    suffix = path.suffix.lower()
    if suffix == ".webp":
        return header.startswith(b"RIFF") and header[8:12] == b"WEBP"
    if suffix == ".png":
        return header.startswith(b"\x89PNG\r\n\x1a\n")
    if suffix in {".jpg", ".jpeg"}:
        return header.startswith(b"\xff\xd8\xff")
    return False


def target(root: Path, page: Path, raw: str) -> Path | None:
    url = urlsplit(raw)
    if url.scheme or url.netloc or not url.path:
        return None
    result = (page.parent / unquote(url.path)).resolve()
    try:
        result.relative_to(root)
    except ValueError:
        return None
    return result


def check(root: Path, require_all: bool) -> dict[str, object]:
    root = root.resolve()
    source_file = root / "assets/images/lessons/SOURCES.md"
    source_text = source_file.read_text(encoding="utf-8") if source_file.exists() else ""
    errors: list[str] = []
    page_counts: dict[str, int] = {}
    assets: set[Path] = set()
    ascii_count = 0

    for day in range(1, LESSON_COUNT + 1):
        rel = Path(f"week{(day - 1) // 7 + 1}/day{day:02}.html")
        page = root / rel
        if not page.is_file():
            errors.append(f"{rel}: missing lesson")
            continue
        parser = Images()
        parser.feed(page.read_text(encoding="utf-8"))
        ascii_count += parser.ascii_count
        page_counts[rel.as_posix()] = sum(tag == "img" for _, tag, _ in parser.items)
        if require_all and page_counts[rel.as_posix()] == 0:
            errors.append(f"{rel}: no lesson illustration")
        for line, tag, attrs in parser.items:
            raw = attrs.get("src") if tag == "img" else attrs.get("srcset", "").split(",")[0].strip().split(" ")[0]
            path = target(root, page, raw or "")
            where = f"{rel}:{line}"
            if path is None:
                errors.append(f"{where}: illustration must be a local file: {raw}")
                continue
            if not path.is_file():
                errors.append(f"{where}: missing asset: {raw}")
                continue
            if "assets/images/lessons/" not in path.relative_to(root).as_posix():
                errors.append(f"{where}: illustration outside lesson assets: {raw}")
                continue
            assets.add(path)
            if path.name not in source_text:
                errors.append(f"{where}: {path.name} has no source entry")
            if not is_valid_asset(path):
                errors.append(f"{where}: invalid or unsupported image: {path.name}")
            if path.suffix.lower() != ".svg" and path.stat().st_size > MAX_RASTER_BYTES:
                errors.append(f"{where}: raster exceeds {MAX_RASTER_BYTES} bytes: {path.name}")
            if tag == "img":
                if not attrs.get("alt", "").strip():
                    errors.append(f"{where}: missing descriptive alt text")
                for dimension in ("width", "height"):
                    if not attrs.get(dimension, "").isdigit() or int(attrs[dimension]) < 1:
                        errors.append(f"{where}: missing positive {dimension}")

    if not source_file.is_file():
        errors.append("assets/images/lessons/SOURCES.md: missing source registry")
    return {
        "lesson_count": len(page_counts),
        "lessons_with_illustrations": sum(count > 0 for count in page_counts.values()),
        "image_elements": sum(page_counts.values()),
        "distinct_assets": len(assets),
        "ascii_diagrams": ascii_count,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--require-all", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = check(args.root, args.require_all)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(
            f"Lessons: {result['lesson_count']}/{LESSON_COUNT}; "
            f"illustrated: {result['lessons_with_illustrations']}; "
            f"images: {result['image_elements']}; assets: {result['distinct_assets']}; "
            f"ASCII diagrams: {result['ascii_diagrams']}; errors: {len(result['errors'])}"
        )
        for error in result["errors"]:
            print(f"  {error}")
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
