"""Exercise the measurement analyser with temporary synthetic records only."""

import csv
import tempfile
from pathlib import Path

from analyze_phase10_measurements import FIELDS, analyze_file


def write_csv(path, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def synthetic_row(index, temperature_c, led):
    volts = 0.5 + 0.01 * temperature_c
    return {
        "run_id": "SYNTHETIC_TEST_ONLY",
        "sample_index": str(index),
        "timestamp_utc": f"2026-10-04T00:00:{index:02d}Z",
        "board_marking": "NO_BOARD_SYNTHETIC",
        "sensor_marking": "NO_SENSOR_SYNTHETIC",
        "firmware_sha256": "0" * 64,
        "reference_c": str(temperature_c),
        "reference_u_c": "0.5",
        "adc_vref_v": "3.3",
        "tmp36_vout_v": str(volts),
        "adc_raw_u16": str(round(volts / 3.3 * 65535)),
        "firmware_reference_v": "3.3",
        "led_observed": str(led),
    }


def expect_invalid(path, rows):
    write_csv(path, rows)
    try:
        analyze_file(path)
    except ValueError:
        return
    raise AssertionError("Invalid measurement record was accepted")


def main():
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "synthetic.csv"
        write_csv(path, [])
        assert analyze_file(path) == {"status": "no_data", "sample_count": 0, "hardware_accepted": False}

        rows = [synthetic_row(i, t, led) for i, (t, led) in enumerate(((25, 0), (31, 1), (29, 1), (27, 0)))]
        write_csv(path, rows)
        report = analyze_file(path)
        assert report["status"] == "analysis_only" and report["hardware_accepted"] is False
        assert [sample["led_expected"] for sample in report["samples"]] == [0, 1, 1, 0]
        assert all(abs(sample["vout_minus_reference_c"]) < 1e-9 for sample in report["samples"])

        wrong_led = [dict(row) for row in rows]
        wrong_led[2]["led_observed"] = "0"
        write_csv(path, wrong_led)
        mismatch = analyze_file(path)
        assert mismatch["status"] == "review_required"
        assert mismatch["samples"][2]["flags"] == ["led_mismatch"]

        wrong_index = [dict(row) for row in rows]
        wrong_index[2]["sample_index"] = "3"
        expect_invalid(path, wrong_index)
        wrong_time = [dict(row) for row in rows]
        wrong_time[2]["timestamp_utc"] = wrong_time[1]["timestamp_utc"]
        expect_invalid(path, wrong_time)
        wrong_hash = [dict(row) for row in rows]
        wrong_hash[0]["firmware_sha256"] = "unknown"
        expect_invalid(path, wrong_hash)
        wrong_ref = [dict(row) for row in rows]
        wrong_ref[0]["adc_vref_v"] = "nan"
        expect_invalid(path, wrong_ref)
        path.write_text("run_id,run_id\nexample,example\n", encoding="utf-8")
        try:
            analyze_file(path)
        except ValueError:
            pass
        else:
            raise AssertionError("Duplicate header was accepted")

    print("Phase 10 measurement analysis: empty, hysteresis, discrepancy and invalid-record cases PASS")


if __name__ == "__main__":
    main()
