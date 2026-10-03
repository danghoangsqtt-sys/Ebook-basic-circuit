"""Render the curated, mobile-first lesson overview SVGs from local JSON.

The JSON is editorial data. This renderer never copies a lesson's ASCII circuit;
each claim is reviewed against the corrected lesson before it enters the spec.
"""

from __future__ import annotations

import argparse
import json
import textwrap
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "docs/visuals/overview-specs.json"
OUT_DIR = ROOT / "assets/images/lessons"
WIDTH = 560
CARD_TOP = 174
CARD_HEIGHT = 200
CARD_GAP = 16
HEIGHT = 1114
PALETTE = ("#54d6c9", "#f5bd6a", "#9cb7ff", "#e7a2cb")


def wrapped(value: str, width: int, max_lines: int) -> list[str]:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Every visible label must contain text")
    lines = textwrap.wrap(value.strip(), width=width, break_long_words=False)
    if len(lines) > max_lines:
        raise ValueError(f"Text is too long for a mobile SVG: {value!r}")
    return lines


def label(x: int, y: int, content: str, size: int, fill: str, weight: int = 400) -> str:
    return (
        f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" '
        f'font-weight="{weight}" font-family="Arial, sans-serif">'
        f"{escape(content)}</text>"
    )


def render(day: int, spec: dict) -> str:
    title = spec.get("title")
    items = spec.get("items")
    note = spec.get("note")
    if not isinstance(items, list) or len(items) != 4:
        raise ValueError(f"Day {day:02d}: exactly four curated blocks are required")
    title_lines = wrapped(title, 27, 2)
    note_lines = wrapped(note, 36, 2)
    kind = spec.get("kind", "flow")
    if kind not in {"flow", "compare", "map"}:
        raise ValueError(f"Day {day:02d}: unknown kind {kind!r}")

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="560" height="{HEIGHT}" '
        f'viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">',
        f"<title id=\"title\">{escape(title)} — Bài {day}</title>",
        f"<desc id=\"desc\">{escape(spec.get('alt', note))}</desc>",
        '<rect width="560" height="1114" rx="24" fill="#101b2d"/>',
        '<rect x="28" y="26" width="96" height="42" rx="21" fill="#25415b"/>',
        label(47, 55, f"BÀI {day:02d}", 24, "#f8fafc", 700),
        label({"flow": 400, "compare": 405, "map": 425}[kind], 55,
              {"flow": "QUY TRÌNH", "compare": "SO SÁNH", "map": "SƠ ĐỒ"}[kind],
              20, "#9ebbd0", 700),
    ]
    for i, line in enumerate(title_lines):
        parts.append(label(32, 113 + i * 40, line, 36, "#f8fafc", 700))
    if kind == "map":
        parts.append('<path d="M 18 151 V 922" stroke="#54d6c9" stroke-width="4" opacity="0.8"/>')
    if kind == "compare":
        parts.extend([
            '<path d="M 23 184 H 16 V 580 H 23 M 23 616 H 16 V 1012 H 23" '
            'stroke="#9cb7ff" stroke-width="4" fill="none"/>',
            '<circle cx="16" cy="382" r="6" fill="#54d6c9"/>',
            '<circle cx="16" cy="814" r="6" fill="#9cb7ff"/>',
        ])
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            raise ValueError(f"Day {day:02d}: block {index + 1} must be an object")
        heading = wrapped(item.get("heading"), 24, 1)[0]
        detail_lines = wrapped(item.get("detail"), 27, 3)
        y = CARD_TOP + index * (CARD_HEIGHT + CARD_GAP)
        accent = PALETTE[index] if kind != "compare" else PALETTE[0 if index < 2 else 2]
        if kind == "map":
            parts.extend([
                f'<path d="M 18 {y + 100} H 29" stroke="#54d6c9" stroke-width="4"/>',
                f'<circle cx="18" cy="{y + 100}" r="7" fill="#54d6c9"/>',
            ])
        parts.extend(
            [
                f'<rect x="29" y="{y}" width="502" height="{CARD_HEIGHT}" rx="20" '
                'fill="#182a43" stroke="#42617e" stroke-width="2"/>',
                f'<rect x="29" y="{y}" width="7" height="{CARD_HEIGHT}" rx="3" fill="{accent}"/>',
                f'<circle cx="77" cy="{y + 47}" r="24" fill="{accent}"/>',
                label(66, y + 56, str(index + 1), 29, "#101b2d", 700),
                label(116, y + 57, heading, 31, "#f8fafc", 700),
            ]
        )
        for line_index, line in enumerate(detail_lines):
            parts.append(label(56, y + 104 + line_index * 38, line, 29, "#dce9f3"))
        if index < 3 and kind == "flow":
            parts.append(
                f'<path d="M 280 {y + CARD_HEIGHT + 1} v 12" stroke="#78e6da" '
                'stroke-width="4" stroke-linecap="round"/>'
            )
            parts.append(
                f'<path d="M 272 {y + CARD_HEIGHT + 9} l 8 8 8 -8" '
                'fill="none" stroke="#78e6da" stroke-width="4"/>'
            )
    parts.extend(
        [
            '<rect x="29" y="1040" width="502" height="54" rx="16" fill="#25415b"/>',
        ]
    )
    if len(note_lines) == 1:
        parts.append(label(47, 1076, note_lines[0], 27, "#f8fafc", 700))
    else:
        parts[-1] = '<rect x="29" y="1025" width="502" height="74" rx="16" fill="#25415b"/>'
        for i, line in enumerate(note_lines):
            parts.append(label(47, 1057 + i * 33, line, 26, "#f8fafc", 700))
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", nargs="*", type=int, help="Only render these lesson numbers")
    parser.add_argument("--check", action="store_true", help="Compare generated SVG with files")
    args = parser.parse_args()
    data = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("overview-specs.json must be a day-keyed object")
    days = sorted(args.days or (int(key) for key in data))
    if len(days) != len(set(days)):
        raise ValueError("Duplicate day")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for day in days:
        if not 1 <= day <= 56:
            raise ValueError(f"Day {day} is out of range")
        svg = render(day, data[f"{day:02d}"])
        path = OUT_DIR / f"day{day:02d}-overview.svg"
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != svg:
                raise ValueError(f"SVG is missing or stale: {path}")
        else:
            path.write_text(svg, encoding="utf-8")
    print(f"{'Checked' if args.check else 'Rendered'} {len(days)} lesson SVGs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
