# Lịch sử thay đổi

Theo cấu trúc Keep a Changelog. Dự án chưa gắn phiên bản phát hành.

## Chưa phát hành

### Tài liệu

- Phase 10 xuất bản A29–A32 và hồ sơ đồ án Pico/TMP36, hoàn tất menu/search 56+32 và bản đồ tiên quyết. Audit/debug cuối thêm skip link cho 89 trang, sửa cuộn mượt để chuyển focus bằng bàn phím, kiểm lại số liệu Phase 8–10 và mobile Chromium/WebKit. `docs/qa/curriculum-final.md` ghi phạm vi PASS nội dung số; CAD/board/đo/reviewer tiếp tục pending.
- Phase 7 qua audit/debug trong phạm vi nội dung số: kiểm kê 56 bài, 80 ID sơ đồ và 17 claim; thay 80 khối ASCII bằng 70 SVG và 10 tham chiếu HTML có thể đọc được. Đối chiếu mạch tham chiếu/datasheet hãng, sửa sai lệch nguồn, linh kiện, giới hạn, phép tính và đồng bộ 56 nhãn menu. Phần cứng thật còn cổng xác minh riêng.
- Phase 8 P8-01 khóa đặc tả A01–A16; P8-02 thêm A01–A04, sơ đồ SVG tự vẽ, ví dụ có nguồn hãng và kiểm thử điều hướng, tìm kiếm, dấu, sao lưu.
- Phase 8 P8-03 xuất bản A05–A08 về diode, cuộn cảm/biến áp/ferrite, nguồn thấp áp và chọn linh kiện từ datasheet hãng; audit/debug độc lập các lỗi điều hướng/tài liệu.
- Phase 8 P8-04 xuất bản A09–A14 về phân tích DC, nguồn tương đương, RC/RL/RLC, nguồn OpenStax/MIT và kiểm phép tính độc lập; sơ đồ cuộn ngang trên mobile, có mô tả chữ và audit/debug.
- Phase 8 P8-05 xuất bản A15–A16 về điện trường, điện dung, Faraday và đường hồi dòng; đối chiếu OpenStax/TI và sửa điều kiện góc trường trong bài tập.
- Phase 8 P8-06 audit đủ 16 bài, lời giải, nguồn và cổng số; sửa README/ARCHITECTURE lệch số bài, giữ các cổng SPICE/ERC/đo phần cứng riêng.
- Phase 9 P9-01 xuất bản A17–A21 về nhị phân/mức điện, Boolean, mux, DFF/counter và FSM/timing; đối chiếu TI/MIT, kiểm bảng chân trị và trace độc lập, giữ phần cứng/timing closure thật pending.
- Phase 9 P9-02 xuất bản A22–A24 về CPU/bus/SRAM/flash, ngoại vi MCU và so Pico non-W với ESP32-C6-DevKitC-1 v1.2; thêm lab GPIO GP25 có kiểm lịch host, giữ nạp/đo board và revision thực tế pending.
- Phase 9 P9-03 xuất bản A25–A28 về bảy họ cảm biến, chọn công nghệ và phép fit TMP36 với dữ liệu tổng hợp; kiểm số học, claim datasheet và sửa hình/QA.
- Phase 9 P9-04 thêm lab Pico non-W/TMP36GT9Z với BOM, netlist, sơ đồ, mã MicroPython và mô phỏng ADC/hysteresis tái lập; sửa đường bypass và kiểm trace theo mã lượng tử, giữ board/chuẩn đo pending.
- Phase 9 P9-05 audit/debug toàn bộ A17–A28 và lab trong phạm vi số, Chromium/WebKit 36 ca mỗi engine; cổng phần cứng riêng tiếp tục pending.
- Phase 10 P10-01 xuất bản A29–A32 và bốn chặng đồ án Pico/TMP36 với nguồn, netlist, BOM, phép tính, mô hình ADC/VREF, phiếu đo và rubric; chưa có CAD/ERC/DRC/PCB/đo thật.
- Phase 10 P10-02 nối đủ 32 bài vào menu/tìm kiếm 88 bài, thêm bản đồ tiên quyết và liên kết ôn tập Bài 56/A28; giữ URL 56 bài cũ.
- Thêm 14 sơ đồ tổng quan theo nội dung Bài 1–14 và bốn ảnh linh kiện CC0/miền công cộng có ghi nguồn; kiểm tra 320/390/1280 px.
- Thêm 14 sơ đồ Bài 15–28 và ba ảnh CC0 cho BJT, MOSFET, DHT22; chú thích rõ giới hạn suy luận từ ảnh linh kiện.
- Thêm 14 sơ đồ Bài 29–42 và ba ảnh CC0 cho máy hiện sóng, PCB, cell Li-ion; sửa minh họa robot dùng đúng driver TB6612FNG.
- Hoàn tất sơ đồ Bài 43–56 và ảnh ESP32 CC0; cả 56 bài đều có hình và qua 168 ca hiển thị mobile/desktop.
- Thêm 12 sơ đồ tổng hợp cuối bài kèm bản diễn giải chữ cho các bài ôn tập, đồ án và định hướng; rà đúng năm hướng học tiếp ở Bài 55.
- Nghiệm thu toàn bộ hình, nguồn CC0/miền công cộng, mô tả thay thế, chú thích và bố cục điện thoại ở 320/360/390/430 px.

