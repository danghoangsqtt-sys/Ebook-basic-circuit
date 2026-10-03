# Kế hoạch nâng cấp website giáo trình điện tử

Ngày chốt: 2026-10-02. Nguồn phạm vi: `docs/brainstorm/session-2026-10-02.md`. Hướng màn hình: `.DHSYSTEM/ui-direction/2026-10-02/`.

Trạng thái 2026-10-04: Phase 1–6 đã hoàn tất; Phase 7–8 qua audit/debug trong phạm vi nội dung số/phân tích và hoạt động giấy/bảng tính có điều kiện. Cổng phần cứng thật vẫn chờ đúng part/module/revision, ERC/đo và người duyệt ở `docs/qa/curriculum-hardware-pending.md`. Phase 8 P8-01…P8-06 PASS nội dung số; Phase 9 P9-01…P9-03 PASS nội dung số A17–A28, P9-04 kế tiếp theo `CURRICULUM-PLAN.md`. Phase 10 chưa mở.

## Nguyên tắc thực hiện

- Hoàn tất Phase 1 theo thứ tự phụ thuộc trước khi mở rộng Phase 2.
- Mỗi nhiệm vụ chỉ hoàn tất khi có kết quả kiểm tra được ghi trong `TRACKER.md`.
- Website được phục vụ qua HTTP(S) trong kiểm tra lưu trữ; mở trực tiếp bằng `file:` chỉ để xem bố cục tĩnh.
- Tên script kiểm tra dưới đây là **tệp cần tạo trong nhiệm vụ tương ứng**, không phải lệnh đã có sẵn ở thời điểm lập kế hoạch.

## Phase inventory

| Phase | Mục tiêu | Điều kiện kết thúc |
| --- | --- | --- |
| Phase 1 | Đọc được trên điện thoại và dùng trọn công cụ đọc/tra cứu cơ bản | P1-01 đến P1-08 đạt nghiệm thu |
| Phase 2 | Quản lý dấu và nâng chất lượng tìm kiếm | P2-01 đến P2-03 đạt nghiệm thu hoặc quyết định hoãn P2-03 |
| Phase 3 | Xuất/nhập và quyết định đồng bộ | P3-01 hoàn tất; P3-02 là cổng quyết định, chỉ tạo backlog backend nếu có nhu cầu |
| Phase 4 | Kiểm định hình và quy chuẩn | P4-01 đến P4-04 đạt nghiệm thu; P4-04 sửa lỗi HIGH từ audit |
| Phase 5 | Minh họa sát nội dung cho 56 bài | P5-01 đến P5-04 đạt nghiệm thu |
| Phase 6 | Sơ đồ tổng hợp và QA toàn bộ | P6-01 đến P6-02 đạt nghiệm thu |
| Phase 7 | Kiểm định lại 56 bài, 80 ASCII, sơ đồ người dùng báo lỗi và mục lục | P7-01 đến P7-06 đạt nghiệm thu và audit/debug |
| Phase 8 | Linh kiện, lý thuyết mạch và trường điện từ | P8-01 đến P8-06 đạt nghiệm thu và audit/debug |
| Phase 9 | Điện tử số, MCU/MPU và cảm biến | P9-01 đến P9-05 đạt nghiệm thu và audit/debug |
| Phase 10 | Thiết kế mạch, đồ án và nghiệm thu toàn sách | P10-01 đến P10-04 đạt nghiệm thu và audit/debug |

## Phase 1 — Đọc được và điều hướng đúng

### P1-01 · Đo hiện trạng và lập kiểm tra liên kết

- **Phụ thuộc:** Không.
- **Công việc:** Liệt kê đủ 56 trang, các link nội bộ và các kiểu khối nội dung khó hiển thị. Ghi lại tràn ngang hiện có ở trang chủ và bài đại diện tại 320/360/390/430 px. Tạo `tools/check_links.py` hoặc công cụ tương đương để báo link HTML nội bộ không tồn tại.
- **Nghiệm thu:** Có danh sách lỗi liên kết/tràn ngang, bài đại diện đầu–giữa–cuối, script kiểm tra link chạy và báo lỗi khi thêm một link hỏng thử nghiệm.
- **Kiểm tra:** `python tools/check_links.py` sau khi script được tạo; browser ở bốn độ rộng.
- **Số liệu khởi điểm:** Quét một lần 57 trang hiện có thấy 73 tham chiếu HTML nội bộ bị hỏng, thuộc 7 đường dẫn đích khác nhau; nhiều nhất là `../front/components.html` (56 lần). Nhiệm vụ vẫn chưa hoàn tất vì cần script được lưu trong dự án và đo viewport.

