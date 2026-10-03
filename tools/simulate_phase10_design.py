"""Algebraic A29–A32 supply/ADC scenarios; no regulator or SPICE model."""

import json


def scenarios():
    result = []
    for temperature_c in (20, 25, 30, 31, 40):
        vout = 0.5 + 0.01 * temperature_c
        for reference_v in (3.3, 3.333):  # exact model and assumed +1% reference
            raw = round(vout / reference_v * 65535)
            estimated_c = (raw * 3.3 / 65535 - 0.5) / 0.01
            result.append({
                "stimulus_c": temperature_c,
                "sensor_v": round(vout, 4),
                "actual_reference_v_assumed": reference_v,
                "software_reference_v_assumed": 3.3,
                "adc_u16": raw,
                "estimated_c": round(estimated_c, 4),
                "error_c": round(estimated_c - temperature_c, 4),
                "sensor_power_upper_mw_at_3v3": 0.165,
            })
    return result


if __name__ == "__main__":
    print(json.dumps({"scope": "ideal linear TMP36, nearest-code 16-bit API scale, "
                               "fixed 3.3V rail; no SMPS/noise/thermal/PCB model",
                      "rows": scenarios()}, ensure_ascii=False, indent=2))
