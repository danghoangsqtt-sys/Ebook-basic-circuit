"""Fetch four reviewed Commons files and convert them to compact local WebP.

The Commons API licence is checked for each exact file before any image is saved.
"""

from __future__ import annotations

import io
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets/images/lessons"
PHOTOS = {
    "File:Electronic-Axial-Lead-Resistors-Array.jpg": ("resistor-array-public-domain.webp", "Public domain"),
    "File:Green light emitting diode led on circuit board.jpg": ("led-on-board-public-domain.webp", "Public domain"),
    "File:Electrolytic capacitors-P1090328.JPG": ("electrolytic-capacitors-cc0.webp", "CC0"),
    "File:EC24 miniature axial inductors.jpg": ("axial-inductors-cc0.webp", "CC0"),
    "File:Generic 2N2222A.jpeg": ("bjt-2n2222a-cc0.webp", "CC0"),
    "File:IRFIBC30 MOS transistor 01.jpg": ("mosfet-irfibc30-cc0.webp", "CC0"),
    "File:DHT22-Temperatur-Sensor.jpg": ("dht22-sensor-cc0.webp", "CC0"),
    "File:Digimess oscilloscope.jpg": ("oscilloscope-digimess-cc0.webp", "CC0"),
    "File:Computer Motherboard Closeup.jpg": ("assembled-pcb-cc0.webp", "CC0"),
    "File:18650 and 21700 lithium ion battery cell.jpg": ("li-ion-cells-cc0.webp", "CC0"),
    "File:ESP32 Espressif ESP-WROOM-32 Dev Board.jpg": ("esp32-dev-board-cc0.webp", "CC0"),
}
HEADERS = {"User-Agent": "ElectricBasicCourse/1.0 (educational media import; Wikimedia Commons API)"}


def fetch(url: str) -> bytes:
    for attempt in range(4):
        request = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if error.code != 429 or attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))
    raise RuntimeError("Unreachable retry state")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for title, (filename, expected) in PHOTOS.items():
        output = OUT_DIR / filename
        if output.is_file():
            print(f"{filename}: already present")
            continue
        query = urllib.parse.urlencode({
            "action": "query", "format": "json", "titles": title,
            "prop": "imageinfo", "iiprop": "url|extmetadata",
        })
        result = json.loads(fetch(f"https://commons.wikimedia.org/w/api.php?{query}"))
        pages = result["query"]["pages"]
        info = next(iter(pages.values()))["imageinfo"][0]
        metadata = info["extmetadata"]
        licence = metadata["LicenseShortName"]["value"]
        if expected.casefold() not in licence.casefold():
            raise ValueError(f"{title}: expected {expected!r}, Commons reports {licence!r}")
        raw = fetch(info["url"])
        with Image.open(io.BytesIO(raw)) as source:
            rgb = ImageOps.exif_transpose(source).convert("RGB")
            rgb.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
            rgb.save(output, "WEBP", quality=82, method=6)
            print(f"{filename}: {rgb.width}×{rgb.height}, {output.stat().st_size} bytes, {licence}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