### P1-02 · Làm lại trang mở đầu

- **Phụ thuộc:** P1-01.
- **Công việc:** Áp dụng hướng `pages/home.html`: thông điệp ngắn, một nút vào Bài 1, lộ trình 8 tuần và danh sách mở đủ 56 bài; rút gọn khối lặp. Mỗi tuần có đường dẫn tới bài đầu và danh sách 7 bài. Đưa đường dẫn “Chuẩn bị dụng cụ và an toàn” tới phần đã có trong Bài 1, sau khi xác nhận nội dung phù hợp. Thay thanh đầu trang bằng điều hướng thích ứng màn hình hẹp. Giữ nội dung tác giả/bìa được xác minh từ trang cũ.
- **Nghiệm thu:** Bài 1 mở từ nút chính; mở trực tiếp được bất kỳ bài nào trong 56 bài từ trang chủ; 8 tuần dẫn tới đúng bài; đường dẫn chuẩn bị/an toàn có đích thật; ở 320–430 px menu và tiêu đề không đè nhau, không cuộn ngang toàn trang.
- **Kiểm tra:** Browser desktop/mobile; kiểm tra click và tab/Enter; `python tools/check_links.py`.

### P1-03 · Sửa khung đọc chung cho 56 bài

- **Phụ thuộc:** P1-01.
- **Công việc:** Tối ưu `style.css`, header bài học, sidebar và vùng đọc. Giữ bảng, `pre`, sơ đồ ASCII trong vùng cuộn ngang riêng. Đưa công cụ đọc ra khỏi header chật; sửa menu bài học trên mobile. Menu cho duyệt 8 tuần/56 bài và xác định bài đang đọc.
- **Nghiệm thu:** Không có tràn ngang toàn trang tại 320/360/390/430 px và zoom 200%; chữ không bị dồn cục; có thể mở/đóng danh sách bài, chọn bất kỳ bài nào, chuyển Bài 1 ↔ Bài 56 bằng chạm và bàn phím; focus trở về vị trí hợp lý khi đóng menu. Bảng/sơ đồ dài vẫn đọc được qua cuộn riêng.
- **Kiểm tra:** Bài 1, bài giữa và Bài 56; kiểm tra thêm bài có bảng/sơ đồ dài; browser ở bốn độ rộng.

### P1-04 · Thanh kéo cỡ chữ vùng bài

- **Phụ thuộc:** P1-03.
- **Công việc:** Thay/điều chỉnh `FontSizeController` hiện có; dùng slider có nhãn, hiển thị px, reset và dải đề xuất 16–24 px. Chỉ áp dụng lên vùng bài; giữ cài đặt khi tải lại. Bắt lỗi `localStorage` bị chặn.
- **Nghiệm thu:** Kéo/chạm/mũi tên bàn phím đổi chữ ngay; reload khôi phục mức đã chọn trên HTTP(S); reset về mặc định; header/menu không bị phóng theo; mức 24 px không che nội dung ở 320 px.
- **Kiểm tra:** Kiểm tra trình duyệt ở min/max, reload, chặn storage, zoom 200%.

### P1-05 · Chỉ mục 56 bài và tìm kiếm nội bộ

