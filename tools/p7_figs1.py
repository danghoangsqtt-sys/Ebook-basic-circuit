"""P7-04 figure builders, part 1: DC circuits, capacitor, diode, PWM, comparator."""

from __future__ import annotations

import math

from p7_svg import S


def d06_1() -> S:
    s = S(360, 430, "KVL: nguồn 5 V nối tiếp R1, R2, R3",
          "Nguồn 5 V nối tiếp R1 = 1 kΩ, R2 = 2 kΩ, R3 = 2 kΩ rồi về GND. Dòng một nhánh 1 mA; "
          "sụt áp 1 V, 2 V, 2 V; 5 − 1 − 2 − 2 = 0.")
    s.t(180, 28, "KVL: vòng nối tiếp 5 V", "h", "middle")
    s.wire("M70 70 H250 V370 H70")
    s.bat_v(70, 70, 370)
    for y1, y2, name, val, vd in [(95, 145, "R1", "1 kΩ", "1 V"), (175, 225, "R2", "2 kΩ", "2 V"),
                                  (255, 305, "R3", "2 kΩ", "2 V")]:
        s.rv(250, y1, y2)
        s.t(272, (y1 + y2) / 2 - 2, f"{name} = {val}")
        s.t(272, (y1 + y2) / 2 + 16, f"sụt áp {vd}", "g b")
    s.t(18, 226, "5 V", "b")
    s.t(236, 84, "5 V", "m", "end")
    s.t(236, 165, "4 V", "m", "end")
    s.t(236, 245, "2 V", "m", "end")
    s.t(236, 335, "0 V", "m", "end")
    s.gnd(70, 370)
    s.t(92, 392, "GND = 0 V", "m")
    s.arrow(105, 70, 175, 70)
    s.t(140, 56, "I = 1 mA", "b", "middle")
    s.t(180, 418, "KVL: 5 − 1 − 2 − 2 = 0", "b", "middle")
    return s


def d06_2() -> S:
    s = S(360, 330, "KCL tại nút A",
          "Dòng I1 = 5 mA đi vào nút A. Hai dòng đi ra: I2 = 3 mA xuống dưới và I3 đi sang phải. "
          "KCL cho I3 = 5 − 3 = 2 mA.")
    s.t(180, 28, "KCL tại nút A", "h", "middle")
    s.wire("M20 130 H340 M180 130 V285")
    s.term(20, 130)
    s.term(340, 130)
    s.term(180, 285)
    s.dot(180, 130)
    s.t(192, 118, "A", "b")
    s.arrow(55, 130, 125, 130)
    s.t(90, 112, "I1 = 5 mA", "b", "middle")
    s.t(90, 156, "đi vào A", "m", "middle")
    s.arrow(180, 165, 180, 235, "ao")
    s.t(194, 205, "I2 = 3 mA", "b")
    s.t(194, 223, "đi ra", "m")
    s.arrow(225, 130, 295, 130, "ao")
    s.t(262, 112, "I3 = 2 mA", "b", "middle")
    s.t(262, 156, "đi ra", "m", "middle")
    s.t(180, 312, "KCL: I1 = I2 + I3 → 5 = 3 + 2 mA", "b", "middle")
    return s


def d06_3() -> S:
    s = S(360, 410, "Cầu chia áp cơ bản",
          "VCC nối tiếp R1 rồi R2 xuống GND. Điểm giữa R1 và R2 là Vout, đo so với GND.")
    s.t(180, 28, "Cầu chia áp cơ bản", "h", "middle")
    s.wire("M130 60 V350 M130 195 H260")
    s.term(130, 60)
    s.t(146, 56, "VCC", "b")
    s.rv(130, 90, 140)
    s.t(158, 120, "R1")
    s.dot(130, 195)
    s.term(260, 195)
    s.t(272, 199, "Vout", "b")
    s.rv(130, 235, 285)
    s.t(158, 265, "R2")
    s.gnd(130, 350)
    s.t(152, 366, "GND", "m")
    s.t(180, 398, "Đo Vout so với GND", "m", "middle")
    return s


