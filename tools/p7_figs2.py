"""P7-04 figure builders, part 2: buses, waveforms, filters, block diagrams."""

from __future__ import annotations

import math

from p7_svg import S, f


def d22_1() -> S:
    s = S(360, 310, "Nối UART giữa hai thiết bị",
          "TX của thiết bị A nối RX của thiết bị B, RX của A nối TX của B, và hai GND nối chung. "
          "UART full-duplex nên hai chiều chạy đồng thời.")
    s.t(180, 28, "UART: TX → RX chéo, GND chung", "h", "middle")
    s.box(20, 60, 90, 160, "p")
    s.box(250, 60, 90, 160, "z")
    s.t(65, 50, "Thiết bị A", "b", "middle")
    s.t(295, 50, "Thiết bị B", "b", "middle")
    for y, a, b in [(100, "TX", "RX"), (150, "RX", "TX"), (200, "GND", "GND")]:
        s.t(102, y + 4, a, "b", "end")
        s.t(258, y + 4, b, "b")
    s.wire("M110 100 H250 M110 150 H250 M110 200 H250")
    s.arrow(150, 100, 215, 100)
    s.arrow(215, 150, 150, 150, "ao")
    s.t(180, 90, "A gửi → B nhận", "m", "middle")
    s.t(180, 140, "B gửi → A nhận", "m", "middle")
    s.t(180, 190, "GND chung", "b", "middle")
    s.t(180, 250, "GND chung là bắt buộc", "m", "middle")
    s.t(180, 270, "Full-duplex: hai chiều đồng thời", "m", "middle")
    s.t(180, 290, "Hai thiết bị cần cùng mức logic", "m", "middle")
    return s


