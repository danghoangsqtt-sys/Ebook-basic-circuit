# P9-04 — Lab mô phỏng Pico + TMP36

## Yêu cầu và ranh giới

Đọc điện áp nhiệt độ, đổi theo **đường danh định** TMP36, bật LED onboard khi số đọc ≥30 °C và tắt khi ≤28 °C. Giữa hai ngưỡng giữ trạng thái trước. Ghi mã ADC, nhiệt danh định và trạng thái LED mỗi giây. Đây là bài mô phỏng quyết định số với ADC lý tưởng; chưa phải nhiệt kế hiệu chuẩn, SPICE, ERC hoặc kết quả board thật.

## BOM tham chiếu, nguồn hãng

| Mục | Mã và điều kiện | Vai trò |
| --- | --- | --- |
| Board | Raspberry Pi Pico RP2040 **non-W**, hình board Rev3 trong [Pico datasheet §2](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf); revision mẫu thật chưa biết | 3V3(OUT) pin 36, AGND pin 33, GP26/ADC0 pin 31, LED onboard GP25. GP25 không phải chân header. |
| Cảm biến | [ADI TMP36GT9Z TO-92, Rev. H](https://www.analog.com/media/en/technical-documentation/data-sheets/tmp35_36_37.pdf), bảng ordering và Fig. 4 | 2,7–5,5 V; 750 mV ở 25 °C, 10 mV/°C danh định; cấp từ 3V3(OUT). **Fig. 4 là bottom view**: chân 1 +VS, 2 VOUT, 3 GND. Không suy thứ tự khi nhìn mặt phẳng trước. |
| Tụ C1 | 0,1 µF gốm, điện áp định mức phù hợp, đặt sát +VS–GND sensor | ADI Rev. H Fig. 24/tr. 10 khuyến nghị bypass; mã/footprint thật chưa chốt. |
| Dây/nguồn | USB cấp Pico theo tài liệu board; rail 3V3(OUT) và AGND tham chiếu | Chưa chọn cáp/adapter cụ thể; không cấp 5 V vào ADC. |

Sơ đồ tự vẽ: [mở SVG](../../assets/images/labs/pico-tmp36-monitor.svg). Bản chữ: rail 3V3(OUT) pin 36 Pico đến TMP36 +VS pin 1 theo **bottom view**; TMP36 VOUT pin 2 đến GP26/ADC0 pin 31; TMP36 GND pin 3 đến AGND pin 33. C1 0,1 µF nối trực tiếp giữa +VS và GND gần sensor. GP25 điều khiển LED có sẵn trên Pico non-W; không mắc LED ngoài vào GP25. Mỗi tên net chỉ xuất hiện trên rail tương ứng; phải xác nhận marking/góc nhìn trên part thật trước khi nối.

Theo [Pico datasheet §2](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf), ADC_VREF được lọc từ 3,3 V trên board, là nguồn/tham chiếu ADC; trong lab mô phỏng đặt **chính xác 3,300 V** để tính. Board thật cần đo/hiệu chuẩn VREF, xem ripple, độ tuyến tính và nhiễu ADC. [MicroPython RP2 quick reference](https://docs.micropython.org/en/v1.26.0/rp2/quickref.html) mô tả `ADC(Pin(26)).read_u16()` trả mã 0–65535 quy chiếu dải 0–3,3 V; phần cứng RP2040 là SAR 12 bit, nên 16 bit API không phải 16 bit độ phân giải/accuracy.

## Netlist và ngân sách điện

| Net | Kết nối | Kiểm trước lắp thật |
| --- | --- | --- |
| +3V3 | Pico pin 36 → TMP36 pin 1 và C1+ | 2,7–5,5 V cho TMP36; rail Pico thực chưa đo. Dòng sensor <50 µA theo ADI trong điều kiện datasheet; ngân sách 3V3(OUT) còn phụ thuộc tải board và VSYS. |
| TEMP_V | TMP36 pin 2 → Pico pin 31 / GP26 / ADC0 | Danh định −40…125 °C cho 0,10…1,75 V, trong dải ADC giả định 0…3,3 V. Sai số/cực trị riêng phải kiểm trước lắp. |
| AGND | TMP36 pin 3, C1− → Pico pin 33 AGND | Đường hồi chung với ADC; không chọn GND oscilloscope tùy ý nếu chưa kiểm setup. |
| LED | GP25 → LED onboard | Phần tử nội bộ board non-W; không là đầu ra tải ngoài. |

Trong mô hình, `V=0,500+0,010T` (V), `raw=round(V/3,3×65535)`, `T_est=(raw×3,3/65535−0,500)/0,010`. Ở −40/25/125 °C điện áp danh định lần lượt 0,10/0,75/1,75 V. Khoảng điện áp một mã API tại 3,3 V là ≈50,35 µV, quy đổi ≈0,0050 °C **bước số học API**; ADC silicon 12 bit có bước lý tưởng ≈0,0806 °C, còn accuracy thực chưa biết. Không dùng các bước này thay sai số cảm biến, tham chiếu hoặc ADC.

## Chạy nhánh mô phỏng và kết quả kỳ vọng

Từ gốc repo: `python tools/simulate_phase9_sensor_lab.py` in JSON với nhiệt kích thích 25, 29, 30, 31, 29, 28, 27, 31 °C, thời điểm 0…7 s, điện áp 0,75/0,79/0,80/0,81/0,79/0,78/0,77/0,81 V và mã ADC lượng tử hóa. `python tools/verify_phase9_sensor_lab.py` đưa cùng mã qua **mã điều khiển thật** bằng fake ADC/LED, so ngưỡng, log, chu kỳ 1 s và dọn LED khi dừng. LED kỳ vọng là `0,0,0,1,1,0,0,1`. Biên đúng 28/30 °C có thể nằm phía đối diện sau lượng tử hóa; dự đoán LED theo số đã giải mã chứ không ép theo nhiệt kích thích lý tưởng. Đây là tín hiệu/kết quả tạo bởi mô hình, không là số đo.

Nếu có board đã xác nhận, cài MicroPython đúng board, đọc [mã mẫu](../../labs/pico_tmp36_monitor.py), chỉ nối theo pinout đã đối chiếu lại, đo rail/ADC_VREF và dùng chuẩn nhiệt phù hợp. Ghi CSV raw/timestamp/điện áp tham chiếu/nhiệt chuẩn/firmware, kiểm riêng điểm fit và điểm validation. Sai khác cần báo bằng `T_est−T_chuẩn` tại từng điểm, điều kiện và bất định chuẩn; chưa có bảng số đo thật nên không điền sai khác giả.

## Rubric

1. Chỉ đúng bottom view TMP36 và bốn net, nêu 3V3/AGND/ADC0/GP25: 2 điểm.
2. Tính 0,75 V tại 25 °C và nêu `read_u16` không là ADC 16 bit: 2 điểm.
3. Dự đoán hysteresis từ **nhiệt giải mã** và giải thích biên lượng tử: 2 điểm.
4. Chạy hai lệnh mô phỏng/kiểm, lưu JSON/log, nêu khác biệt giữa mô hình và board: 2 điểm.
5. Lập phiếu phép đo thật với VREF, chuẩn nhiệt, raw và sai khác, không nhận số mô phỏng là số đo: 2 điểm.

**Nguồn/giới hạn:** [ADI TMP36 Rev. H](https://www.analog.com/media/en/technical-documentation/data-sheets/tmp35_36_37.pdf), [Pico datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf), [MicroPython RP2 quick reference v1.26](https://docs.micropython.org/en/v1.26.0/rp2/quickref.html). Board và sensor thật, revision, điện áp tham chiếu, accuracy, đáp ứng nhiệt và duyệt kỹ thuật vẫn pending.
