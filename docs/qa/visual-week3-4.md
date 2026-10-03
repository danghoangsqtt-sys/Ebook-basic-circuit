# Kiểm định hình minh họa Bài 15–28

Ngày 2026-10-03. Phạm vi P5-02. Mỗi bài có một SVG nội dung được biên tập theo bài, không chép lại sơ đồ ASCII cũ.

| Bài | Chủ đề hình | Kiểm tra chuyên môn chính |
| --- | --- | --- |
| 15 | BJT NPN switch | R base, tải collector, emitter GND, pinout theo model. |
| 16 | Driver relay | Diode flyback ngược song song cuộn, tách tiếp điểm tải. |
| 17 | Common emitter | Phân cực và điểm Q; ngõ ra đảo pha. |
| 18 | NMOS switch | RDS(on) tại VGS thực, không dùng VGS(th) để chứng minh bật đủ. |
| 19 | PWM | Duty, tần số, V trung bình và lọc RC. |
| 20 | Op-amp | Đảo/không đảo/follower/comparator, dải nguồn và common-mode. |
| 21 | Báo nhiệt | NTC → so ngưỡng → driver → relay/buzzer. |
| 22 | UART | Start/data/parity/stop; TX–RX chéo và mức logic. |
| 23 | I2C | SDA, SCL, pull-up, địa chỉ 7 bit, GND chung. |
| 24 | SPI | SCK, MOSI, MISO, CS và mode. |
| 25 | ADC | Dải đầu vào, lấy mẫu, LSB và hiệu chuẩn. |
| 26 | Interrupt | ISR ngắn, xử lý ở vòng chính, chống dội. |
| 27 | Cảm biến số | DHT22, DS18B20, PIR; pull-up và mức logic. |
| 28 | Trạm đo | DHT22/BME280, ESP32, OLED và log SD đúng bus. |

Ảnh Bài 15 là 2N2222A để nhận dạng vỏ BJT, không đại diện pinout của BC337. Ảnh Bài 18 là IRFIBC30 chỉ minh họa vỏ MOSFET, không được hiểu là khuyến nghị đóng cắt tại GPIO 3,3 V. Ảnh Bài 27 là DHT22/AM2302 rời. Giấy phép CC0, tác giả, biến đổi và trang tệp ghi trong [`SOURCES.md`](../../assets/images/lessons/SOURCES.md); đối chiếu trực tiếp: [2N2222A](https://commons.wikimedia.org/wiki/File:Generic_2N2222A.jpeg), [IRFIBC30](https://commons.wikimedia.org/wiki/File:IRFIBC30_MOS_transistor_01.jpg), [DHT22](https://commons.wikimedia.org/wiki/File:DHT22-Temperatur-Sensor.jpg).

## Kết quả

- `render_lesson_visuals.py --days 15 … 28 --check` và `integrate_lesson_visuals.py --days 15 … 28 --check`: 14/14 mới nhất.
- `check_visuals.py`: 28/56 bài có hình, 38 phần tử ảnh, 39 tài sản, 80 ASCII, 0 lỗi.
- `check_links.py`: 59 trang, 525 tham chiếu cục bộ, 0 lỗi.
- `build_search_index.py --check`: 56 bài, mới.
- `qa_lesson_visuals.py --start 15 --end 28`: 42 cặp bài/viewport ở 320, 390, 1280 px; ảnh tải được, có alt, không tràn ngang hoặc lỗi JS.
- `qa_browser.py --quick`: PASS Chromium cho trang đầu, chức năng đọc, thư viện dấu và sao lưu.

Chưa thử trên thiết bị vật lý; các ca trên dùng Chromium giả lập kích thước màn hình.