def d22_2() -> S:
    s = S(380, 270, "Khung UART 8N1 với dữ liệu 0x55",
          "Đường truyền nghỉ ở mức HIGH. Start bit LOW dài một bit. Tám bit dữ liệu, bit thấp nhất D0 truyền "
          "trước; ví dụ 0x55 là 1,0,1,0,1,0,1,0. Sau đó một stop bit HIGH rồi lại nghỉ HIGH.")
    s.t(190, 28, "Khung UART 8N1 (ví dụ dữ liệu 0x55)", "h", "middle")
    bw = 28
    xs = 60
    yh, yl = 100, 140
    bits = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    labels = ["Start", "D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "Stop"]
    d = f"M20 {yh} H{xs}"
    level = 1
    for i, b in enumerate(bits):
        x = xs + i * bw
        if b != level:
            d += f" V{yh if b else yl}"
            level = b
        d += f" H{x + bw}"
    if level == 0:
        d += f" V{yh}"
    d += f" H360"
    s.parts.append(f'<path class="w" d="{d}"/>')
    for i, lab in enumerate(labels):
        x = xs + i * bw
        s.parts.append(f'<path class="gr" d="M{x} 82 V150"/>')
        s.t(x + bw / 2, 76, lab, "s", "middle")
    s.parts.append(f'<path class="gr" d="M{xs + 10 * bw} 82 V150"/>')
    s.parts.append(f'<path class="ao" marker-start="url(#ao)" marker-end="url(#ao)" d="M{xs} 166 L{xs + bw} 166"/>')
    s.t(xs + bw / 2, 184, "1 bit", "o b", "middle")
    s.t(10, yh - 8, "HIGH", "s")
    s.t(10, yl + 14, "LOW", "s")
    s.lines(20, 216, ["Nghỉ = HIGH; Start = LOW dài 1 bit", "Dữ liệu 5–8 bit, bit thấp (LSB) truyền trước",
                      "Parity: không/lẻ/chẵn; Stop: 1 hoặc 2 bit HIGH"], 17, "m")
    return s


def d23_2() -> S:
    s = S(400, 395, "Khung I2C ghi một byte vào thiết bị",
          "Điều kiện START: SDA xuống khi SCL cao. Sau đó 7 bit địa chỉ 0x3C là 0111100, bit R/W bằng 0 là ghi, "
          "slave kéo SDA xuống ở xung ACK, tiếp theo 8 bit dữ liệu 0xAE là 10101110 và ACK thứ hai. "
          "Điều kiện STOP: SDA lên khi SCL cao.")
    s.t(200, 24, "Khung I2C: ghi 1 byte (0xAE) vào địa chỉ 0x3C", "h", "middle")
    bw = 17
    x0 = 64
    yh_c, yl_c = 62, 94
    yh_d, yl_d = 142, 174
    addr = [0, 1, 1, 1, 1, 0, 0]
    seq = addr + [0, 0] + [1, 0, 1, 0, 1, 1, 1, 0] + [0]
    ack_slots = {8, 17}
    # ACK bands
    for k in ack_slots:
        x = x0 + k * bw
        s.parts.append(f'<rect x="{x}" y="50" width="{bw}" height="140" fill="#fef3c7"/>')
    # slot grid
    for k in range(19):
        x = x0 + k * bw
        s.parts.append(f'<path class="gr" d="M{x} 50 V190"/>')
    # SCL
    d = f"M30 {yh_c} H{x0}"
    for k in range(18):
        x = x0 + k * bw
        d += f" V{yl_c} H{x + bw / 2} V{yh_c} H{x + bw}"
    d += f" H394"
    s.parts.append(f'<path class="w" d="{d}"/>')
    # SDA
    d = f"M30 {yh_d} H{x0 - 10} V{yl_d}"
    level = 0
    for k, v in enumerate(seq):
        x = x0 + k * bw
        if v != level:
            d += f" V{yh_d if v else yl_d}"
            level = v
        d += f" H{x + bw}"
    d += f" H{x0 + 18 * bw + 4} V{yh_d} H394"
    s.parts.append(f'<path class="w" d="{d}"/>')
    s.t(4, yl_c - 8, "SCL", "b")
    s.t(4, yl_d - 8, "SDA", "b")
    for k, v in enumerate(seq):
        x = x0 + k * bw + bw / 2
        s.t(x, 204, str(v), "s", "middle")
    # markers
    def marker(x: float, num: str) -> None:
        s.parts.append(f'<circle cx="{f(x)}" cy="236" r="8" fill="#0f766e"/>')
        s.parts.append(f'<text x="{f(x)}" y="240" font-size="11" font-weight="700" text-anchor="middle" style="fill:#fff">{num}</text>')

    def bracket(xa: float, xb: float) -> None:
        s.parts.append(f'<path class="d" d="M{f(xa)} 218 V222 H{f(xb)} V218"/>')

    bracket(x0, x0 + 7 * bw)
    bracket(x0 + 7 * bw, x0 + 8 * bw)
    bracket(x0 + 8 * bw, x0 + 9 * bw)
    bracket(x0 + 9 * bw, x0 + 17 * bw)
    bracket(x0 + 17 * bw, x0 + 18 * bw)
    marker(x0 - 10, "1")
    marker(x0 + 3.5 * bw, "2")
    marker(x0 + 7.5 * bw, "3")
    marker(x0 + 8.5 * bw, "4")
    marker(x0 + 13 * bw, "5")
    marker(x0 + 17.5 * bw, "6")
    marker(x0 + 18 * bw + 14, "7")
    s.lines(14, 270, [
        "1 START: SDA xuống khi SCL ở mức cao",
        "2 Địa chỉ 7 bit 0x3C = 0111100 (bit cao trước)",
        "3 R/W = 0: ghi     4 ACK: slave kéo SDA xuống",
        "5 Dữ liệu 0xAE = 10101110     6 ACK lần hai",
        "7 STOP: SDA lên khi SCL ở mức cao",
        "NACK: SDA vẫn cao ở xung ACK → thiết bị không nhận/lỗi",
    ], 17, "m")
    return s


def d24_1() -> S:
    s = S(400, 392, "SPI: bus dùng chung và CS riêng cho từng slave",
          "Master nối MOSI, MISO, SCK dùng chung tới thẻ SD và màn TFT; các đường này không nối với nhau. "
          "Master có hai dây CS riêng: CS_SD chỉ tới thẻ SD, CS_TFT chỉ tới màn TFT, active LOW. "
          "Ba thiết bị nối GND chung.")
    s.t(200, 24, "SPI: bus chung + CS riêng", "h", "middle")
    ys = {"MOSI": 120, "MISO": 95, "SCK": 70}
    boxes = [("Master", 10, "p"), ("Thẻ SD", 150, "z"), ("Màn TFT", 290, "y")]
    pin_off = {"MOSI": 20, "MISO": 50, "SCK": 80}
    for name, bx, cls in boxes:
        s.box(bx, 190, 100, 100, cls)
        s.t(bx + 50, 244, name, "b", "middle")
        for i, (net, off) in enumerate(pin_off.items()):
            s.t(bx + off, 206 + (i % 2) * 14, net, "s", "middle")
    # bus lines: from master drop to TFT drop
    mx = {k: 10 + v for k, v in pin_off.items()}
    sx = {k: 150 + v for k, v in pin_off.items()}
    tx = {k: 290 + v for k, v in pin_off.items()}
    for net, y in ys.items():
        s.wire(f"M{mx[net]} 190 V{y} H{tx[net]} V190")
        s.dot(sx[net], y)
        s.wire(f"M{sx[net]} {y} V190")
    s.t(112, 114, "MOSI →", "m")
    s.t(112, 89, "MISO ←", "m")
    s.t(112, 64, "SCK →", "m")
    # CS lines
    s.wire("M30 290 V362 H310 V290")
    s.wire("M60 290 V337 H170 V290")
    s.t(66, 326, "CS_SD", "m")
    s.t(36, 378, "CS_TFT", "m")
    # grounds
    for gx in (90, 230, 370):
        s.t(gx, 282, "GND", "s", "middle")
        s.wire(f"M{gx} 290 V300")
        s.parts.append(f'<path class="w" d="M{gx - 12} 300 H{gx + 12} M{gx - 8} 306 H{gx + 8} M{gx - 4} 312 H{gx + 4}"/>')
    s.t(214, 330, "GND chung ở cả ba thiết bị", "m")
    return s


def d26_1() -> S:
    s = S(360, 400, "Khử rung nút nhấn bằng tụ RC",
          "VCC_logic qua R_pullup 10 kΩ tới nút GPIO. Công tắc nhấn từ nút GPIO xuống GND. Tụ 100 nF cũng "
          "nối từ nút GPIO xuống GND, song song với công tắc, đặt sát nút GPIO. GPIO ở chế độ INPUT.")
    s.t(180, 28, "Khử rung bằng RC", "h", "middle")
    s.wire("M110 50 V170 M110 170 V212 M110 262 V330 M110 170 H320 M110 330 H230")
    s.term(110, 50)
    s.t(126, 46, "VCC_logic", "b")
    s.rv(110, 80, 130)
    s.t(134, 110, "R_pullup = 10 kΩ")
    s.dot(110, 170)
    s.parts.append('<circle cx="110" cy="212" r="4.5" class="c"/><circle cx="110" cy="262" r="4.5" class="c"/>')
    s.parts.append('<path class="w" d="M110 262 L90 224"/>')
    s.t(76, 242, "Nút nhấn", "b", "end")
    s.t(76, 258, "(công tắc)", "m", "end")
    s.cap_v(230, 170, 330)
    s.dot(230, 170)
    s.t(250, 255, "C = 100 nF", "b")
    s.term(320, 170)
    s.t(320, 154, "GPIO (INPUT)", "b", "end")
    s.gnd(170, 330)
    s.t(192, 358, "GND", "m")
    s.t(180, 392, "Thả nút: τ ≈ R×C = 10 kΩ × 100 nF = 1 ms", "m", "middle")
    return s


def d28_1() -> S:
    s = S(360, 560, "Luồng xử lý: setup, loop và ISR nút nhấn",
          "Biến thể DHT22: setup chạy một lần, khởi tạo Serial, DHT22, I2C với OLED, SPI với SD, ngắt nút nhấn và bộ lập "
          "lịch millis. loop lặp mãi: mỗi 2000 ms đọc cảm biến, kiểm tra NaN, cập nhật OLED, cảnh báo nếu "
          "nhiệt độ trên 35; mỗi 10000 ms ghi SD; nếu cờ nút nhấn đặt thì in tóm tắt. ISR chỉ đặt cờ.")
    s.t(180, 26, "Luồng xử lý của chương trình", "h", "middle")
    s.box(15, 42, 330, 130, "p")
    s.t(25, 62, "setup()  (chạy 1 lần)", "b")
    s.lines(25, 84, ["• Serial.begin(115200)", "• DHT22 + OLED I2C: begin()", "• SPI: SD.begin()",
                     "• attachInterrupt(btnPin, onBtn, FALLING)", "• Khởi tạo timer hoặc lịch millis()"], 18, "m")
    s.arrow(180, 172, 180, 206)
    s.box(15, 208, 330, 200, "z")
    s.t(25, 228, "loop()  (lặp mãi)", "b")
    s.lines(25, 250, ["• Mỗi 2000 ms: đọc DHT22", "     – Kiểm tra NaN, bỏ mẫu lỗi",
                      "     – Cập nhật OLED", "     – Nếu nhiệt độ > 35: LED ON + buzzer",
                      "• Mỗi 10000 ms: ghi SD: millis,temp,humi", "• Nếu btnFlag = true: in tóm tắt qua Serial"], 18, "m")
    s.box(15, 452, 330, 78, "y")
    s.t(25, 474, "ISR onBtn()  (ngắt nút nhấn)", "b")
    s.lines(25, 496, ["• btnFlag = true  (chỉ đặt cờ)", "• Không xử lý nặng trong ISR"], 18, "m")
    s.parts.append('<path class="ao" stroke-dasharray="6 4" marker-end="url(#ao)" d="M300 452 L300 410"/>')
    s.t(292, 436, "cờ btnFlag", "o b", "end")
    return s


def d30_1() -> S:
    s = S(360, 380, "Màn hình oscilloscope: trục, ô chia và trigger",
          "Màn hình lưới 8 ô ngang và 6 ô dọc. Trục dọc là điện áp, mỗi ô bằng giá trị VOLTS/DIV; trục ngang "
          "là thời gian, mỗi ô bằng TIME/DIV. Đường đứt ngang là mức trigger; điểm tròn là chỗ sóng cắt mức "
          "này khi đi lên và được căn ở giữa màn hình.")
    s.t(180, 26, "Màn hình oscilloscope", "h", "middle")
    x0, y0, cell = 20, 46, 40
    s.parts.append(f'<rect x="{x0}" y="{y0}" width="320" height="240" fill="#0f172a" stroke="#475569" stroke-width="2"/>')
    for i in range(1, 8):
        s.parts.append(f'<path d="M{x0 + i * cell} {y0} V{y0 + 240}" stroke="#334155" stroke-width="{2 if i == 4 else 1}"/>')
    for j in range(1, 6):
        s.parts.append(f'<path d="M{x0} {y0 + j * cell} H{x0 + 320}" stroke="#334155" stroke-width="{2 if j == 3 else 1}"/>')
    cy = y0 + 120
    pts = []
    for px in range(0, 321, 4):
        phase = math.pi / 6 + 2 * math.pi * (px - 160) / 160
        pts.append(f"{x0 + px},{cy - 70 * math.sin(phase):.1f}")
    s.parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#4ade80" stroke-width="2.5" stroke-linejoin="round"/>')
    ty = cy - 35
    s.parts.append(f'<path d="M{x0} {ty} H{x0 + 320}" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="6 4"/>')
    s.parts.append(f'<circle cx="{x0 + 160}" cy="{ty}" r="5" fill="none" stroke="#fbbf24" stroke-width="2"/>')
    s.parts.append(f'<text x="{x0 + 6}" y="{ty - 5}" font-size="11" style="fill:#fbbf24">mức trigger</text>')
    s.parts.append(f'<text x="{x0 + 6}" y="{cy + 14}" font-size="11" style="fill:#cbd5e1">0 V (GND)</text>')
    s.parts.append(f'<path d="M{x0 + 200} {y0 + 252} H{x0 + 240}" stroke="#0f766e" stroke-width="2.5" marker-start="url(#ah)" marker-end="url(#ah)"/>')
    s.t(x0 + 220, y0 + 268, "1 ô = TIME/DIV", "g b", "middle")
    s.parts.append(f'<path d="M{x0 + 330} {y0 + 80} V{y0 + 120}" stroke="#0f766e" stroke-width="2.5" marker-start="url(#ah)" marker-end="url(#ah)"/>')
    s.lines(14, 334, ["Trục dọc: điện áp, 1 ô = VOLTS/DIV (mũi tên bên phải)", "Trục ngang: thời gian; sóng căn theo điểm trigger ở giữa"], 17, "m")
    return s


def d31_1() -> S:
    s = S(400, 300, "Bộ lọc RC thông thấp và thông cao",
          "Thông thấp: Vin qua R nối tiếp tới Vout, tụ C từ Vout xuống GND. Thông cao: Vin qua tụ C nối tiếp "
          "tới Vout, điện trở R từ Vout xuống GND.")
    s.t(95, 30, "LPF (thông thấp)", "b", "middle")
    s.t(300, 30, "HPF (thông cao)", "b", "middle")
    s.wire("M20 90 H55 M110 90 H175 M220 90 H250 M300 90 H370 M335 90 V200")
    s.term(20, 90)
    s.t(20, 72, "Vin", "b")
    s.rh(55, 110, 90)
    s.t(82, 95, "R", "b", "middle")
    s.dot(150, 90)
    s.cap_v(150, 90, 200)
    s.t(172, 150, "C", "b")
    s.gnd(150, 200)
    s.term(175, 90)
    s.t(175, 72, "Vout", "b", "end")
    s.term(220, 90)
    s.t(220, 72, "Vin", "b")
    s.cap_h(250, 300, 90)
    s.t(275, 66, "C", "b", "middle")
    s.dot(335, 90)
    s.rv(335, 120, 170)
    s.t(357, 150, "R", "b")
    s.gnd(335, 200)
    s.term(370, 90)
    s.t(370, 72, "Vout", "b", "end")
    s.lines(15, 252, ["f thấp: X_C lớn → Vout ≈ Vin", "f cao: X_C nhỏ → Vout giảm"], 17, "m")
    s.lines(215, 252, ["f cao: X_C nhỏ → Vout ≈ Vin", "f thấp: X_C lớn → Vout giảm"], 17, "m")
    s.t(200, 290, "Cả hai: f_c = 1/(2πRC)", "b", "middle")
    return s


def d31_2() -> S:
    s = S(400, 345, "Bộ lọc thông dải: HPF rồi LPF",
          "Vin qua C1 nối tiếp tới nút 1; R1 từ nút 1 xuống GND tạo HPF. Từ nút 1 qua R2 nối tiếp tới nút 2 "
          "là Vout; C2 từ nút 2 xuống GND tạo LPF.")
    s.t(200, 24, "Thông dải = HPF (C1, R1) + LPF (R2, C2)", "h", "middle")
    s.parts.append('<rect x="38" y="52" width="112" height="210" rx="10" class="d" fill="none"/>')
    s.parts.append('<rect x="160" y="52" width="150" height="210" rx="10" class="d" fill="none"/>')
    s.t(94, 70, "HPF", "o b", "middle")
    s.t(235, 70, "LPF", "o b", "middle")
    s.wire("M20 110 H50 M100 110 H220 M130 110 V150 M130 200 V235 M220 110 H280 M280 110 H350")
    s.term(20, 110)
    s.t(20, 92, "Vin", "b")
    s.cap_h(50, 100, 110)
    s.t(75, 86, "C1", "b", "middle")
    s.dot(130, 110)
    s.rv(130, 150, 200)
    s.t(146, 180, "R1", "b")
    s.gnd(130, 235)
    s.rh(165, 220, 110)
    s.t(192, 115, "R2", "b", "middle")
    s.dot(280, 110)
    s.cap_v(280, 110, 235)
    s.t(298, 175, "C2", "b")
    s.term(350, 110)
    s.t(350, 92, "Vout", "b", "end")
    s.gnd(280, 235)
    s.t(200, 292, "f_cH ≈ 1/(2πR1C1) < f_cL ≈ 1/(2πR2C2)", "b", "middle")
    s.t(200, 312, "Hai tầng RC tương tác tải: công thức chỉ gần đúng", "m", "middle")
    s.t(200, 332, "Băng thông ≈ f_cL − f_cH", "m", "middle")
    return s


def d37_1() -> S:
    s = S(400, 470, "Kiến trúc MQTT: publish, broker và subscribe",
          "ESP32 publish nhiệt độ lên topic home/room1/temperature tới broker; broker chuyển tin cho "
          "Dashboard/App đã subscribe. Thiết bị điều khiển publish lệnh lên home/room1/led/cmd; broker "
          "chuyển tin cho ESP32 đã subscribe topic đó.")
    s.t(200, 26, "MQTT: mọi tin đi qua broker", "h", "middle")
    s.boxed(10, 150, 90, 100, ["ESP32 /", "cảm biến"], "p")
    s.boxed(155, 150, 90, 100, ["MQTT", "Broker"], "y")
    s.boxed(300, 60, 90, 70, ["Dashboard", "/ App"], "z")
    s.boxed(300, 270, 90, 70, ["Điều khiển", "(app/web)"], "z")
    s.arrow(100, 185, 155, 185)
    s.arrow(155, 220, 100, 220, "ao")
    s.arrow(245, 170, 300, 115)
    s.arrow(300, 295, 245, 230, "ao")

    def num(x: float, y: float, n: str) -> None:
        s.parts.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="9" fill="#0f766e"/>')
        s.parts.append(f'<text x="{f(x)}" y="{f(y + 4)}" font-size="12" font-weight="700" text-anchor="middle" style="fill:#fff">{n}</text>')

    num(127, 172, "1")
    num(272, 128, "2")
    num(272, 278, "3")
    num(127, 234, "4")
    s.lines(14, 368, [
        "1 ESP32 publish home/room1/temperature = 25.3",
        "2 Broker chuyển tin cho Dashboard/App đã subscribe",
        "3 Điều khiển publish home/room1/led/cmd = ON/OFF",
        "4 Broker → ESP32 đã subscribe topic",
        "   home/room1/led/cmd",
        "Mũi tên chỉ hướng tin; đăng ký topic trước",
    ], 18, "m")
    return s


def d42_1() -> S:
    s = S(400, 720, "Hệ thống robot WiFi: nguồn và tín hiệu",
          "Phần A: USB 5 V qua TP4056 sạc cell LiPo 1S có mạch bảo vệ; pin qua boost 5 V cấp cho ESP32, "
          "VM của TB6612FNG và motor, HC-SR04 và servo; ESP32 3,3 V cấp VCC của TB6612FNG; GND nối chung. "
          "Phần B: ESP32 điều khiển TB6612FNG bằng AIN, BIN, PWM và STBY; TRIG tới HC-SR04 còn ECHO qua chia "
          "áp 10k/15k về GPIO; servo SG90; OLED SSD1306 qua I2C; pin 1S qua chia áp 100k/100k vào ADC34.")
    s.t(200, 24, "A. Cấp nguồn", "h", "middle")
    chain = [("USB 5 V", 40, 75), ("TP4056 (sạc)", 100, 140), ("LiPo 1S +", 165, 215), ("Boost 5 V", 240, 280)]
    s.boxed(10, 40, 125, 36, ["USB 5 V"], "p")
    s.boxed(10, 100, 125, 40, ["TP4056 (sạc)"], "p")
    s.boxed(10, 164, 125, 52, ["Cell LiPo 1S", "+ mạch bảo vệ 1S"], "p")
    s.boxed(10, 240, 125, 40, ["Boost 5 V"], "y")
    s.arrow(72, 76, 72, 99)
    s.arrow(72, 140, 72, 163)
    s.arrow(72, 216, 72, 239)
    s.t(80, 94, "khi sạc", "s")
    s.wire("M135 260 H185 M185 80 V260")
    s.dot(185, 260)
    loads = [(80, ["ESP32", "chân 5V"]), (140, ["TB6612FNG VM", "+ motor"]), (200, ["HC-SR04", "VCC"]), (260, ["Servo SG90", "nguồn"])]
    for y, items in loads:
        s.wire(f"M185 {y} H225")
        s.boxed(225, y - 24, 165, 48, items, "z", first_bold=True, dy=16)
    s.t(160, 252, "5 V", "b", "end")
    s.lines(14, 306, ["ESP32 3,3 V → VCC của TB6612FNG; mọi GND nối chung", "USB 5 V → TP4056 → cell 1S khi sạc; kiểm tra power-path",
                      "nếu vừa sạc vừa chạy"], 16, "m")

    s.t(200, 384, "B. Tín hiệu", "h", "middle")
    s.boxed(150, 400, 80, 290, ["ESP32", "Web Server", "cổng 80"], "p")
    s.boxed(5, 440, 105, 70, ["Pin 1S", "chia áp", "100k/100k"], "y", dy=16)
    s.arrow(110, 475, 150, 475)
    s.t(112, 466, "ADC34", "s")
    right = [
        (400, 100, ["TB6612FNG", "AIN1/2, BIN1/2", "PWMA/B, STBY=HIGH", "→ motor A/B"], True),
        (515, 76, ["HC-SR04", "TRIG ← GPIO", "ECHO → chia áp", "10k/15k → GPIO"], False),
        (605, 36, ["SG90: SERVO_PIN"], True),
        (655, 50, ["SSD1306 OLED", "I2C: SDA, SCL"], False),
    ]
    for y, h, items, one in right:
        s.boxed(285, y, 110, h, items, "z", dy=16)
        cy = y + h / 2
        s.parts.append(f'<path class="a" d="M230 {f(cy)} L285 {f(cy)}" marker-end="url(#ah)"' + ('' if one else ' marker-start="url(#ah)"') + '/>')
    return s


def d51_1() -> S:
    s = S(400, 290, "Vòng điều khiển PID",
          "Setpoint r vào bộ cộng với dấu cộng; từ đó trừ giá trị đo. Sai số e vào bộ PID; PID cho u, "
          "ví dụ PWM, vào khối driver, heater và lò. Đầu ra y là nhiệt độ lò, cảm biến nhiệt đo y và đưa "
          "về bộ cộng với dấu trừ.")
    s.t(200, 26, "Vòng điều khiển PID", "h", "middle")
    s.parts.append('<circle cx="62" cy="100" r="17" class="c"/>')
    s.t(62, 105, "Σ", "b", "middle")
    s.t(38, 88, "+", "b")
    s.t(70, 135, "−", "b")
    s.arrow(14, 100, 44, 100)
    s.t(14, 86, "r (setpoint)", "b")
    s.arrow(79, 100, 108, 100)
    s.t(93, 88, "e", "b", "middle")
    s.boxed(110, 75, 70, 50, ["PID"], "p")
    s.arrow(180, 100, 212, 100)
    s.t(196, 88, "u", "b", "middle")
    s.t(196, 120, "PWM", "s", "middle")
    s.boxed(214, 65, 120, 70, ["Driver +", "heater + lò"], "y")
    s.arrow(334, 100, 380, 100)
    s.t(360, 86, "y (°C)", "b", "middle")
    s.wire("M358 100 V210 M358 210 H300")
    s.dot(358, 100)
    s.arrow(358, 210, 300, 210)
    s.boxed(150, 188, 150, 44, ["Cảm biến nhiệt"], "z")
    s.wire("M150 210 H62 V117")
    s.arrow(62, 160, 62, 119)
    s.t(200, 262, "e = r − (giá trị đo của cảm biến)", "b", "middle")
    s.t(200, 280, "y là đầu ra của quá trình, không phải u", "m", "middle")
    return s


BUILDERS_2 = {
    "d22-1": d22_1, "d22-2": d22_2, "d23-2": d23_2, "d24-1": d24_1, "d26-1": d26_1,
    "d28-1": d28_1, "d30-1": d30_1, "d31-1": d31_1, "d31-2": d31_2, "d37-1": d37_1,
    "d42-1": d42_1, "d51-1": d51_1,
}
