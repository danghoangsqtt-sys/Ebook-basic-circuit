# Kiểm định hình minh họa Bài 1–14

Ngày 2026-10-03. Phạm vi P5-01, sau khi Phase 4 đã sửa 31 nhóm lỗi kỹ thuật trong các sơ đồ ký tự.

## Đối chiếu nội dung

| Bài | Hình tự vẽ | Điều được làm rõ |
| --- | --- | --- |
| 1 | Bản đồ khái niệm | V là hiệu điện thế hai điểm; GND là mốc quy ước; đo áp song song. |
| 2 | Bản đồ breadboard | Nhóm 5 lỗ, rãnh giữa, rail có thể đứt đoạn, thông mạch khi tắt nguồn. |
| 3 | Quy trình đọc màu | Nâu–đen–đỏ–vàng kim = 1 kΩ ±5%. |
| 4 | Quy trình mắc LED | Mỗi LED có R riêng; ví dụ 3,3 V, Vf 2 V, 220 Ω cho khoảng 5,9 mA. |
| 5 | So sánh | Nối tiếp chung dòng, song song chung áp. |
| 6 | Quy trình cầu chia áp | R1/R2 và ảnh hưởng tải song song R2. |
| 7 | Bản đồ dự án | Bốn GPIO, bốn điện trở, GND chung và thử từng nhánh. |
| 8 | So sánh tụ | Tụ gốm, điện phân, điện dung và điện áp định mức. |
| 9 | Quy trình RC | τ=RC; 63,2% khi nạp và 36,8% còn lại khi xả sau một τ. |
| 10 | Bản đồ cuộn cảm | Năng lượng từ trường, dòng không đổi đột ngột, RL và diode flyback. |
| 11 | Quy trình diode | Phân cực thuận/nghịch, hai diode mỗi đường dẫn trong cầu. |
| 12 | Quy trình Zener | R nối tiếp, Zener mắc nghịch song song tải, kiểm công suất. |
| 13 | Quy trình nguồn | LM7805 và AMS1117-3.3, tụ theo datasheet, tổn hao nhiệt. |
| 14 | Quy trình mini project | 9 V → 5 V → 3,3 V, tụ nối GND, đo từng rail trước khi gắn tải. |

Ảnh thật ở Bài 3, 4, 8, 10 chỉ minh họa ngoại hình linh kiện; chú thích không suy sơ đồ chân hoặc giá trị điện từ ảnh. Từng trang tệp ghi giấy phép miền công cộng hoặc CC0, tác giả và biến đổi tại [`assets/images/lessons/SOURCES.md`](../../assets/images/lessons/SOURCES.md). Các trang tệp: [điện trở](https://commons.wikimedia.org/wiki/File:Electronic-Axial-Lead-Resistors-Array.jpg), [LED](https://commons.wikimedia.org/wiki/File:Green_light_emitting_diode_led_on_circuit_board.jpg), [tụ](https://commons.wikimedia.org/wiki/File:Electrolytic_capacitors-P1090328.JPG), [cuộn cảm](https://commons.wikimedia.org/wiki/File:EC24_miniature_axial_inductors.jpg).

## Cổng kiểm định

- `python tools/render_lesson_visuals.py --days 1 … 14 --check`: 14 SVG khớp dữ liệu biên tập.
- `python tools/integrate_lesson_visuals.py --days 1 … 14 --check`: 14 trang có khối hình mới nhất.
- `python tools/check_visuals.py`: 56 bài, 14 có hình, 21 phần tử ảnh, 22 tài sản, 80 sơ đồ ASCII, 0 lỗi. Bài 15–56 xử lý trong P5-02 đến P5-04.
- `python tools/check_links.py`: 59 trang, 508 tham chiếu cục bộ, 0 liên kết hỏng.
- `python tools/build_search_index.py --check`: 56 bài, chỉ mục mới.
- `python tools/qa_lesson_visuals.py --start 1 --end 14`: 42 cặp bài/viewport (320, 390, 1280 px), ảnh tải được/có alt, không tràn ngang hay lỗi JS.
- `python tools/qa_browser.py --quick`: PASS Chromium, trang đầu và chức năng đọc/tìm/lưu.

Đã kiểm tra ảnh render trên 320 px ở Bài 3, 5, 8, 12: nhãn, phép tính và nguồn đọc được. Đây là kiểm tra trình duyệt giả lập; chưa thay thế kiểm thử màn hình và cử chỉ trên thiết bị thật.