def d06_4() -> S:
    s = S(360, 420, "Cầu chia áp có tải R_load",
          "VCC qua R1 = 10 kΩ tới Vout. Từ Vout xuống GND có R2 = 10 kΩ song song với R_load.")
    s.t(180, 28, "Cầu chia áp có tải", "h", "middle")
    s.wire("M120 60 V340 M120 200 H70 M120 200 H250 V340 M250 340 H120")
    s.term(120, 60)
    s.t(136, 56, "VCC", "b")
    s.rv(120, 90, 140)
    s.t(148, 120, "R1 = 10 kΩ")
    s.dot(120, 200)
    s.term(70, 200)
    s.t(60, 204, "Vout", "b", "end")
    s.rv(120, 245, 295)
    s.t(148, 275, "R2 = 10 kΩ")
    s.rv(250, 245, 295)
    s.t(270, 275, "R_load")
    s.dot(250, 200)
    s.gnd(185, 340)
    s.t(205, 362, "GND", "m")
    s.t(180, 400, "R_load song song R2 → Vout giảm", "m", "middle")
    return s


def d06_5() -> S:
    s = S(360, 420, "Cầu chia áp LDR cho ADC",
          "3,3 V qua R_fixed 10 kΩ tới nút Vout, rồi LDR xuống GND. Vout đi tới đầu vào ADC của ESP32. "
          "Trời sáng R_LDR nhỏ nên Vout thấp.")
    s.t(180, 28, "Cầu chia áp LDR", "h", "middle")
    s.wire("M120 60 V350 M120 195 H250")
    s.term(120, 60)
    s.t(136, 56, "VCC = 3,3 V", "b")
    s.rv(120, 90, 140)
    s.t(148, 120, "R_fixed = 10 kΩ")
    s.dot(120, 195)
    s.term(250, 195)
    s.t(262, 192, "Vout", "b")
    s.t(262, 210, "→ ADC ESP32", "m")
    s.rv(120, 240, 290)
    s.t(100, 270, "LDR", "b", "end")
    s.arrow(205, 232, 150, 255, "ao")
    s.arrow(210, 252, 150, 275, "ao")
    s.t(214, 240, "ánh sáng", "m")
    s.gnd(120, 350)
    s.t(142, 372, "GND", "m")
    s.t(180, 408, "Sáng: R_LDR nhỏ → Vout thấp", "m", "middle")
    return s


def d08_1() -> S:
    s = S(360, 280, "Cấu tạo cơ bản của tụ điện",
          "Hai bản cực dẫn điện ngăn cách bởi lớp điện môi cách điện. Bản trên tích điện dương, bản dưới "
          "tích điện âm; điện trường E hướng từ bản dương sang bản âm trong điện môi.")
    s.t(180, 28, "Cấu tạo tụ điện", "h", "middle")
    s.wire("M130 70 V42 M130 190 V222")
    s.term(130, 42)
    s.term(130, 222)
    s.t(142, 46, "đầu A", "m")
    s.t(142, 230, "đầu B", "m")
    s.parts.append('<rect x="40" y="70" width="180" height="20" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>')
    s.parts.append('<rect x="40" y="90" width="180" height="80" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>')
    s.parts.append('<rect x="40" y="170" width="180" height="20" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>')
    for x in range(60, 221, 30):
        s.t(x, 85, "+", "b", "middle")
        s.t(x, 185, "−", "b", "middle")
    for x in (70, 190):
        s.arrow(x, 98, x, 162)
    s.t(130, 134, "E", "b", "middle")
    s.t(130, 152, "(điện trường)", "s", "middle")
    s.t(232, 84, "Bản cực 1", "b")
    s.t(232, 100, "(dẫn điện)", "m")
    s.t(232, 124, "Điện môi", "b")
    s.t(232, 140, "cách điện: không khí,", "m")
    s.t(232, 156, "gốm, oxit…", "m")
    s.t(232, 184, "Bản cực 2", "b")
    s.t(232, 200, "(dẫn điện)", "m")
    s.t(180, 268, "Điện tích dồn vào hai bản khi có điện áp", "m", "middle")
    return s


