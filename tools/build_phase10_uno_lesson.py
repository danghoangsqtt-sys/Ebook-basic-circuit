"""Publish A33: overview of MCU board families plus a detailed Arduino Uno R3 case.

Source of the lesson text and figure is this script. It also links A32 -> A33.
The Uno is a worked example for transfer to other boards, not a hardware claim.
"""

from html import escape
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("p10", ROOT / "tools/build_phase10_lessons.py")
p10 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p10)
source = p10.source

UNO = "https://docs.arduino.cc/hardware/uno-rev3/"
UNO_DS = "https://docs.arduino.cc/resources/datasheets/A000066-datasheet.pdf"
AVR = "https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf"
TMP = p10.TMP
PICO = p10.PICO

ITEM = {
    "id": "a33", "title": "Họ Board MCU & Chi Tiết Arduino Uno R3", "base": "A22;A23;A24;A31", "units": "6",
    "subtitle": "Nhìn tổng quan các họ board, rồi đi sâu một board mẫu để tự suy ra cách đọc các board khác.",
    "alt": "Sơ đồ khối Arduino Uno R3: USB hoặc jack DC đi qua bộ ổn áp tới rail 5 V, vi điều khiển ATmega328P ở giữa, bên phải là ba nhóm chân: D0 đến D13, A0 đến A5 và chân nguồn.",
    "caption": "Khối khái niệm của Uno R3 theo tài liệu hãng; không phải netlist hay sơ đồ nguyên lý.",
    "transcript": "Nguồn vào là cổng USB hoặc jack DC 7 đến 12 volt khuyến nghị. Nguồn đi qua bộ ổn áp trên board tạo rail 5 volt cấp cho ATmega328P chạy 16 MHz, bộ nhớ flash 32 KB, SRAM 2 KB và EEPROM 1 KB. Bên phải là ba nhóm chân: D0 đến D13 gồm 6 chân PWM; A0 đến A5 là ngõ vào ADC 10 bit, trong đó A4 và A5 dùng cho I2C; cuối cùng là các chân nguồn 5V, 3V3, VIN, GND và AREF.",
    "objectives": [
        "Phân biệt năm họ board (AVR, Cortex-M, MCU có radio, STM32, MPU) theo lõi, mức logic và điểm cần cẩn thận.",
        "Đọc một board mẫu (Uno R3) theo thứ tự nguồn → lõi/bộ nhớ → chân/ngoại vi → giới hạn dòng, và tính ADC, LED, nhiệt ổn áp.",
        "Áp tám câu hỏi chuyển giao để tự phân tích board khác mà không suy giới hạn từ họ chip sang module khác.",
    ],
    "body": f'''<h2>1. Bản đồ tổng quan: các họ board hay gặp khi học điện tử</h2>
<p>Một “board” gồm chip vi điều khiển cộng nguồn, cổng nạp/USB, tụ, đầu nối và đôi khi module radio. Hai board cùng họ chip vẫn có thể khác nhau về nguồn và chân, nên bảng dưới chỉ để định hướng; số liệu cuối cùng luôn lấy từ tài liệu hãng theo <strong>mã board và revision</strong> (xem A24).</p>
<div class="table-wrap"><table><caption>Năm họ board, phân loại để định hướng — chưa phải bảng chọn mua</caption><thead><tr><th>Họ</th><th>Ví dụ</th><th>Lõi và mức logic thường gặp</th><th>Điểm mạnh khi học</th><th>Điểm cần cẩn thận</th></tr></thead><tbody>
<tr><td>AVR 8 bit</td><td>Arduino Uno R3 (ATmega328P)</td><td>8 bit; logic 5 V</td><td>Cấu trúc đơn giản, ít lớp trừu tượng, tài liệu hãng đầy đủ</td><td>Bộ nhớ nhỏ (SRAM 2 KB), ADC 10 bit, không có radio</td></tr>
<tr><td>ARM Cortex-M0+</td><td>Raspberry Pi Pico (RP2040)</td><td>32 bit; logic 3,3 V</td><td>Nhiều SRAM hơn, có MicroPython (A22–A23)</td><td>GPIO không chịu 5 V; LED GP25 chỉ có trên non-W</td></tr>
<tr><td>MCU có radio</td><td>Họ ESP32, ví dụ ESP32-C6-DevKitC-1</td><td>32 bit (Xtensa hoặc RISC-V); logic 3,3 V</td><td>Wi-Fi/BLE và nhiều ngoại vi</td><td>Dòng đỉnh khi phát sóng, chân strapping, khác biệt chip với module (A24)</td></tr>
<tr><td>STM32</td><td>Board Nucleo/Discovery</td><td>32 bit Cortex-M; thường 3,3 V</td><td>Họ rộng, công cụ chuyên nghiệp</td><td>Hàng trăm biến thể; phải đọc đúng mã chip và manual board</td></tr>
<tr><td>MPU/SBC</td><td>Raspberry Pi chạy Linux</td><td>Lõi ứng dụng cùng hệ điều hành</td><td>Mạng, camera, giao diện đồ họa</td><td>Không phải MCU thời gian thực cứng; nguồn và khởi động phức tạp hơn</td></tr>
</tbody></table></div>
<h2>2. Vì sao chọn Uno R3 làm board mẫu</h2>
<p>Bài này chọn Uno R3 vì bốn lý do học thuật, <strong>không</strong> dựa trên thống kê thị phần (không có nguồn kiểm chứng trong giáo trình): có tài liệu hãng chính thức ({source(UNO,'Arduino Uno Rev3')}, {source(UNO_DS,'datasheet A000066')}); logic 5 V trùng mức của các mạch HC ở A17; đủ ngoại vi cơ bản (GPIO, PWM, ADC, UART, I²C, SPI); và không có radio nên ít biến số hơn. Sau khi nắm Uno, bạn dùng cùng khung câu hỏi ở mục 6 cho board khác.</p>
<h2>3. Uno R3 từng lớp</h2>
<p><strong>Lớp 1 — nguồn.</strong> USB hoặc jack DC đi qua mạch ổn áp trên board tạo rail 5 V. Hãng khuyến nghị Vin 7–12 V và nêu giới hạn 6–20 V; chân 3,3 V chỉ cấp tối đa khoảng 50 mA. <strong>Lớp 2 — lõi và bộ nhớ.</strong> Chip {source(AVR,'ATmega328P')} chạy 16 MHz, flash 32 KB (0,5 KB bootloader), SRAM 2 KB, EEPROM 1 KB. <strong>Lớp 3 — chân.</strong> 14 chân số (6 PWM) và 6 ngõ analog.</p>
<div class="table-wrap"><table><caption>Thông số Uno R3 theo tài liệu hãng — đọc lại đúng bản tài liệu trước khi thiết kế</caption><thead><tr><th>Mục</th><th>Giá trị</th></tr></thead><tbody>
<tr><td>Vi điều khiển / xung</td><td>ATmega328P / 16 MHz</td></tr><tr><td>Điện áp làm việc</td><td>5 V</td></tr>
<tr><td>Vin khuyến nghị / giới hạn</td><td>7–12 V / 6–20 V</td></tr>
<tr><td>Dòng DC mỗi chân I/O</td><td>20 mA (tài liệu board); datasheet chip nêu mức tuyệt đối cao hơn, không phải điểm vận hành</td></tr>
<tr><td>Dòng chân 3,3 V</td><td>50 mA</td></tr>
<tr><td>Flash / SRAM / EEPROM</td><td>32 KB (0,5 KB bootloader) / 2 KB / 1 KB</td></tr>
<tr><td>Chân số / PWM / analog</td><td>14 / 6 / 6</td></tr>
</tbody></table></div>
<div class="table-wrap"><table><caption>Nhóm chức năng chân thường dùng — đối chiếu bảng pinout hãng cho đúng revision</caption><thead><tr><th>Nhóm</th><th>Chân</th><th>Ghi chú học tập</th></tr></thead><tbody>
<tr><td>UART</td><td>D0 (RX), D1 (TX)</td><td>Dùng chung với cổng USB nạp/serial; tránh nối tải lên hai chân này khi nạp</td></tr>
<tr><td>Ngắt ngoài</td><td>D2, D3</td><td>Đọc nút/cảm biến xung không cần thăm dò liên tục</td></tr>
<tr><td>PWM</td><td>D3, D5, D6, D9, D10, D11</td><td>Điều sáng LED, điều khiển servo/động cơ qua tầng công suất riêng</td></tr>
<tr><td>SPI</td><td>D10 (SS), D11 (MOSI), D12 (MISO), D13 (SCK)</td><td>D13 còn nối LED trên board</td></tr>
<tr><td>I²C</td><td>A4 (SDA), A5 (SCL)</td><td>Chia sẻ chân với ngõ analog</td></tr>
<tr><td>ADC</td><td>A0–A5</td><td>10 bit; tham chiếu 5 V, chân AREF hoặc tham chiếu nội</td></tr>
</tbody></table></div>
<h2>4. Bốn phép tính mẫu trên Uno</h2>
<p><strong>(a) ADC với tham chiếu 5 V.</strong> Một mã ứng với 5/1024 ≈ 4,88 mV. TMP36 ở 25 °C xuất 0,750 V (theo {source(TMP,'ADI TMP36 Rev. H')}) nên mã = ⌊0,750/5×1024⌋ = ⌊153,6⌋ = 153, T_est = (153×5/1024 − 0,5)/0,010 ≈ 24,71 °C. Mỗi mã tương ứng 0,488 °C: độ phân giải khá thô vì cảm biến chỉ dùng khoảng 8% thang đo.</p>
<p><strong>(b) Tham chiếu nội 1,1 V (danh định).</strong> Cùng 0,750 V cho mã ⌊698,18⌋ = 698, T_est ≈ 24,98 °C, mỗi mã 0,107 °C; tới 60 °C (1,10 V) thì bão hòa. Nhưng 1,1 V chỉ là danh định: <em>giả sử</em> tham chiếu thật lệch ±0,1 V mà phần mềm vẫn dùng 1,1 V thì kết quả thành 32,5 °C hoặc 18,75 °C thay vì 25 °C. Giả định ±0,1 V là số đặt ra để thấy tác động, không phải dung sai chip; muốn chính xác phải đọc datasheet chip và hiệu chuẩn bằng phép đo (A28).</p>
<p><strong>(c) LED.</strong> Từ 5 V, LED giả định V_F = 2 V và R = 330 Ω: I = (5−2)/330 ≈ 9,09 mA, thấp hơn mức 20 mA của tài liệu board. Sáu LED như vậy cộng thành 54,5 mA; đó mới là phép cộng, giới hạn tổng của chip và nguồn phải đọc riêng trong datasheet.</p>
<p><strong>(d) Nhiệt ổn áp từ Vin.</strong> Giả sử ổn áp tuyến tính, P ≈ (Vin − 5)·I. Với 9 V và 100 mA là 0,40 W; với 12 V và 150 mA là 1,05 W. Vì thế hãng khuyến nghị 7–12 V thay vì dùng 20 V. Đây là mô hình, chưa phải phép đo nhiệt; đối chiếu schematic hãng khi cần chính xác.</p>
<h2>5. Mã minh họa (chưa biên dịch)</h2>
<p>Đoạn dưới <strong>chưa biên dịch và chưa chạy trên Uno thật</strong>; nó chỉ cho thấy API đọc TMP36 qua tham chiếu nội 1,1 V. Theo tài liệu Arduino, vài lần đọc đầu sau khi đổi tham chiếu có thể chưa chính xác nên nên bỏ qua.</p>
<pre><code>const int PIN_TMP = A0;

void setup() {{
  analogReference(INTERNAL);   // tham chiếu nội 1,1 V (ATmega328P)
  Serial.begin(9600);
}}

void loop() {{
  int raw = analogRead(PIN_TMP);      // 0..1023
  float v = raw * 1.1 / 1024.0;       // volt, giả định đúng 1,1 V
  float t = (v - 0.5) / 0.010;        // TMP36 danh định
  Serial.println(t);
  delay(1000);
}}</code></pre>
<h2>6. Từ Uno sang board khác: tám câu hỏi chuyển giao</h2>
<div class="table-wrap"><table><caption>Khung câu hỏi dùng được cho mọi board</caption><thead><tr><th>Câu hỏi</th><th>Uno R3</th><th>Pico (A22–A24)</th><th>Cách làm với board mới</th></tr></thead><tbody>
<tr><td>1. Mức logic?</td><td>5 V</td><td>3,3 V</td><td>Đọc datasheet; không nối 5 V vào chân 3,3 V</td></tr>
<tr><td>2. Dòng mỗi chân?</td><td>20 mA (board)</td><td>Theo datasheet RP2040/Pico</td><td>Tìm bảng dòng đúng chip và đúng board; không suy từ họ khác</td></tr>
<tr><td>3. Nguồn vào?</td><td>USB hoặc Vin 7–12 V</td><td>USB/VSYS (A30)</td><td>Vẽ đường nguồn từ cổng vào tới rail logic</td></tr>
<tr><td>4. ADC?</td><td>10 bit; 5 V/AREF/1,1 V</td><td>12 bit; VREF từ 3,3 V (A31)</td><td>Tính LSB = V_ref/2^N rồi ra độ phân giải đo</td></tr>
<tr><td>5. Bus và chân?</td><td>Chân cố định</td><td>Nhiều chân gán lại được</td><td>Đọc bảng pinout đúng revision</td></tr>
<tr><td>6. Bộ nhớ?</td><td>32 KB / 2 KB / 1 KB</td><td>2 MB flash board, 264 kB SRAM chip</td><td>Lập ngân sách như A24, ghi rõ chip hay board</td></tr>
<tr><td>7. Cách nạp?</td><td>Bootloader qua USB</td><td>BOOTSEL và UF2</td><td>Đọc hướng dẫn nạp của hãng</td></tr>
<tr><td>8. Biến thể/clone?</td><td>Board clone có thể khác chip USB hoặc ổn áp</td><td>non-W khác W</td><td>Đối chiếu schematic đúng mã board bạn có</td></tr>
</tbody></table></div>
<div class="callout callout-practice"><div class="callout-header">🔬 Phạm vi bài này</div><p>Không có board Uno thật hoặc phép đo trong giáo trình; số liệu ở mục 4 là mô hình lý tưởng, kiểm bằng <code>python tools/verify_phase10_uno_model.py</code>. Cổng phần cứng nằm ở <a href="../docs/qa/curriculum-hardware-pending.md">sổ chờ phần cứng</a>.</p></div>''',
    "exercise": "Dùng Uno với tham chiếu 5 V đọc TMP36: tính kích thước một mã (mV), mã ở 25 °C (0,750 V), T_est và bước nhiệt độ mỗi mã; nêu một cách cải thiện độ phân giải và rủi ro đi kèm; rồi viết ba câu hỏi bạn sẽ đặt đầu tiên khi nhận một board lạ.",
    "answer": "<ol><li>2 điểm: 5/1024 ≈ 4,88 mV; mã = 153; T_est ≈ 24,71 °C; bước ≈ 0,488 °C.</li><li>2 điểm: dùng tham chiếu nội 1,1 V (mã 698, bước 0,107 °C) hoặc khuếch đại tín hiệu.</li><li>2 điểm: rủi ro là tham chiếu danh định có sai số, cần hiệu chuẩn; tín hiệu bão hòa ở 60 °C.</li><li>2 điểm: ba câu từ bảng mục 6, ví dụ mức logic, dòng chân/nguồn, bits/tham chiếu ADC; không suy từ họ chip khác.</li></ol>",
    "checks": ["Tôi nêu được năm họ board", "Tôi tính được LSB và bước nhiệt độ của ADC", "Tôi không suy giới hạn từ họ chip sang board khác"],
    "source": f'{source(UNO,"Arduino Uno Rev3")}, {source(UNO_DS,"A000066 datasheet")}, {source(TMP,"ADI TMP36 Rev. H")}',
}


