# Kế hoạch nâng cấp website giáo trình điện tử

Ngày chốt: 2026-10-02. Nguồn phạm vi: `docs/brainstorm/session-2026-10-02.md`. Hướng màn hình: `.DHSYSTEM/ui-direction/2026-10-02/`.

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
