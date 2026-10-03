# Kế hoạch tái biên soạn giáo trình điện tử — Phase 7–10

- Ngày lập: 2026-10-03
- Nguồn: `docs/brainstorm/session-2026-10-03-curriculum-rebuild.md` và sáu ảnh người dùng gửi
- Trạng thái: **kế hoạch, chưa triển khai**; Phase 1–6 trong `ROADMAP.md` giữ trạng thái hoàn tất của đợt trước
- Giả định để lập kế hoạch: giữ 56 bài hiện có làm tuyến nhập môn; dự kiến thêm **32 bài chuyên sâu** cho người mới hướng tới thực hành kỹ sư. Số bài, độ khó toán và board chưa được người dùng xác nhận; P7-01 chốt lại trước khi viết A01–A32.
- Không tạo giấy phép mới: giáo trình giữ bản quyền riêng; ảnh ngoài chỉ CC0/miền công cộng kiểm theo từng tệp hoặc hình tự tạo.

## Mục tiêu và thước đo

| Yêu cầu | Bằng chứng kết thúc |
| --- | --- |
| Ký hiệu/sơ đồ mạch rõ và đúng | 80/80 khối ASCII có quyết định xử lý, trong đó sáu ví dụ người dùng nêu có bản nguồn chỉnh sửa được, hình web và phiếu duyệt chuyên môn |
| Họ linh kiện đầy đủ | Điện trở, tụ, diode, cuộn cảm, nguồn/adapter có bảng nhận biết–thông số–chọn–đo và bài tập có đáp án; không đánh đồng các biến thể |
| Nền tảng mạch và trường | KCL/KVL, nút/vòng, chồng chất, Thévenin/Norton, RC/RL/RLC, AC và trường điện/từ có ví dụ giải, giả định, mô phỏng/đo và kiểm tra tiên quyết |
| Điện tử số và xử lý | Bảng chân trị, tổ hợp, tuần tự, FSM/timing, CPU–bộ nhớ–bus, MCU so với MPU và ngoại vi có bài tập/lab |
| Cảm biến và thiết kế | Ma trận cảm biến theo đại lượng/nguyên lý/ngõ ra/nguồn/sai số; bài chọn–hiệu chuẩn; đồ án từ yêu cầu tới sơ đồ, tính toán, PCB và kiểm thử |
| Điều hướng và đọc trên điện thoại | 56 bài cũ và bài mới có tiêu đề/mục lục/tìm kiếm đúng; hình đọc hoặc phóng được ở 320 px/24 px, có diễn giải không phụ thuộc màu |

## Giả định cần giải quyết ở đầu Phase 7

1. **Phạm vi:** 56 bài hiện tại + 32 bài mới là baseline lập kế hoạch. Nếu người dùng chọn đúng 56 bài hoặc phụ lục, P7-01 cập nhật mã bài và khối lượng; không viết bài mới trước khi cập nhật ma trận.
2. **Độc giả/mức toán:** baseline là người mới hướng tới thực hành. Bài nhập môn dùng đại số và trực quan; bài nâng cao có phụ lục giải tích/số phức rõ điều kiện tiên quyết. Không gắn nhãn “không cần kiến thức đầu vào” cho phần chuyên sâu.
3. **Phần cứng:** chưa biết board và dụng cụ sẵn có. Các bài lý thuyết dùng ví dụ datasheet có mã/revision; lab có nhánh mô phỏng cho tới khi có board cụ thể. Nếu có board, chốt mã/revision và điện áp chân trước khi xuất sơ đồ đấu dây.
4. **Duyệt kỹ thuật:** cần người có chuyên môn xác nhận mạch cấp nguồn, LiPo, motor/relay, chuyển mức và nội dung gần điện lưới. Chưa có người duyệt thì ghi trạng thái `chưa xác minh phần cứng`, không tuyên bố bài thực hành đã an toàn/đúng trên thiết bị thật.

## Bản đồ bài mới dự kiến

Không thay URL `week1/day01.html`…`week8/day56.html`; bài mới dự kiến ở `advanced/a01.html`…`advanced/a32.html`. Mã và số lượng được xác nhận ở P7-01. Mỗi bài có mục tiêu, tiên quyết, nội dung, nguồn theo từng claim, sơ đồ, ví dụ, thực hành hoặc mô phỏng, bài tập và lời giải.

