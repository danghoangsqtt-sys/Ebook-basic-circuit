# Theo dõi tiến độ

- Cập nhật: 2026-10-04
- Trạng thái: Phase 1–6 hoàn tất; Phase 7–10 PASS trong phạm vi nội dung số/phân tích/mô hình có điều kiện; nghiệm thu phần cứng và reviewer còn pending
- Phase hiện tại: Phase 10 cổng nội dung số đã rà cuối; cổng phần cứng theo `docs/qa/curriculum-hardware-pending.md`
- Việc kế tiếp khi có thiết bị: chốt part/board/revision, dựng CAD và ERC/DRC, đo, reviewer ký từng mạch rủi ro; xem `docs/qa/curriculum-final.md`
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
| Phase 7 | 6 | 6 số / 4 đầy đủ | P7-04/P7-06 PASS nội dung số; phần cứng thật còn chờ |
| Phase 8 | 6 | 6 số / 0 phần cứng | P8-01…P8-06 PASS nội dung số; phần cứng thật còn chờ |
| Phase 9 | 5 | 5 số / 0 phần cứng | P9-01…P9-05 PASS nội dung số/mô phỏng; phần cứng pending |
| Phase 10 | 4 | 4 số / 0 phần cứng | P10-01…P10-04 qua cổng số; reviewer/CAD/đo còn chờ |

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
| 2026-10-03 | Lập kế hoạch Phase 7–10 theo giả định 56 bài cũ + khoảng 32 bài mới; số bài/độc giả/board chưa phải quyết định người dùng và phải xác nhận ở P7-01 |

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

## Phase 7–10 — Tái biên soạn giáo trình (cổng số đã rà cuối)

Nguồn task và tiêu chí: `.DHSYSTEM/CURRICULUM-PLAN.md`. Phase 7–10 có bằng chứng nội dung số tại `docs/qa/curriculum-final.md`; phần cứng thật chưa nghiệm thu. Báo cáo Phase 4–6 chỉ là kết quả QA hình cũ.

| Phase | Task | Trạng thái |
| --- | --- | --- |
| 7 | P7-01–P7-03/P7-05 PASS; P7-04/P7-06 PASS nội dung số, phần cứng pending | Qua cổng số, chưa nghiệm thu thiết bị thật |
| 8 | P8-01…P8-06 PASS nội dung số; phần cứng pending | `docs/qa/curriculum-phase8.md`; 16/16 bài, 75 trang/890 link, Chromium/WebKit, audit/debug |
| 9 | P9-01…P9-05 PASS nội dung số/mô phỏng; phần cứng pending | Qua cổng số; `docs/qa/curriculum-phase9.md` và audit/debug |
| 10 | P10-01…P10-04 PASS phạm vi số; reviewer/đo/CAD pending | `docs/qa/curriculum-phase10.md`, `docs/qa/curriculum-final.md`; audit/debug cuối |

Mỗi P7-06/P8-06/P9-05/P10-04 là cổng `dh-audit` và `dh-debug`; chỉ chuyển Phase sau khi lỗi chặn đã được sửa và bằng chứng được điền. Các câu hỏi còn mở về phạm vi, độc giả, toán, board và người duyệt nằm ở `CURRICULUM-PLAN.md`.

2026-10-03 P7-01: ma trận 56 bài/80 khối ASCII, đề cương 32 bài A01–A32, kiểm tiêu đề và vị trí đạt; commit `dded216` đã push. `docs/qa/curriculum-phase7.md` ghi giới hạn kiểm kê; P7-02 sẽ xác minh kỹ thuật từng sơ đồ.

2026-10-03 P7-02: đăng ký 80/80 khối hiện hành và 17 claim cần kiểm; 48 schematic, 4 waveform, 12 pinout/vật lý, 10 luồng, 6 văn bản tra. Sáu hình người dùng nêu còn lỗi đọc ASCII; lỗi điện học lịch sử không được tự coi là lỗi hiện hành. Commit `fe045a1` đã push, clean/0 ahead; xem `docs/qa/curriculum-phase7.md`.

