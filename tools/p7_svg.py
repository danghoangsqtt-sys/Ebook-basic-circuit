"""Helpers for the hand-authored P7-04 schematic/waveform/block SVG set.

Every figure is a small Python function that returns an ``S`` object. Run
``python tools/p7_render.py`` to (re)write the SVG files in
``assets/images/lessons``. The SVG files are the editable source of record;
this module only keeps their geometry reproducible.
"""

from __future__ import annotations

from xml.sax.saxutils import escape

CSS = (
    "text{font-family:Arial,Helvetica,sans-serif;fill:#0f172a;font-size:13px}"
    ".w{stroke:#334155;stroke-width:2.5;fill:none;stroke-linecap:round;stroke-linejoin:round}"
    ".k{stroke:#334155;stroke-width:3.5;fill:none;stroke-linecap:round}"
    ".c{fill:#fff;stroke:#475569;stroke-width:2}"
    ".p{fill:#dbeafe;stroke:#1e40af;stroke-width:2}"
    ".y{fill:#fef3c7;stroke:#b45309;stroke-width:2}"
    ".z{fill:#dcfce7;stroke:#15803d;stroke-width:2}"
    ".d{stroke:#64748b;stroke-width:1.5;fill:none;stroke-dasharray:5 4}"
    ".gr{stroke:#cbd5e1;stroke-width:1;fill:none}"
    ".n{fill:#0f766e}.b{font-weight:700}.m{fill:#475569;font-size:12px}"
    ".g{fill:#0f766e}.o{fill:#b45309}.h{font-size:15px;font-weight:700}.s{font-size:11px}"
    ".wh{fill:#fff}.a{stroke:#0f766e;stroke-width:2.2;fill:none}"
    ".ao{stroke:#b45309;stroke-width:2.2;fill:none}"
)

DEFS = (
    '<defs>'
    '<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
    'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#0f766e"/></marker>'
    '<marker id="ao" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
    'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#b45309"/></marker>'
    '<marker id="ad" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
    'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#334155"/></marker>'
    '</defs>'
)


def f(value: float) -> str:
    text = f"{value:.1f}"
    return text[:-2] if text.endswith(".0") else text


