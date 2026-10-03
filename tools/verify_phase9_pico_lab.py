"""Host-side command-sequence oracle for the Pico GP25 lab, not hardware simulation."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "labs/pico_gpio_blink.py"
spec = importlib.util.spec_from_file_location("pico_gpio_blink", LAB)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class FakePin:
    OUT = "OUT"
    events: list[tuple[str, int | str]] = []

    def __init__(self, number: int, mode: str, *, value: int) -> None:
        assert (number, mode, value) == (25, self.OUT, 0)
        self.events.append(("init", number))

    def value(self, level: int) -> None:
        assert level in (0, 1)
        self.events.append(("level", level))


def run_case(high_ms: int, low_ms: int, cycles: int) -> list[tuple[str, int | str]]:
    FakePin.events = []
    sleeps: list[int] = []
    module.blink(FakePin, sleeps.append, cycles=cycles, high_ms=high_ms, low_ms=low_ms)
    assert FakePin.events == [("init", 25)] + [("level", bit) for _ in range(cycles) for bit in (1, 0)]
    assert sleeps == [duration for _ in range(cycles) for duration in (high_ms, low_ms)]
    assert FakePin.events[-1] == ("level", 0)
    return FakePin.events


def main() -> None:
    assert len(run_case(250, 250, 4)) == 9
    assert len(run_case(100, 400, 3)) == 7
    assert 1000 / (250 + 250) == 2
    assert 250 / (250 + 250) == 0.5
    assert 1000 / (100 + 400) == 2
    assert 100 / (100 + 400) == 0.2
    for args in ((0, 250, 1), (250, -1, 1), (250, 250, -1)):
        try:
            module.blink(FakePin, lambda _: None, cycles=args[2], high_ms=args[0], low_ms=args[1])
        except ValueError:
            pass
        else:
            raise AssertionError(f"Expected ValueError for {args}")
    print("P9-02 Pico GP25 host schedule: 250/250 and 100/400 ms, output order, off-after-finite-run and invalid inputs PASS")


if __name__ == "__main__":
    main()