2026-10-03 P7-03: thay sáu sơ đồ người dùng chỉ ra bằng SVG tự vẽ có bản chữ, sửa an toàn/GND/đo điện, lỗi d/e trên breadboard và đáy sóng AC; 74 ASCII còn lại. Reviewer độc lập rà hình học và phát hiện lỗi đã sửa. 56/56 bài có hình, 0/580 liên kết hỏng, search index mới, 9 ca viewport và 12 ca 24 px/theme PASS. Commit `e1df893` đã push, clean/0 ahead; xem `docs/qa/curriculum-phase7.md`.

2026-10-03 P7-05: đồng bộ 48 nhãn menu sai/lệch với `h1` thật; 56/56 URL giữ nguyên. Thêm `tools/check_navigation.py`; link 59 trang/656 tham chiếu 0 hỏng, chỉ mục 56 bài hiện hành, JS syntax PASS. Đã rà lại câu an toàn Bài 1 và nhận xét ký hiệu Bài 3. P7-04 đang đổi HTML nên sẽ chạy lại cổng trước P7-06; xem `docs/qa/curriculum-phase7.md`.

2026-10-03 P7-04 tiến độ: đã chuyển 80/80 khối ASCII thành 70 SVG + 10 HTML có bản chữ, 56/56 bài có hình; 168 ca viewport 24 px và 56 ca dark 320 px PASS, 59 trang/709 tham chiếu 0 hỏng. Rà kỹ thuật độc lập phát hiện và sửa nhiều lỗi P1/P2 trong sơ đồ, BOM, mức điện áp và mã ví dụ; chi tiết `docs/qa/curriculum-phase7.md` và phiên `dh-debug`. Chưa có board/module cụ thể, reviewer phần cứng, ERC/mô phỏng/đo cho toàn bộ mạch rủi ro; P7-04/P7-06 chưa nghiệm thu, không chuyển Phase 8.

2026-10-03 P7-04/P7-06 cổng nội dung số: đã đối chiếu sơ đồ ứng dụng và datasheet hãng ở `docs/curriculum/reference-circuit-review.md`, sửa thêm lỗi nguồn/giới hạn/tính toán tại D12/D13/D16/D19/D21/D23/D24/D30/D32/D36/D40/D42 và đồng bộ `coverage-matrix.csv`. Audit độc lập cuối không thấy P0/P1 trong vùng đã sửa; bốn lệch P2 đã sửa bằng `dh-debug`. 80 ID/17 claim locator, 56/56 ảnh, 709 link, 56 menu/search, 168 viewport 24 px, Chromium quick PASS. `docs/qa/curriculum-hardware-pending.md` giữ cổng part/module/revision, ERC/đo và người duyệt. Phase 8 được phép soạn nhánh số theo phụ lục `CURRICULUM-PLAN.md`, không được hiểu là Phase 7 đã chứng nhận mạch thật.

2026-10-03 P8-01: `docs/curriculum/advanced-phase8-syllabus.md` khóa 16 mã A01–A16, từng bài có outcome, tiên quyết/toán, thời lượng, ví dụ giải, hoạt động số, bài tập/đáp án/rubric và nguồn gốc. Kiểm cấu trúc 16/16 đủ trường/URL HTTPS PASS; bằng chứng `docs/qa/curriculum-phase8.md`. Chưa có 16 trang A01–A16 hoặc phép mô phỏng/đo thật.

2026-10-03 P8-02: A01–A04 và bốn SVG tự vẽ đã xuất bản; đối chiếu Vishay, TDK, Murata, Nichicon và mạch tham chiếu ADI/TI. Ma trận A01–A04, sổ nguồn hình và sổ mạch có giới hạn claim. 63 trang/754 liên kết 0 lỗi, menu 56+4, search 60, Chromium full 109 ca bài/viewport, WebKit quick và sao lưu/dấu A01 PASS. Audit `dh-audit` sửa ba lệch tài liệu qua `dh-debug`; không còn P0/P1 được xác nhận. Chưa có CSV SimSurfing, ERC hoặc đo mạch thật; xem `docs/qa/curriculum-phase8.md`.

