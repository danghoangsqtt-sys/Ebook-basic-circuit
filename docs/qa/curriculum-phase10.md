# Kiểm Phase 10 — đồ án và nghiệm thu giáo trình

Ngày bắt đầu 2026-10-04. Hồ sơ này ghi nghiệm thu **nội dung số/mô hình** theo từng task. Phần cứng, schematic CAD/ERC/DRC, board, chuẩn nhiệt, phép đo, PCB và reviewer kỹ thuật vẫn ở [sổ pending](curriculum-hardware-pending.md); không dùng PASS số làm chứng nhận mạch thật.

## P10-01 — A29–A32, đồ án bốn chặng

- [Đề cương](../curriculum/advanced-phase10-syllabus.md), [sổ nguồn](../curriculum/advanced-phase10-source-ledger.md), [hồ sơ đồ án](../projects/pico-tmp36-design.md) và [ma trận](../curriculum/advanced-coverage-matrix.csv) khớp bốn bài. A29 yêu cầu/net/BOM, A30 nguồn USB thấp áp, A31 TMP36/ADC/MCU, A32 carrier PCB khái niệm. Mỗi chặng có yêu cầu, sơ đồ khối, schematic net bằng chữ, BOM, ngân sách nguồn/sai số, phép tính, mô hình số, phiếu đo và mẫu báo sai khác. Hình A29–A32 tự vẽ và có bản chữ; [nguồn hình](../../assets/images/advanced/SOURCES.md) đối chiếu Raspberry Pi/ADI/MicroPython.
- [Mô hình Phase 10](../../tools/simulate_phase10_design.py) xuất 10 kịch bản nhiệt 20/25/30/31/40 °C × ADC_VREF giả định 3,300/3,333 V, chỉ là đại số sensor/ADC lý tưởng; không mô phỏng SMPS/SPICE/PCB. [`verify_phase10_design.py`](../../tools/verify_phase10_design.py) kiểm độc lập 0,70/0,90 V, P_U1<0,165 mW theo <50 µA ở 3,3 V, code 14894 tại 25 °C, nửa bước ADC 12 bit ≈0,0403 °C, thành phần VREF giả định 1%≈0,75 °C và đủ 4 bài/ma trận: PASS. Kịch bản +1% VREF thực ở 25 °C giải theo 3,3 V cho sai lệch khoảng −0,74 °C; không là đặc tính Pico được bảo đảm.
- `check_advanced.py`: 32/32 bài, 0 lỗi; `check_links.py`: 91 trang/1060 tham chiếu cục bộ, 0 hỏng trước tích hợp P10-02. Chromium và WebKit riêng A29–A32 ở 320/360/390/430 px, chữ 24 px, hình tải, transcript và đáp án mở: mỗi engine 16 ca PASS. URL nền 56 bài không đổi.

**Giới hạn:** không có part/board thật, schematic CAD, ERC/DRC, Gerber, nạp MicroPython, VREF/raw/chuẩn nhiệt đo hoặc chữ ký reviewer. A32 là hồ sơ chuẩn bị thiết kế PCB, chưa là PCB sản xuất. P10-01 đạt phạm vi số; P10-02 phải tích hợp điều hướng và tìm kiếm trước khi công bố đủ 88 bài.

## P10-02 — menu, tìm kiếm và đường tiên quyết 56+32

- `assets/js/sidebar-data.js` có 56 bài nền và 32 bài A theo đúng tiêu đề/URL; trang chủ dùng cùng `CURRICULUM`. `advanced/a28.html` nối A29, `week8/day56.html` nối ôn tập sang A29–A32, trang [bản đồ tiên quyết](../../advanced/path.html) và [bảng đường học](../curriculum/prerequisite-paths.md) cho bốn tuyến. Không đổi URL bài nền.
- `build_search_index.py` tạo lại và `--check` xác nhận **88 bài**. `check_navigation.py` PASS 56+32; `check_links.py` sau mở rộng quét cả `advanced/path.html`: 92 trang/1100 tham chiếu, 0 file/fragment/escape hỏng; `check_advanced.py` 32/32. `node --check assets/js/sidebar-data.js` PASS.
- `qa_browser.py --quick --browser chromium`: 4 viewport trang chủ, 280 ca bài/viewport, reader/library/backup PASS. `qa_phase10_browser.py`: A29–A32 và bản đồ tiên quyết ở 320/360/390/430 px, chữ bài 24 px; Chromium/WebKit mỗi engine 20 ca PASS, hình/đáp án/transcript/không tràn.

