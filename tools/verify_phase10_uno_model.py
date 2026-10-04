"""Independent arithmetic gate for lesson A33 (Arduino Uno R3 worked example).

Pure host model: ideal 10-bit ADC and nominal references. It is not a
measurement of any Uno board, regulator or sensor.
"""

import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def adc10(vin, vref):
    """Ideal 10-bit conversion: floor(vin / vref * 1024), clipped to 1023."""
    return min(1023, math.floor(vin / vref * 1024))


def decode_c(code, vref_assumed):
    """TMP36 nominal transfer V = 0.500 + 0.010 * T (deg C)."""
    return (code * vref_assumed / 1024 - 0.5) / 0.010


def main():
    # 1) LSB sizes and temperature steps for the two references used in the lesson.
    assert abs(5 / 1024 * 1000 - 4.8828125) < 1e-9
    assert abs(5 / 1024 / 0.010 - 0.48828125) < 1e-9
    assert abs(1.1 / 1024 * 1000 - 1.07421875) < 1e-9
    assert abs(1.1 / 1024 / 0.010 - 0.107421875) < 1e-9

    # 2) TMP36 at 25 deg C (0.750 V) read with a 5 V reference.
    code5 = adc10(0.75, 5.0)
    assert code5 == 153
    assert abs(decode_c(code5, 5.0) - 24.70703125) < 1e-6

    # 3) Same input with the nominal 1.1 V internal reference.
    code11 = adc10(0.75, 1.1)
    assert code11 == 698
    assert abs(decode_c(code11, 1.1) - 24.98046875) < 1e-6
    assert adc10(0.90, 1.1) < 1023  # 40 deg C still in range
    assert adc10(1.10, 1.1) == 1023  # 60 deg C reaches full scale (saturates)

    # 4) Assumed reference error of +/-0.1 V while software still assumes 1.1 V.
    low = decode_c(adc10(0.75, 1.2), 1.1)   # actual 1.2 V
    high = decode_c(adc10(0.75, 1.0), 1.1)  # actual 1.0 V
    assert abs(low - 18.75) < 1e-6 and abs(high - 32.5) < 1e-6

    # 5) LED series resistor and a six-LED budget (assumed VF = 2 V).
    i_led = (5.0 - 2.0) / 330 * 1000
    assert abs(i_led - 9.0909090909) < 1e-6 and i_led < 20.0
    assert abs(6 * i_led - 54.5454545) < 1e-4

    # 6) Linear-regulator dissipation from the VIN adapter example.
    assert abs((9 - 5) * 0.100 - 0.40) < 1e-12
    assert abs((12 - 5) * 0.150 - 1.05) < 1e-12

    html = (ROOT / "advanced/a33.html").read_text(encoding="utf-8")
    for needle in ("4,88 mV", "0,488", "698", "1,05 W", "9,09 mA", "chưa biên dịch", "Bài tập độc lập"):
        assert needle in html, needle
    print("A33 Uno model: arithmetic and lesson anchors PASS")


if __name__ == "__main__":
    main()