2026-10-03 P8-03: A05–A08 và bốn SVG tự vẽ xuất bản; đối chiếu diode/LED/TVS Vishay/Nexperia/Littelfuse, Würth/ADI inductor/bead, MEAN WELL adapter, TI LM7805/LM2596 và Murata đúng mã tụ. Audit độc lập không thấy P0/P1; hai P2 điều hướng/trạng thái được sửa trong `session-phase8-p8-03-audit.json`. Chỉ phép tính giấy/bảng tính; chưa có ERC/SPICE/đo thật. Bằng chứng `docs/qa/curriculum-phase8.md`.

2026-10-03 P8-04: A09–A14 có sáu sơ đồ tự vẽ, ví dụ, hoạt động bảng tính và đáp án; OpenStax/MIT chứng minh phương pháp, ADI có mạch lab tham khảo. `verify_phase8_numeric.py` kiểm độc lập nghiệm DC, RC/RL và RLC; 73 trang/868 link 0 hỏng, menu 56+14, search 70, checker 14/14. Chromium full 189 ca bài/viewport và WebKit quick 136 ca cùng reader/library/backup PASS. Rà chéo không thấy P0/P1; hai P2 hình A09/A10 đã sửa và xác minh 320 px trong `session-phase8-p8-04-audit.json`. Không có SPICE/đo/PCB thật; xem `docs/qa/curriculum-phase8.md`.

2026-10-04 P8-05: A15–A16 và hai SVG tự vẽ đã xuất bản theo OpenStax §8.1/8.3/13.1 và TI SCAA082A §1.6; bảng tính trường/điện dung/đường hồi có `verify_phase8_fields.py` kiểm độc lập. Rà `dh-audit` phát hiện và `dh-debug` sửa điều kiện góc trường xoay so với cố định. 16/16 trang nâng cao, 75 trang/890 link 0 hỏng, menu 56+16, search 72; Chromium full 205 ca bài/viewport PASS, WebKit riêng A15/A16 320 px/24 px PASS. Chưa FEM/PCB/EMC đo, P8-06 chưa audit cuối; xem `docs/qa/curriculum-phase8.md`.

2026-10-04 P8-06 cổng Phase 8 số: đối chiếu 16 bài A01–A16 với syllabus/ma trận, mỗi bài có mục tiêu, hình/nguồn/mô tả, hoạt động số, bài tập và đáp án/rubric. Hai bộ tính độc lập cho mạch/trường PASS; 75 trang/890 link 0 hỏng, menu 56+16, search 72, 56 bài nền/80 ID, Chromium full 205 ca và WebKit 16 bài ở 320 px/24 px PASS. Audit `dh-audit` thấy README/ARCHITECTURE còn ghi 4 bài, `dh-debug` đã sửa; không còn P0/P1 xác nhận trong phạm vi số. Cổng phần cứng riêng vẫn pending, không có SPICE/FEM/ERC/đo thật; xem `docs/qa/curriculum-phase8.md`.

2026-10-04 P9-01: xuất bản A17–A21, năm SVG tự vẽ, đề cương và sổ nguồn TI/MIT. Audit `dh-audit` thấy A17 thiếu tính biên nhiễu, A20 Q cạnh 4 chưa thể quyết định, A21 hình FSM thiếu hướng; `dh-debug` đã sửa và ghi `session-phase9-p9-01-audit.json`. Phép tính/logic độc lập PASS: bốn/tám hàng chân trị, DFF/mod-4, FSM và setup 65 ns, biên A17 theo tải. 21/21 trang nâng cao, menu 56+21, search 77, 80 trang/940 link cục bộ 0 hỏng, Chromium full 245 ca bài/viewport; sau sửa Chromium/WebKit A17–A21 mỗi loại 15 ca mobile/24 px PASS. Phần cứng IC và timing closure thật pending; xem `docs/qa/curriculum-phase9.md`.

2026-10-04 P9-02: xuất bản A22–A24 và ba SVG tự vẽ, đối chiếu Pico board Rev3 reference/RP2040 với Espressif DevKitC-1 v1.2 và batch schematic; lab GP25 Pico non-W có host fake Pin PASS nhưng chưa nạp/đo board. Audit `dh-audit` sửa A22 ranh giới chip/flash và nhánh bus qua `dh-debug`; WebKit một lần hỏi đáp trả quá sớm, test chờ trạng thái rồi cả hai engine 24 bài × 3 viewport 24 px PASS. 24/24 bài nâng cao, menu 56+24, search 80, 83 trang/972 link 0 hỏng, Chromium full 269 ca bài/viewport và reader/library/backup PASS. Sổ QA và hardware pending ghi rõ phạm vi.

