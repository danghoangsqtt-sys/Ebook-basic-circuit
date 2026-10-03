# Kiểm định hình minh họa Bài 43–56

Ngày 2026-10-03. Phạm vi P5-04, hoàn tất minh họa từng bài của Phase 5.

| Bài | Hình tự vẽ | Điều kiểm tra |
| --- | --- | --- |
| 43 | Từ ý tưởng đến hệ thống | Yêu cầu SRS có cách kiểm; sơ đồ khối gồm nguồn, cảm biến, xử lý, đầu ra. |
| 44 | Khung firmware | Module, state machine, scheduler không delay. |
| 45 | Tích hợp/debug | Thử từng module, log cấu trúc và đo rail/timing. |
| 46 | Layout PCB | Đường hồi GND, vùng công suất/tín hiệu, test point đúng net. |
| 47 | Kiểm thử/hiệu chuẩn | Test từ SRS, số đo tham chiếu, lưu số đo gốc và chạy bền. |
| 48 | Bộ tài liệu | README, sơ đồ/BOM, manual, hồ sơ test. |
| 49 | Kịch bản demo | Mục tiêu, kiến trúc, ca bình thường/lỗi, bằng chứng. |
| 50 | Tổng kết đồ án | Mục tiêu đạt/chưa đạt, chứng cứ, bài học và portfolio. |
| 51 | PID | Setpoint → e → PID → tải → feedback, dt và chống tích phân bão hòa. |
| 52 | FreeRTOS | Task đo, queue, xử lý, giao tiếp; đồng bộ dữ liệu. |
| 53 | BLE ESP32 | Advertise, GATT service, read/notify/write; kiểm đúng model. |
| 54 | EMC | Decoupling gần IC, vòng dòng nhỏ, ground plane liên tục. |
| 55 | Học tiếp | Embedded, phần cứng, điều khiển/robot, IoT. |
| 56 | Tổng kết khóa | Đo/lắp, thiết kế mạch, firmware, hoàn thiện đồ án. |

Ảnh [bo ESP-WROOM-32](https://commons.wikimedia.org/wiki/File:ESP32_Espressif_ESP-WROOM-32_Dev_Board.jpg) ở Bài 53 do Ubahnverleih tạo và công bố CC0; caption giới hạn pinout theo đúng bo trong ảnh. Bản WebP 1200 × 921 và chi tiết nguồn ở [`SOURCES.md`](../../assets/images/lessons/SOURCES.md).

## Cổng kiểm định

- `render_lesson_visuals.py --check` và `integrate_lesson_visuals.py --check`: toàn bộ 56 SVG và 56 khối bài còn mới.
- `check_visuals.py --require-all`: 56/56 bài có hình, 70 phần tử ảnh, 71 tài sản dùng trong bài, 80 sơ đồ ASCII đã qua rà kỹ thuật, 0 lỗi.
- `check_links.py`: 59 trang, 557 tham chiếu cục bộ, 0 lỗi.
- `build_search_index.py --check`: 56 bài, mới.
- `qa_lesson_visuals.py`: 168 cặp bài/viewport 320/390/1280 px; tất cả ảnh tải được, có alt, không tràn ngang hoặc lỗi JS.
- `qa_browser.py --quick`: PASS Chromium các luồng đọc, tìm, thư viện và sao lưu.

Chưa thử trên điện thoại vật lý; các ca mobile là Chromium giả lập viewport.
