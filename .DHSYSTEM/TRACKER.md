# Theo dõi tiến độ

- Cập nhật: 2026-10-02
- Trạng thái: Phase 1–3 hoàn tất; Phase 4–6 hình minh họa đã lên kế hoạch
- Phase hiện tại: Phase 4 (in_progress)
- Việc kế tiếp: P4-01
- Phiên bản phát hành: chưa có

## Tổng quan

| Phase | Tổng nhiệm vụ | Hoàn tất | Trạng thái |
| --- | ---: | ---: | --- |
| Phase 1 | 8 | 8 | Hoàn tất; audit/debug PASS |
| Phase 2 | 3 | 3 | Hoàn tất; audit/debug PASS |
| Phase 3 | 2 | 2 | Hoàn tất; audit/debug PASS |
| Phase 4 | 3 | 0 | Đã lên kế hoạch |
| Phase 5 | 4 | 0 | Đã lên kế hoạch |
| Phase 6 | 2 | 0 | Đã lên kế hoạch |

## Phase 1

| ID | Việc | Trạng thái | Bằng chứng nghiệm thu |
| --- | --- | --- | --- |
| P1-01 | Đo hiện trạng và kiểm tra liên kết | PASS | `docs/qa/baseline-phase1.md`; 57 trang, 479 tham chiếu, 73 link hỏng, 16 phép đo Chromium; fixture exit 1/0 đúng |
| P1-02 | Trang mở đầu | PASS | 8 tuần, 56 link bài có thật; Chromium 320–1280 px không tràn; menu click/Enter/Escape, skip link; anchor chuẩn bị Bài 1 |
| P1-03 | Khung đọc mobile | PASS | Chromium Bài 1/28/56 ở 320–430 px và viewport zoom 200%; không tràn; sidebar 8 tuần/56 bài, Escape/focus |
| P1-04 | Thanh kéo cỡ chữ | PASS | Playwright HTTP: 24 px/reload/reset/ArrowLeft, storage bị chặn, Bài 1 ở 160–430 px không tràn |
| P1-05 | Chỉ mục và tìm kiếm nội bộ | PASS | `build_search_index.py --check` 56 bài; Playwright Bài 1/28/56, có/không dấu, câu dài, không kết quả, Escape/focus |
| P1-06 | Chọn chữ và tra cứu | PASS | Chromium desktop/mobile 320–430; WebKit mobile; menu/Google/YouTube/tìm bài, Escape/focus; chưa thiết bị thật |
| P1-07 | Bút đánh dấu | PASS | Chromium+WebKit chọn xuyên inline, lưu/reload/xóa/jump; quote trùng, mất neo, storage lỗi; chưa điện thoại thật |
| P1-08 | Liên kết và nghiệm thu | PASS | 0 link hỏng; Chromium 56 bài, WebKit mẫu; `docs/qa/phase1-results.md` |

## Phase 2

| ID | Việc | Trạng thái |
| --- | --- | --- |
| P2-01 | Thư viện đoạn đã đánh dấu | PASS |
| P2-02 | Tìm kiếm nâng cao | PASS |
| P2-03 | Quyết định nhiều màu và ghi chú | PASS — hoãn tính năng |

## Phase 3

| ID | Việc | Trạng thái |
| --- | --- | --- |
| P3-01 | Xuất/nhập dữ liệu đọc | PASS |
| P3-02 | Cổng quyết định tài khoản/đồng bộ | PASS — hoãn backend |

## Decision log

| Ngày | Quyết định |
| --- | --- |
| 2026-10-02 | Trang đầu giới thiệu gọn và lộ trình 8 tuần |
| 2026-10-02 | Tìm trong 56 bài trước; liên kết nguồn ngoài là bước bổ sung |
| 2026-10-02 | Giữ HTML/CSS/JavaScript thuần cho Phase 1–2 |
| 2026-10-02 | Bản quyền riêng; chưa chọn giấy phép, chưa tạo LICENSE |
| 2026-10-02 | Giữ bút đánh dấu một màu và schema v1; hoãn nhiều màu/ghi chú vì chưa có nhu cầu được xác nhận |
| 2026-10-02 | Hoãn tài khoản/đồng bộ vì chưa xác nhận nhu cầu nhiều thiết bị hoặc điều kiện riêng tư/chi phí; dùng JSON để chuyển dữ liệu |

