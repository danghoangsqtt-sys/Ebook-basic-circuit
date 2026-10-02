# UI Direction — 2026-10-02

## Trạng thái

Đã được người dùng chốt: trang mở đầu giới thiệu giáo trình gọn, tìm bài liên quan trong 56 bài trước rồi mới mở rộng ra ngoài.

## Pages inventory

| Trang | Tệp | Vai trò | Trạng thái |
| --- | --- | --- | --- |
| Hub | `index.html` | Mở hai bản mẫu | Có |
| Trang mở đầu | `pages/home.html` | Giới thiệu và lộ trình | Hướng bố cục đã chốt |
| Trang đọc bài | `pages/reader.html` | Minh họa chế độ đọc và công cụ chọn chữ | Hướng công cụ đã chốt |

## Lựa chọn giao diện

- Nền sáng, chữ xanh đậm để đọc bài dài; cam đất làm điểm nhấn hành động và thông tin kỹ thuật.
- Trang mở đầu có một thông điệp chính, một hành động chính, lộ trình 8 tuần theo nhóm hai tuần; bớt số liệu và đoạn quảng bá lặp.
- Thanh điều hướng trên điện thoại dùng menu gọn, không đưa mọi liên kết lên một hàng.
- Trang đọc dành chiều rộng chủ yếu cho văn bản. Thanh kéo thay đổi riêng cỡ chữ bài học; mẫu này có thao tác kéo thật và lưu thử nghiệm bằng `localStorage`.
- Menu đánh dấu/tra cứu mới là minh họa vị trí và nhãn. Chức năng thật nằm trong phase triển khai.
- Mục lục trang đầu nạp từ `assets/js/sidebar-data.js`, cho mở đủ 56 bài trong 8 tuần; trang đọc mẫu dẫn về mục lục này. Giao diện triển khai cần đưa danh sách tương đương vào menu bài học trên điện thoại.

## Kiểm tra UX cần làm khi triển khai

- 320, 360, 390, 430 px; điện thoại xoay ngang; phóng chữ và zoom trình duyệt.
- Bài có bảng lớn, công thức, mã và sơ đồ ASCII.
- Chọn chữ bằng chuột, bàn phím và nhấn giữ trên điện thoại; bảo đảm vẫn sao chép được.
- Giữ dấu đánh dấu qua tải lại; không tô nhầm khi nội dung bài thay đổi.
- Kiểm tra liên kết thật trong website. Mẫu chỉ liên kết giữa các màn hình mẫu.