def d08_2() -> S:
    s = S(400, 370, "Nhận dạng tụ hóa 100 µF 25 V",
          "Thân tụ trụ có dải trắng với dấu trừ ở phía cực âm. Chân ngắn là cực âm, chân dài là cực dương "
          "khi chân chưa bị cắt. Thân ghi 100 µF và 25 V là điện áp định mức tối đa.")
    s.t(200, 28, "Tụ hóa 100 µF / 25 V", "h", "middle")
    s.parts.append('<rect x="150" y="50" width="120" height="140" rx="10" fill="#1e293b" stroke="#0f172a" stroke-width="2"/>')
    s.parts.append('<path d="M160 50 H176 V190 H160 Q150 190 150 180 V60 Q150 50 160 50 Z" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>')
    for y in (88, 125, 162):
        s.t(163, y + 6, "−", "b", "middle")
    s.parts.append('<text x="224" y="110" fill="#fff" font-size="17" font-weight="700" text-anchor="middle" style="fill:#fff">100 µF</text>')
    s.parts.append('<text x="224" y="134" fill="#fff" font-size="15" text-anchor="middle" style="fill:#fff">25 V</text>')
    s.parts.append('<path d="M163 190 V240 M257 190 V300" stroke="#64748b" stroke-width="4" stroke-linecap="round"/>')
    s.t(163, 262, "chân NGẮN", "b", "middle")
    s.t(163, 278, "cực ÂM (−)", "m", "middle")
    s.t(257, 322, "chân DÀI", "b", "middle")
    s.t(257, 338, "cực DƯƠNG (+)", "m", "middle")
    s.lines(138, 92, ["Dải trắng + dấu −", "là cực ÂM (−)"], 16, "m", "end")
    s.lines(282, 92, ["100 µF: điện dung"], 16, "m")
    s.lines(282, 130, ["25 V: áp định mức", "tối đa, không vượt"], 16, "m")
    s.t(200, 362, "Chân đã cắt: tin dải trắng/dấu −", "o b", "middle")
    return s


def d08_3() -> S:
    s = S(360, 330, "Vị trí tụ tách nguồn 100 nF",
          "Tụ 100 nF nối giữa ray VCC và ray GND, đặt sát chân VCC và GND của IC. Chân VCC và GND của IC "
          "lấy từ hai ray này.")
    s.t(180, 28, "Tụ tách nguồn đặt sát IC", "h", "middle")
    s.wire("M30 100 H275 V135 M30 250 H275 V215")
    s.term(30, 100)
    s.t(30, 86, "VCC", "b")
    s.t(30, 242, "GND", "b")
    s.cap_v(170, 100, 250)
    s.dot(170, 100)
    s.dot(170, 250)
    s.t(150, 180, "C = 100 nF", "b", "end")
    s.box(230, 135, 90, 80, "p")
    s.t(275, 168, "IC", "b", "middle")
    s.t(275, 152, "VCC", "s", "middle")
    s.t(275, 207, "GND", "s", "middle")
    s.parts.append('<path class="ao" marker-start="url(#ao)" marker-end="url(#ao)" d="M174 68 L271 68"/>')
    s.t(222, 56, "sát chân IC", "o b", "middle")
    s.t(180, 300, "Vòng tụ → chân VCC → IC → chân GND càng ngắn càng tốt", "m", "middle")
    return s


def d09_1() -> S:
    s = S(360, 320, "Mạch RC nạp tụ",
          "Nguồn 5 V, công tắc S và R = 100 kΩ nối tiếp tới nút V_C. Duy nhất một tụ C = 100 µF nối từ nút "
          "V_C xuống GND; V_C đo so với GND.")
    s.t(180, 28, "Mạch RC nạp tụ", "h", "middle")
    s.wire("M50 80 H75 M135 80 H170 M230 80 H335 M50 240 H285 M285 240 V240")
    s.bat_v(50, 80, 240)
    s.t(30, 166, "5 V", "b", "end")
    s.parts.append('<circle cx="75" cy="80" r="4" class="c"/><circle cx="135" cy="80" r="4" class="c"/>')
    s.parts.append('<path class="w" d="M75 80 L125 60"/>')
    s.t(105, 50, "S", "b", "middle")
    s.rh(170, 230, 80)
    s.t(200, 54, "R = 100 kΩ", "b", "middle")
    s.dot(285, 80)
    s.cap_v(285, 80, 240)
    s.t(260, 166, "C = 100 µF", "b", "end")
    s.term(335, 80)
    s.t(335, 64, "V_C", "b", "end")
    s.gnd(180, 240)
    s.t(202, 266, "GND = 0 V", "m")
    s.t(180, 304, "Một nhánh duy nhất xuống GND qua tụ", "m", "middle")
    return s