Audit P10-02 bắt một nhãn sai trong bản đồ ban đầu: D03 là điện trở/mã màu (không phải tên bài “định luật Ohm”), D22 là giao tiếp số (thay cho D25 ADC/DAC ở đường logic). `dh-debug` đã sửa và kiểm lại link; trạng thái bài theo tiêu đề thật. Tệp `tools/build_phase10_bridge.py` lúc đầu ghi A28 thành công nhưng in ký tự mũi tên lỗi trên console cp1252 Windows; đã đổi thông báo ASCII, chạy lại PASS. Không có URL/nhãn sai còn xác nhận trong vùng mới.

## P10-03 — rà cuối nội dung số, nguồn và a11y

- [Ma trận nghiệm thu](curriculum-final.md) ánh xạ P7-01…P10-04 sang bài/đầu ra/bằng chứng và tách cổng phần cứng. Sổ nguồn Phase 8–10 và chú thích hình ghi hãng/tài liệu; giả định VREF, ADC lý tưởng và độ chính xác cảm biến không được trình bày như phép đo.
- Các phép kiểm độc lập Phase 8 (`verify_phase8_numeric.py`, `verify_phase8_fields.py`), Phase 9 (bốn `verify_phase9_*.py`) và Phase 10 (`verify_phase10_design.py`) PASS; 32/32 bài nâng cao, menu 56+32, search 88, 80 ID hình/17 claim, 56/56 bài nền có hình. `check_links.py`: 92 trang/1189 tham chiếu, 0 hỏng; `git diff --check` không có lỗi khoảng trắng.
- Audit phát hiện 88 bài và trang lộ trình thiếu skip link, và bộ cuộn mượt chặn chuyển focus của link. `dh-debug` thêm skip link/landmark cho 89 trang, sửa `assets/js/main.js` để link này dùng điều hướng native, đồng thời cập nhật generator Phase 9/10. `ensure_lesson_skip_links.py --check`: 89/89. `qa_accessibility_basics.py`: Chromium và WebKit mỗi engine 3 ca kích hoạt bằng bàn phím, URL hash và focus ở main PASS. Chromium kiểm Tab đầu tiên; WebKit đặt focus trước khi Enter do cấu hình Tab mặc định bỏ qua link. Đây là kiểm a11y cơ bản, không thay thế audit WCAG toàn diện.
- Chromium/WebKit A29–A32 và bản đồ tiên quyết tiếp tục được kiểm 320/360/390/430 px ở cỡ chữ 24 px, 20 ca/engine PASS. Các bài gốc có kiểm riêng trong QA Phase 7–9. Không có P0/P1 đã xác nhận trong phạm vi nội dung số.

P10-03 đạt phần rà số. Reviewer nguồn/ADC/PCB, kết quả ERC/DRC, phần cứng và đo thật vẫn pending theo [sổ phần cứng](curriculum-hardware-pending.md).

## P10-04 — audit/debug cuối toàn đợt

Audit Tier 1–3 tại `.DHSYSTEM/audit-report.md` rà lại ma trận Phase 7–10, trạng thái task và tài liệu. Lỗi stale ở `AI-GUIDE.md`, `CURRICULUM-PLAN.md`, `TRACKER.md`, `ROADMAP.md`, `HANDOFF.json` đã đồng bộ qua `dh-debug`; lỗi skip link/focus có phiên `.DHSYSTEM/debug/session-phase10-a11y-skip-link.json`. Các cổng tính toán, menu, link, search, hình, Chromium/WebKit và bàn phím đều PASS theo P10-03 ở trên. `qa_browser.py --quick --browser chromium` cũng PASS 4 viewport trang chủ, 280 ca bài/viewport, reader/library/backup.

Kết luận: **PASS audit/debug phạm vi nội dung số/mô hình host; Phase 10 vẫn mở cổng nghiệm thu phần cứng**. Chưa có board/part thật, CAD/ERC/DRC, kết quả đo hoặc chữ ký reviewer theo [sổ phần cứng](curriculum-hardware-pending.md). Không tạo tag hồi tố cho Phase 7–10; cổng Git persistence được kiểm riêng sau khi lưu thay đổi.
