"""Insert curated overview figures and reviewed public media into lesson pages."""

from __future__ import annotations

import argparse
import json
import re
from html import escape
from pathlib import Path
from urllib.parse import quote

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SPECS = ROOT / "docs/visuals/overview-specs.json"
ASSETS = ROOT / "assets/images/lessons"
PHOTOS = {
    3: ("resistor-array-public-domain.webp", "Evan-Amos", "Public domain", "Electronic-Axial-Lead-Resistors-Array.jpg", "Sáu điện trở chân cắm với các vạch màu khác nhau; vạch vàng kim là vạch sai số 5%.", "Ảnh điện trở nhiều giá trị. Đọc mã từ phía đối diện vạch vàng kim; màu và giá trị cụ thể của ảnh được ghi tại trang nguồn."),
    4: ("led-on-board-public-domain.webp", "Leon Brooks", "Public domain", "Green light emitting diode led on circuit board.jpg", "LED màu xanh lục gắn trên một mạch in nhỏ, có hai chân đi xuống PCB.", "LED gắn trên PCB. Ảnh giúp nhận dạng vỏ linh kiện, không đủ để suy chân anode/cathode hoặc điện trở hạn dòng của mạch."),
    8: ("electrolytic-capacitors-cc0.webp", "Elcap", "CC0 1.0", "Electrolytic capacitors-P1090328.JPG", "Nhiều kiểu tụ điện phân, dạng trụ xuyên lỗ và dạng dán bề mặt, có kích thước khác nhau.", "Các kiểu tụ điện phân bằng nhôm và tantalum; cần đọc dấu cực và điện áp định mức trên đúng linh kiện trước khi lắp."),
    10: ("axial-inductors-cc0.webp", "Retired electrician", "CC0 1.0", "EC24 miniature axial inductors.jpg", "Mười cuộn cảm nhỏ dạng trục màu xanh đặt song song trên băng giấy.", "Cuộn cảm EC24 dạng trục trông gần giống điện trở; tra ký hiệu và đo kiểm trước khi lắp."),
    15: ("bjt-2n2222a-cc0.webp", "MarkMossGH", "CC0 1.0", "Generic 2N2222A.jpeg", "Transistor lưỡng cực 2N2222A vỏ TO-92 nhìn từ phía mặt phẳng và ba chân kim loại.", "Ví dụ transistor BJT 2N2222A vỏ TO-92. Bài thực hành có thể dùng BC337; ảnh không xác định thứ tự chân của linh kiện bạn cầm, hãy tra datasheet đúng mã."),
    18: ("mosfet-irfibc30-cc0.webp", "Retired electrician", "CC0 1.0", "IRFIBC30 MOS transistor 01.jpg", "Các MOSFET IRFIBC30 trong vỏ TO-220 cách điện đặt cạnh nhau.", "Ngoại hình MOSFET IRFIBC30 vỏ TO-220 cách điện. Ảnh không ngụ ý mã này đóng cắt đủ ở GPIO 3,3 V; phải kiểm RDS(on) tại VGS dùng thật."),
    27: ("dht22-sensor-cc0.webp", "Ubahnverleih", "CC0 1.0", "DHT22-Temperatur-Sensor.jpg", "Cảm biến nhiệt độ và độ ẩm DHT22 màu trắng, mặt trước có các lỗ thông khí.", "Cảm biến DHT22 rời. Không suy thứ tự chân hay điện trở kéo lên chỉ từ ảnh mặt trước; đối chiếu datasheet/module thực tế."),
    30: ("oscilloscope-digimess-cc0.webp", "Stablenode", "CC0 1.0", "Digimess oscilloscope.jpg", "Máy hiện sóng Digimess loại analog nhìn chính diện, có màn hình và nhiều núm chỉnh.", "Ví dụ máy hiện sóng analog Digimess; vị trí núm Volt/div, Time/div và Trigger thay đổi theo model. Ảnh không đại diện giao diện máy số hiện nay."),
    33: ("assembled-pcb-cc0.webp", "Lenharth Systems", "CC0 1.0", "Computer Motherboard Closeup.jpg", "Cận cảnh bo mạch máy tính có linh kiện SMD, đầu nối, đường mạch và tụ điện.", "Ví dụ PCB đã lắp linh kiện ở mật độ cao. Đây là bo máy tính, không phải layout KiCad của bài; dùng ảnh để nhận diện lớp mạch, vị trí và linh kiện."),
    41: ("li-ion-cells-cc0.webp", "Sevenethics", "CC0 1.0", "18650 and 21700 lithium ion battery cell.jpg", "Hai cell Li-ion hình trụ kích cỡ 18650 và 21700 đặt cạnh nhau.", "Hai cell Li-ion 18650 và 21700 để nhận diện kích cỡ. Ảnh không phải LiPo dạng túi, không cho biết dòng sạc/xả an toàn; đọc datasheet của cell dùng thật."),
}


