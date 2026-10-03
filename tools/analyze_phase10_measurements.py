"""Analyse recorded Pico/TMP36 measurements without certifying the hardware.

The CSV must come from an actual, identified board and reference setup. This
tool checks the record and calculates discrepancies; it never emits a hardware
PASS or substitutes for a schematic/ERC, instrument calibration, or reviewer.
"""

import argparse
import csv
import json
import math
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from labs.pico_tmp36_monitor import next_alarm, nominal_celsius  # noqa: E402

FIELDS = (
    "run_id", "sample_index", "timestamp_utc", "board_marking", "sensor_marking",
    "firmware_sha256", "reference_c", "reference_u_c", "adc_vref_v",
    "tmp36_vout_v", "adc_raw_u16", "firmware_reference_v", "led_observed",
)
SHA256 = re.compile(r"[0-9a-fA-F]{64}\Z")


def number(row, field, line):
    try:
        value = float(row[field])
    except (ValueError, TypeError) as exc:
        raise ValueError(f"CSV line {line}: {field} must be numeric") from exc
    if not math.isfinite(value):
        raise ValueError(f"CSV line {line}: {field} must be finite")
    return value


def integer(row, field, line, low, high):
    try:
        value = int(row[field])
    except (ValueError, TypeError) as exc:
        raise ValueError(f"CSV line {line}: {field} must be an integer") from exc
    if not low <= value <= high:
        raise ValueError(f"CSV line {line}: {field} outside {low}..{high}")
    return value


def analyze_file(path):
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if len(reader.fieldnames or ()) != len(set(reader.fieldnames or ())):
            raise ValueError("CSV has duplicate column names")
        missing = set(FIELDS) - set(reader.fieldnames or ())
        if missing:
            raise ValueError(f"CSV missing columns: {', '.join(sorted(missing))}")
        records = list(reader)

    if not records:
        return {"status": "no_data", "sample_count": 0, "hardware_accepted": False}

    runs = {}
    results = []
    for line, row in enumerate(records, 2):
        if None in row:
            raise ValueError(f"CSV line {line}: extra unnamed columns")
        for field in FIELDS:
            if row.get(field) is None or not row[field].strip():
                raise ValueError(f"CSV line {line}: {field} is blank")
        run_id = row["run_id"].strip()
        board = row["board_marking"].strip()
        sensor = row["sensor_marking"].strip()
        firmware_sha = row["firmware_sha256"].strip().lower()
        if not SHA256.fullmatch(firmware_sha):
            raise ValueError(f"CSV line {line}: firmware_sha256 is not 64 hex digits")
        index = integer(row, "sample_index", line, 0, 10**9)
        try:
            timestamp = datetime.fromisoformat(row["timestamp_utc"].replace("Z", "+00:00"))
        except ValueError as exc:
            raise ValueError(f"CSV line {line}: timestamp_utc must be ISO 8601 UTC") from exc
        if timestamp.utcoffset() != timedelta(0):
            raise ValueError(f"CSV line {line}: timestamp_utc must include UTC offset")
        raw = integer(row, "adc_raw_u16", line, 0, 65535)
        led_observed = integer(row, "led_observed", line, 0, 1)
        reference_c = number(row, "reference_c", line)
        reference_u_c = number(row, "reference_u_c", line)
        vref = number(row, "adc_vref_v", line)
        vout = number(row, "tmp36_vout_v", line)
        firmware_vref = number(row, "firmware_reference_v", line)
        if reference_u_c < 0:
            raise ValueError(f"CSV line {line}: reference_u_c must be non-negative")
        if not 0 < vref <= 5.5 or not 0 <= vout <= 5.5:
            raise ValueError(f"CSV line {line}: voltage outside recording range 0..5.5 V")
        if not 2.7 <= firmware_vref <= 3.3:
            raise ValueError(f"CSV line {line}: firmware_reference_v outside lab code range 2.7..3.3 V")

        identity = (board, sensor, firmware_sha, firmware_vref)
        previous = runs.get(run_id)
        if previous is None:
            if index != 0:
                raise ValueError(f"CSV line {line}: first sample in run {run_id} must be index 0")
            previous = {"index": -1, "timestamp": None, "alarm": False, "identity": identity}
        elif identity != previous["identity"] or index != previous["index"] + 1 or timestamp <= previous["timestamp"]:
            raise ValueError(f"CSV line {line}: run identity changed, index skipped, or UTC time did not increase")

        firmware_c = nominal_celsius(raw, firmware_vref)
        measured_vref_c = (raw * vref / 65535 - 0.5) / 0.01
        vout_c = (vout - 0.5) / 0.01
        expected_alarm = next_alarm(previous["alarm"], firmware_c)
        previous.update(index=index, timestamp=timestamp, alarm=expected_alarm)
        runs[run_id] = previous
        flags = []
        if led_observed != int(expected_alarm):
            flags.append("led_mismatch")
        if not 2.7 <= vref <= 3.3:
            flags.append("vref_outside_lab_model")
        if vout > vref:
            flags.append("vout_above_adc_vref")
        if not -40 <= reference_c <= 125:
            flags.append("reference_outside_tmp36_rated_range")
        results.append({
            "run_id": run_id,
            "sample_index": index,
            "timestamp_utc": timestamp.isoformat(),
            "firmware_c": round(firmware_c, 6),
            "measured_vref_c": round(measured_vref_c, 6),
            "vout_c": round(vout_c, 6),
            "firmware_minus_reference_c": round(firmware_c - reference_c, 6),
            "vout_minus_reference_c": round(vout_c - reference_c, 6),
            "adc_estimated_vout_minus_dmm_v": round(raw * vref / 65535 - vout, 6),
            "reference_u_c": reference_u_c,
            "led_expected": int(expected_alarm),
            "led_observed": led_observed,
            "flags": flags,
        })
    return {
        "status": "review_required" if any(r["flags"] for r in results) else "analysis_only",
        "sample_count": len(results),
        "run_count": len(runs),
        "hardware_accepted": False,
        "samples": results,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()
    try:
        report = analyze_file(args.csv_file)
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Measurement record error: {exc}\n")
    print(json.dumps(report, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