| Mã dự kiến | Nhóm | Nội dung |
| --- | --- | --- |
| A01–A08 | Linh kiện và nguồn | A01 họ điện trở; A02 điện trở đặc biệt/đo; A03 tụ; A04 tụ trong mạch thực; A05 diode; A06 cuộn cảm/biến áp/ferrite; A07 adapter/nguồn và pin; A08 chọn linh kiện từ datasheet + bài tổng hợp |
| A09–A16 | Lý thuyết mạch và trường | A09 mô hình/KCL/KVL; A10 phương pháp nút/vòng; A11 chồng chất/nguồn phụ thuộc; A12 Thévenin/Norton; A13 RC/RL; A14 RLC/AC/trở kháng; A15 điện trường–điện dung; A16 từ trường–cảm ứng–đường hồi dòng/EMC |
| A17–A24 | Điện tử số và xử lý | A17 nhị phân/mức logic; A18 Boolean/cổng; A19 mạch tổ hợp; A20 chốt/flip-flop/bộ đếm; A21 FSM/clock/timing; A22 CPU–bộ nhớ–bus/MCU–MPU–SoC; A23 ngoại vi MCU/ngắt/timer/ADC/DMA; A24 so sánh họ board và lab có mã cụ thể |
| A25–A32 | Cảm biến và thiết kế | A25 bản đồ cảm biến; A26 nhiệt/ánh sáng/từ; A27 áp suất/chuyển động/khoảng cách; A28 tín hiệu số, sai số/hiệu chuẩn/lọc; A29 quy trình phân tích yêu cầu và sơ đồ khối; A30 thiết kế nguồn thấp áp + chọn linh kiện; A31 thiết kế cảm biến/MCU + PCB; A32 đồ án tích hợp, đo và phân tích sai khác |

## Hồ sơ bằng chứng bắt buộc

- `docs/curriculum/coverage-matrix.csv` hoặc bảng tương đương: 56 bài cũ + bài mới; chủ đề, mục tiêu, tiên quyết, bài tập, sơ đồ, nguồn, mức độ và trạng thái. `Có` nghĩa là dạy và kiểm tra được; từ khóa xuất hiện thoáng qua không tính là đủ.
- `docs/curriculum/diagram-register.csv`: đủ 80 ID cũ; đường dẫn/dòng **hiện hành**, loại hình (mạch/đồ thị/breadboard/bảng/chữ), rủi ro, quyết định giữ/vẽ lại/bỏ, lý do, người duyệt, bằng chứng, trạng thái. Danh sách `docs/qa/visual-technical-audit.md` là baseline lịch sử, phải tái xác nhận trên HTML hiện tại.
- `docs/curriculum/technical-claims.csv`: mỗi claim quan trọng gắn URL/tên tài liệu gốc, hãng, part number, revision, trang/bảng, ngày kiểm và điều kiện áp dụng. Datasheet IC không tự chứng minh pinout module của nhà bán khác.
- Nguồn sơ đồ điện chỉnh sửa được (ưu tiên KiCad `.kicad_sch`) và SVG web; mô tả chữ nêu quan hệ điện/net/cực tính. ERC, mô phỏng và tính tay hỗ trợ kiểm định nhưng không thay phép đo hoặc duyệt chuyên môn.
- Bằng chứng kiểm tra theo task ở `docs/qa/curriculum-phase{7,8,9,10}.md`; `TRACKER.md` ghi kết quả thật, không đánh dấu PASS từ dự định.

## Phase 7 — Khôi phục độ tin cậy của 56 bài hiện có

| Task | Phụ thuộc | Việc và tệp chính | Điều kiện hoàn thành |
| --- | --- | --- | --- |
| P7-01 | Không | Lập ma trận 56 bài, đồ thị tiên quyết, quyết định số bài mới/độ khó/board; `docs/curriculum/coverage-matrix.csv`, `docs/curriculum/syllabus.md` | 56/56 bài có mục tiêu, tiên quyết, phần đã có/thiếu/nông/sai và vị trí; A01–A32 được xác nhận hoặc thay thế trong roadmap trước P8-01 |
| P7-02 | P7-01 | Tái kiểm 80 ASCII trên HTML hiện hành; lập rubric sơ đồ và sổ claim; `diagram-register.csv`, `technical-claims.csv`, `docs/visuals/VISUAL-GUIDE.md` | 80/80 có ID, loại, rủi ro, quyết định và trạng thái; P0/P1 an toàn được đánh dấu rõ; không dùng kết luận cũ như trạng thái lỗi hiện tại |
| P7-03 | P7-02 | Vẽ lại sáu ví dụ D01-1…D01-4, D02-1, D03-1; sửa câu văn liên quan; nguồn sơ đồ + SVG + HTML/alt | Cực tính/nút/đơn vị/điều kiện rõ; GND phân biệt common/chassis/PE; AC thực hành thấp áp cách ly; breadboard đúng model và rail; hình đọc được 320 px, reviewer ký |
| P7-04 | P7-02 | Xử lý các sơ đồ đấu nối/nguy cơ cao còn lại và quyết định cho mọi khối; `week*/day*.html`, nguồn hình | 80/80 có quyết định và bằng chứng; mọi schematic/đồ thị/breadboard cần để học đều được vẽ lại nếu chữ gây mơ hồ, khối giữ nguyên phải vượt kiểm đọc 320 px; mọi mạch P0/P1 đối chiếu datasheet đúng package/module, net, công suất/dung sai; 0 P0 mở trước khi dùng bài thực hành |
| P7-05 | P7-01, P7-03 | Đồng bộ mục lục/tiêu đề/tìm kiếm/dẫn chiếu; rà các câu an toàn Bài 1 và nhận xét chuẩn ký hiệu Bài 3 | 56/56 mục menu khớp trang; search index tái tạo; URL cũ hoạt động; không còn khẳng định an toàn tuyệt đối hoặc độ phổ biến không nguồn |
| P7-06 | P7-03…P7-05 | `dh-audit` nội dung, sơ đồ, mobile, nguồn; `dh-debug` sửa lỗi; lưu `docs/qa/curriculum-phase7.md` | 6/6 ví dụ được ký duyệt; 80/80 có quyết định; 0 P0 mở; link/index/ảnh/mobile đạt; reviewer ghi phần chưa thử phần cứng |

