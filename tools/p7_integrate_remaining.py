"""Integrate the remaining P7-04 diagrams from the hand-authored SVG builders.

Run without flags to validate the ID-to-ASCII mapping; --apply edits lesson HTML
and appends provenance rows for new SVGs. This is a one-time editorial tool.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from html import escape
from pathlib import Path
import re

from p7_render import BUILDERS


ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "docs/curriculum/diagram-register.csv"
SOURCES = ROOT / "assets/images/lessons/SOURCES.md"
ASCII = re.compile(r'<div class="circuit-ascii">.*?</div>', re.DOTALL)
HARDWARE_REVIEW = {"d21-1", "d21-2", "d42-1"}


def figure(name: str) -> str:
    drawing = BUILDERS[name]()
    diagram_id = name.upper()
    title = escape(drawing.title)
    desc = escape(drawing.desc)
    caution = (
        " Đây là sơ đồ để phân tích/mô phỏng; chỉ lắp trên phần cứng sau khi "
        "xác minh đúng part/module, nguồn, dòng và duyệt mạch cụ thể."
        if name in HARDWARE_REVIEW else ""
    )
    return (
        '      <figure class="figure figure--overview">\n'
        f'        <img src="../assets/images/lessons/{name}.svg" width="{drawing.w}" '
        f'height="{drawing.h}" loading="lazy" decoding="async" alt="{desc}">\n'
        '        <figcaption class="figure-caption">'
        f'<div class="figure-number">Sơ đồ {diagram_id} — {title}</div>'
        f'<div class="figure-text">{desc}{caution}</div>'
        '<div class="figure-source">Sơ đồ tự vẽ từ ví dụ trong bài; cần kiểm '
        f'các thông số cụ thể trước khi lắp. <a href="../assets/images/lessons/{name}.svg" '
        'target="_blank" rel="noopener">Mở hình lớn</a>.</div></figcaption>\n'
        '      </figure>\n'
        f'      <details class="summary-transcript"><summary>Đọc mô tả {diagram_id}</summary>'
        f'<p>{desc}{caution}</p></details>'
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    rows = list(csv.DictReader(REGISTER.open(encoding="utf-8", newline="")))
    per_page: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        name = row["id"].lower()
        if name in BUILDERS or name == "d10-1":
            per_page[row["path"]].append(name)
    found = sum(len(ASCII.findall((ROOT / path).read_text(encoding="utf-8"))) for path in per_page)
    expected = sum(map(len, per_page.values()))
    if found == 0 and all(row["planned_action"] != "redraw_pending" for row in rows):
        print("Already integrated: no ASCII blocks remain in mapped lessons")
        return 0
    if found != expected or found != 27:
        raise SystemExit(f"Mapping changed: {found} ASCII blocks for {expected} IDs; expected 27")
    print(f"Mapped {found} remaining ASCII blocks: 26 SVG replacements and D10-1 reference")
    if not args.apply:
        return 0

    for path, ids in per_page.items():
        lesson = ROOT / path
        source = lesson.read_text(encoding="utf-8")
        matches = list(ASCII.finditer(source))
        if len(matches) != len(ids):
            raise SystemExit(f"Unexpected block count in {path}: {len(matches)} != {len(ids)}")
        changes = []
        for match, name in zip(matches, ids):
            replacement = match.group(0) if name == "d10-1" else figure(name)
            changes.append((match.start(), match.end(), replacement))
        for start, end, replacement in reversed(changes):
            source = source[:start] + replacement + source[end:]
        lesson.write_text(source, encoding="utf-8", newline="\n")

    source_text = SOURCES.read_text(encoding="utf-8")
    additions = []
    for asset in sorted((ROOT / "assets/images/lessons").glob("d[0-9][0-9]-*.svg")):
        if f"`{asset.name}`" in source_text:
            continue
        day = int(asset.name[1:3])
        additions.append(
            f"| `{asset.name}` | Bài {day} | Tự vẽ từ bài học và sổ P7-04; "
            "đối chiếu kỹ thuật ở `docs/curriculum/diagram-register.csv` | "
            "Nội dung dự án | SVG nguồn chỉnh sửa được; chưa tự chứng nhận phép đo phần cứng. |"
        )
    if additions:
        SOURCES.write_text(source_text.rstrip() + "\n\n## Sơ đồ P7-04\n\n"
                           + "\n".join(additions) + "\n", encoding="utf-8", newline="\n")
    print(f"Integrated 26 diagrams; added {len(additions)} source records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
