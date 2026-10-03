"""P9-02 GPIO lab: on-board LED of original, non-wireless Raspberry Pi Pico.

Target reference: Raspberry Pi Pico RP2040 board, datasheet Figure 1 Rev3.
The LED is driven by GP25 on this board, not by an exposed header pin.
Do not use this pin mapping for Pico W or ESP32-C6-DevKitC-1.

MicroPython on the verified original Pico: copy this file as main.py and reset.
Host: python tools/verify_phase9_pico_lab.py checks only the command schedule.
"""


def blink(pin_factory, sleep_ms, cycles=None, high_ms=250, low_ms=250):
    """Command the built-in LED high then low, leaving it low after finite runs."""
    if high_ms <= 0 or low_ms <= 0 or (cycles is not None and cycles < 0):
        raise ValueError("positive delays and non-negative cycle count required")
    led = pin_factory(25, pin_factory.OUT, value=0)
    count = 0
    while cycles is None or count < cycles:
        led.value(1)
        sleep_ms(high_ms)
        led.value(0)
        sleep_ms(low_ms)
        count += 1
    return led


if __name__ == "__main__":
    from machine import Pin
    from time import sleep_ms

    blink(Pin, sleep_ms)