def d11_1() -> S:
    s = S(360, 340, "Cấu tạo và ký hiệu diode",
          "Cấu trúc P-N có vùng nghèo giữa hai bán dẫn; cực A nối phía P, cực K nối phía N. Ký hiệu mạch là "
          "tam giác hướng từ A sang K với vạch đứng ở phía K. Dòng quy ước đi từ A sang K khi phân cực thuận.")
    s.t(180, 28, "Cấu tạo diode và ký hiệu", "h", "middle")
    s.wire("M40 100 H18 M300 100 H342")
    s.term(18, 100)
    s.term(342, 100)
    s.t(18, 82, "A", "b")
    s.t(342, 82, "K", "b", "end")
    s.parts.append('<rect x="40" y="65" width="100" height="70" fill="#fee2e2" stroke="#b91c1c" stroke-width="2"/>')
    s.parts.append('<rect x="140" y="65" width="60" height="70" fill="#e2e8f0" stroke="#64748b" stroke-width="2" stroke-dasharray="4 3"/>')
    s.parts.append('<rect x="200" y="65" width="100" height="70" fill="#dbeafe" stroke="#1e40af" stroke-width="2"/>')
    s.t(90, 108, "P", "h", "middle")
    s.t(250, 108, "N", "h", "middle")
    s.t(170, 156, "vùng nghèo", "m", "middle")
    s.t(170, 172, "(rào thế)", "m", "middle")
    s.wire("M30 250 H130 M180 250 H330")
    s.parts.append('<path d="M130 232 V268 L180 250 Z" fill="#fff" stroke="#334155" stroke-width="2.5" stroke-linejoin="round"/>')
    s.parts.append('<path class="w" d="M180 232 V268"/>')
    s.t(30, 226, "A (anode)", "b")
    s.t(330, 226, "K (cathode)", "b", "end")
    s.arrow(55, 288, 125, 288)
    s.t(180, 292, "dòng quy ước A → K", "m")
    s.t(180, 318, "Vạch đứng ở phía K (cathode)", "m", "middle")
    return s


def d19_1() -> S:
    s = S(360, 390, "PWM với ba độ rộng xung",
          "Ba dạng sóng vuông cùng chu kỳ T = 8 ô thời gian. Duty 25% có điện áp trung bình 1,25 V, duty 50% "
          "có 2,50 V, duty 75% có 3,75 V ở mức 5 V.")
    s.t(180, 28, "PWM: ba độ rộng xung (mức 5 V)", "h", "middle")
    cell = 16
    x0 = 90
    s.parts.append(f'<path class="ao" marker-start="url(#ao)" marker-end="url(#ao)" d="M{x0} 58 L{x0 + 8 * cell} 58"/>')
    s.t(x0 + 4 * cell, 48, "chu kỳ T = 8 ô", "o b", "middle")
    for i, (hi, pct, vavg) in enumerate([(2, "25%", "1,25 V"), (4, "50%", "2,50 V"), (6, "75%", "3,75 V")]):
        yh = 90 + i * 100
        yl = yh + 40
        d = f"M{x0} {yl}"
        for p in range(2):
            xs = x0 + p * 8 * cell
            d += f" V{yh} H{xs + hi * cell} V{yl} H{xs + 8 * cell}"
        s.parts.append(f'<path class="w" d="{d}"/>')
        s.t(8, yh + 26, f"Duty {pct}", "b")
        s.t(x0 - 8, yh + 5, "5 V", "m", "end")
        s.t(x0 - 8, yl + 5, "0 V", "m", "end")
        s.t(x0 + 8 * cell, yl + 26, f"V_avg = {vavg}", "g b", "middle")
    s.t(180, 384, "D = T_on / T × 100%", "b", "middle")
    return s


