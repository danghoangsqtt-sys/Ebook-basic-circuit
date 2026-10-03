"""Build and integrate the 12 reviewed end-of-lesson summary diagrams."""

from __future__ import annotations

import argparse
import json
import re
import textwrap
from html import escape, unescape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "docs/visuals/summary-specs.json"
ASSETS = ROOT / "assets/images/lessons"
DAYS = (7, 14, 21, 28, 35, 42, 43, 48, 49, 50, 55, 56)
COLORS = ("#63d8cc", "#f8c476", "#aebdff", "#edadd2", "#83d2ef")


def lines(value: str, width: int, limit: int) -> list[str]:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Missing diagram text")
    result = textwrap.wrap(value.strip(), width=width, break_long_words=False)
    if len(result) > limit:
        raise ValueError(f"Diagram text too long: {value!r}")
    return result


def text(x: int, y: int, value: str, size: int, color: str, weight: int = 400) -> str:
    return (f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" '
            f'font-size="{size}" font-weight="{weight}" fill="{color}">'
            f'{escape(value)}</text>')


def render(day: int, spec: dict) -> str:
    mode = spec["mode"]
    nodes = spec["nodes"]
    if mode not in {"block", "mindmap"} or len(nodes) not in {4, 5}:
        raise ValueError(f"Day {day}: invalid mode or node count")
    title_lines = lines(spec["title"], 29, 2)
    hub_lines = lines(spec["hub"], 29, 2)
    top_extra = (len(title_lines) - 1) * 42
    hub_extra = (len(hub_lines) - 1) * 36
    base = 257 + top_extra + hub_extra
    height = base + len(nodes) * 195 + 30
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="560" height="{height}" '
        f'viewBox="0 0 560 {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(spec["title"])} — Bài {day}</title>',
        f'<desc id="desc">{escape(spec["hub"])}; '
        f'{escape("; ".join(node["heading"] + ": " + node["detail"] for node in nodes))}</desc>',
        f'<rect width="560" height="{height}" rx="24" fill="#102036"/>',
        '<rect x="24" y="22" width="154" height="42" rx="21" fill="#254761"/>',
        text(43, 52, f"BÀI {day:02d} · TỔNG KẾT", 20, "#e8f4fa", 700),
        *[text(27, 112+j*42, line, 34, "#f7fbff", 700)
          for j, line in enumerate(title_lines)],
        f'<rect x="26" y="{139+top_extra}" width="508" height="{90+hub_extra}" '
        'rx="22" fill="#226174" stroke="#76e3dc" stroke-width="3"/>',
        *[text(49, 193+top_extra+j*36, line, 30, "#ffffff", 700)
          for j, line in enumerate(hub_lines)],
    ]
    if mode == "mindmap":
        parts.append(f'<path d="M 65 {229+top_extra+hub_extra} V {base-4 + (len(nodes)-1)*195+91}" '
                     'stroke="#76e3dc" stroke-width="4" fill="none"/>')
    for i, node in enumerate(nodes):
        heading = lines(node["heading"], 23, 1)[0]
        detail = lines(node["detail"], 27, 2)
        y = base + i * 195
        x = 91 if mode == "mindmap" else 26
        w = 443 if mode == "mindmap" else 508
        if mode == "mindmap":
            parts.extend([
                f'<path d="M 65 {y+83} H 91" stroke="#76e3dc" stroke-width="4"/>',
                f'<circle cx="65" cy="{y+83}" r="8" fill="{COLORS[i]}"/>',
            ])
        else:
            parts.extend([
                f'<path d="M 280 {y-28} V {y-3}" stroke="#76e3dc" stroke-width="4"/>',
                f'<path d="M 271 {y-13} l 9 10 9 -10" stroke="#76e3dc" '
                'stroke-width="4" fill="none"/>',
            ])
        parts.extend([
            f'<rect x="{x}" y="{y}" width="{w}" height="166" rx="20" '
            'fill="#1c304a" stroke="#426480" stroke-width="2"/>',
            f'<rect x="{x}" y="{y}" width="8" height="166" rx="4" fill="{COLORS[i]}"/>',
            text(x+27, y+59, heading, 32, "#f7fbff", 700),
        ])
        for j, line in enumerate(detail):
            parts.append(text(x+27, y+107+j*34, line, 29, "#deedf5"))
    parts.append('</svg>')
    return '\n'.join(parts) + '\n'