## Nhật ký kiểm tra

Phase 1 đã triển khai; bằng chứng nghiệm thu theo từng nhiệm vụ và `docs/qa/phase1-results.md`.

2026-10-02 P1-01: `python tools/check_links.py` trả exit 1 đúng kỳ vọng vì 73 link hỏng thuộc 4 đích thiếu; fixture độc lập kiểm tra exit 1/0. Chromium 148 đo `index.html`, Bài 1, 28, 56 ở 320/360/390/430 px. Bài 1 tràn đến 714 px; trang đầu có nav bị cắt dù toàn trang không cuộn ngang. Chi tiết trong `docs/qa/baseline-phase1.md`. Chưa kiểm thử thiết bị thật.

2026-10-02 P1-02: trang chủ mới có hero, cách học, lộ trình 8 tuần và danh sách 56 bài từ `CURRICULUM`; Playwright Chromium ở 320/360/390/430/768/1280 px không tràn ngang, không lỗi JS. Kiểm tra menu click/Enter/Escape và skip link; liên kết dụng cụ mở anchor thật trong Bài 1. `node --check assets/js/home.js` đạt. 62 link hỏng còn lại nằm trong trang bài, xử lý ở P1-08.

2026-10-02 P1-03: Chromium trên Bài 1/28/56 tại 320/360/390/430 px và mức viewport quy đổi zoom 200% không tràn ngang; bảng/sơ đồ cuộn riêng. Sidebar có 8 tuần/56 bài, nút tuần và menu hỗ trợ Enter/Escape, focus quay về nút menu. `node --check assets/js/main.js` và `sidebar-data.js` đạt. Thiết bị thật chưa kiểm tra.

2026-10-02 P1-04: Chromium trên HTTP xác nhận slider 16–24 px đổi chữ vùng bài ngay, giữ header, reload và reset đúng; ArrowLeft hoạt động. Storage bị chặn vẫn điều chỉnh được, không lỗi JS. Bài 1 ở 24 px tại 160/180/195/215/320/360/390/430 px không tràn ngang.

2026-10-02 P1-05: chỉ mục sinh từ 56 HTML (420691 byte); `python tools/build_search_index.py --check` đạt. Playwright Chromium trên Bài 1/28/56 xác nhận tìm `dien ap` ra Bài 1 đầu, URL đúng từ từng tuần, không kết quả có hướng dẫn, Escape đóng và trả focus. Tác vụ xây chỉ mục kiểm tra thêm truy vấn có dấu/câu dài ở 320/360 px.

2026-10-02 P1-06: chọn chữ và mở menu bằng chuột phải, phím hoặc cảm ứng mô phỏng; ba lệnh Google/YouTube/tìm bài hoạt động. Lỗi menu tự đóng khi focus gây scroll được sửa và kiểm tra lại trên Chromium 320–430 px; WebKit mobile mô phỏng cảm ứng đã mở menu và chạy tra cứu nội bộ/Google. Chưa thử long press trên iOS/Android thật.

2026-10-02 P1-07: Chromium+WebKit tích hợp trên Bài 1 xác nhận tô/lưu/tải lại/nhảy đến/xóa. Chọn xuyên `<em>` tạo các mảnh mark chung một bản ghi. Chromium kiểm tra quote trùng bị từ chối, sửa nội dung thành mất neo, storage bị chặn không tô nhầm, `?highlight=<id>` và Enter. Dữ liệu chỉ trên thiết bị; chưa thử nhấn giữ trên điện thoại thật.

