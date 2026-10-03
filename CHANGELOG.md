# Lịch sử thay đổi

Theo cấu trúc Keep a Changelog. Dự án chưa gắn phiên bản phát hành.

## Chưa phát hành

### Tài liệu

- Phase 7 qua audit/debug trong phạm vi nội dung số: kiểm kê 56 bài, 80 ID sơ đồ và 17 claim; thay 80 khối ASCII bằng 70 SVG và 10 tham chiếu HTML có thể đọc được. Đối chiếu mạch tham chiếu/datasheet hãng, sửa sai lệch nguồn, linh kiện, giới hạn, phép tính và đồng bộ 56 nhãn menu. Phần cứng thật còn cổng xác minh riêng.
- Phase 8 P8-01 khóa đặc tả A01–A16 với ví dụ, hoạt động số, bài tập/rubric và nguồn chính; các trang bài mới chưa xuất bản.
- Thêm 14 sơ đồ tổng quan theo nội dung Bài 1–14 và bốn ảnh linh kiện CC0/miền công cộng có ghi nguồn; kiểm tra 320/390/1280 px.
- Thêm 14 sơ đồ Bài 15–28 và ba ảnh CC0 cho BJT, MOSFET, DHT22; chú thích rõ giới hạn suy luận từ ảnh linh kiện.
- Thêm 14 sơ đồ Bài 29–42 và ba ảnh CC0 cho máy hiện sóng, PCB, cell Li-ion; sửa minh họa robot dùng đúng driver TB6612FNG.
- Hoàn tất sơ đồ Bài 43–56 và ảnh ESP32 CC0; cả 56 bài đều có hình và qua 168 ca hiển thị mobile/desktop.
- Thêm 12 sơ đồ tổng hợp cuối bài kèm bản diễn giải chữ cho các bài ôn tập, đồ án và định hướng; rà đúng năm hướng học tiếp ở Bài 55.
- Nghiệm thu toàn bộ hình, nguồn CC0/miền công cộng, mô tả thay thế, chú thích và bố cục điện thoại ở 320/360/390/430 px.

- Hoàn tất kiểm định Phase 4: phân loại 80 sơ đồ ký tự và sửa 31 nhóm lỗi kỹ thuật trong sơ đồ, lời giảng, bài thực hành trước đợt vẽ hình.

- Lập kế hoạch Phase 4–6 làm mới hình cho 56 bài; thêm baseline và cổng kiểm tra ảnh/nguồn.

- Chốt hướng nâng cấp trang mở đầu, đọc trên điện thoại, công cụ chọn chữ và tìm kiếm bài liên quan.
- Tạo kiến trúc, roadmap, tracker, schema dữ liệu cục bộ và bản mẫu giao diện.

### Mã ứng dụng

- Mẫu hình Bài 1–2 dùng ảnh CC0 và SVG responsive; chú thích hình theo thanh cỡ chữ người đọc.

- Thiết kế lại trang mở đầu với lộ trình 8 tuần, mục lục mở trực tiếp 56 bài và điều hướng mobile.
- Sửa khung đọc 56 bài trên điện thoại, giữ bảng/sơ đồ cuộn riêng và cải thiện menu bàn phím.
- Thêm thanh kéo cỡ chữ vùng bài 16–24 px, lưu thiết lập và hoạt động khi lưu trữ trình duyệt bị chặn.
- Thêm chỉ mục tự sinh từ 56 bài và hộp tìm kiếm tiếng Việt có dấu/không dấu trên trang đọc.
- Thêm menu chọn chữ để sao chép, tìm giải thích trên Google, video YouTube và bài học liên quan.
- Thêm bút đánh dấu lưu cục bộ, khôi phục theo câu trích/ngữ cảnh và danh sách dấu của bài đang đọc.
- Sửa toàn bộ liên kết nội bộ còn hỏng và kiểm tra cả anchor; bổ sung bộ kiểm thử trình duyệt cho trang đầu, 56 bài và các thao tác đọc.
- Thêm thư viện dấu xuyên 56 bài với tìm/lọc, kiểm tra vị trí neo, mở đúng đoạn và xóa từng dấu.
- Bổ sung từ đồng nghĩa điện tử Anh–Việt và đoạn trích tìm kiếm căn theo vị trí khớp; lưu bộ truy vấn đánh giá.
- Thêm xuất/nhập JSON dữ liệu đọc với kiểm tra tệp, xem trước xung đột, gộp hoặc thay thế và cố khôi phục khi ghi lỗi.