**Thứ tự trong Phase:** P7-01 → P7-02 → P7-03/P7-04; P7-05 có thể bắt đầu sau P7-01 nhưng nghiệm thu sau sửa bài; P7-06 cuối cùng. Với P0 còn mở, tạm khóa hướng dẫn lắp mạch liên quan và không chuyển bài đó sang trạng thái đạt.

## Phase 8 — Linh kiện, lý thuyết mạch và trường

| Task | Phụ thuộc | Việc | Điều kiện hoàn thành |
| --- | --- | --- | --- |
| P8-01 | P7-06 | Khóa syllabus A01–A16, ma trận tiên quyết và mức toán; định nghĩa bộ bài mẫu/nguồn từng chương | Mỗi bài có outcome, thời lượng tương đối, ví dụ, thực hành/mô phỏng, bài tập và rubric; đối chiếu 56 bài để tránh lặp |
| P8-02 | P8-01 | Viết A01–A04: họ điện trở/tụ, nhận dạng, thông số, sai số, phép đo và lựa chọn | Mỗi họ có ít nhất một bài nhận biết, chọn qua datasheet, đo/mô phỏng và lời giải; phân biệt loại/điều kiện áp dụng |
| P8-03 | P8-01 | Viết A05–A08: diode/cuộn cảm/biến áp/ferrite, adapter/nguồn/pin, chọn linh kiện tổng hợp | Pinout/cực tính/giới hạn gắn part cụ thể; bài nguồn dùng thấp áp cách ly; bài tập công suất/nhiệt/dung sai có lời giải |
| P8-04 | P8-01 | Viết A09–A14: phân tích DC, nguồn tương đương, quá độ và AC/RLC | KCL/KVL, nút/vòng, chồng chất, Thévenin/Norton, RC/RL/RLC mỗi phương pháp có giải độc lập + mô phỏng/đo + giả định/miền áp dụng + đáp án |
| P8-05 | P8-04 | Viết A15–A16: điện trường/từ trường ứng dụng, cảm ứng và liên hệ PCB/EMC | Có kiểm tra tiên quyết; bản trực quan và bản toán phù hợp; ít nhất một ví dụ trường → linh kiện → mạch/layout đo được |
| P8-06 | P8-02…P8-05 | Audit học thuật, bài tập/đáp án, nguồn và an toàn; debug lỗi; `docs/qa/curriculum-phase8.md` | 16 bài dự kiến đạt rubric; 0 P0/P1 về kỹ thuật/safety; dữ liệu menu/search/link mới khớp; ghi rõ bài chưa xác minh bằng đo thật |

## Phase 9 — Điện tử số, MCU/MPU và cảm biến