- **Phụ thuộc:** P1-01.
- **Công việc:** Tạo script trích `title`, đề mục, văn bản tìm kiếm và URL từ 56 HTML; xuất `assets/js/search-index.js` với schema trong `schemas/search-index.schema.json`. Chuẩn hóa truy vấn tiếng Việt có/không dấu; với câu chọn dài, rút các từ khóa có nghĩa, bỏ từ quá phổ biến và giới hạn độ dài truy vấn. Xếp hạng tiêu đề > đề mục > nội dung; giới hạn kết quả và hiển thị đoạn khớp hoặc gợi ý rút ngắn khi không có kết quả.
- **Nghiệm thu:** Chỉ mục có đúng 56 bài, không trỏ tới file thiếu; tìm “điện áp” và “dien ap” đưa bài liên quan vào kết quả; chọn cả một câu vẫn trả kết quả hữu ích hoặc lời nhắc sửa truy vấn rõ ràng; không phải duy trì danh sách thủ công.
- **Kiểm tra:** `python tools/build_search_index.py --check` sau khi script được tạo; thử truy vấn có dấu/không dấu, từ không có kết quả, và link kết quả.

### P1-06 · Chọn chữ và lệnh tra cứu

- **Phụ thuộc:** P1-03, P1-05.
- **Công việc:** Tạo menu thao tác khi chọn chữ trong vùng bài: “Tìm giải thích trên Google”, “Tìm video YouTube”, “Tìm bài liên quan”. Desktop hỗ trợ chuột phải trên đoạn chọn; mobile dùng thanh nổi khi chọn chữ. Có nút/lệnh rõ để mở menu bằng bàn phím sau khi chọn bằng Shift+Arrow. Dùng `URLSearchParams` để tạo truy vấn; không thay menu gốc khi không có đoạn chọn hợp lệ.
- **Nghiệm thu:** Ba lệnh hoạt động với chuột, chạm và bàn phím; sau Shift+Arrow có thể mở menu, Tab qua lệnh, Escape đóng và trả focus mà không mất đoạn chọn; Context Menu/Shift+F10 được kiểm tra. Đoạn tiếng Việt được mã hóa đúng; Google/YouTube mở tab mới; tìm nội bộ hiển thị kết quả trong website; sao chép văn bản vẫn dùng được.
- **Kiểm tra:** Desktop và ít nhất một iOS Safari cùng một Android Chrome trên thiết bị thật hoặc dịch vụ thiết bị từ xa; truy vấn có dấu, dấu câu, đoạn dài; kiểm tra menu không bị che bởi tay nắm chọn chữ, bàn phím ảo hoặc mép viewport.

### P1-07 · Bút đánh dấu bền qua tải lại

- **Phụ thuộc:** P1-06.
- **Công việc:** Lưu bản ghi theo `schemas/highlight-record.schema.json`; tô và bỏ dấu; khôi phục theo quote + ngữ cảnh sau reload. Có danh sách dấu **của bài hiện tại** để tìm lại, tới đoạn, xóa dấu và xem trạng thái neo. Chỉ chấp nhận Selection trong văn xuôi hợp lệ; tránh form, menu, code và bảng tương tác. Thông báo bằng chữ/trạng thái tiếp cận được khi lưu thất bại hoặc không neo lại được dấu.
- **Nghiệm thu:** Đánh dấu và xóa dấu hoạt động; reload vẫn hiện dấu; danh sách dấu hiện tại dùng được bằng bàn phím và screen reader, không dựa riêng vào màu; quote trùng hoặc HTML thay đổi không tô nhầm; lưu thất bại không làm hỏng bài đọc; người đọc biết dữ liệu chỉ ở thiết bị này.
- **Kiểm tra:** Kịch bản lựa chọn qua thẻ inline, hai quote giống nhau, sửa nội dung mẫu, chặn storage, mobile long press trên iOS Safari và Android Chrome, thao tác bàn phím và screen reader.

### P1-08 · Dọn liên kết và nghiệm thu toàn phase

- **Phụ thuộc:** P1-02 đến P1-07.
- **Công việc:** Thay hoặc bỏ các link tới `front/*` và `appendix/*` chưa có đích. Nếu viết trang phụ mới, nội dung phải được biên tập và kiểm tra riêng; mặc định dùng trang/anchor hiện có. Kiểm tra hồi quy sidebar, tiến độ bài học, theme, checklist, in trang và đáp án.
- **Nghiệm thu:** Link nội bộ đều hợp lệ; tất cả tiêu chí thành công trong `PROJECT-CONTEXT.md` đạt; không làm mất các tính năng cũ.
- **Kiểm tra:** `python tools/check_links.py`, `python tools/build_search_index.py --check`, `node --check assets/js/main.js`; browser ở desktop/mobile và zoom 200%.