2026-10-02 P1-08: `check_links.py` 57 trang/470 tham chiếu, 0 lỗi file/fragment/escape. `qa_browser.py` Chromium kiểm tra 56 bài ở 320 px và các viewport 160–430 px ở 24 px cho Bài 1/28/56; WebKit kiểm tra mẫu. Sửa khối báo cáo Bài 7 tràn ngang. Menu, slider, tiến độ, checklist, đáp án, in, tìm kiếm, đánh dấu, theme đều qua kiểm tra. Thiết bị thật chưa kiểm tra.

2026-10-02 Audit Phase 1: Tier 1 và Tier 3 PASS; Tier 2 thấy mô tả kiến trúc còn ở thì tương lai, `dh-debug` đã sửa và lưu session. Báo cáo `.DHSYSTEM/audit-report.md`. Phase 1 hoàn tất.

2026-10-02 P2-01: trang thư viện dấu xuyên bài, lọc theo đoạn/bài/trạng thái; kiểm tra neo qua HTML của bài, không nhảy vào dấu mất neo; xóa một dấu không ảnh hưởng dấu khác. Chromium và WebKit kiểm tra hai bài/4 viewport; `check_links.py` quét 58 trang/479 tham chiếu, 0 lỗi. Chi tiết `docs/qa/highlight-library.md`.

2026-10-02 P2-02: 7 truy vấn tiếng Việt/Anh được chạy trên Bài 1/28/56 trong `qa_browser.py`; kết quả đầu đúng bài, có đề mục/đoạn trích. Chromium toàn bộ 56 bài và WebKit mẫu qua kiểm tra; chỉ mục còn mới. P2-03 quyết định hoãn nhiều màu/ghi chú, không đổi dữ liệu dấu v1.

2026-10-02 Audit Phase 2: Tier 1 và Tier 3 PASS; Tier 2 thấy kiến trúc thiếu thư viện dấu, `dh-debug` đã cập nhật tài liệu và bốn sidecar Mermaid; chúng khớp nhau. Báo cáo `.DHSYSTEM/audit-report.md`. Phase 2 hoàn tất.

2026-10-02 P3-01: xuất/nhập JSON khôi phục dấu, cỡ chữ, theme, tiến độ và checklist. Kiểm tra tệp sai, thiếu trường, version cũ, ngày sai, quote dài, xung đột ID và lỗi ghi giữa chừng; Chromium toàn bộ 56 bài, WebKit mẫu; trang sao lưu ở 320–430 px không tràn. 59 trang/487 link nội bộ, 0 lỗi. P3-02 hoãn backend vì chưa có nhu cầu/điều kiện được xác nhận; JSON là cách chuyển dữ liệu hiện hoạt.

2026-10-02 Audit Phase 3: Tier 1 PASS; Tier 2 thiếu module sao lưu trong kiến trúc, `dh-debug` đã cập nhật sơ đồ và bốn sidecar Mermaid. Tier 3 phát hiện `Date.parse` chấp nhận ngày 31/02; `dh-debug` sửa kiểm tra lịch và thêm ca hồi quy. Chromium toàn bộ 56 bài và WebKit mẫu qua lại; `check_links.py` 59 trang/487 tham chiếu, 0 lỗi; chỉ mục còn mới. Báo cáo `.DHSYSTEM/audit-report.md`. Phase 3 hoàn tất.

## Phase 4–6 — Đợt hình minh họa

Nguồn `docs/brainstorm/session-2026-10-02-visuals.md`; hai ảnh CC0 và hai SVG Bài 1–2 là mẫu thực hiện trước khi mở milestone.

| Task | Trạng thái | Bằng chứng |
| --- | --- | --- |
| P4-01 | IN_PROGRESS | Đã ghi plan và bắt đầu cổng kiểm tra hình |
| P4-02 | PLANNED | — |
| P4-03 | PLANNED | — |
| P5-01 | PLANNED | — |
| P5-02 | PLANNED | — |
| P5-03 | PLANNED | — |
| P5-04 | PLANNED | — |
| P6-01 | PLANNED | — |
| P6-02 | PLANNED | — |
