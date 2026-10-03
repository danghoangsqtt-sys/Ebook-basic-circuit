# Kiểm định hình minh họa Bài 29–42

Ngày 2026-10-03. Phạm vi P5-03.

| Bài | Mục tiêu hình | Điểm kiểm kỹ thuật |
| --- | --- | --- |
| 29 | Mô phỏng mạch | Mô hình cần đối chiếu với phép đo. |
| 30 | Máy hiện sóng | Probe ×1/×10, Volt/div, Time/div và trigger. |
| 31 | Bộ lọc | f_c của RC là mốc −3 dB lý tưởng; tải thay đổi đáp ứng. |
| 32 | Buck/boost | Công thức duty chỉ gần đúng lý tưởng; mạch thật có phản hồi/tổn hao. |
| 33 | Quy trình PCB | Schematic → footprint → layout/DRC → Gerber. |
| 34 | Hàn và kiểm | Kiểm cực, mối hàn và ngắn mạch trước cấp nguồn. |
| 35 | PCB buck | LM2596, vòng chuyển mạch nhỏ và FB tránh nút SW. |
| 36 | RTC DS3231 | Nguồn chính, pin dự phòng và I2C. |
| 37 | ESP32 IoT | Wi-Fi, cảm biến, HTTP/MQTT và trạng thái đầu ra. |
| 38 | Stepper/servo | A4988 cần cài giới hạn dòng; nguồn motor đủ dòng. |
| 39 | Cầu H | L298N, IN1/IN2, ENA/PWM và hai đầu motor. |
| 40 | HC-SR04 | ECHO 5 V phải hạ mức cho ESP32, timeout và d=v·t/2. |
| 41 | Cell Li-ion | Một cell, TP4056, module bảo vệ và rail ổn áp. |
| 42 | Robot Wi-Fi | Bài dùng **TB6612FNG**, LiPo 1S qua bảo vệ và boost 5 V, ECHO qua chia áp. |

Ảnh Digimess ở Bài 30 là máy analog để nhận diện núm, không đại diện giao diện máy số. Ảnh Bài 33 là bo máy tính đã lắp linh kiện, không phải PCB KiCad của bài. Ảnh Bài 41 là cell Li-ion hình trụ 18650/21700, không phải LiPo dạng túi; thông số sạc phải lấy từ cell dùng thật. Ba trang tệp xác nhận CC0: [máy hiện sóng](https://commons.wikimedia.org/wiki/File:Digimess_oscilloscope.jpg), [bo mạch](https://commons.wikimedia.org/wiki/File:Computer_Motherboard_Closeup.jpg), [hai cell Li-ion](https://commons.wikimedia.org/wiki/File:18650_and_21700_lithium_ion_battery_cell.jpg). Chi tiết nguồn/biến đổi ở [`SOURCES.md`](../../assets/images/lessons/SOURCES.md).

Một ảnh động cơ bước loại 28BYJ-48 được thử rồi loại trước tích hợp vì không phù hợp ví dụ A4988/NEMA 17 trong Bài 38. Sơ đồ Bài 42 được sửa từ L298N sang TB6612FNG sau khi đối chiếu bài.

## Cổng kiểm định

- `render_lesson_visuals.py --days 29 … 42 --check` và `integrate_lesson_visuals.py --days 29 … 42 --check`: 14/14 cập nhật.
- `check_visuals.py`: 42/56 bài có hình, 55 phần tử ảnh, 56 tài sản, 80 ASCII, 0 lỗi.
- `check_links.py`: 59 trang, 542 tham chiếu cục bộ, 0 lỗi.
- `build_search_index.py --check`: 56 bài, mới.
- `qa_lesson_visuals.py --start 29 --end 42`: 42 cặp bài/viewport 320/390/1280 px, ảnh tải được, có alt, không tràn hay lỗi JS.
- `qa_browser.py --quick`: PASS Chromium các luồng đọc/tìm/thư viện/sao lưu.

Chưa thử trên thiết bị vật lý; cổng viewport dùng Chromium.
