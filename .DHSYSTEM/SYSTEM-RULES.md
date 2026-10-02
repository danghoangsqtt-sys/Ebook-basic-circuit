# Quy tắc triển khai

## Kiến trúc

- Giữ HTML, CSS, JavaScript thuần cho Phase 1–2. Không thêm framework hay backend để giải quyết việc hiển thị và công cụ đọc.
- Tính năng dùng chung đặt trong `assets/`; tránh sao chép 56 phiên bản logic vào các trang bài.
- Tạo chỉ mục tìm kiếm từ nội dung nguồn trong `week*/day*.html`; không duy trì thủ công danh sách thứ hai dễ lệch.
- Tính năng mới phải hoạt động khi `localStorage` thất bại, chỉ mất khả năng lưu trạng thái.

## HTML và CSS

- Dùng phần tử có ngữ nghĩa, nhãn điều khiển rõ, thứ tự tab tự nhiên và trạng thái focus nhìn thấy được.
- Bố cục nền ở 320 CSS px là một cột; thêm cột khi đủ chỗ. Tránh chiều rộng cố định buộc cuộn ngang toàn trang.
- Bảng, mã, công thức và sơ đồ ASCII rộng được cuộn trong khung riêng; cho biết cách cuộn nếu cần.
- Cỡ chữ người đọc điều chỉnh chỉ áp vào vùng bài, không phóng header/menu.
- Tối ưu khoảng bấm trên mobile khoảng 44 × 44 CSS px; tối thiểu đáp ứng WCAG 2.2 target size khi áp dụng.

## JavaScript và dữ liệu

- Không dùng `innerHTML` với đoạn người dùng chọn hay dữ liệu lưu; đưa văn bản qua `textContent`.
- Tạo URL ngoài bằng `URL`/`URLSearchParams`; mở bằng liên kết có `rel="noopener noreferrer"`.
- Chỉ đọc Selection nằm trong vùng nội dung được phép và có độ dài hợp lý; không đọc từ form hay điều hướng.
- Dấu đánh dấu lưu theo cấu trúc có `version`, `lessonId`, `quote`, ngữ cảnh và thông tin vị trí. Xác minh lại đoạn trích trước khi tô.
- Không chặn chuột phải khi người dùng chưa chọn đoạn trong bài. Menu thao tác chọn chữ dùng được bằng bàn phím, có nút đóng.
- Dấu đánh dấu có biểu đạt bằng chữ/danh sách và trạng thái cho công nghệ hỗ trợ; màu chỉ là tín hiệu bổ sung.

## Chất lượng

- Mỗi nhiệm vụ có kiểm tra theo ROADMAP. Test tự động tập trung vào tìm kiếm, neo dấu, liên kết và di chuyển bàn phím; kiểm tra giao diện bằng viewport thực tế hoặc browser automation.
- Trước khi hoàn thành Phase 1, kiểm tra Bài 1, một bài giữa giáo trình và Bài 56; mỗi loại có bảng/sơ đồ dài nếu có.
- Kiểm tra ở 320, 360, 390, 430 px, desktop, zoom 200% và khi chữ kéo tới mức lớn nhất.
- Commit theo Conventional Commits khi làm tính năng; ghi thay đổi hướng người dùng trong `CHANGELOG.md` theo Keep a Changelog.
- Phiên bản khi phát hành theo SemVer; hiện chưa có tag/version, không tự tuyên bố bản phát hành.

## Mẫu chú thích

- Tốt: `// Quote khớp nhưng ngữ cảnh khác: bỏ qua để tránh tô sai sau khi bài được sửa.`
- Tránh: `// Tìm quote.` khi dòng kế tiếp đã cho thấy việc tìm kiếm.

## Nguồn kỹ thuật

Xem `.DHSYSTEM/STACKS.md` và cache `static-web` để biết thực hành, điểm cần tránh và nguồn chính thức.