class S:
    def __init__(self, w: int, h: int, title: str, desc: str) -> None:
        self.w, self.h, self.title, self.desc = w, h, title, desc
        self.wires: list[str] = []
        self.parts: list[str] = []

    # --- primitives -------------------------------------------------
    def wire(self, d: str) -> None:
        self.wires.append(d)

    def raw(self, xml: str) -> None:
        self.parts.append(xml)

    def t(self, x: float, y: float, text: str, cls: str = "", anchor: str = "start") -> None:
        extra = f' class="{cls}"' if cls else ""
        a = f' text-anchor="{anchor}"' if anchor != "start" else ""
        self.parts.append(f'<text x="{f(x)}" y="{f(y)}"{extra}{a}>{escape(text)}</text>')

    def lines(self, x: float, y: float, items: list[str], dy: float = 17, cls: str = "",
              anchor: str = "start") -> None:
        for i, item in enumerate(items):
            self.t(x, y + i * dy, item, cls, anchor)

    def dot(self, x: float, y: float) -> None:
        self.parts.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="4.5" class="n"/>')

    def term(self, x: float, y: float) -> None:
        self.parts.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="4.5" class="c"/>')

    def arrow(self, x1: float, y1: float, x2: float, y2: float, cls: str = "a", both: bool = False) -> None:
        marker = "ao" if cls == "ao" else "ah"
        start = f' marker-start="url(#{marker})"' if both else ""
        self.parts.append(
            f'<path class="{cls}" d="M{f(x1)} {f(y1)} L{f(x2)} {f(y2)}" '
            f'marker-end="url(#{marker})"{start}/>'
        )

    def box(self, x: float, y: float, w: float, h: float, cls: str = "p", rx: int = 8) -> None:
        self.parts.append(f'<rect class="{cls}" x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{rx}"/>')

    def boxed(self, x: float, y: float, w: float, h: float, items: list[str], cls: str = "p",
              first_bold: bool = True, dy: float = 17, size_cls: str = "") -> None:
        self.box(x, y, w, h, cls)
        total = (len(items) - 1) * dy
        y0 = y + h / 2 - total / 2 + 4
        for i, item in enumerate(items):
            c = ("b " if (i == 0 and first_bold) else "") + size_cls
            self.t(x + w / 2, y0 + i * dy, item, c.strip(), "middle")

    # --- components -------------------------------------------------
    def rv(self, cx: float, y1: float, y2: float) -> None:
        self.parts.append(f'<rect class="c" x="{f(cx - 13)}" y="{f(y1)}" width="26" height="{f(y2 - y1)}" rx="4"/>')

    def rh(self, x1: float, x2: float, cy: float) -> None:
        self.parts.append(f'<rect class="c" x="{f(x1)}" y="{f(cy - 13)}" width="{f(x2 - x1)}" height="26" rx="4"/>')

    def gnd(self, x: float, y: float) -> None:
        self.parts.append(
            f'<path class="w" d="M{f(x)} {f(y)} V{f(y + 10)} M{f(x - 15)} {f(y + 10)} H{f(x + 15)} '
            f'M{f(x - 10)} {f(y + 16)} H{f(x + 10)} M{f(x - 5)} {f(y + 22)} H{f(x + 5)}"/>'
        )

    def cap_v(self, cx: float, y1: float, y2: float, plus: bool = False) -> None:
        cy = (y1 + y2) / 2
        self.wires.append(f"M{f(cx)} {f(y1)} V{f(cy - 5)} M{f(cx)} {f(y2)} V{f(cy + 5)}")
        self.parts.append(
            f'<path class="k" d="M{f(cx - 17)} {f(cy - 5)} H{f(cx + 17)} M{f(cx - 17)} {f(cy + 5)} H{f(cx + 17)}"/>'
        )
        if plus:
            self.t(cx + 22, cy - 8, "+", "b")

    def cap_h(self, x1: float, x2: float, cy: float) -> None:
        cx = (x1 + x2) / 2
        self.wires.append(f"M{f(x1)} {f(cy)} H{f(cx - 5)} M{f(x2)} {f(cy)} H{f(cx + 5)}")
        self.parts.append(
            f'<path class="k" d="M{f(cx - 5)} {f(cy - 17)} V{f(cy + 17)} M{f(cx + 5)} {f(cy - 17)} V{f(cy + 17)}"/>'
        )

    def bat_v(self, cx: float, y1: float, y2: float) -> None:
        cy = (y1 + y2) / 2
        self.wires.append(f"M{f(cx)} {f(y1)} V{f(cy - 6)} M{f(cx)} {f(y2)} V{f(cy + 6)}")
        self.parts.append(
            f'<path class="w" d="M{f(cx - 17)} {f(cy - 6)} H{f(cx + 17)}"/>'
            f'<path class="k" style="stroke-width:6" d="M{f(cx - 9)} {f(cy + 6)} H{f(cx + 9)}"/>'
        )
        self.t(cx + 22, cy - 3, "+", "b")
        self.t(cx + 22, cy + 17, "−", "b")

    def diode_v(self, cx: float, y1: float, y2: float, up: bool = False) -> None:
        cy = (y1 + y2) / 2
        if not up:  # anode top, cathode bottom
            tri = f"M{f(cx - 12)} {f(cy - 12)} H{f(cx + 12)} L{f(cx)} {f(cy + 8)} Z"
            bar = f"M{f(cx - 12)} {f(cy + 8)} H{f(cx + 12)}"
            self.wires.append(f"M{f(cx)} {f(y1)} V{f(cy - 12)} M{f(cx)} {f(y2)} V{f(cy + 8)}")
        else:  # anode bottom, cathode top
            tri = f"M{f(cx - 12)} {f(cy + 12)} H{f(cx + 12)} L{f(cx)} {f(cy - 8)} Z"
            bar = f"M{f(cx - 12)} {f(cy - 8)} H{f(cx + 12)}"
            self.wires.append(f"M{f(cx)} {f(y1)} V{f(cy - 8)} M{f(cx)} {f(y2)} V{f(cy + 12)}")
        self.parts.append(f'<path d="{tri}" fill="#fff" stroke="#334155" stroke-width="2.5" stroke-linejoin="round"/>')
        self.parts.append(f'<path class="w" d="{bar}"/>')

    def diode_h(self, x1: float, x2: float, cy: float, led: bool = False) -> None:
        cx = (x1 + x2) / 2
        self.wires.append(f"M{f(x1)} {f(cy)} H{f(cx - 10)} M{f(x2)} {f(cy)} H{f(cx + 10)}")
        self.parts.append(
            f'<path d="M{f(cx - 10)} {f(cy - 12)} V{f(cy + 12)} L{f(cx + 10)} {f(cy)} Z" fill="#fff" '
            f'stroke="#334155" stroke-width="2.5" stroke-linejoin="round"/>'
            f'<path class="w" d="M{f(cx + 10)} {f(cy - 12)} V{f(cy + 12)}"/>'
        )
        if led:
            self.parts.append(
                f'<path class="ao" marker-end="url(#ao)" d="M{f(cx - 2)} {f(cy - 18)} L{f(cx + 12)} {f(cy - 32)}"/>'
                f'<path class="ao" marker-end="url(#ao)" d="M{f(cx + 8)} {f(cy - 14)} L{f(cx + 22)} {f(cy - 28)}"/>'
            )

    # --- output ------------------------------------------------------
    def render(self) -> str:
        w, h = self.w, self.h
        out = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-labelledby="title desc"><title id="title">{escape(self.title)}</title>'
            f'<desc id="desc">{escape(self.desc)}</desc>{DEFS}<rect width="{w}" height="{h}" rx="18" fill="#f8fafc"/>'
            f"<style>{CSS}</style>"
        ]
        if self.wires:
            out.append(f'<path class="w" d="{" ".join(self.wires)}"/>')
        out.extend(self.parts)
        out.append("</svg>\n")
        return "\n".join(out)
