# Giáo trình Kỹ thuật Điện tử Cơ bản

Website tĩnh tiếng Việt gồm 56 bài nền tảng trong 8 tuần và các bài chuyên sâu đang được biên soạn. Bắt đầu tại [trang mở đầu](index.html) hoặc [Bài 1](week1/day01.html).

## Xem tại máy

Từ thư mục dự án, chạy `python -m http.server 8000`, rồi mở `http://localhost:8000/`. Dùng HTTP để lưu cỡ chữ, checklist và các đoạn đánh dấu trong trình duyệt; hành vi lưu trữ khi mở tệp `file:` có thể khác giữa trình duyệt.

Trang đầu có lộ trình 8 tuần, danh sách 56 bài nền tảng và các bài chuyên sâu đã xuất bản. Trong mỗi bài, bạn có thể chỉnh cỡ chữ, tìm trong toàn bộ giáo trình, chọn một đoạn để tra Google/YouTube/bài liên quan hoặc đánh dấu. Dấu đã lưu hiện trong danh sách của bài. Các chức năng lưu hiện dùng bộ nhớ của trình duyệt trên thiết bị đang đọc.

[Thư viện dấu](highlights.html) tập hợp các đoạn đã lưu trong nhiều bài. Bạn có thể lọc theo bài hoặc trạng thái, tìm trong đoạn trích, mở lại bài và xóa từng dấu. Trạng thái vị trí được kiểm tra với nội dung bài khi trang thư viện tải.

Tìm kiếm nội bộ chấp nhận từ khóa có hoặc không dấu và một số thuật ngữ Anh–Việt trong bài. Kết quả hiển thị đề mục và đoạn trích phù hợp; [bộ truy vấn kiểm tra](docs/qa/search-evaluation.md) ghi các trường hợp đã thử.

[Sao lưu dữ liệu đọc](reader-data.html) tải tệp JSON gồm dấu, tiến độ, checklist và cài đặt. Khi nhập, trang kiểm tra tệp, cho xem trước số lượng/xung đột rồi mới ghi sau khi bạn xác nhận. Bạn có thể gộp với dữ liệu hiện có hoặc thay thế. Tệp được xử lý trong trình duyệt, không gửi lên máy chủ.

Chưa có tài khoản hoặc đồng bộ tự động. Nếu chuyển thiết bị, xuất JSON ở thiết bị cũ rồi nhập tại thiết bị mới.

## Kiểm tra dự án

Chạy `python tools/check_links.py` để kiểm tra link/fragment nội bộ và `python tools/build_search_index.py --check` để xác nhận chỉ mục tìm kiếm. Nếu đã cài Playwright Python và trình duyệt của nó, chạy `python tools/qa_browser.py`; thêm `--quick --browser webkit` để kiểm tra mẫu với WebKit. [Kết quả nghiệm thu Phase 1](docs/qa/phase1-results.md).

Cả 56 bài đã có sơ đồ tổng quan riêng; 12 bài ôn tập/đồ án có thêm sơ đồ khối hoặc sơ đồ tư duy ở cuối bài. Ảnh chụp linh kiện được thêm ở những bài phù hợp. Chạy `python tools/check_visuals.py --require-all` để kiểm tra độ phủ, mô tả thay thế, tệp nguồn và ghi nguồn; chạy `python tools/qa_lesson_visuals.py` để kiểm tra hình ở 320/360/390/430/1280 px và `python tools/qa_summary_visuals.py` để kiểm tra sơ đồ tổng hợp. [Báo cáo nghiệm thu hình](docs/qa/visual-final.md) có kết quả và ảnh chụp màn hình mẫu; [danh mục nguồn hình](assets/images/lessons/SOURCES.md), [kiểm kê ban đầu](docs/brainstorm/visual-inventory-2026-10-02.md), [báo cáo rà kỹ thuật](docs/qa/visual-technical-audit.md), [ánh xạ sơ đồ tổng hợp](docs/qa/visual-summaries.md) và các báo cáo [tuần 1–2](docs/qa/visual-week1-2.md), [3–4](docs/qa/visual-week3-4.md), [5–6](docs/qa/visual-week5-6.md), [7–8](docs/qa/visual-week7-8.md) ghi chi tiết. Ảnh ngoài chỉ dùng nguồn CC0/miền công cộng đã xác minh; sơ đồ do dự án tự tạo.

## Kế hoạch nâng cấp

- [Roadmap theo phase](.DHSYSTEM/ROADMAP.md)
- [Kiến trúc](.DHSYSTEM/ARCHITECTURE.md)
- [Tiến độ](.DHSYSTEM/TRACKER.md)
- [Bản mẫu giao diện](.DHSYSTEM/ui-direction/2026-10-02/index.html)
- [Phiên brainstorm đã chốt](docs/brainstorm/session-2026-10-02.md)

Phase 1 đã triển khai trang đầu, giao diện đọc mobile, cỡ chữ, tìm kiếm, chọn chữ và đánh dấu. Phase 2 đã mở thư viện dấu và nâng tìm kiếm. Phase 3 đã bổ sung xuất/nhập dữ liệu đọc; tài khoản/đồng bộ hiện được hoãn theo quyết định trong tracker.

Phase 4 đã kiểm và sửa 31 nhóm lỗi sơ đồ/nội dung kỹ thuật. Phase 5 đã minh họa đủ 56 bài; Phase 6 bổ sung 12 sơ đồ tổng hợp và hoàn tất kiểm tra hình toàn giáo trình.

Phase 7 đã qua cổng rà soát nội dung số: 80 khối ký tự đã được thay bằng 70 SVG và 10 bảng/đoạn HTML có thể đọc, menu 56 bài đã khớp tiêu đề. [Sổ kiểm Phase 7](docs/qa/curriculum-phase7.md) ghi các lỗi điện học đã sửa và phần cứng chưa được nghiệm thu. Phase 8 đã có [đặc tả A01–A16](docs/curriculum/advanced-phase8-syllabus.md) và bốn bài đầu [A01](advanced/a01.html), [A02](advanced/a02.html), [A03](advanced/a03.html), [A04](advanced/a04.html), cùng [sổ mạch/datasheet](docs/curriculum/reference-circuit-review.md). Các bài A05–A32 đang theo kế hoạch.

## Bản quyền

© 2026 Lê Bá Đăng Hoàng. Giữ bản quyền riêng; hiện chưa cấp giấy phép tái sử dụng mã hoặc nội dung. Chủ dự án sẽ chọn giấy phép nếu muốn công bố quyền sử dụng sau này.
