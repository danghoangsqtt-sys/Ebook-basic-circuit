# Theo dõi tiến độ

- Cập nhật: 2026-10-02
- Trạng thái: đang triển khai Phase 1
- Phase hiện tại: Phase 1
- Việc kế tiếp: P1-02
- Phiên bản phát hành: chưa có

## Tổng quan

| Phase | Tổng nhiệm vụ | Hoàn tất | Trạng thái |
| --- | ---: | ---: | --- |
| Phase 1 | 8 | 1 | Đang thực hiện |
| Phase 2 | 3 | 0 | Chờ Phase 1 |
| Phase 3 | 2 | 0 | Chờ Phase 2 / cổng quyết định |

## Phase 1

| ID | Việc | Trạng thái | Bằng chứng nghiệm thu |
| --- | --- | --- | --- |
| P1-01 | Đo hiện trạng và kiểm tra liên kết | PASS | `docs/qa/baseline-phase1.md`; 57 trang, 479 tham chiếu, 73 link hỏng, 16 phép đo Chromium; fixture exit 1/0 đúng |
| P1-02 | Trang mở đầu | Đang thực hiện | Hợp đồng `phases/phase-1/tasks/P1-02.md` |
| P1-03 | Khung đọc mobile | Đang thực hiện | Hợp đồng `phases/phase-1/tasks/P1-03.md` |
| P1-04 | Thanh kéo cỡ chữ | Chưa bắt đầu | — |
| P1-05 | Chỉ mục và tìm kiếm nội bộ | Chưa bắt đầu | — |
| P1-06 | Chọn chữ và tra cứu | Chưa bắt đầu | — |
| P1-07 | Bút đánh dấu | Chưa bắt đầu | — |
| P1-08 | Liên kết và nghiệm thu | Chưa bắt đầu | — |

## Phase 2

| ID | Việc | Trạng thái |
| --- | --- | --- |
| P2-01 | Thư viện đoạn đã đánh dấu | Chờ |
| P2-02 | Tìm kiếm nâng cao | Chờ |
| P2-03 | Quyết định nhiều màu và ghi chú | Chờ |

## Phase 3

| ID | Việc | Trạng thái |
| --- | --- | --- |
| P3-01 | Xuất/nhập dữ liệu đọc | Chờ |
| P3-02 | Cổng quyết định tài khoản/đồng bộ | Chờ |

## Decision log

| Ngày | Quyết định |
| --- | --- |
| 2026-10-02 | Trang đầu giới thiệu gọn và lộ trình 8 tuần |
| 2026-10-02 | Tìm trong 56 bài trước; liên kết nguồn ngoài là bước bổ sung |
| 2026-10-02 | Giữ HTML/CSS/JavaScript thuần cho Phase 1–2 |
| 2026-10-02 | Bản quyền riêng; chưa chọn giấy phép, chưa tạo LICENSE |

## Nhật ký kiểm tra

Chưa có mã Phase 1 để nghiệm thu. Chỉ xác nhận cấu trúc tài liệu kế hoạch và bản mẫu giao diện ở bước crystallize.

2026-10-02 P1-01: `python tools/check_links.py` trả exit 1 đúng kỳ vọng vì 73 link hỏng thuộc 4 đích thiếu; fixture độc lập kiểm tra exit 1/0. Chromium 148 đo `index.html`, Bài 1, 28, 56 ở 320/360/390/430 px. Bài 1 tràn đến 714 px; trang đầu có nav bị cắt dù toàn trang không cuộn ngang. Chi tiết trong `docs/qa/baseline-phase1.md`. Chưa kiểm thử thiết bị thật.
