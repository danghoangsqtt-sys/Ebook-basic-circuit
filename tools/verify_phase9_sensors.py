"""Independent arithmetic and scope checks for P9-03 paper sensor lessons."""

from __future__ import annotations

from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = {number: (ROOT / "advanced" / f"a{number}.html").read_text(encoding="utf-8") for number in range(25, 29)}


def has(page: int, *needles: str) -> None:
    for needle in needles:
        assert needle in PAGES[page], (page, needle)


def near(actual: Decimal, expected: str, tolerance: str = "0.0001") -> None:
    assert abs(actual - Decimal(expected)) <= Decimal(tolerance), (actual, expected)


def main() -> None:
    for part in ("TMP36", "DS18B20", "OPT3001", "DRV5032", "BMP280", "LSM6DSOX", "VL53L1X"):
        has(25, part)
    for page in range(25, 29):
        has(page, "figure-source", "summary-transcript", "answer-content", "Bài tập độc lập")
    has(25, "0,01 lux chỉ ở range thấp nhất", "I/O mặc định 1,8 V", "IC trần")
    has(26, "TMP36 analog", "DS18B20 1-Wire", "OPT3001", "DRV5032", "LDR", "reed switch")
    has(27, "0,0016 hPa", "typical</em> ±1 hPa", "I/O 1,8 V", "3,3 V")
    has(28, "dữ liệu tổng hợp", "điểm kiểm", "0,0045 V")

    # TMP36 nominal model, separate from its accuracy specification.
    nominal = (Decimal("0.760") - Decimal("0.500")) / Decimal("0.010")
    near(nominal, "26")
    # Fit only endpoint samples; the middle sample is held out.
    low_t, low_v = Decimal("0"), Decimal("0.510")
    high_t, high_v = Decimal("50"), Decimal("1.005")
    check_t, check_v = Decimal("25"), Decimal("0.762")
    slope = (high_v - low_v) / (high_t - low_t)
    intercept = low_v - slope * low_t
    corrected = (check_v - intercept) / slope
    raw = (check_v - Decimal("0.500")) / Decimal("0.010")
    near(slope, "0.0099", "0")
    near(intercept, "0.510", "0")
    near(corrected, "25.454545", "0.000001")
    near(corrected - check_t, "0.454545", "0.000001")
    near(raw - check_t, "1.2", "0")
    near(check_v - (intercept + slope * check_t), "0.0045", "0")
    near(Decimal("0.002") / Decimal("0.010"), "0.2", "0")
    near(sum((Decimal("24.9"), Decimal("25.4"), Decimal("25.1"))) / 3, "25.133333", "0.000001")
    print("P9-03 sensors: seven-part map, four page scopes and independent arithmetic PASS")


if __name__ == "__main__":
    main()