def d19_2() -> S:
    s = S(360, 290, "PWM qua bộ lọc RC thành điện áp tương tự",
          "Chân GPIO_PWM qua R = 10 kΩ tới nút V_analog_out; tụ C = 100 nF nối từ nút đó xuống GND. "
          "Tần số PWM 10 kHz lớn hơn nhiều tần số cắt khoảng 159 Hz nên gợn sóng bị lọc.")
    s.t(180, 28, "PWM → RC → điện áp tương tự", "h", "middle")
    s.wire("M30 100 H70 M140 100 H330")
    s.term(30, 100)
    s.t(30, 80, "GPIO_PWM", "b")
    s.rh(70, 140, 100)
    s.t(105, 105, "10 kΩ", "b", "middle")
    s.dot(250, 100)
    s.cap_v(250, 100, 200)
    s.t(272, 155, "C = 100 nF", "b")
    s.term(330, 100)
    s.t(330, 80, "V_analog_out", "b", "end")
    s.gnd(250, 200)
    s.t(180, 258, "f_c = 1/(2πRC) ≈ 159 Hz", "b", "middle")
    s.t(180, 278, "f_PWM = 10 kHz ≫ f_c → gợn sóng nhỏ", "m", "middle")
    return s


def d21_1() -> S:
    s = S(360, 420, "Phân áp NTC và bộ so sánh LM358",
          "3,3 V qua R_ref 10 kΩ tới nút V_sensor, rồi NTC 10 kΩ xuống GND. V_sensor vào đầu vào đảo của "
          "LM358. Một biến trở cho V_ref vào đầu vào không đảo. Nóng thì NTC nhỏ, V_sensor nhỏ hơn V_ref "
          "và ngõ ra lên HIGH.")
    s.t(180, 28, "NTC + R_ref → bộ so sánh", "h", "middle")
    s.wire("M60 50 V310 M60 170 H225 M170 225 V340 M183 262 H225 M335 215 H350")
    s.term(60, 50)
    s.t(76, 46, "VCC = 3,3 V", "b")
    s.rv(60, 80, 130)
    s.t(84, 110, "R_ref 10 kΩ", "m")
    s.dot(60, 170)
    s.t(66, 160, "V_sensor", "b")
    s.rv(60, 200, 250)
    s.t(84, 222, "NTC 10 kΩ", "m")
    s.t(84, 238, "t° ↑ → R ↓", "m")
    s.gnd(60, 310)
    s.term(170, 225)
    s.t(182, 229, "VCC", "m")
    s.rv(170, 240, 290)
    s.parts.append('<path class="ao" marker-start="url(#ao)" d="M183 262 L215 262"/>')
    s.t(188, 254, "V_ref", "b")
    s.t(150, 270, "biến trở", "m", "end")
    s.gnd(170, 340)
    s.parts.append('<path d="M225 140 L225 290 L335 215 Z" fill="#dbeafe" stroke="#1e40af" stroke-width="2"/>')
    s.t(232, 176, "−", "b")
    s.t(232, 268, "+", "b")
    s.t(284, 220, "LM358", "b", "middle")
    s.t(280, 125, "cấp 5 V", "m", "middle")
    s.t(345, 200, "OUT", "b", "end")
    s.term(350, 215)
    s.t(345, 320, "OUT = HIGH khi nóng", "g b", "end")
    s.t(345, 338, "(V_sensor < V_ref)", "m", "end")
    s.t(180, 402, "Giữ cả hai đầu vào trong miền common-mode của LM358", "m", "middle")
    return s


