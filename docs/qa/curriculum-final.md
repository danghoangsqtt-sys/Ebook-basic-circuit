# Nghiệm thu nội dung số Phase 7–10

Ngày rà cuối: 2026-10-04. Phạm vi đã kiểm là HTML/CSS/JS, hình tự vẽ, lời giải, phép tính và mô hình Python chạy trên host. Không có board, linh kiện thực, file CAD, kết quả ERC/DRC, phép đo hoặc chữ ký reviewer để nghiệm thu phần cứng. Các điều kiện còn thiếu nằm trong [sổ phần cứng](curriculum-hardware-pending.md).

| Yêu cầu trong kế hoạch | Bài/đầu ra | Bằng chứng hiện có | Kết luận |
| --- | --- | --- | --- |
| P7-01…P7-02: 56 bài, 80 hình/claim | `week*/day*.html`, ma trận và sổ hình | [QA Phase 7](curriculum-phase7.md), `docs/curriculum/coverage-matrix.csv`, `docs/curriculum/diagram-register.csv`, `docs/curriculum/technical-claims.csv` | PASS kiểm kê số |
| P7-03…P7-06: sửa sơ đồ, dẫn chiếu, audit/debug | 70 SVG + 10 HTML thay khối ASCII; menu 56 bài | [QA Phase 7](curriculum-phase7.md), `docs/curriculum/reference-circuit-review.md`, `.DHSYSTEM/audit-report.md` | PASS biên tập/số; reviewer mạch thật pending |
| P8-01…P8-06: linh kiện, phân tích, trường | A01–A16, rubric và mô hình đại số | [QA Phase 8](curriculum-phase8.md), `docs/curriculum/advanced-phase8-syllabus.md`, ma trận A01–A16 | PASS nội dung số; phép đo pending |
| P9-01…P9-05: logic, MCU, cảm biến, lab | A17–A28; host fake Pico/TMP36 | [QA Phase 9](curriculum-phase9.md), [lab](../labs/pico-tmp36-monitor.md), `tools/verify_phase9_*.py` | PASS nội dung/mô hình host; board pending |
| P10-01: bốn chặng đồ án | A29–A32, yêu cầu, net bằng chữ, BOM, ngân sách, bài tập | [hồ sơ thiết kế](../projects/pico-tmp36-design.md), [QA Phase 10](curriculum-phase10.md), `tools/verify_phase10_design.py` | PASS hồ sơ/mô hình số; CAD/PCB/đo pending |
| P10-02: tuyến 56+32 | Menu, search, bản đồ tiên quyết | [bản đồ](../../advanced/path.html), `check_navigation.py`, `check_links.py`, `build_search_index.py --check` | PASS đường học số |
| P10-03: claims, nguồn, hình, a11y/mobile | 88 bài, 89 trang có skip link; sổ nguồn từng Phase | [sổ nguồn Phase 9](../curriculum/advanced-phase9-source-ledger.md), [Phase 10](../curriculum/advanced-phase10-source-ledger.md), `assets/images/advanced/SOURCES.md`, `qa_accessibility_basics.py`, `qa_phase10_browser.py` | PASS vòng rà số; reviewer vật lý pending |
| P10-04: audit/debug cuối | State, tracker, báo cáo audit | `.DHSYSTEM/audit-report.md`, `curriculum-phase10.md` | Cổng số PASS; **không đóng nghiệm thu phần cứng** |

## Kiểm nội dung và mô phỏng

Sổ nguồn Phase 8–10 dùng tài liệu hãng cho các ví dụ có part cụ thể. Pico non-W/TMP36GT9Z trong đồ án đối chiếu [Pico datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf), [ADI TMP36 Rev. H](https://www.analog.com/media/en/technical-documentation/data-sheets/tmp35_36_37.pdf) và [MicroPython RP2 quick reference](https://docs.micropython.org/en/v1.26.0/rp2/quickref.html). Cách nhìn chân TMP36 TO-92 là **bottom view**; GP26 là ADC0 và GP25 là LED tích hợp trên Pico non-W. Mã `read_u16()` là giá trị API 0…65535, không phải lời hứa độ chính xác ADC 16 bit. Các con số 3,300/3,333 V, đáp ứng sensor lý tưởng và sai số VREF 1% là giả định mô hình, được ghi ngay cạnh kết quả.

Phép kiểm độc lập của Phase 8/9/10 chạy lại công thức và trạng thái logic, thay vì coi output mô phỏng là bằng chứng đo. Không có P0/P1 **đã xác nhận** trong phạm vi nội dung số sau các phiên debug; kết luận này không bao phủ board, package hay module chưa chọn.

## Kiểm website

- 56 bài nền + 32 bài nâng cao, search 88 bài; mục lục/URL/fragment kiểm bằng script, không có link nội bộ hỏng ở lần chạy cuối.
- Chromium/WebKit: A29–A32 và bản đồ tại 320/360/390/430 px, cỡ chữ 24 px; hình, transcript, đáp án và tràn ngang được kiểm. Bài nền/nhóm trước có kết quả theo QA từng Phase.
- Liên kết bỏ qua menu dẫn tới landmark `main` có tiêu điểm bàn phím trên 89 trang bài/lộ trình. Chromium kiểm Tab đầu tiên; WebKit kiểm kích hoạt bằng bàn phím sau khi đặt focus vì cấu hình Tab mặc định của WebKit bỏ qua liên kết. Đây là kiểm a11y cơ bản, chưa phải chứng nhận WCAG toàn diện.

## Việc cần khi có thiết bị và reviewer

Chốt mã board/part/package/revision và dụng cụ; dựng schematic CAD, ERC/DRC, kiểm net/nguồn/return, nạp firmware trên board, đo rail/VREF/raw ADC/nhiệt/LED và sai khác theo phiếu đồ án. Reviewer kỹ thuật ký riêng các mạch có rủi ro. Sau bằng chứng đó mới đổi trạng thái nghiệm thu phần cứng của Phase 7–10.
