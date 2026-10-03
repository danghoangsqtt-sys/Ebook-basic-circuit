# QA Phase 8 — Linh kiện, phân tích mạch và trường

Ngày mở: 2026-10-03. Phạm vi đang thực hiện là nội dung số, phép tính và hoạt động mô phỏng **dự kiến**. Phase 7 đã qua audit trong phạm vi này; cổng phần cứng thật ở [`curriculum-hardware-pending.md`](curriculum-hardware-pending.md) vẫn mở. Không ghi bài mới đã xuất bản, mô phỏng đã chạy hoặc mạch đã đo khi chưa có tệp bằng chứng.

## P8-01 — Khóa hợp đồng A01–A16

- [`advanced-phase8-syllabus.md`](../curriculum/advanced-phase8-syllabus.md) có đúng 16 mã A01–A16, mỗi mã một mục duy nhất. Mỗi mục có outcome kiểm được, tiên quyết/M0–M2, thời lượng tương đối, ví dụ giải bằng số, hoạt động giấy/bảng tính/simulator có dữ liệu kỳ vọng, bài tập khác ví dụ với đáp án/rubric và nguồn gốc có URL cùng phạm vi áp dụng.
- Ma trận tiên quyết nối A01–A16 với 56 bài D trong [`syllabus.md`](../curriculum/syllabus.md) và [`coverage-matrix.csv`](../curriculum/coverage-matrix.csv). A01–A08 mở rộng lựa chọn linh kiện/datasheet; A09–A16 mở rộng giải mạch nhiều ẩn, quá độ, AC và trường–layout. Các phần này không coi việc nêu tên linh kiện hay công thức một bước ở bài D là đã dạy đủ năng lực mới.
- Nguồn thông số linh kiện là tài liệu hãng Vishay, TDK, Murata, Nichicon, Würth, TI và ADI; định luật/mô hình tham chiếu OpenStax/MIT. Ví dụ số không gắn part được gắn nhãn **giả định bài toán**. Không suy giới hạn của một IC sang module/PCB khác.
- Kiểm cấu trúc bằng Python: 16/16 heading đúng thứ tự A01–A16; mỗi mục có đủ sáu trường bắt buộc và ít nhất một URL HTTPS — PASS. Agent biên soạn đã kiểm lại ví dụ số và vị trí bảng nguồn; đây là review tĩnh, chưa phải review trang xuất bản.

**Kết luận P8-01:** PASS cho đặc tả nội dung số. Bước kế tiếp P8-02 viết A01–A04; bài mới chỉ được tính là hoàn thành khi có HTML/SVG, nguồn sát claim, lời giải, chỉ mục/liên kết/hiển thị và audit/debug riêng.

## P8-02 — A01–A04 và tích hợp bộ đọc

- Bốn bài [A01–A04](../../advanced/) đã có mục tiêu, hình SVG tự vẽ có mô tả chữ, ví dụ giải từng bước, hoạt động giấy/bảng tính có kết quả kỳ vọng, bài tập khác ví dụ với lời giải và rubric. [Ma trận A01–A04](../curriculum/advanced-coverage-matrix.csv) ghi bài nền, đầu ra và giới hạn xác minh. Nguồn hình ở [`SOURCES.md`](../../assets/images/advanced/SOURCES.md).
- Các số part-specific đã đối chiếu với Vishay Doc. 28952 Rev. 28-May-2026 (MCT 0603 AT 0,110 W/MCA 1206 AT 0,270 W ở P70 general), TDK B57891M Jan-2018 (100 kΩ và bảng R/T curve 4003), và trang Murata GRM188R61A106MAAL# (10 µF ±20%, 10 V, X5R). Phần trăm Ceff 60%/70% là **giả định bài toán**, không được gán cho part Murata. Sổ [`reference-circuit-review.md`](../curriculum/reference-circuit-review.md) bổ sung mạch đo shunt Kelvin của ADI CN0560 và mạch bypass của TI SCEA042 để đối chiếu topology/placement, không lấy BOM của chúng làm thiết kế mặc định.
- Tích hợp menu, trang đầu, tìm kiếm 60 bài, tiến độ, dấu và JSON backup cho mã `a01`–`a04`; 56 URL nền vẫn giữ. `check_advanced.py`: 4/4 trang, 0 lỗi; `check_navigation.py`: 56+4 tiêu đề/URL; `check_links.py`: 63 trang/754 tham chiếu, 0 hỏng; `build_search_index.py --check`: 60 bài hiện hành. `check_visuals.py --require-all`: 56/56 bài nền, 0 lỗi; `check_diagram_register.py`: 80 ID; `qa_lesson_visuals.py --widths 320 390 1280 --font-size 24`: 168 ca nền PASS. Chromium full: 4 viewport trang đầu, 109 ca bài/viewport, bộ đọc/thư viện/backup PASS; Chromium quick và WebKit quick đều PASS, bao gồm kiểm bản ghi A01 đi qua thư viện dấu và sao lưu.
- Audit độc lập theo `dh-audit` không xác nhận P0/P1; ba lệch mô tả trạng thái/nguồn hình P2 được sửa và lưu trong [debug session](../../.DHSYSTEM/debug/session-phase8-p8-02-audit.json). Phép kiểm sơ đồ A04 tính endpoint theo SVG, điện trở nối tại x=315; báo nghi hở mạch ban đầu được rút lại sau đối chiếu.

**Giới hạn P8-02:** hoạt động giấy/bảng tính và kiểm trình duyệt được thực hiện; chưa xuất CSV đường C–V đúng part từ SimSurfing, chưa chạy simulator/nghiệm thu ERC, chưa đo mạch hay board thật. Các hướng dẫn phần cứng là kế hoạch có điều kiện và vẫn theo [sổ phần cứng pending](curriculum-hardware-pending.md).