def figure(day: int, spec: dict) -> str:
    height = (257 + (len(lines(spec['title'], 29, 2))-1)*42
              + (len(lines(spec['hub'], 29, 2))-1)*36
              + len(spec['nodes']) * 195 + 30)
    alt = spec['title'] + '. ' + spec['hub'] + '. ' + '; '.join(
        node['heading'] + ': ' + node['detail'] for node in spec['nodes'])
    rows = ''.join(
        f'            <li><strong>{escape(node["heading"])}</strong>: '
        f'{escape(node["detail"])} (mục {escape(node["section"])}).</li>\n'
        for node in spec['nodes'])
    return (
        f'      <section class="lesson-summary" aria-labelledby="summary-day{day:02d}">\n'
        f'        <h2 id="summary-day{day:02d}">Sơ đồ tổng hợp Bài {day}</h2>\n'
        '        <div class="figure figure--summary">\n'
        f'          <img src="../assets/images/lessons/day{day:02d}-summary.svg" '
        f'width="560" height="{height}" loading="lazy" decoding="async" '
        f'alt="{escape(alt, quote=True)}">\n'
        '          <div class="figure-caption">\n'
        f'            <div class="figure-number">{escape(spec["title"])}</div>\n'
        f'            <div class="figure-text">{escape(spec["hub"])}. '
        'Các nhánh bên dưới dẫn tới nội dung đã học trong bài.</div>\n'
        '            <div class="figure-source">Nguồn: tự vẽ cho giáo trình; '
        'đối chiếu theo các mục của bài.</div>\n'
        '          </div>\n'
        '        </div>\n'
        '        <details class="summary-transcript"><summary>Đọc nội dung sơ đồ bằng chữ</summary>\n'
        f'          <ol>\n{rows}          </ol>\n'
        '        </details>\n'
        '      </section>\n\n'
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = json.loads(SPEC.read_text(encoding='utf-8'))
    if set(data) != {f'{day:02d}' for day in DAYS}:
        raise ValueError('Summary spec must cover the 12 planned lessons exactly')
    for day in DAYS:
        spec = data[f'{day:02d}']
        page = ROOT / f'week{(day-1)//7+1}/day{day:02d}.html'
        html = page.read_text(encoding='utf-8')
        headings = [unescape(re.sub(r'<[^>]+>', ' ', value)).strip()
                    for value in re.findall(r'<h[23]\b[^>]*>(.*?)</h[23]>', html, re.S | re.I)]
        for node in spec['nodes']:
            if not any(node['section'].casefold() in heading.casefold() for heading in headings):
                raise ValueError(f'Day {day}: missing section {node["section"]!r}')
        asset = ASSETS / f'day{day:02d}-summary.svg'
        svg = render(day, spec)
        if args.check:
            if not asset.is_file() or asset.read_text(encoding='utf-8') != svg:
                raise ValueError(f'Stale summary SVG: {asset}')
        else:
            asset.write_text(svg, encoding='utf-8')
        block = figure(day, spec)
        start = f'      <section class="lesson-summary" aria-labelledby="summary-day{day:02d}">'
        if start in html:
            pattern = re.compile(re.escape(start) + r'.*?      </section>\n\n', re.S)
            updated, count = pattern.subn(lambda _: block, html, count=1)
            if count != 1:
                raise ValueError(f'Day {day}: duplicate or malformed summary')
        else:
            marker = '      <div class="lesson-nav">'
            if html.count(marker) != 1:
                raise ValueError(f'Day {day}: missing or ambiguous lesson navigation')
            updated = html.replace(marker, block + marker, 1)
        if args.check:
            if updated != html:
                raise ValueError(f'Stale summary HTML: {page}')
        else:
            page.write_text(updated, encoding='utf-8')
    print(f'{"Checked" if args.check else "Built"} {len(DAYS)} summary diagrams and lesson blocks')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
