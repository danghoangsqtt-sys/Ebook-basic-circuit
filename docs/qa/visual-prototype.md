# Nghiệm thu mẫu hình Bài 1–2 — P4-03

Ngày: 2026-10-02. Phục vụ website tĩnh qua HTTP cục bộ bằng `ThreadingHTTPServer`; kiểm tra bằng Playwright Chromium.

## Nội dung mẫu

- Bài 1: sơ đồ điện tích SVG có bản dọc riêng cho màn hình ≤600 px và ảnh thật đồng hồ DT830D từ nguồn CC0.
- Bài 2: ảnh hai mặt breadboard 400 lỗ từ nguồn CC0, chú thích rõ đây là ảnh minh họa nguyên lý cho bài học về loại 830 lỗ.
- Tất cả hình có alt text, kích thước và mục nguồn trong `assets/images/lessons/SOURCES.md`. Caption dùng biến cỡ chữ vùng đọc.

## Kết quả trình duyệt

| Trang | Rộng 320 | 360 | 390 | 430 | Mức chữ 24 px |
| --- | --- | --- | --- | --- | --- |
| Bài 1 | 2 ảnh tải, không tràn | Đạt | Đạt | Đạt | Chú thích 24 px, không tràn |
| Bài 2 | 1 ảnh tải, không tràn | Đạt | Đạt | Đạt | Chú thích 24 px, không tràn |

Ảnh có `loading="lazy"`, nên phép thử cuộn đến từng ảnh và đợi `img.decode()` trước khi xác nhận `naturalWidth > 0`. Ở 1280 px, cả hai trang tải ảnh và không tràn trong theme tối/sáng. Trên điện thoại, `<picture>` của Hình 1.1 chọn `charge-carriers-mobile.svg`.

## Lệnh kiểm tra

- `python tools/check_visuals.py`: 56 bài, 2 bài có hình, 3 `<img>`, 4 tệp hình, 80 ASCII, 0 lỗi ở thời điểm mẫu.
- `python tools/check_links.py`: mọi tham chiếu nội bộ hợp lệ.
- `python tools/build_search_index.py --check`: chỉ mục khớp HTML sau khi sửa Bài 1–2.
- `python tools/qa_browser.py --quick`: hồi quy trang chủ, bài học đại diện và công cụ đọc.

Giới hạn: chưa có thiết bị iOS/Android thật và chưa có người học hoặc kỹ sư điện tử độc lập duyệt hình. Các mạch có lỗi trong `visual-technical-audit.md` chưa được coi là mẫu để vẽ lại.
