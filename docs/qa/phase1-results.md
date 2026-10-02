# Nghiệm thu Phase 1 — 02/10/2026

## Kết quả

- `python tools/check_links.py`: 57 trang, 470 tham chiếu nội bộ, **0** tệp thiếu, fragment thiếu hoặc đường dẫn thoát thư mục. Trước Phase 1 có 73 liên kết hỏng; 62 liên kết còn lại sau khi thay trang đầu đã được sửa trong P1-08. Bộ kiểm tra nay xác thực cả fragment tĩnh.
- `python tools/build_search_index.py --check`: chỉ mục 56 bài, 420691 byte, khớp nội dung HTML.
- `node --check` toàn bộ JavaScript trong `assets/js`: đạt. `git diff --check`: đạt.
- `python tools/qa_browser.py`: Chromium qua 4 viewport trang đầu (320/360/390/430 px), 56 bài ở 320 px và 21 phép đo Bài 1/28/56 ở 24 px, viewport 160–430 px. Tổng 77 phép đo bài, **không tràn ngang toàn trang**. Bảng, mã và sơ đồ dài vẫn cuộn trong vùng riêng.
- `python tools/qa_browser.py --quick --browser webkit`: WebKit qua 4 viewport trang đầu và 24 phép đo bài đại diện, không tràn ngang.

## Luồng tương tác

Bộ kiểm tra chạy trên HTTP cục bộ và xác nhận: trang đầu có 8 tuần, 56 liên kết bài duy nhất; sidebar mỗi bài có 56 mục; menu mobile mở/đóng bằng nút và Escape, trả focus; thanh cỡ chữ 16–24 px cập nhật ngay, điều khiển bằng phím, giữ qua tải lại và reset; tiến độ 1/56; checklist lưu qua tải lại; đáp án mở; bố cục in ẩn thanh đầu và vẫn hiện bài; tìm `dien ap` xếp Bài 1 đầu; tìm bài liên quan từ đoạn chọn; đánh dấu hiện, lưu, nhảy tới, xóa; chuyển theme. Không có lỗi JavaScript trong các luồng này.

Các ca P1-06/P1-07 trước đó đã thử chuột phải, bàn phím, cảm ứng mô phỏng, URL Google/YouTube, chọn qua thẻ inline, trùng câu trích, mất neo và lưu trữ bị chặn trên Chromium/WebKit. Bản ghi chi tiết ở `.DHSYSTEM/TRACKER.md`.

## Giới hạn

Chromium và WebKit ở đây chạy trên Windows với viewport/cảm ứng mô phỏng. Chưa kiểm tra bằng điện thoại iOS/Android thật, trình đọc màn hình thật hoặc in trên máy in. Dữ liệu cỡ chữ/checklist/đánh dấu lưu trong trình duyệt hiện tại; đồng bộ và xuất nhập dữ liệu thuộc Phase 3.