| Task | Phụ thuộc | Việc | Điều kiện hoàn thành |
| --- | --- | --- | --- |
| P9-01 | P8-06 | Viết A17–A21: nhị phân/Boolean, tổ hợp, tuần tự, FSM, clock/timing | Có bảng chân trị, một mạch tổ hợp, một FSM có kiểm timing; đáp án/giới hạn logic rõ |
| P9-02 | P9-01 | Viết A22–A24: CPU–bộ nhớ–bus, MCU/MPU, ngoại vi và so sánh họ board | Ít nhất một lab ngoại vi; ví dụ board có mã/revision và nguồn hãng; không suy giới hạn chân từ họ chip sang module khác |
| P9-03 | P8-06, P9-02 | Viết A25–A28: bản đồ cảm biến, nhận diện, giao tiếp, hiệu chuẩn và sai số | Mỗi nhóm ghi đại lượng, nguyên lý, nguồn/I/O, dải, sai số/độ phân giải, đáp ứng; có một bài so sánh công nghệ và một bài kiểm sai số |
| P9-04 | P9-02, P9-03 | Lab tích hợp số–MCU–cảm biến; nhánh mô phỏng khi thiếu board/thiết bị | BOM/model/revision, giới hạn nguồn/GPIO/ADC, sơ đồ và phép đo kỳ vọng; lab chạy được trên board đã chốt hoặc có mô phỏng tái lập |
| P9-05 | P9-01…P9-04 | Audit/debug; `docs/qa/curriculum-phase9.md` | Bài tập logic/FSM, ngoại vi, chọn/hiệu chuẩn cảm biến qua rubric; 0 P0/P1; menu/search/link/mobile đạt |

## Phase 10 — Thiết kế mạch và nghiệm thu toàn giáo trình

| Task | Phụ thuộc | Việc | Điều kiện hoàn thành |
| --- | --- | --- | --- |
| P10-01 | P9-05 | Viết A29–A32 và đồ án tăng dần: nguồn thấp áp, khối cảm biến, hệ MCU, PCB tích hợp | Mỗi đồ án có yêu cầu, sơ đồ khối, schematic, BOM, ngân sách nguồn/sai số, phép tính, mô phỏng, bước đo và báo cáo sai khác |
| P10-02 | P10-01 | Tích hợp mục lục/tìm kiếm/đường học tiên quyết xuyên 56 bài cũ + bài mới; cập nhật phần ôn tập | Không có URL/lần dẫn sai; học viên đi được theo tiến trình hoặc tra cứu chủ đề; số bài công bố khớp thực tế |
| P10-03 | P10-01, P10-02 | Rà lời giải, claims, hình, nguồn ảnh, a11y/mobile; ký duyệt mạch rủi ro; `docs/qa/curriculum-final.md` | Ma trận yêu cầu → bài → bằng chứng đầy đủ; 0 P0/P1; các phép đo thật/phần chưa đo ghi riêng; 320/360/390/430 px và chữ 24 px đọc được |
| P10-04 | P10-03 | Audit toàn đợt, debug và nghiệm thu lần cuối | Tất cả task Phase 7–10 có bằng chứng trong tracker; không đóng Phase khi còn lỗi chặn hoặc reviewer chưa ký phần cần ký |

## Cổng thực hiện chung sau mỗi Phase

1. Chạy `dh-audit` đối chiếu mã nguồn, ma trận, claim, sơ đồ, bài tập và điều hướng. Dùng `dh-debug` cho lỗi xác nhận, kiểm lại vùng bị sửa, ghi báo cáo phase.
2. Với bài đã sửa: chạy `python tools/check_links.py`, `python tools/check_visuals.py --require-all`, tạo lại chỉ mục bằng `python tools/build_search_index.py` rồi `--check`; kiểm viewport bằng công cụ QA hiện có và kiểm thủ công các sơ đồ điện. Các lệnh là cổng kỹ thuật, không thay duyệt nội dung.
3. Chỉ ghi `PASS` trong `TRACKER.md` khi đã có đường dẫn bằng chứng. Cập nhật `HANDOFF.json` cùng Phase/task kế tiếp. Không sửa trạng thái lịch sử Phase 1–6.

## Nguồn quy chiếu khi viết và kiểm

- [MIT 6.002 Circuits and Electronics syllabus](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/syllabus/) — thứ tự và mức sâu của phân tích mạch, lý thuyết–đo–bài tập.
- [MIT 6.013 Electromagnetics and Applications readings](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/pages/readings/) — chương trường điện từ ứng dụng.
- [MIT 6.004 Computation Structures syllabus](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/syllabus/) — tuyến logic số đến kiến trúc xử lý.
- [KiCad Schematic Editor documentation](https://docs.kicad.org/9.0/en/eeschema/eeschema.html) — net, ký hiệu, ERC, xuất SVG; chọn phiên bản công cụ thực dùng khi triển khai.
- [Raspberry Pi Pico series documentation](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) và [Espressif ESP32-C6 getting started](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c6/get-started/) chỉ là nguồn ứng viên board; không phải quyết định mua hoặc pinout của lab.

Nguồn được xem ngày 2026-10-03. Khi triển khai, dùng datasheet/revision của **part và board thực tế**; ghi trang/bảng chứng minh từng thông số. Không sao chép nguyên văn nội dung/hình của nguồn tham khảo vào giáo trình.
