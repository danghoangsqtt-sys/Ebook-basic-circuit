# Nghiệm thu hình minh họa toàn giáo trình — P6-02

Ngày kiểm: 2026-10-03. Phạm vi: 56 bài HTML, 56 sơ đồ tổng quan, 12 sơ đồ tổng hợp, ảnh linh kiện thật và 80 sơ đồ ký tự đã rà ở Phase 4. Giáo trình giữ bản quyền riêng; ảnh bên ngoài trong dự án là các tệp CC0/miền công cộng được ghi theo trang tệp cụ thể tại `assets/images/lessons/SOURCES.md`.

## Kết quả

| Cổng | Kết quả |
| --- | --- |
| Độ phủ và nguồn | `check_visuals.py --require-all`: 56/56 bài có đúng một hình tổng quan, 12/12 bài dự kiến có hình tổng hợp; 82 phần tử ảnh, 83 tài sản dùng (có biến thể SVG mobile), 0 lỗi. Mỗi raster có bản ghi nguồn tệp và CC0/miền công cộng; mỗi SVG ghi tự vẽ/nội dung dự án. |
| Tính hiện hành | `render_lesson_visuals.py --check`, `integrate_lesson_visuals.py --check` và `build_summary_visuals.py --check` đều PASS. 12/12 nhánh sơ đồ tổng hợp ánh xạ tới đề mục thật trong bài. |
| Hiển thị toàn giáo trình | `qa_lesson_visuals.py`: 280 ca, 56 bài × 320/360/390/430/1280 px, ảnh tải được, có alt và chú thích/nguồn, không tràn ngang. |
| Sơ đồ tổng hợp | `qa_summary_visuals.py` Chromium và WebKit: mỗi trình duyệt 12 SVG kiểm biên chữ + 36 ca bài/viewport ở 320/390/1280 px, cỡ chữ bài 24 px và bản diễn giải mở, không tràn. |
| Luồng ứng dụng | `qa_browser.py` Chromium toàn bộ: 4 viewport trang đầu, 77 ca bài/viewport, thao tác đọc, dấu, thư viện, sao lưu PASS. WebKit quick: 4 viewport trang đầu, 24 ca bài/viewport và cùng luồng chính PASS. |
| Nội bộ | `check_links.py`: 59 trang/569 tham chiếu cục bộ, 0 link/fragment hỏng. `build_search_index.py --check`: 56 bài hiện hành, 458960 byte. |

## Rà nội dung và khả năng đọc

- Bài 55 trước đó ghi “bốn hướng” trong SVG tổng quan nhưng bài nêu năm hướng. Đã sửa thành bốn **nhóm** bao phủ năm hướng; sơ đồ tư duy cuối bài liệt kê đủ Firmware, Embedded Linux, PCB, IoT và Robotics.
- Bài 42 dùng sơ đồ nhánh cho cảm biến, web, driver TB6612FNG và nguồn LiPo; không vẽ nguồn thành bước nối tiếp của luồng điều khiển. Các hình mô tả khái niệm/quy trình, không thay sơ đồ đấu dây chi tiết trong bài.
- Kiểm tra cỡ chữ 24 px phát hiện câu mã màu trong bài tập Bài 7 làm tràn ngang ở 320 px. `dh-debug` đã thêm ngắt dòng cho `.exercise-text`; Chromium/WebKit sau sửa đều PASS. Màu chữ ghi nguồn được tăng tương phản ở giao diện tối.
- Hình SVG có `<title>`/`<desc>`; HTML có alt, chú thích nguồn. 12 sơ đồ tổng hợp có bản diễn giải chữ mở được bằng bàn phím. Nhãn SVG được kiểm không cắt tại biên viewBox.

## Ảnh mẫu đã xem

- [Nguồn hai rail, 320 px](visual-samples/day14-summary-320px.png)
- [Robot TB6612FNG, 320 px, nền tối](visual-samples/day42-summary-320px.png)
- [Robot TB6612FNG, 320 px, nền sáng](visual-samples/day42-summary-320px-light.png)
- [Năm hướng học tiếp, 390 px](visual-samples/day55-summary-390px.png)

Ảnh cắt vùng hình/chú thích sau khi ẩn thanh đầu trang *chỉ khi chụp* để không che phần đầu SVG; website thực vẫn giữ thanh đầu trang. Trong trình duyệt, người đọc cuộn trang để xem toàn hình.

## Giới hạn

Chưa thử bằng điện thoại iOS/Android vật lý, screen reader vật lý hoặc dựng mạch/đo phần cứng. Kiểm tra giấy phép dựa trên trang tệp đã đối chiếu lúc nhập và bản ghi nguồn tại ngày nêu trong manifest; quyền của toàn giáo trình không đổi.