## Phase 2 — Công cụ học tập

### P2-01 · Thư viện đoạn đã đánh dấu

- **Phụ thuộc:** Phase 1.
- **Công việc:** Mở rộng danh sách dấu của từng bài ở Phase 1 thành thư viện **xuyên 56 bài** với tìm/lọc theo bài, đoạn trích, trạng thái neo và nút tới vị trí trong bài; xóa từng dấu.
- **Nghiệm thu:** Có thể tìm và mở lại dấu đã lưu từ bài khác; dấu không neo được không dẫn tới vị trí sai.
- **Kiểm tra:** Nhiều bài, nhiều dấu, quote trùng, reload.

### P2-02 · Tìm kiếm nội bộ nâng cao

- **Phụ thuộc:** P1-05.
- **Công việc:** Tìm theo đề mục/trích đoạn; thêm từ đồng nghĩa điện tử được biên tập (ví dụ điện áp/voltage) và đánh giá chất lượng xếp hạng.
- **Nghiệm thu:** Kết quả có tiêu đề bài, đề mục và đoạn khớp; truy vấn phổ biến tìm đúng bài, không có link hỏng.
- **Kiểm tra:** Tập truy vấn tiếng Việt có/không dấu và thuật ngữ Anh–Việt được lưu cùng script kiểm tra.

### P2-03 · Quyết định nhiều màu và ghi chú

Quyết định 2026-10-02: hoãn triển khai nhiều màu/ghi chú. Yêu cầu hiện tại chỉ xác nhận một bút đánh dấu, thư viện dấu vẫn dùng schema v1. Nếu người đọc cần thêm, mở hợp đồng riêng gồm di trú dữ liệu và kiểm thử.

- **Phụ thuộc:** P2-01.
- **Công việc:** Đánh giá nhu cầu thực tế; nếu có, mở rộng schema và UI cho nhiều màu/ghi chú, gồm chuyển đổi dữ liệu dấu cũ.
- **Nghiệm thu:** Có quyết định ghi trong tracker. Nếu triển khai, dấu cũ vẫn mở được và ghi chú lưu qua reload.
- **Kiểm tra:** Kịch bản chuyển đổi dữ liệu phiên bản 1 → 2.

## Phase 3 — Dữ liệu người đọc và cổng quyết định đồng bộ

### P3-01 · Xuất/nhập dữ liệu đọc

- **Phụ thuộc:** Phase 2.
- **Công việc:** Xuất dấu/cài đặt ra JSON có phiên bản; nhập với kiểm tra schema, báo xung đột và cho người dùng xem trước.
- **Nghiệm thu:** Xuất rồi nhập khôi phục đúng dữ liệu; tệp sai không xóa dữ liệu hiện có.
- **Kiểm tra:** Tệp hợp lệ, thiếu trường, phiên bản cũ, quote không neo được.

### P3-02 · Cổng quyết định tài khoản/đồng bộ

Quyết định 2026-10-02: hoãn backend/tài khoản/đồng bộ. Chưa có nhu cầu nhiều thiết bị hoặc ràng buộc quyền riêng tư/chi phí được xác nhận; trang xuất/nhập JSON là cách chuyển dữ liệu. Mở lại khi có yêu cầu rõ về thiết bị, tài khoản, lưu trữ và chi phí.

- **Phụ thuộc:** P3-01 và nhu cầu người dùng được xác nhận.
- **Công việc:** Thu thập yêu cầu quyền riêng tư, thiết bị, sao lưu và chi phí vận hành trước khi chọn backend. Nếu chưa có nhu cầu, đóng ở trạng thái “chưa triển khai”.
- **Nghiệm thu:** Có quyết định và lý do; không tạo backend theo suy đoán.

## Quality gate cuối mỗi phase

- Không còn nhiệm vụ dở dang hoặc lỗi chặn thuộc phase.
- Kết quả kiểm tra được ghi trong `TRACKER.md` với ngày và bằng chứng.
- `HANDOFF.json` phản ánh phase hiện tại và nhiệm vụ kế tiếp.