2026-10-04 P9-03: xuất bản A25–A28 và bốn SVG; ma trận bảy sensor IC trần theo ADI/TI/Bosch/ST, so công nghệ và ví dụ fit TMP36 trên dữ liệu tổng hợp. Audit `dh-audit` phát hiện lệch resolution/accuracy/mode của BMP280 và hình fit A28; `dh-debug` sửa theo datasheet Rev. 1.26, sửa thêm race ReaderData trong QA; `.DHSYSTEM/debug/session-phase9-p9-03-audit.json`. 28/28 bài nâng cao, menu 56+28, search 84, 87 trang/1012 link 0 hỏng, verify số học PASS, Chromium/WebKit riêng Phase 9 mỗi engine 36 ca ở 320/390/430 px/24px PASS, Chromium toàn site 301 ca bài/viewport và reader/library/backup PASS. Cổng sensor/board/chuẩn đo thật còn pending.

2026-10-04 P9-04/P9-05: lab Pico non-W/TMP36GT9Z có BOM, netlist, SVG, mã MicroPython, mô phỏng ADC lý tưởng và fake ADC/LED; trace `0,0,0,1,1,0,0,1` PASS. Audit phát hiện tụ C1 cắt TEMP_V, `dh-debug` sửa sơ đồ và kịch bản lượng tử; `.DHSYSTEM/debug/session-phase9-p9-04-audit.json`. Cổng số Phase 9: bốn verify P9 PASS, 28/28 bài, menu 56+28, search 84, 87 trang/1012 link 0 hỏng, 80 ID sơ đồ và 56/56 hình bài nền; Chromium/WebKit mỗi engine 36 ca Phase 9 mobile/24 px PASS. Phần cứng, chuẩn nhiệt, ADC thật và reviewer pending; tag checkpoint Phase 7–9 không đầy đủ nên audit Tier 1 ghi rõ thay vì tạo hồi tố. Xem `docs/qa/curriculum-phase9.md` và `.DHSYSTEM/audit-report.md`. Mở P10-01 nhánh số.

2026-10-04 P10-01/P10-02: A29–A32 và bốn chặng đồ án Pico/TMP36 xuất bản với hồ sơ yêu cầu/net/BOM/ngân sách/sai khác; `verify_phase10_design.py` PASS 10 ca ADC/VREF mô hình. Menu 56+32, search 88, bản đồ tiên quyết, 92 trang link nội bộ 0 hỏng; Chromium/WebKit mỗi engine 20 ca Phase 10 mobile/24 px PASS. Xem `docs/qa/curriculum-phase10.md`.

2026-10-04 P10-03/P10-04: ma trận yêu cầu → bài → bằng chứng tại `docs/qa/curriculum-final.md`; audit/debug cuối sửa stale state và skip link/focus 89 trang. Phase 8/9/10 verify PASS, 32/32 bài A, 56+32 menu, search 88, 92 trang/1189 tham chiếu 0 hỏng, 80 ID hình, 56/56 bài nền có hình, Chromium quick full và Chromium/WebKit Phase 10/a11y PASS. Không có P0/P1 đã xác nhận trong phạm vi số. `.DHSYSTEM/audit-report.md` kết luận cổng số PASS; nghiệm thu Phase 7–10 về phần cứng, CAD/ERC/DRC, đo và reviewer chưa đóng. Git tag checkpoint lịch sử không đầy đủ, không tạo hồi tố.

2026-10-04 P10-04 tiếp tục cổng vật lý: tạo `docs/qa/pico-tmp36-bringup.md`, CSV chỉ header và công cụ phân tích log đo với `hardware_accepted: false` cố định. Test tổng hợp tạm kiểm `no_data`, hysteresis on/hold/off, LED mismatch và bản ghi lỗi PASS; CSV hiện có 0 mẫu đo thật. Thiếu KiCad/ngspice trong môi trường và chưa có board/part/reviewer, nên CAD/ERC/DRC và nghiệm thu vật lý tiếp tục pending.
