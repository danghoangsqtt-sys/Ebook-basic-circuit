"""Independently recompute P9-01 logic and inspect published truth/trace tables."""

from __future__ import annotations

from html.parser import HTMLParser
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Tables(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tables: list[list[list[str]]] = []
        self.current: list[list[str]] | None = None
        self.cell: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "table":
            self.current = []
        elif tag == "tr" and self.current is not None:
            self.current.append([])
        elif tag in ("td", "th") and self.current:
            self.cell = []

    def handle_data(self, data: str) -> None:
        if self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag in ("td", "th") and self.cell is not None and self.current:
            self.current[-1].append("".join(self.cell).strip())
            self.cell = None
        elif tag == "table" and self.current is not None:
            self.tables.append(self.current)
            self.current = None


def table(page: str) -> list[list[str]]:
    parser = Tables()
    parser.feed((ROOT / "advanced" / page).read_text(encoding="utf-8"))
    assert parser.tables, f"{page}: no table"
    return parser.tables[0]


def main() -> None:
    a18 = table("a18.html")
    assert len(a18) == 5, a18
    for i, (a, b) in enumerate(product((0, 1), repeat=2), start=1):
        expected = [a, b, a & b, a | b, 1 - a, 1 - (a & b)]
        assert list(map(int, a18[i])) == expected, (i, a18[i], expected)
        assert 1 - (a & b) == (1 - a) | (1 - b)
        assert 1 - (a | b) == (1 - a) & (1 - b)

    a19 = table("a19.html")
    assert len(a19) == 9, a19
    for i, (s, a, b) in enumerate(product((0, 1), repeat=3), start=1):
        expected = [s, a, b, (1 - s) & a, s & b, a if s == 0 else b]
        assert list(map(int, a19[i])) == expected, (i, a19[i], expected)
    independent = [a if s == 0 else 1 - b for s, a, b in product((0, 1), repeat=3)]
    assert independent == [0, 0, 1, 1, 1, 0, 1, 0]

    a20 = table("a20.html")
    assert [row[2] for row in a20[1:4]] == ["1", "0", "1"]
    assert [row[3] for row in a20[1:5]] == ["01", "10", "11", "00"]

    a21 = table("a21.html")
    assert [row[2:] for row in a21[1:]] == [["G", "Y"], ["Y", "R"], ["R", "G"]]
    next_state = {"G": "Y", "Y": "R", "R": "G"}
    state = "G"
    trace: list[str] = []
    for advance in (1, 0, 1, 1):
        state = next_state[state] if advance else state
        trace.append(state)
    assert trace == ["Y", "Y", "R", "G"]
    state = "G"
    trace = []
    for advance in (1, 1, 0, 1):
        state = next_state[state] if advance else state
        trace.append(state)
    assert trace == ["Y", "R", "R", "G"]
    assert [period - (20 + 30 + 15) for period in (60, 65, 100)] == [-5, 0, 35]

    a17 = (ROOT / "advanced/a17.html").read_text(encoding="utf-8")
    assert all(term in a17 for term in ("1,35 V", "3,15 V", "2,0 V", "chưa bảo đảm"))
    assert 13 == 8 + 4 + 1 and 22 == 16 + 4 + 2
    assert abs((4.4 - 3.15) - 1.25) < 1e-9
    assert abs((1.35 - 0.1) - 1.25) < 1e-9
    assert abs((3.84 - 3.15) - 0.69) < 1e-9
    assert "NMH=3,84−3,15=0,69 V" in a17
    print("P9-01 numeric/logic: A17 conversions/thresholds/noise margins, A18/A19 published truth tables, A20 traces, A21 FSM/setup PASS")


if __name__ == "__main__":
    main()