## Milestone hình minh họa — Phase 4–6

Nguồn: `docs/brainstorm/session-2026-10-02-visuals.md` và `docs/brainstorm/visual-inventory-2026-10-02.md`. Phase 1–3 ở trên đã hoàn tất; Phase 4–6 là đợt mới. Ảnh ngoài chỉ CC0/miền công cộng được xác minh trên trang tệp; dự án tiếp tục giữ bản quyền riêng và không tạo `LICENSE`.

| Task | Phụ thuộc | Kết quả |
| --- | --- | --- |
| P4-01 | Không | Script kiểm tra ảnh/nguồn và baseline 56 bài |
| P4-02 | P4-01 | Audit đủ 80 sơ đồ ASCII và danh sách lỗi kỹ thuật |
| P4-03 | P4-01 | Quy chuẩn hình và mẫu Bài 1–2 trên điện thoại |
| P4-04 | Audit Phase 4 | Sửa lỗi kỹ thuật đã xác nhận trước khi tạo thêm hình |
| P5-01 | Phase 4 | Minh họa Bài 1–14, audit và sửa lỗi |
| P5-02 | P5-01 | Minh họa Bài 15–28, audit và sửa lỗi |
| P5-03 | P5-02 | Minh họa Bài 29–42, audit và sửa lỗi |
| P5-04 | P5-03 | Minh họa Bài 43–56, audit và sửa lỗi |
| P6-01 | Phase 5 | 12 sơ đồ tư duy/khối cho bài ôn tập và dự án |
| P6-02 | P6-01 | QA 56/56 bài, nguồn, mobile, alt/caption và nội dung |

Chi tiết đường dẫn, kế hoạch từng tệp và lệnh nghiệm thu nằm trong `.DHSYSTEM/phases/phase-{4,5,6}/tasks/`. Sau mỗi Phase chạy `dh-audit`; phát hiện lỗi thì `dh-debug` và sửa trước Phase kế tiếp.

## Milestone tái biên soạn — Phase 7–10

Nguồn: `docs/brainstorm/session-2026-10-03-curriculum-rebuild.md`; kế hoạch thực thi: `.DHSYSTEM/CURRICULUM-PLAN.md`. Đợt này đánh số tiếp để giữ nguyên lịch sử Phase 1–6. Các kết quả hình Phase 4–6 là bằng chứng về tài sản/hiển thị trong phạm vi cũ, **không** là chứng nhận độ đúng hoặc độ đầy đủ kiến thức cho Phase 7–10.

| Phase | Task theo thứ tự | Kết quả bắt buộc |
| --- | --- | --- |
| 7 | P7-01 → P7-02 → P7-03/P7-04 → P7-05 → P7-06 | Ma trận 56 bài, 80 quyết định sơ đồ, sáu ví dụ đã duyệt, 56 mục menu đúng, audit/debug |
| 8 | P8-01 → P8-02/P8-03/P8-04 → P8-05 → P8-06 | Họ linh kiện, phân tích mạch và trường có ví dụ, đo/mô phỏng, lời giải, audit/debug |
| 9 | P9-01 → P9-02 → P9-03/P9-04 → P9-05 | Logic/FSM, MCU/MPU, bản đồ cảm biến và lab, audit/debug |
| 10 | P10-01 → P10-02/P10-03 → P10-04 | Đồ án, liên kết toàn sách, duyệt kỹ thuật, audit/debug cuối |

**Giả định kế hoạch:** 56 bài cũ + tối đa 32 bài chuyên sâu cho người mới hướng tới thực hành. P7-01 xác nhận lại số bài, độc giả, toán và board/dụng cụ trước khi viết bài mới. Chưa có câu trả lời của người dùng cho hai lựa chọn đầu; xem đây là giả định có thể sửa, không phải quyết định đã chốt. Ảnh ngoài tiếp tục chỉ CC0/miền công cộng theo từng tệp hoặc hình tự tạo; không tạo `LICENSE`.

Mỗi Phase chỉ kết thúc sau `dh-audit`, `dh-debug` nếu có lỗi, và bằng chứng ghi ở `TRACKER.md`/`HANDOFF.json`. Không đánh dấu PASS trước khi thực hiện.