def figure(day: int, spec: dict) -> str:
    headings = "; ".join(f"{item['heading']}: {item['detail']}" for item in spec["items"])
    alt = spec.get("alt") or f"{spec['title']}. {headings}"
    overview = (
        '      <div class="figure figure--overview">\n'
        f'        <img src="../assets/images/lessons/day{day:02d}-overview.svg" width="560" height="1114" loading="lazy" decoding="async" alt="{escape(alt, quote=True)}">\n'
        '        <div class="figure-caption">\n'
        f'          <div class="figure-number">Sơ đồ tổng quan Bài {day}</div>\n'
        f'          <div class="figure-text">{escape(spec["title"])}. {escape(spec["note"])}.</div>\n'
        '          <div class="figure-source">Nguồn: tự vẽ cho giáo trình; nội dung đối chiếu với bài học.</div>\n'
        '        </div>\n'
        '      </div>\n'
    )
    if day not in PHOTOS:
        return overview
    filename, author, licence, source, photo_alt, caption = PHOTOS[day]
    with Image.open(ASSETS / filename) as image:
        width, height = image.size
    url = f"https://commons.wikimedia.org/wiki/File:{quote(source)}"
    photo = (
        '      <div class="figure figure--equipment">\n'
        f'        <img src="../assets/images/lessons/{filename}" width="{width}" height="{height}" loading="lazy" decoding="async" alt="{escape(photo_alt, quote=True)}">\n'
        '        <div class="figure-caption">\n'
        f'          <div class="figure-number">Ảnh linh kiện Bài {day}</div>\n'
        f'          <div class="figure-text">{escape(caption)}</div>\n'
        f'          <div class="figure-source">Ảnh: {escape(author)}, <a href="{escape(url, quote=True)}" target="_blank" rel="noopener">Wikimedia Commons</a> ({escape(licence)}); đã thu nhỏ và chuyển WebP.</div>\n'
        '        </div>\n'
        '      </div>\n'
    )
    return overview + "\n" + photo


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", nargs="*", type=int)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    specs = json.loads(SPECS.read_text(encoding="utf-8"))
    days = sorted(args.days or (int(key) for key in specs))
    for day in days:
        path = ROOT / f"week{(day - 1) // 7 + 1}/day{day:02d}.html"
        html = path.read_text(encoding="utf-8")
        start = f"<!-- LESSON VISUALS START day{day:02d} -->"
        end = f"<!-- LESSON VISUALS END day{day:02d} -->"
        block = f"      {start}\n{figure(day, specs[f'{day:02d}'])}      {end}\n\n"
        if start in html:
            pattern = re.compile(rf"      {re.escape(start)}.*?      {re.escape(end)}\n\n", re.S)
            updated, count = pattern.subn(lambda _: block, html)
            if count != 1:
                raise ValueError(f"Cannot replace figure block in {path}")
        else:
            first_heading = re.search(r"(?m)^      <h2(?:\s|>)", html)
            if not first_heading:
                raise ValueError(f"No lesson heading in {path}")
            updated = html[:first_heading.start()] + block + html[first_heading.start():]
        if args.check:
            if updated != html:
                raise ValueError(f"Lesson visual block is stale: {path}")
        else:
            path.write_text(updated, encoding="utf-8")
    print(f"{'Checked' if args.check else 'Integrated'} {len(days)} lesson visual blocks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
