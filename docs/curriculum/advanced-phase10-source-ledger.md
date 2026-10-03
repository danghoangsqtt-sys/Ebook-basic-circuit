# Sổ nguồn Phase 10 — đồ án A29–A32

Đối chiếu internet ngày 2026-10-04. Mã board là Pico RP2040 **non-W**; Rev3 chỉ là hình board trong datasheet. TMP36GT9Z TO-92 theo ADI Rev. H; chưa có mẫu vật lý. Số học và hình khối do dự án tự tạo.

| Nguồn hãng | Claim trong A29–A32 | Không được suy |
| --- | --- | --- |
| [Pico board datasheet §2 và §4.5](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf) | Pin 31 GP26/ADC0, 33 AGND, 36 3V3(OUT); ADC_VREF lọc từ 3V3; USB VBUS qua D1 tới VSYS rồi nguồn board; khuyên tải ngoài 3V3(OUT) dưới 300 mA tùy điều kiện. | 3V3/VREF thật đúng 3,300 V; dòng tổng board hoặc hiệu suất nguồn đã đo; một PCB thật là Rev3. |
| [Pico board documentation](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) | Pico đời đầu non-W có LED onboard GP25; Pico W khác đường LED. | GP25 là chân header hoặc cùng mã điều khiển chạy Pico W/ESP32. |
| [ADI TMP36 Rev. H](https://www.analog.com/media/en/technical-documentation/data-sheets/tmp35_36_37.pdf) | TMP36GT9Z TO-92 trong ordering; Fig. 4 bottom view: 1 +VS, 2 VOUT, 3 GND; Fig. 24 khuyến nghị 0,1 µF gốm gần nguồn; supply 2,7–5,5 V, dòng dưới 50 µA, VOUT 750 mV ở 25 °C và 10 mV/°C danh định. | Dùng góc nhìn mặt trước cho chân TO-92; 0,750 V là kết quả đo; ±2 °C typical toàn dải là worst-case; đáp ứng bật điện là đáp ứng nhiệt. |
| [MicroPython RP2 quick reference v1.26](https://docs.micropython.org/en/v1.26.0/rp2/quickref.html) | `ADC(Pin(26)).read_u16()` dùng mã 0…65535; RP2040 ADC silicon 12 bit. | API 16 bit cho 16 bit accuracy; host fake là nạp firmware/đo ADC thật. |

**Giả định bài toán:** 3,300 V chính xác trong mô hình, 1 s/mẫu, kích thích 20–40 °C và ngưỡng 30/28 °C. Giả định VREF lệch 1% ở A31 để thảo luận sai số là số đặt ra, không phải thông số Pico. Bước mã lý tưởng khác accuracy hệ. Tệp `docs/projects/pico-tmp36-design.md` giữ bốn schematic net/BOM/ngân sách/phiếu đo; dữ liệu thật và reviewer pending.