- Hoàn tất kiểm định Phase 4: phân loại 80 sơ đồ ký tự và sửa 31 nhóm lỗi kỹ thuật trong sơ đồ, lời giảng, bài thực hành trước đợt vẽ hình.

- Lập kế hoạch Phase 4–6 làm mới hình cho 56 bài; thêm baseline và cổng kiểm tra ảnh/nguồn.

- Chốt hướng nâng cấp trang mở đầu, đọc trên điện thoại, công cụ chọn chữ và tìm kiếm bài liên quan.
- Tạo kiến trúc, roadmap, tracker, schema dữ liệu cục bộ và bản mẫu giao diện.

### Mã ứng dụng

- Mẫu hình Bài 1–2 dùng ảnh CC0 và SVG responsive; chú thích hình theo thanh cỡ chữ người đọc.

- Thiết kế lại trang mở đầu với lộ trình 8 tuần, mục lục mở trực tiếp 56 bài và điều hướng mobile.
- Sửa khung đọc 56 bài trên điện thoại, giữ bảng/sơ đồ cuộn riêng và cải thiện menu bàn phím.
- Thêm thanh kéo cỡ chữ vùng bài 16–24 px, lưu thiết lập và hoạt động khi lưu trữ trình duyệt bị chặn.
- Thêm chỉ mục tự sinh từ 56 bài và hộp tìm kiếm tiếng Việt có dấu/không dấu trên trang đọc.
- Thêm menu chọn chữ để sao chép, tìm giải thích trên Google, video YouTube và bài học liên quan.
- Thêm bút đánh dấu lưu cục bộ, khôi phục theo câu trích/ngữ cảnh và danh sách dấu của bài đang đọc.
- Sửa toàn bộ liên kết nội bộ còn hỏng và kiểm tra cả anchor; bổ sung bộ kiểm thử trình duyệt cho trang đầu, 56 bài và các thao tác đọc.
- Thêm thư viện dấu xuyên 56 bài với tìm/lọc, kiểm tra vị trí neo, mở đúng đoạn và xóa từng dấu.
- Bổ sung từ đồng nghĩa điện tử Anh–Việt và đoạn trích tìm kiếm căn theo vị trí khớp; lưu bộ truy vấn đánh giá.
- Thêm xuất/nhập JSON dữ liệu đọc với kiểm tra tệp, xem trước xung đột, gộp hoặc thay thế và cố khôi phục khi ghi lỗi.
