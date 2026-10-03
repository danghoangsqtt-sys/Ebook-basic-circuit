# Hướng dẫn đọc dự án cho tác nhân triển khai

## Đọc theo thứ tự

1. `PROJECT-CONTEXT.md`: phạm vi đã chốt, người dùng và quy tắc sản phẩm.
2. `ROADMAP.md`: nhiệm vụ theo thứ tự, phụ thuộc và nghiệm thu.
3. `ARCHITECTURE.md`: ranh giới module, dữ liệu và các quyết định kỹ thuật.
4. `SYSTEM-RULES.md`: quy tắc sửa mã và kiểm tra.
5. `TRACKER.md`: tiến độ thật trước khi nhận việc.
6. `ui-direction/2026-10-02/index.html`, `pages/home.html`, `pages/reader.html`, `notes.md`, `design.md`: mẫu giao diện đã chốt về hướng; các nút đánh dấu/tra cứu trong mẫu vẫn là minh họa.
7. `STAKEHOLDER-REVIEW.md`: các lỗ hổng đã được đưa vào điều kiện nghiệm thu.

## Bản đồ mã hiện tại

| Vùng | Tệp |
| --- | --- |
| Trang đầu | `../index.html` |
| Bài học | `../week1/day01.html` … `../week8/day56.html` |
| CSS chung | `../assets/css/style.css` |
| Điều hướng/tương tác chung | `../assets/js/main.js`, `../assets/js/sidebar-data.js` |
| Phiên brainstorm gốc | `../docs/brainstorm/session-2026-10-02.md` |

## Trạng thái quyết định

- Trang đầu: giới thiệu gọn, nhấn lộ trình 8 tuần.
- Tìm liên quan: 56 bài nội bộ trước, nguồn ngoài sau.
- Giữ website tĩnh; không có DHSYSTEM profile tổ chức.
- Bản quyền riêng, chưa cấp giấy phép; không thêm LICENSE.

## Cập nhật tiến độ

Chỉ đánh dấu nhiệm vụ hoàn tất trong `TRACKER.md` sau khi có bằng chứng theo tiêu chí của ROADMAP. Giữ `HANDOFF.json` cùng trạng thái với tracker.

## Đợt hình minh họa

Đọc `../docs/brainstorm/session-2026-10-02-visuals.md`, `../docs/brainstorm/visual-inventory-2026-10-02.md`, `phases/phase-4/` đến `phase-6/` và `../assets/images/lessons/SOURCES.md` trước khi làm hình. Giữ bản quyền riêng, chỉ nhận ảnh CC0/miền công cộng đã xác minh trên trang tệp.

## Đợt tái biên soạn Phase 7–10

Đọc `../docs/brainstorm/session-2026-10-03-curriculum-rebuild.md`, `CURRICULUM-PLAN.md` và trạng thái `TRACKER.md`/`HANDOFF.json`. Phase 1–6 đã đóng; P7–P10 có bằng chứng qua cổng nội dung số/mô hình tại `docs/qa/curriculum-final.md`, còn nghiệm thu phần cứng và reviewer trong sổ pending. Bộ 32 bài đã được xuất bản theo giả định phạm vi của P7-01; board thực hành cụ thể chưa được cung cấp. Sau mỗi Phase chạy `dh-audit`, dùng `dh-debug` khi có lỗi rồi mới tiến.