def npn(s: S, bx: float, cy: float, cx: float) -> None:
    """NPN: base bar at x=bx, collector goes up-right to (cx, cy-25), emitter down-right to (cx, cy+25)."""
    s.parts.append(f'<path class="k" d="M{bx} {cy - 20} V{cy + 20}"/>')
    s.parts.append(f'<path class="w" d="M{bx} {cy - 10} L{cx} {cy - 28}"/>')
    s.parts.append(f'<path class="w" marker-end="url(#ad)" d="M{bx} {cy + 10} L{cx} {cy + 28}"/>')


def d21_2() -> S:
    s = S(360, 610, "Hệ thống báo nhiệt tự động: relay, LED đỏ và tiếp điểm",
          "Ba khối riêng. A: ngõ ra OUT qua R_B 1 kΩ vào chân B của BC337, emitter nối GND, collector nối cuộn "
          "relay lên +5 V, diode 1N4007 ngược song song cuộn (cathode +5 V, anode phía collector). "
          "B: LED đỏ từ OUT qua R 2,2 kΩ xuống GND báo nhiệt cao; khi OUT thấp, LED tắt. "
          "C: tiếp điểm COM–NO của relay đóng cắt nguồn 12 V riêng của quạt.")
    s.t(20, 24, "A. Tầng relay (BC337)", "b")
    s.wire("M240 50 H290 M240 70 V50 M290 50 V80 M290 125 V150 H240 M240 115 V187 M30 215 H205 M240 243 V282")
    s.t(248, 40, "+5 V", "b")
    s.term(240, 50)
    s.rv(240, 70, 115)
    s.t(222, 88, "Cuộn relay", "m", "end")
    s.t(222, 104, "≤ 25 mA", "m", "end")
    s.diode_v(290, 80, 125, up=True)
    s.t(306, 106, "1N4007", "m")
    s.dot(240, 150)
    npn(s, 205, 215, 240)
    s.t(120, 255, "BC337", "b", "middle")
    s.t(120, 271, "(NPN)", "m", "middle")
    s.t(188, 207, "B", "s", "end")
    s.t(247, 182, "C", "s")
    s.t(247, 250, "E", "s")
    s.term(30, 215)
    s.t(30, 197, "OUT", "b")
    s.rh(60, 115, 215)
    s.t(88, 233 + 8, "R_B 1 kΩ", "m", "middle")
    s.gnd(240, 282)

    s.t(20, 346, "B. LED đỏ chỉ thị nhiệt cao", "b")
    s.wire("M30 390 H70 M125 390 H170 M215 390 H255")
    s.term(30, 390)
    s.t(30, 374, "OUT", "b")
    s.rh(70, 125, 390)
    s.t(97, 395, "2,2 kΩ", "s", "middle")
    s.diode_h(170, 215, 390, led=True)
    s.gnd(255, 390)
    s.t(30, 424, "Đỏ sáng khi nóng; tắt khi OUT thấp", "m")

    s.t(20, 466, "C. Tiếp điểm relay: nguồn quạt 12 V riêng", "b")
    s.wire("M30 520 H80 M150 520 H205 M257 520 H300")
    s.term(30, 520)
    s.t(30, 502, "+12 V riêng", "b")
    s.parts.append('<circle cx="80" cy="520" r="4.5" class="c"/><circle cx="150" cy="520" r="4.5" class="c"/>')
    s.parts.append('<path class="w" d="M80 520 L142 495"/>')
    s.t(80, 542, "COM", "m", "middle")
    s.t(150, 542, "NO", "m", "middle")
    s.parts.append('<circle cx="231" cy="520" r="26" class="c"/>')
    s.t(231, 525, "Quạt", "b", "middle")
    s.gnd(300, 520)
    s.t(300, 556, "GND 12 V", "m", "middle")
    s.t(180, 584, "Dòng quạt chỉ qua tiếp điểm relay, không qua LM358 hay BC337", "m", "middle")
    return s


BUILDERS_1 = {
    "d06-1": d06_1, "d06-2": d06_2, "d06-3": d06_3, "d06-4": d06_4, "d06-5": d06_5,
    "d08-1": d08_1, "d08-2": d08_2, "d08-3": d08_3, "d09-1": d09_1, "d11-1": d11_1,
    "d19-1": d19_1, "d19-2": d19_2, "d21-1": d21_1, "d21-2": d21_2,
}
