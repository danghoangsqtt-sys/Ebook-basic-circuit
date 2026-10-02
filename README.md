# Giáo trình Kỹ thuật Điện tử Cơ bản

Website tĩnh tiếng Việt gồm 56 bài tự học điện tử thực hành trong 8 tuần. Bắt đầu tại [trang mở đầu](index.html) hoặc [Bài 1](week1/day01.html).

## Xem tại máy

Từ thư mục dự án, chạy `python -m http.server 8000`, rồi mở `http://localhost:8000/`. Dùng HTTP để lưu cỡ chữ, checklist và các đoạn đánh dấu trong trình duyệt; hành vi lưu trữ khi mở tệp `file:` có thể khác giữa trình duyệt.

Trang đầu có lộ trình 8 tuần và danh sách 56 bài. Trong mỗi bài, bạn có thể chỉnh cỡ chữ, tìm trong toàn bộ giáo trình, chọn một đoạn để tra Google/YouTube/bài liên quan hoặc đánh dấu. Dấu đã lưu hiện trong danh sách của bài. Các chức năng lưu hiện dùng bộ nhớ của trình duyệt trên thiết bị đang đọc.

## Kiểm tra dự án

Chạy `python tools/check_links.py` để kiểm tra link/fragment nội bộ và `python tools/build_search_index.py --check` để xác nhận chỉ mục tìm kiếm. Nếu đã cài Playwright Python và trình duyệt của nó, chạy `python tools/qa_browser.py`; thêm `--quick --browser webkit` để kiểm tra mẫu với WebKit. [Kết quả nghiệm thu Phase 1](docs/qa/phase1-results.md).

## Kế hoạch nâng cấp

- [Roadmap theo phase](.DHSYSTEM/ROADMAP.md)
- [Kiến trúc](.DHSYSTEM/ARCHITECTURE.md)
- [Tiến độ](.DHSYSTEM/TRACKER.md)
- [Bản mẫu giao diện](.DHSYSTEM/ui-direction/2026-10-02/index.html)
- [Phiên brainstorm đã chốt](docs/brainstorm/session-2026-10-02.md)

Phase 1 đã triển khai trang đầu, giao diện đọc mobile, cỡ chữ, tìm kiếm, chọn chữ và đánh dấu. Phase 2 mở thư viện dấu trên toàn bộ bài và nâng cao tìm kiếm; Phase 3 thêm xuất/nhập dữ liệu đọc.

## Bản quyền

© 2026 Lê Bá Đăng Hoàng. Giữ bản quyền riêng; hiện chưa cấp giấy phép tái sử dụng mã hoặc nội dung. Chủ dự án sẽ chọn giấy phép nếu muốn công bố quyền sử dụng sau này.
