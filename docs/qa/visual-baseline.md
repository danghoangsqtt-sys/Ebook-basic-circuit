# Baseline hình minh họa — Phase 4

Ngày đo: 2026-10-02. Nguồn: 56 bài `week1/day01.html` đến `week8/day56.html`.

| Chỉ số | Hiện trạng |
| --- | ---: |
| Trang bài học | 56 |
| Trang có ít nhất một ảnh nội dung | 2 |
| Phần tử `<img>` trong bài | 3 |
| Tài sản hình riêng biệt, gồm bản mobile | 4 |
| Khối `circuit-ascii` cần rà kỹ thuật | 80 |

Ba ảnh nội dung hiện nằm ở Bài 1–2: hai ảnh chụp nguồn CC0 và sơ đồ điện tích tự vẽ có bản ngang/dọc. Chúng là mẫu trước khi triển khai hàng loạt. Các icon SVG trong thanh điều hướng là thành phần giao diện, không tính là minh họa bài học.

## Kết quả kiểm tra

- `python tools/check_visuals.py`: 56/56 trang, 2 trang có hình, 3 `<img>`, 4 tài sản, 80 sơ đồ ký tự, **0 lỗi**.
- Bộ kiểm tra nhận lỗi thử nghiệm trên bản sao tạm: thiếu alt, tệp ảnh không tồn tại và tệp không có bản ghi nguồn đều trả mã 1.
- `python tools/check_links.py`: tham chiếu nội bộ hợp lệ. Hai ảnh WebP khoảng 140–146 KB mỗi tệp; SVG tự vẽ nhỏ.

## Rủi ro cần giải quyết

1. 54 bài chưa có minh họa nội dung. Phase 5 sẽ bổ sung hình theo danh mục đã biên tập; Phase 6 buộc kiểm tra `--require-all`.
2. 80 sơ đồ ký tự chưa được xác thực toàn bộ. P4-02 phải phân loại trước khi quyết định giữ, sửa hay thay bằng SVG.
3. Ảnh thiết bị thật phải khớp model trong bài. Bài 1–2 đã sửa model DT830D và ghi rõ ảnh breadboard 400 lỗ chỉ minh họa nguyên lý của loại 830 lỗ.
4. Chưa có kiểm thử thiết bị thật hay người soát kỹ thuật độc lập; các sơ đồ nguồn, pin và tải cảm cần kiểm tra chặt trước khi xuất bản.
