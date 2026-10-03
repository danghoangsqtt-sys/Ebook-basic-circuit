"""Exercise production monitor with fake ADC/LED and check physical units."""

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("monitor", ROOT / "labs/pico_tmp36_monitor.py")
monitor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(monitor)
spec = importlib.util.spec_from_file_location("sim", ROOT / "tools/simulate_phase9_sensor_lab.py")
sim = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sim)


class FakeADC:
    def __init__(self, codes):
        self.codes = iter(codes)

    def read_u16(self):
        return next(self.codes)


class FakeLED:
    def __init__(self):
        self.values = []

    def value(self, state):
        self.values.append(state)


def main():
    rows = sim.model()
    assert [row["ideal_v"] for row in rows] == [.75, .79, .8, .81, .79, .78, .77, .81]
    # Quantization near thresholds matters: 30 C and 28 C code values can
    # decode slightly below/above the exact boundary, so independently derive
    # the expected LED trace from the quantized voltage, not the stimulus label.
    expected = []
    state = False
    for row in rows:
        decoded = (row["adc_u16"] * 3.3 / 65535 - .5) / .01
        state = decoded >= 30 or (state and decoded > 28)
        expected.append(int(state))
        assert abs(decoded - row["stimulus_c"]) < .003
    assert [row["led"] for row in rows] == expected
    assert expected == [0, 0, 0, 1, 1, 0, 0, 1]
    led = FakeLED()
    delays = []
    logs = []
    monitor.run(FakeADC([r["adc_u16"] for r in rows]), led, delays.append,
                samples=len(rows), log=logs.append)
    assert led.values == [0] + expected + [0]
    assert delays == [1000] * len(rows)
    assert len(logs) == len(rows) and all("raw=" in line for line in logs)
    for invalid in (-1, 65536, 1.2):
        try:
            monitor.nominal_celsius(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid ADC code accepted")
    assert monitor.next_alarm(False, 31) and monitor.next_alarm(True, 29)
    assert not monitor.next_alarm(True, 27)
    print("P9-04 ideal stimulus, ADC conversion, hysteresis, log and cleanup: PASS")
    print("LED model trace:", expected)


if __name__ == "__main__":
    main()