def svg():
    title = "A33 — Họ Board MCU & Chi Tiết Arduino Uno R3"
    box = lambda x, y, w, h, fill: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}"/>'
    text = lambda x, y, s, size=18, fill="white", anchor="middle": f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" text-anchor="{anchor}">{escape(s)}</text>'
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="900" height="480" viewBox="0 0 900 480" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title><desc id="desc">{escape(ITEM["alt"])}</desc>',
        '<rect width="900" height="480" rx="24" fill="#0f172a"/>',
        '<g font-family="Arial">',
        text(35, 50, title, 25, "#e2e8f0", "start").replace('<text ', '<text font-weight="bold" '),
        box(30, 90, 220, 110, "#164e63"), text(140, 132, "USB-B  ·  5 V"), text(140, 160, "Jack DC", 18), text(140, 185, "Vin 7–12 V khuyến nghị", 16),
        box(30, 250, 220, 120, "#14532d"), text(140, 292, "Ổn áp trên board"), text(140, 320, "→ rail 5 V", 18), text(140, 345, "3V3 tối đa ~50 mA", 16),
        box(300, 90, 280, 280, "#1e293b"), text(440, 135, "ATmega328P", 22), text(440, 170, "16 MHz", 18),
        text(440, 215, "Flash 32 KB", 18), text(440, 245, "SRAM 2 KB", 18), text(440, 275, "EEPROM 1 KB", 18), text(440, 320, "ADC 10 bit", 18),
        box(630, 90, 240, 75, "#713f12"), text(750, 122, "D0–D13", 20), text(750, 148, "6 chân PWM", 16),
        box(630, 185, 240, 75, "#713f12"), text(750, 217, "A0–A5", 20), text(750, 243, "A4 SDA · A5 SCL", 16),
        box(630, 280, 240, 90, "#713f12"), text(750, 312, "5V · 3V3 · VIN", 18), text(750, 338, "GND · AREF", 18),
        '<path d="M250 145H300M250 310H275V230H300M580 128H630M580 222H630M580 325H630" stroke="#93c5fd" stroke-width="4" fill="none"/>',
        text(45, 430, "Khái niệm theo tài liệu hãng · không là netlist, không là phép đo", 18, "#cbd5e1", "start"),
        '</g></svg>',
    ]
    return "".join(parts) + "\n"


def link_a32():
    page = ROOT / "advanced/a32.html"
    html = page.read_text(encoding="utf-8")
    if 'href="a33.html"' in html:
        return
    nxt = ('<a href="a33.html" class="lesson-nav-btn"><div><div class="nav-label">Bài tiếp →</div>'
           f'<div class="nav-title">A33: {escape(ITEM["title"])}</div></div></a>')
    marker = '</a></div></article>'
    assert html.count(marker) == 1, "unexpected A32 nav shell"
    page.write_text(html.replace(marker, '</a>' + nxt + '</div></article>'), encoding="utf-8", newline="\n")


def main():
    previous = ("a32", "A32: Tích Hợp PCB & Báo Cáo Sai Khác")
    (ROOT / "advanced/a33.html").write_text(p10.render(ITEM, previous, None), encoding="utf-8", newline="\n")
    (ROOT / "assets/images/advanced/a33.svg").write_text(svg(), encoding="utf-8", newline="\n")
    link_a32()
    print("a33 published; a32 linked")


if __name__ == "__main__":
    main()
