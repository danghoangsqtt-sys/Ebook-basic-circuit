"""Render the P7-04 SVG set: python tools/p7_render.py [--sheet OUT.png] [ids...]"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from p7_figs1 import BUILDERS_1  # noqa: E402
from p7_figs2 import BUILDERS_2  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/images/lessons"
BUILDERS = {**BUILDERS_1, **BUILDERS_2}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="*")
    parser.add_argument("--sheet", type=Path)
    args = parser.parse_args()
    ids = args.ids or sorted(BUILDERS)
    sizes = {}
    for name in ids:
        fig = BUILDERS[name]()
        (OUT / f"{name}.svg").write_text(fig.render(), encoding="utf-8", newline="\n")
        sizes[name] = (fig.w, fig.h)
    print("wrote", len(ids), "SVG files")
    if args.sheet:
        from playwright.sync_api import sync_playwright

        cells = "".join(
            f'<figure style="margin:0;border:1px solid #ccc"><figcaption style="font:12px sans-serif">{n} {sizes[n]}</figcaption>'
            f'<img src="{(OUT / (n + ".svg")).as_uri()}" style="max-width:100%"></figure>'
            for n in ids
        )
        html = f'<body style="margin:8px;background:#e5e7eb;display:grid;grid-template-columns:repeat(2,1fr);gap:8px">{cells}</body>'
        page_file = args.sheet.with_suffix(".html")
        page_file.write_text(html, encoding="utf-8")
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 900, "height": 900})
            page.goto(page_file.as_uri())
            page.wait_for_timeout(500)
            page.screenshot(path=str(args.sheet), full_page=True)
            browser.close()
        print("sheet", args.sheet)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
