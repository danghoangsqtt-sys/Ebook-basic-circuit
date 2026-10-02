# P2-01 — Thư viện dấu xuyên bài

Chạy `python tools/qa_browser.py --quick` và `python tools/qa_browser.py --quick --browser webkit` trên HTTP cục bộ: cả hai đạt. Luồng tạo dấu trong Bài 1 và Bài 28, mở thư viện thấy hai bài, lọc theo bài, tìm đoạn trích, kiểm tra vị trí neo, tạo dấu mất neo mẫu, lọc trạng thái và xác nhận link mất neo không có `?highlight`. Xóa dấu mẫu giữ nguyên hai dấu khác; mở dấu còn neo cuộn tới `<mark>` đúng bài. Trang thư viện không tràn ngang ở 320/360/390/430 px.

`python tools/check_links.py`: 58 trang, 479 tham chiếu nội bộ, 0 lỗi. Bộ quét nay nhận cả trang HTML bổ sung ở thư mục gốc. Chưa kiểm thử trên thiết bị điện thoại thật; đối chiếu neo cần tải HTML bài cùng origin nên khi mất kết nối, trạng thái hiển thị “Chưa kiểm tra được vị trí”.
