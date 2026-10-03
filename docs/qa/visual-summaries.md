# QA sơ đồ tổng hợp — P6-01

Ngày kiểm: 2026-10-03. Tất cả 12 SVG tự vẽ từ `docs/visuals/summary-specs.json`; không lấy ảnh ngoài. Mỗi sơ đồ đặt cuối bài trước điều hướng, có alt, chú thích/nguồn và bản diễn giải bằng chữ trong `<details>`.

| Bài | Kiểu | Nhánh/khối và đề mục được đối chiếu |
| --- | --- | --- |
| 07 | Sơ đồ khối quy trình | Tính R → §2.2; lắp bốn nhánh → §2.4; đo trước nạp → §2.5; chạy/đo lại → §2.7. |
| 14 | Sơ đồ khối quy trình | Sơ đồ nguồn → §2.1; tính linh kiện → §2.2; lắp an toàn → §2.3; đo hai rail → §2.4. |
| 21 | Sơ đồ khối tín hiệu | NTC → §2.1; so ngưỡng và driver → §2.2; kiểm hai phía ngưỡng → §2.5. |
| 28 | Sơ đồ khối hệ thống | Đọc cảm biến, xử lý ESP32, OLED/SD → §2.1–2.2; đối chiếu số đo → §3. |
| 35 | Sơ đồ khối quy trình | Schematic LM2596S-5.0 → §2.1; KiCad → §2.2; vòng dòng nhanh → §2.3; đo nguồn/ripple → §3. |
| 42 | Sơ đồ tư duy hệ thống | HC-SR04/ECHO, TB6612FNG và nguồn LiPo → §2–2.1; lệnh web/AUTO → §2.2. Nguồn là nhánh riêng, không nằm trong chuỗi tín hiệu. |
| 43 | Sơ đồ tư duy | FR/NFR → §2; kiến trúc khối và BOM → §3; lịch dự án → §1. |
| 48 | Sơ đồ tư duy | README → §2; User Manual và tài liệu mạch/BOM → §1; Doxygen/test/version → §1, §3. |
| 49 | Sơ đồ tư duy | Tiến độ → §1; kịch bản và kết quả → §2; pin/WiFi/dự phòng offline → §3. |
| 50 | Sơ đồ tư duy | Chức năng và chất lượng → §1; nhìn lại → §2; portfolio → §3. |
| 55 | Sơ đồ tư duy | Năm hướng Firmware, Embedded Linux, PCB, IoT, Robotics → §1; chọn hướng và làm dự án → §2. Đã sửa sơ đồ tổng quan cũ từ “bốn hướng” thành bốn *nhóm* bao phủ năm hướng của bài. |
| 56 | Sơ đồ tư duy | Mạch/nguồn và firmware/bus → §1; PCB/kiểm thử và trình bày dự án → §2. |

## Kiểm tra

- `python tools/build_summary_visuals.py --check`: 12/12 SVG và HTML đúng dữ liệu biên tập, mỗi nhánh trỏ tới đề mục có trong bài.
- `python tools/qa_summary_visuals.py`: 12/12 SVG có chữ nằm trong viewBox; 36 ca bài/viewport tại 320/390/1280 px tải được, không tràn, có alt và bản chữ.
- `python tools/check_visuals.py --require-all`: 56/56 bài có hình, 82 phần tử ảnh, 83 tài sản dùng, 0 lỗi.
- `python tools/check_links.py`: 59 trang, 569 tham chiếu cục bộ, 0 hỏng.
- `python tools/build_search_index.py --check`: chỉ mục 56 bài hiện hành.

Giới hạn: chưa thử trên điện thoại vật lý; SVG mô tả khái niệm hoặc quy trình, không thay thế schematic và phép đo trong bài.
