# P3-01 — Kiểm tra mã nguồn và xuất/nhập dữ liệu đọc

## Bản đồ mã và dữ liệu trước khi chốt Phase 3

- `index.html` mở trang chủ; 56 tệp `week*/day*.html` nạp `assets/js/main.js` và `sidebar-data.js`. `main.js` quản lý menu, tiến độ, checklist, theme, cỡ chữ và tải các công cụ tìm/đánh dấu.
- `assets/js/highlights.js` lưu mảng dấu version 1 trong `localStorage['ebook-highlights-v1']`. Mỗi dấu có mã bài, quote, ngữ cảnh và vị trí; trang bài chỉ tô khi neo khớp chắc chắn. `highlights.html` và `highlight-library.js` đọc cùng khóa để lọc và xác minh neo xuyên bài.
- `assets/js/search.js` dùng `search-index.js` được sinh từ 56 bài, không dùng dữ liệu cá nhân. `tools/check_links.py` kiểm tra link/fragment tĩnh; `tools/qa_browser.py` thử luồng trình duyệt.
- Dữ liệu khác nằm ở `lessonProgress`, `checklist_<pathname>`, `ebook-fontsize-px`, `ebook-theme`, `weekStates`. `ebook-fontsize` là khóa cũ được `main.js` đọc khi chưa có khóa px; bản xuất cũng chuyển đổi giá trị này trước khi tạo JSON.

## Định dạng và xử lý

Tệp JSON `electric-basic-reader-data` version 1 gồm `exportedAt`, dấu, tiến độ, checklist, cỡ chữ, theme và trạng thái tuần. Mã kiểm tra toàn bộ trường, kiểu, giới hạn số/độ dài, ID dấu trùng và khóa ngoài phạm vi trước khi xem trước. Tệp tối đa 5 MB. Dữ liệu của tệp chỉ được ghi sau nút xác nhận. Chế độ gộp giữ dấu hiện có nếu cùng ID, thêm dấu mới và hợp nhất các ô tiến độ/checklist đã đánh dấu; chế độ thay thế dùng đúng nội dung tệp. Cả hai dùng cài đặt từ tệp. Khi ghi giữa chừng lỗi, mã cố khôi phục toàn bộ khóa đã chạm và báo rõ nếu khôi phục thất bại.

## Bằng chứng trình duyệt

`python tools/qa_browser.py` trên Chromium đạt: xuất rồi nhập khôi phục đúng dấu, cỡ chữ 21 px, theme sáng, tiến độ và checklist; xem trước đúng số dấu/xung đột; gộp không ghi đè dấu cùng ID; từ chối JSON hỏng, thiếu trường, version cũ, ngày sai, quote quá dài; lỗi ghi lần hai được báo và dữ liệu cũ khôi phục. Khóa cỡ chữ cũ được chuyển đổi 4 → 20 px. Trang sao lưu không tràn ngang ở 320/360/390/430 px. `python tools/qa_browser.py --quick --browser webkit` đạt cùng luồng đại diện. `python tools/check_links.py`: 59 trang, 487 tham chiếu, 0 lỗi.

Giới hạn: trình duyệt không cung cấp giao dịch nhiều khóa cho `localStorage`; khi thiết bị từ chối cả thao tác rollback, ứng dụng báo rõ và người đọc cần dùng tệp sao lưu để khôi phục. Tệp JSON lưu trên thiết bị người đọc, không có máy chủ đồng bộ. Chưa thử trên iOS/Android thật.
