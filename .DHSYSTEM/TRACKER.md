# Theo dõi tiến độ

- Cập nhật: 2026-10-03
- Trạng thái: Phase 1–6 hoàn tất; milestone hình minh họa đã audit/debug PASS
- Phase hiện tại: Hoàn tất Phase 6
- Việc kế tiếp: Không có trong kế hoạch đã chốt
- Phiên bản phát hành: chưa có

## Tổng quan

| Phase | Tổng nhiệm vụ | Hoàn tất | Trạng thái |
| --- | ---: | ---: | --- |
| Phase 1 | 8 | 8 | Hoàn tất; audit/debug PASS |
| Phase 2 | 3 | 3 | Hoàn tất; audit/debug PASS |
| Phase 3 | 2 | 2 | Hoàn tất; audit/debug PASS |
| Phase 4 | 4 | 4 | Hoàn tất; audit/debug PASS |
| Phase 5 | 4 | 4 | Hoàn tất; audit/debug PASS |
| Phase 6 | 2 | 2 | Hoàn tất; audit/debug PASS |

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
| P4-01 | PASS | 56 bài/3 img/4 tài sản/80 ASCII; fixture 3 lỗi phát hiện đúng |
| P4-02 | PASS | 80/80 sơ đồ phân loại; 31 nhóm phát hiện; `docs/qa/visual-technical-audit.md` |
| P4-03 | PASS | `docs/qa/visual-prototype.md`; 8 mobile cases, caption 24px, QA Chromium |
| P4-04 | PASS | 31/31 nhóm lỗi đã sửa; `docs/qa/visual-technical-fixes.md`; QA Chromium và cổng link/asset/index đạt |
| P5-01 | PASS | 14 SVG và 4 ảnh thật đã kiểm giấy phép; `docs/qa/visual-week1-2.md`; 42 ca mobile/desktop, link/asset/index PASS |
| P5-02 | PASS | 14 SVG, ba ảnh CC0; `docs/qa/visual-week3-4.md`; 42 ca viewport và cổng link/asset/index PASS |
| P5-03 | PASS | 14 SVG và ba ảnh CC0; `docs/qa/visual-week5-6.md`; 42 ca viewport và cổng link/asset/index PASS |
| P5-04 | PASS | 14 SVG, ảnh ESP32 CC0; `docs/qa/visual-week7-8.md`; 56/56 bài và 168 ca viewport PASS |
| P6-01 | PASS | 12 SVG, bản diễn giải chữ; `docs/qa/visual-summaries.md`; 36 ca viewport và 12 SVG bounds PASS |
| P6-02 | PASS | `docs/qa/visual-final.md`; 56/56 bài, 280 ca viewport, Chromium/WebKit 24 px PASS |

2026-10-02 P4-01: `python tools/check_visuals.py` 0 lỗi; fixture thiếu alt, ảnh, nguồn đều trả exit 1. Baseline `docs/qa/visual-baseline.md`.

2026-10-02 P4-02: rà 80 sơ đồ ở 56 bài; 36 ưu tiên cao, 29 vừa, 15 thấp. Ghi 31 nhóm lỗi/điểm sửa kỹ thuật, ưu tiên mạch nguồn, pinout, flyback, bus và bảo vệ GPIO.

2026-10-02 P4-03: quy chuẩn `docs/visuals/VISUAL-GUIDE.md`; Bài 1–2 hiển thị tốt ở 320–430px/24px, 0 tràn, 0 asset hỏng, search index tạo lại.

2026-10-03 P4-04: sửa 31 nhóm lỗi kỹ thuật trên 34 bài, kể cả đáp án Zener còn mâu thuẫn khi audit lại. 59 trang/490 liên kết nội bộ 0 hỏng; 56 bài/80 sơ đồ ASCII/4 tài sản ảnh 0 lỗi; search index 56 bài còn mới; Chromium quick PASS. Chi tiết `docs/qa/visual-technical-fixes.md`. Phase 4 audit/debug PASS trong phạm vi kiểm tra tài liệu, không thay thế thử phần cứng thật.

