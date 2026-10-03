"""Deterministic ideal TMP36/Pico ADC stimulus; not SPICE or hardware data."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPERATURES_C = (25, 29, 30, 31, 29, 28, 27, 31)
REFERENCE_V = 3.3


def model(temperatures=TEMPERATURES_C):
    rows = []
    active = False
    for index, temperature in enumerate(temperatures):
        volts = 0.5 + 0.01 * temperature
        raw = round(volts / REFERENCE_V * 65535)
        nominal_c = (raw * REFERENCE_V / 65535 - 0.5) / 0.01
        if nominal_c >= 30:
            active = True
        elif nominal_c <= 28:
            active = False
        rows.append({"second": index, "stimulus_c": temperature,
                     "ideal_v": round(volts, 4), "adc_u16": raw,
                     "decoded_c": round(nominal_c, 4), "led": int(active)})
    return rows


if __name__ == "__main__":
    print(json.dumps({"assumptions": "ideal linear TMP36, 3.3 V ADC reference, "
                                     "nearest-code quantization, 1 s samples, no noise",
                      "rows": model()}, ensure_ascii=False, indent=2))
