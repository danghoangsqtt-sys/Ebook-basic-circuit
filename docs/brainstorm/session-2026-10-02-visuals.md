# Phiên brainstorm — làm mới hình minh họa giáo trình

- Ngày: 2026-10-02
- Trạng thái: Đã chốt hướng biên tập; sẵn sàng chuyển sang `dh-crystallize`
- Workflow: `dh-brainstorm` v1.1.0, DHSYSTEM fw 2.19.0
- Phạm vi: 56 bài trong 8 tuần; đợt hình minh họa mới, độc lập với Phase 1–3 nâng cấp website đã hoàn tất
- Danh mục bài: [visual-inventory-2026-10-02.md](visual-inventory-2026-10-02.md)

## Vấn đề và bằng chứng từ mã nguồn

- Trước đợt này, 56 trang bài học chỉ có ba khối hình bằng chữ/emoji, không có ảnh bài học thực; cả ba khối nằm ở Bài 1–2. Có 80 khối `circuit-ascii` trên 56 bài; chúng cần kiểm tra và vẽ lại theo độ ưu tiên, không thay cơ học bằng ảnh trang trí.
- Hình 1.1 từng dẫn tới [sơ đồ nguyên tử trên Commons](https://commons.wikimedia.org/wiki/File:Atom_diagram.png); trang tệp tự cảnh báo thiết kế này thiếu chính xác ở nhiều điểm và giấy phép là CC BY-SA 3.0. Văn bản bài học còn mô tả electron “quay quanh” như quỹ đạo. Đã thay bằng sơ đồ khái niệm tự vẽ và sửa câu liên quan.
- Hình 1.2 ghi DT-830B nhưng liên kết đến tệp model ET-973; không có ảnh thật trong trang. Đã thay bằng [ảnh CC0 của K.Venkataramana](https://commons.wikimedia.org/wiki/File:Digital_Multimeter_%28To_measure_Voltage%2C_Current_and_Resistance%29.jpg), nhìn trên ảnh là DT830D, và sửa đúng model trong chú thích.
- Hình 2.1 dẫn tới bài hướng dẫn SparkFun nhưng chưa dùng một tệp ảnh cụ thể. Đã thay bằng [ảnh hai mặt breadboard CC0 của Guhuru](https://commons.wikimedia.org/wiki/File:Breadboard.png), ghi rõ ảnh là loại 400 lỗ còn bài học hướng dẫn loại 830 lỗ.
- Khi rà Bài 2, phát hiện hướng dẫn đo thông mạch nhắc cắm jumper vào nguồn 3 V rồi lại yêu cầu không cấp điện. Đã sửa thành ngắt hoàn toàn nguồn trước khi đo.

## Quyết định đã chốt cùng người dùng

| Quyết định | Lý do | Trạng thái |
| --- | --- | --- |
| Kết hợp ảnh thiết bị thật với sơ đồ tự vẽ | Ảnh cho thấy thiết bị thật; sơ đồ giải thích quan hệ điện và tín hiệu | Đã chốt |
| Ảnh từ mạng chỉ dùng CC0/miền công cộng; còn lại tự tạo | Dự án giữ bản quyền riêng, chưa chọn giấy phép phát hành | Đã chốt |
| Không suy giấy phép từ cả website; xác minh trên trang của từng tệp | Tránh đưa nhầm CC BY/CC BY-SA hoặc nội dung hạn chế vào kho | Đã chốt |
| Ghi model, loại linh kiện, số lỗ hoặc mã board đúng với ảnh; ảnh tương tự phải ghi “ví dụ” | Tránh người học sao chép sơ đồ sai theo hình | Đã chốt |
| Infographic để tóm tắt quy trình/khái niệm, sơ đồ khối để diễn tả hệ thống, sơ đồ tư duy để liên kết kiến thức | Mỗi loại hình có mục tiêu học tập khác nhau | Đã chốt |

## Hướng triển khai nội dung

1. **Kiểm tra trước khi vẽ.** Với từng bài, đối chiếu sơ đồ ASCII, câu giải thích, bảng linh kiện và bước thực hành. Với sơ đồ mạch dùng linh kiện cụ thể, đối chiếu datasheet đúng mã. Ghi lỗi nội dung phát hiện được và sửa cùng hình.
2. **Ảnh thật.** Dùng cho linh kiện, thiết bị đo, breadboard, module và các bước thao tác. Mỗi ảnh phải hiện đúng model nếu bài nêu model; chỉ chèn sau khi xác minh nguồn và chất lượng ảnh.
3. **Sơ đồ tự vẽ.** Dùng SVG cho mạch, đường dòng, thời gian tín hiệu, luồng điều khiển và sơ đồ khối. Nhãn, chân, GND, giá trị, cực tính và chú giải phải kiểm tra ở cỡ điện thoại.
4. **Infographic.** Thêm ở bài nền tảng và bài thực hành: mã màu điện trở, chọn điện trở LED, đo bằng multimeter, quy trình KiCad, kiểm thử, lắp ráp, an toàn pin.
5. **Sơ đồ tư duy.** Thêm ở các bài ôn tập 7/14/21/28/35/42/49/56 và các bài định hướng 43/48/55, gắn mỗi nhánh với đề mục/bài tương ứng.
6. **Quản lý tài sản.** Lưu tại `assets/images/lessons/`, tên có ý nghĩa; ảnh raster nén WebP, SVG là nguồn chỉnh sửa. Ghi tác giả, URL tệp, giấy phép, ngày kiểm tra, xử lý và bài dùng trong `assets/images/lessons/SOURCES.md`.

## Nghiên cứu nguồn ảnh

- Đã tải, tối ưu và dùng hai ảnh CC0 ở Bài 1–2: [DMM DT830D](https://commons.wikimedia.org/wiki/File:Digital_Multimeter_%28To_measure_Voltage%2C_Current_and_Resistance%29.jpg) và [breadboard 400 lỗ hai mặt](https://commons.wikimedia.org/wiki/File:Breadboard.png). Tệp và lịch sử nguồn ở `assets/images/lessons/`.
- Ứng viên cho bài sau: [ảnh board ESP-WROOM-32 CC0](https://commons.wikimedia.org/wiki/File:ESP32_Espressif_ESP-WROOM-32_Dev_Board.jpg) cho Bài 37 nếu đúng loại board được dạy; [ảnh oscilloscope CC0](https://commons.wikimedia.org/wiki/File:Esselte_oscilloscope.jpg) cho Bài 30 nếu chỉ minh họa thiết bị, không dùng để chỉ số đo cụ thể. Cần kiểm tra trực quan và nội dung bài trước khi tải/dùng.
- Không dùng một ảnh chỉ vì kết quả tìm kiếm hiển thị chữ “CC0”; phải xem mục Licensing của trang tệp. Ví dụ một số kết quả Commons chỉ có *dữ liệu cấu trúc* CC0, còn chính tệp là CC BY-SA.

## Phases

Các Phase dưới đây thuộc **đợt hình minh họa**, không đánh số lại Phase 1–3 của đợt nâng cấp website trước.

### Visual Phase 1 — Kiểm định và quy chuẩn

- Rà 56 bài theo danh mục, lập phiếu cho từng hình/sơ đồ: mục tiêu học, nội dung, độ đúng, nguồn, giấy phép, trạng thái.
- Sửa các lỗi nội dung kỹ thuật gắn với hình. Duyệt ưu tiên Bài 2, 11–18, 32, 35, 39–41, 54 vì có mạch, nguồn hoặc an toàn.
- Chuẩn hóa template ảnh + chú thích + alt text + nguồn; thiết lập kiểm tra ảnh hỏng, ảnh vượt kích thước và trang thiếu hình thiết yếu.
- Mẫu hoàn thành ở Bài 1–2: hai ảnh CC0 và một sơ đồ tự vẽ.

### Visual Phase 2 — Minh họa chi tiết 8 tuần

- Sản xuất và tích hợp ảnh thật, SVG mạch và infographic theo danh mục 56 bài; ưu tiên tuần 1–4 rồi tuần 5–8 trong cùng Phase.
- Mỗi sơ đồ điện được soát với bài và datasheet đúng mã trước khi thay sơ đồ ASCII. Ảnh thật chỉ dùng sau khi kiểm tra model, chân và nguồn.
- Các bài không có sơ đồ ký tự vẫn được đánh giá theo mục tiêu học; không thêm hình chỉ để đủ số lượng.

### Visual Phase 3 — Tổng hợp và bảo đảm chất lượng

- Thêm sơ đồ khối cho bài dự án/hệ thống; sơ đồ tư duy cho bài ôn tập, định hướng và tổng kết.
- Soát hình trên màn hình 320/360/390/430 px, chế độ chữ lớn, bàn phím, alt text, tải trang và độ rõ của nhãn khi thu nhỏ.
- Kiểm tra 100% nguồn CC0/miền công cộng, liên kết và nội dung chú thích; chốt danh mục 56/56 bài với trạng thái đạt hoặc lý do không cần hình.

## Tiêu chí chấp nhận

- Mỗi hình trả lời một câu hỏi của bài; không sai mã linh kiện, pinout, cực tính, số lỗ, chiều dòng hoặc điều kiện đo.
- Không còn hình chữ/emoji giả làm ảnh, nguồn không khớp ảnh, hoặc sơ đồ ký tự quan trọng không được rà soát.
- Infographic và sơ đồ tư duy có nội dung đọc được cả khi không xem ảnh nhờ alt text hoặc mô tả gần hình.
- Chỉ có ảnh ngoài CC0/miền công cộng đã ghi nguồn; hình tự vẽ được ghi rõ; ảnh không tạo cuộn ngang toàn trang trên điện thoại.
- Mỗi tuần có danh mục kiểm tra, mã bài và trạng thái hình để audit sau từng Phase.

## Câu hỏi còn mở

- Có cần giữ các sơ đồ ký tự như phiên bản văn bản hỗ trợ truy cập sau khi SVG được duyệt, hay thay hoàn toàn bằng hình kèm mô tả? Đề xuất giữ phần giải thích văn bản và bỏ phần ASCII trùng lặp theo từng bài.
- Những bài cần ảnh chụp phần cứng cụ thể nhưng không tìm được ảnh CC0 phù hợp: dùng ảnh tự chụp của tác giả hoặc chỉ dùng sơ đồ tự vẽ, tùy vật mẫu sẵn có.
- Các sơ đồ mạch liên quan an toàn điện/pin nên có người am hiểu điện tử soát lần cuối trước khi công bố rộng rãi.

## Project meta intake (FEAT-009)

Kho đã có `.DHSYSTEM/PROJECT-META.md` ghi tên, tác giả, loại dự án và trạng thái bản quyền; đợt brainstorm này chỉ thay hình nội dung. Tạm miễn tạo hồ sơ người dùng toàn cục và `.DHSYSTEM/META.md` vì không cần thêm thông tin để quyết định hướng minh họa.

## Bước tiếp theo

Chuyển phiên này qua `dh-crystallize` để tạo tác vụ, checklist theo 56 bài và điểm kiểm định kỹ thuật, sau đó `dh-auto` thực hiện từng Visual Phase với `dh-audit` và `dh-debug` sau mỗi Phase.
