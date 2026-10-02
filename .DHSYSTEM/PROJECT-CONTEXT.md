<!-- crystallize_version: 0.8.0 -->
# Bối cảnh sản phẩm

## DHSYSTEM active profile (FEAT-009)

Không có profile tổ chức được liên kết. Thông tin chưa biết được giữ là `chưa xác định`.

<product_vision>

## Phạm vi sản phẩm

Giúp người học đọc và thực hành trọn bộ 56 bài điện tử trên desktop và điện thoại, dễ bắt đầu từ trang mở đầu, điều chỉnh cỡ chữ, đánh dấu đoạn quan trọng và tra cứu trực tiếp từ đoạn được chọn.

## Người dùng chính

- Người mới học điện tử, cần lộ trình 8 tuần dễ theo dõi.
- Người đã làm việc với ESP32/firmware nhưng cần nền tảng đo kiểm và phân tích mạch.
- Người đọc tài liệu dài trên điện thoại, cần chữ thoáng và thao tác chạm dễ dùng.

## Tổng quan phase

- **Phase 1:** Trang mở đầu gọn, mobile reflow, liên kết đúng, thanh kéo chữ, đánh dấu và tra cứu Google/YouTube/bài nội bộ.
- **Phase 2:** Danh sách dấu đã lưu; tìm kiếm sâu hơn theo đề mục, trích đoạn và từ đồng nghĩa; nhiều màu/ghi chú khi cần.
- **Phase 3:** Xuất/nhập dữ liệu đọc; chỉ quyết định về tài khoản và đồng bộ nhiều thiết bị sau khi có nhu cầu rõ ràng.

## Ngoài phạm vi hiện tại

- Không xây backend, đăng nhập, cơ sở dữ liệu, AI giải thích tự động hoặc bộ thu thập tài liệu từ web trong Phase 1–2.
- Không viết lại nội dung 56 bài trong đợt nâng cấp giao diện; chỉ chỉnh nội dung cần thiết để sửa liên kết hoặc nhãn điều hướng.
- Không tự cấp giấy phép mở cho mã và nội dung.

</product_vision>

## Quy tắc sản phẩm

1. “Tìm bài liên quan” tra trong 56 bài của website trước; kết quả ngoài website là lựa chọn bổ sung do người dùng bấm.
2. Tìm Google/YouTube mở trang kết quả tìm kiếm cho đoạn đã chọn; không cam kết có sẵn lời giải thích hoặc video phù hợp.
3. Dấu đánh dấu và cỡ chữ được lưu trên thiết bị hiện tại; UI phải nói rõ không đồng bộ giữa thiết bị.
4. Khi không thể khôi phục vị trí dấu một cách chắc chắn sau khi sửa bài, không tô vào đoạn khác; báo dấu chưa định vị được.
5. Nội dung cần có thể chọn/copy bình thường; công cụ bổ sung không được khóa toàn bộ menu gốc của trình duyệt.
6. Phase 1 phải có đường duyệt đủ 56 bài và danh sách dấu của bài hiện tại; Phase 2 mở rộng thư viện dấu xuyên bài.

## Quyết định giao diện đã chốt

- Trang đầu là trang giới thiệu ngắn với lời hứa rõ ràng, nút vào Bài 1 và lộ trình 8 tuần.
- Màn hình hẹp dùng menu gọn; bài học một cột, bảng/sơ đồ rộng cuộn trong khung riêng.
- Hướng thiết kế từ `.DHSYSTEM/ui-direction/2026-10-02/`: nền sáng, chữ xanh đậm, cam nhấn, thân bài đủ lớn.

## Tiêu chí thành công

- Không có cuộn ngang toàn trang hay chữ/nút đè nhau ở 320, 360, 390 và 430 CSS px.
- Hoàn thành luồng mở Bài 1, điều chỉnh chữ, chọn đoạn, đánh dấu, tra cứu và quay lại bài bằng chuột lẫn chạm.
- Cỡ chữ và dấu lưu qua tải lại; lỗi lưu trữ không làm trang đọc ngừng hoạt động.
- Các liên kết điều hướng tới tệp nội bộ đều tồn tại.
- Các luồng chọn chữ, sao chép, đánh dấu và tra cứu được kiểm tra trên iOS Safari và Android Chrome thực tế hoặc thiết bị từ xa tương đương.

## Ràng buộc

- Kho mã hiện chỉ có HTML/CSS/JS và ảnh; chưa có build tool, package manifest, backend hay test harness.
- `localStorage` có thể bị chặn và có hành vi không đáng tin cậy ở `file:`; nghiệm thu lưu trữ trên địa chỉ HTTP(S).
- Có nội dung kỹ thuật dài, bảng và sơ đồ ASCII; không được che nội dung để đạt “không tràn ngang”.

## Câu hỏi dành cho phase sau

- Nhiều màu đánh dấu và ghi chú riêng có cần thiết không? Mặc định đưa vào Phase 2 sau khi có dữ liệu sử dụng.
- Có cần viết riêng các trang Hướng dẫn/Linh kiện/Phụ lục không? Phase 1 xử lý các liên kết hỏng bằng đích đã có; biên tập trang mới cần nội dung riêng.

## Milestone hình minh họa (Phase 4–6)

Quyết định ngày 2026-10-02: biên tập hình cho 56 bài theo `docs/brainstorm/session-2026-10-02-visuals.md`. Đợt này cho phép sửa văn bản kỹ thuật gắn với hình, thay cho giới hạn không viết lại bài của Phase 1–3. Kết hợp ảnh thật CC0/miền công cộng được xác minh theo tệp với SVG tự tạo; mỗi bài có hình sát nội dung, caption/alt rõ và nguồn. Rà 80 sơ đồ ASCII, ưu tiên sơ đồ nguồn, pinout, tải cảm và pin LiPo. Thêm infographic, sơ đồ khối và sơ đồ tư duy cho bài phù hợp.