2026-10-03 P5-01: 14/14 bài của tuần 1–2 có sơ đồ riêng, 4 ảnh thật đã kiểm CC0/miền công cộng trên trang tệp và lưu WebP. 42 ca Chromium 320/390/1280 px PASS; 59 trang/508 tham chiếu cục bộ 0 hỏng; chỉ mục mới, Chromium quick PASS. Chi tiết `docs/qa/visual-week1-2.md`.

2026-10-03 P5-02: 14/14 bài tuần 3–4 có sơ đồ riêng, 3 ảnh BJT/MOSFET/DHT22 CC0 với giới hạn diễn giải ghi ngay ở caption. 42 ca viewport PASS; 59 trang/525 tham chiếu 0 hỏng; chỉ mục và Chromium quick PASS. Chi tiết `docs/qa/visual-week3-4.md`.

2026-10-03 P5-03: 14/14 bài tuần 5–6 có sơ đồ riêng, 3 ảnh Digimess/PCB/cell Li-ion CC0. Loại ảnh động cơ bước sai loại trước tích hợp; sửa sơ đồ Bài 42 về TB6612FNG. 42 ca viewport PASS; 59 trang/542 tham chiếu 0 hỏng; chỉ mục và Chromium quick PASS. Chi tiết `docs/qa/visual-week5-6.md`.

2026-10-03 P5-04: 14/14 bài tuần 7–8 có sơ đồ riêng, ảnh bo ESP-WROOM-32 CC0. 56/56 bài có hình; 168 ca viewport 320/390/1280 px PASS, 59 trang/557 tham chiếu 0 hỏng, index và Chromium quick PASS. Chi tiết `docs/qa/visual-week7-8.md`.

2026-10-03 Audit Phase 5: Tier 1 và Tier 3 PASS; Tier 2 phát hiện README/kiến trúc cũ, `dh-debug` đã sửa và lưu phiên. 56 SVG đúng spec, 56/56 bài có hình, 168 ca viewport PASS, 0 link/asset hỏng; xem `.DHSYSTEM/audit-report.md`. Phase 5 hoàn tất; chuyển P6-01.

2026-10-03 P6-01: thêm 12 sơ đồ tổng hợp cuối bài kèm bản chữ, ánh xạ từng nhánh/khối tới đề mục. Sửa tổng quan Bài 55 để bốn nhóm bao phủ đúng năm hướng học trong bài. 12 SVG không cắt chữ; 36 ca viewport PASS; 56/56 bài có hình, 82 phần tử ảnh/83 tài sản, 59 trang/569 tham chiếu 0 hỏng, index và Chromium quick PASS. Chi tiết `docs/qa/visual-summaries.md`.

2026-10-03 P6-02: nghiệm thu 56/56 bài, 83 tài sản/83 bản ghi nguồn, 280 ca viewport; Chromium/WebKit mỗi loại 36 ca sơ đồ tại 24 px với bản chữ mở đều PASS. `dh-debug` sửa tràn Bài 7 ở 320 px do chuỗi mã màu không ngắt; tăng tương phản nguồn ảnh. Chromium toàn bộ luồng và WebKit mẫu PASS, 569 liên kết 0 hỏng, chỉ mục hiện hành. Chi tiết `docs/qa/visual-final.md`.

2026-10-03 Audit Phase 6: Tier 1 PASS; Tier 2 sửa số nhánh 49/49 trên 12 sơ đồ; Tier 3 thêm đối chiếu bài dùng ảnh trong manifest và fixture phát hiện sai bài. Các cổng asset/link/index/Chromium/WebKit PASS; xem `.DHSYSTEM/audit-report.md`. Phase 6 và milestone hình Phase 4–6 hoàn tất.
