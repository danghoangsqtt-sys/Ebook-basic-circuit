# Giáo trình Kỹ thuật Điện tử Cơ bản

Website tĩnh tiếng Việt gồm 56 bài tự học điện tử thực hành trong 8 tuần. Bắt đầu tại [trang mở đầu](index.html) hoặc [Bài 1](week1/day01.html).

## Xem tại máy

Từ thư mục dự án, chạy `python -m http.server 8000`, rồi mở `http://localhost:8000/`. Dùng HTTP để lưu cỡ chữ, checklist và các đoạn đánh dấu trong trình duyệt; hành vi lưu trữ khi mở tệp `file:` có thể khác giữa trình duyệt.

Trang đầu có lộ trình 8 tuần và danh sách 56 bài. Trong mỗi bài, bạn có thể chỉnh cỡ chữ, tìm trong toàn bộ giáo trình, chọn một đoạn để tra Google/YouTube/bài liên quan hoặc đánh dấu. Dấu đã lưu hiện trong danh sách của bài. Các chức năng lưu hiện dùng bộ nhớ của trình duyệt trên thiết bị đang đọc.

[Thư viện dấu](highlights.html) tập hợp các đoạn đã lưu trong nhiều bài. Bạn có thể lọc theo bài hoặc trạng thái, tìm trong đoạn trích, mở lại bài và xóa từng dấu. Trạng thái vị trí được kiểm tra với nội dung bài khi trang thư viện tải.

Tìm kiếm nội bộ chấp nhận từ khóa có hoặc không dấu và một số thuật ngữ Anh–Việt trong bài. Kết quả hiển thị đề mục và đoạn trích phù hợp; [bộ truy vấn kiểm tra](docs/qa/search-evaluation.md) ghi các trường hợp đã thử.

[Sao lưu dữ liệu đọc](reader-data.html) tải tệp JSON gồm dấu, tiến độ, checklist và cài đặt. Khi nhập, trang kiểm tra tệp, cho xem trước số lượng/xung đột rồi mới ghi sau khi bạn xác nhận. Bạn có thể gộp với dữ liệu hiện có hoặc thay thế. Tệp được xử lý trong trình duyệt, không gửi lên máy chủ.

Chưa có tài khoản hoặc đồng bộ tự động. Nếu chuyển thiết bị, xuất JSON ở thiết bị cũ rồi nhập tại thiết bị mới.

## Kiểm tra dự án

Chạy `python tools/check_links.py` để kiểm tra link/fragment nội bộ và `python tools/build_search_index.py --check` để xác nhận chỉ mục tìm kiếm. Nếu đã cài Playwright Python và trình duyệt của nó, chạy `python tools/qa_browser.py`; thêm `--quick --browser webkit` để kiểm tra mẫu với WebKit. [Kết quả nghiệm thu Phase 1](docs/qa/phase1-results.md).

Cả 56 bài đã có sơ đồ tổng quan riêng; ảnh chụp linh kiện được thêm ở những bài phù hợp. Chạy `python tools/check_visuals.py --require-all` để kiểm tra độ phủ, mô tả thay thế, tệp nguồn và ghi nguồn; chạy `python tools/qa_lesson_visuals.py` để kiểm tra hình ở 320/390/1280 px. [Danh mục nguồn hình](assets/images/lessons/SOURCES.md), [kiểm kê ban đầu](docs/brainstorm/visual-inventory-2026-10-02.md), [báo cáo rà kỹ thuật](docs/qa/visual-technical-audit.md) và các báo cáo [tuần 1–2](docs/qa/visual-week1-2.md), [3–4](docs/qa/visual-week3-4.md), [5–6](docs/qa/visual-week5-6.md), [7–8](docs/qa/visual-week7-8.md) ghi chi tiết. Ảnh ngoài chỉ dùng nguồn CC0/miền công cộng đã xác minh; sơ đồ do dự án tự tạo. Sơ đồ tư duy và sơ đồ khối tổng hợp của Phase 6 đang thực hiện.

## Kế hoạch nâng cấp

- [Roadmap theo phase](.DHSYSTEM/ROADMAP.md)
- [Kiến trúc](.DHSYSTEM/ARCHITECTURE.md)
- [Tiến độ](.DHSYSTEM/TRACKER.md)
- [Bản mẫu giao diện](.DHSYSTEM/ui-direction/2026-10-02/index.html)
- [Phiên brainstorm đã chốt](docs/brainstorm/session-2026-10-02.md)

Phase 1 đã triển khai trang đầu, giao diện đọc mobile, cỡ chữ, tìm kiếm, chọn chữ và đánh dấu. Phase 2 đã mở thư viện dấu và nâng tìm kiếm. Phase 3 đã bổ sung xuất/nhập dữ liệu đọc; tài khoản/đồng bộ hiện được hoãn theo quyết định trong tracker.

## Bản quyền

© 2026 Lê Bá Đăng Hoàng. Giữ bản quyền riêng; hiện chưa cấp giấy phép tái sử dụng mã hoặc nội dung. Chủ dự án sẽ chọn giấy phép nếu muốn công bố quyền sử dụng sau này.
