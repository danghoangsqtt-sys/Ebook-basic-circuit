"""Pico (original non-W) + TMP36GT9Z temperature monitor.

Reference only: Raspberry Pi Pico datasheet, board drawing Rev3; ADI
TMP35/36/37 Rev H, TO-92 T-3-1. Verify the actual board and sensor marking,
pin orientation, rails and ADC reference before any physical connection.
The conversion is nominal and is not a calibrated thermometer.
"""

ADC_REF_V = 3.3  # model assumption; measure ADC_VREF for a real experiment
ADC_FULL_SCALE = 65535
ON_C = 30.0
OFF_C = 28.0


def nominal_celsius(raw, reference_v=ADC_REF_V):
    if not isinstance(raw, int) or not 0 <= raw <= ADC_FULL_SCALE:
        raise ValueError("ADC code must be an integer from 0 to 65535")
    if not 2.7 <= reference_v <= 3.3:
        raise ValueError("reference_v outside this lab's declared 2.7–3.3 V model")
    volts = raw * reference_v / ADC_FULL_SCALE
    return (volts - 0.5) / 0.01


def next_alarm(previous, temperature_c, on_c=ON_C, off_c=OFF_C):
    if off_c >= on_c:
        raise ValueError("off_c must be below on_c")
    if temperature_c >= on_c:
        return True
    if temperature_c <= off_c:
        return False
    return bool(previous)


def run(adc, led, sleep_ms, samples=None, period_ms=1000, reference_v=ADC_REF_V,
        log=print):
    """Read ADC0 and update onboard LED; samples=None runs until interrupted."""
    if samples is not None and (not isinstance(samples, int) or samples < 0):
        raise ValueError("samples must be non-negative or None")
    if period_ms <= 0:
        raise ValueError("period_ms must be positive")
    alarm = False
    led.value(0)
    count = 0
    try:
        while samples is None or count < samples:
            raw = adc.read_u16()
            degrees = nominal_celsius(raw, reference_v)
            alarm = next_alarm(alarm, degrees)
            led.value(int(alarm))
            log("raw=%d; nominal_C=%.2f; alarm=%d" % (raw, degrees, alarm))
            count += 1
            sleep_ms(period_ms)
    finally:
        led.value(0)


if __name__ == "__main__":
    from machine import ADC, Pin
    from time import sleep_ms

    run(ADC(Pin(26)), Pin(25, Pin.OUT, value=0), sleep_ms)
