# Nhật ký kiểm định Phase 7 — giáo trình

## P7-01 — Kiểm kê và đề cương (2026-10-03)

### Cách thu thập

- Đọc trực tiếp 56 tệp HTML hiện hành `week1/day01.html` đến `week8/day56.html` bằng bộ phân tích HTML; lấy `h1.lesson-title` (riêng bài 56 lấy `h1`), từng mục tiêu `.objectives-list li`, toàn bộ `h2`, `.exercise-item`, `.answer-toggle`, `.figure` và `.circuit-ascii` cùng số dòng nguồn.
- Kết quả một hàng mỗi bài ở [`../curriculum/coverage-matrix.csv`](../curriculum/coverage-matrix.csv). Trường `coverage_observed` và `gap_or_review_need` là nhận định biên tập từ đề mục, mục tiêu và các phần bài liên quan, **chưa phải chứng nhận đúng kỹ thuật**. `prerequisites_inferred` là sơ đồ tiên quyết suy luận, cần giáo viên kiểm khi dùng thực tế.
- Tám trang D14, D21, D28, D35, D42, D49, D55, D56 không có `.objectives-list`; cột mục tiêu ghi rõ suy luận từ `h2`, cần viết mục tiêu đo được khi sửa các trang này.
- 56/56 trang có tiêu đề và đề mục; tổng 80 khối `.circuit-ascii` trên HTML hiện hành. CSV ghi chính xác dòng bắt đầu của từng khối, làm đầu vào cho P7-02. Đếm `.figure` là đếm thẻ CSS, không xác nhận hình đúng hoặc đủ.
- Bài tập không nằm trong `h2` của đa số trang; vì vậy đã đếm `.exercise-item` và nút `.answer-toggle` trực tiếp. Số đếm này không đánh giá chất lượng lời giải hoặc bài tập ẩn trong bảng/đoạn văn.

### Khoảng trống và bất nhất có bằng chứng

| Bằng chứng hiện hành | Kết luận dùng để phân việc |
| --- | --- |
| D03 có đề mục “Mã màu”, “Sai số”, “Đọc nhãn SMD”, “Đo và phân loại” (`week1/day03.html`) | Không mô tả sách là “chỉ nói một loại điện trở”; A01–A02 cần đi sâu nhận dạng họ linh kiện, thông số và chọn part. |
| D08, D10, D11, D12 lần lượt dạy tụ, cuộn cảm, diode và Zener; D13 dạy adapter/regulator | Chủ đề đã có phần nhập môn nhưng cần tuyến chuyên sâu A03–A08 về đặc tính thực, điều kiện áp dụng, phép đo và lựa chọn theo datasheet. |
| D06 có KCL/KVL; D09 có RC; D10 có RL; D31 có bộ lọc; D54 có EMC | Không gọi lý thuyết mạch/trường “hoàn toàn vắng mặt”. A09–A16 bổ sung phương pháp nút/vòng, tương đương nguồn, quá độ/AC và liên hệ trường với linh kiện/layout có bài giải. |
| D22–D26 dạy UART/I2C/SPI/ADC/ngắt trước một tuyến logic số; D44 có state machine firmware | A17–A21 cung cấp nền logic tổ hợp, tuần tự và timing trước giao tiếp; A22–A24 đi vào kiến trúc CPU/MCU/MPU và ngoại vi. |
| D27 dạy DHT22/DS18B20/PIR; D40 dạy HC-SR04/IR; D47 có offset calibration | A25–A28 cần bản đồ cảm biến và bài chọn/hiệu chuẩn theo đại lượng, nguyên lý, giao tiếp và sai số. |
| `assets/js/sidebar-data.js` đặt D10 là “Diode & PN junction”, D20 là “LDR + BJT”, D22 là “MOSFET”; tiêu đề thật tương ứng D10 “Cuộn Cảm & Mạch RL”, D20 “Op-Amp…”, D22 “Giao Tiếp Số — UART Cơ Bản” | P7-05 phải đối chiếu đủ 56 mục menu với tiêu đề thật và chỉ mục tìm kiếm, không sửa qua phỏng đoán thứ tự tuần. |
| D01 có bốn khối ASCII người dùng chỉ ra; D02 một khối breadboard; D03 một khối ký hiệu điện trở | Sáu ví dụ này ưu tiên vẽ lại và duyệt kỹ thuật ở P7-03. Vị trí hiện hành nằm trong CSV và sổ hình P7-02. |

### Giới hạn và cổng tiếp theo

- Kiểm kê chưa xác minh từng câu, phép tính, mạch điện, pinout, nguồn ảnh hoặc đáp án. P7-02/P7-03/P7-04 và audit chuyên môn sẽ quyết định lỗi nào thực sự tồn tại và cách sửa; báo cáo hình cũ không thay kiểm định hiện tại.
- Chưa có quyết định từ người dùng về số bài, mức toán và board/thiết bị. [`../curriculum/syllabus.md`](../curriculum/syllabus.md) khóa **baseline tác nghiệp** 56 + 32 cho việc triển khai được yêu cầu; không gán pinout board hoặc yêu cầu mua thiết bị. Các lab phần cứng phải chờ mã/revision/nguồn được xác minh, dùng mô phỏng khi thiếu thiết bị.
- P7-01 chỉ hoàn thành hồ sơ kiểm kê/đề cương. Không dùng dòng này làm PASS cho toàn Phase 7. Sau P7-02–P7-05 phải chạy `dh-audit`, `dh-debug` khi có lỗi, ghi bằng chứng riêng và chỉ chuyển Phase khi P7-06 đạt.

### Lệnh đối chiếu

```powershell
@'
import csv
from pathlib import Path
from bs4 import BeautifulSoup
r=list(csv.DictReader(Path('docs/curriculum/coverage-matrix.csv').open(encoding='utf-8',newline='')))
assert len(r)==56 and [x['day'] for x in r]==[f'D{i:02}' for i in range(1,57)]
assert all(Path(x['path']).is_file() and x['objectives'] and x['section_evidence'] and x['gap_or_review_need'] for x in r)
for x in r:
    s=BeautifulSoup(Path(x['path']).read_text(encoding='utf-8'),'html.parser')
    h=s.select_one('h1.lesson-title') or s.find('h1')
    assert h.get_text(' ',strip=True)==x['title_actual']
assert sum(0 if x['ascii_evidence']=='0 khối' else len(x['ascii_evidence'].split(',')) for x in r)==80
syllabus=Path('docs/curriculum/syllabus.md').read_text(encoding='utf-8')
import re
assert sorted(set(re.findall(r'\bA(?:0[1-9]|[12][0-9]|3[0-2])\b(?= —)',syllabus)))==[f'A{i:02}' for i in range(1,33)]
print('P7-01 inventory OK: 56 lessons, 80 ASCII blocks, 32 advanced codes')
'@ | python -
git diff --check
```

## P7-02 — Sổ 80 sơ đồ và claim kỹ thuật (2026-10-03)

### Phương pháp

- Lấy ID từ danh mục kiểm Phase 4 như khóa truy vết rồi xác định lại từng `.circuit-ascii` trên HTML hiện tại; vị trí dòng cũ không được dùng làm vị trí hiện hành. `diagram-register.csv` lưu loại hình, rủi ro đọc/lắp và quyết định xử lý. `technical-claims.csv` lưu 17 phát biểu đầu tiên cần nguồn hoặc xác minh part/revision.
- Một nhãn ưu tiên lịch sử chỉ giúp chọn thứ tự duyệt. Không tự động biến nó thành lỗi đang tồn tại. `visual_unresolved` nghĩa là khối ASCII vẫn chưa chuyển thành hình rõ ràng; nó không xác nhận mạch đã sai. `needs_revision` ở sổ claim là câu hiện tại cần sửa sau khi so với nguồn.
- Đối chiếu tự động: 80 ID duy nhất, mọi `path:line` trỏ đúng dòng mở `.circuit-ascii`; gồm 48 schematic/ký hiệu, 4 waveform/timing, 12 breadboard/pinout/vật lý, 10 luồng/hệ thống, 6 bảng tra văn bản. Sổ claim có 17 ID duy nhất, tất cả tham chiếu ID sơ đồ có thật, URL có nguồn đều là HTTPS.
- Kiểm tra mẫu hiện hành: sáu ví dụ trong ảnh người dùng vẫn là ASCII tại D01-1…D01-4, D02-1, D03-1. Các chú thích cực/nút ở D01-1 và rail D02-1 đã được bổ sung sau audit cũ, nhưng bố cục ký tự vẫn khó đọc trên điện thoại. Ký hiệu diode `▷|` còn ở D04-1/D11-1…D11-3, cần chuẩn hóa trong lượt vẽ lại.

### Phát hiện ưu tiên

| Vị trí | Phát hiện hiện tại | Hành động |
| --- | --- | --- |
| `week1/day01.html:334` | Chú thích Power/Signal GND có thể bị hiểu là phải tách ground trên mọi mạch ESP32; tài liệu TI không cho phép suy ra quy tắc chung đó. | P7-03 sửa ví dụ GND và giải thích đường hồi dòng theo mạch cụ thể. |
| `week1/day01.html:347,355` | Câu điện áp thấp DC “không gây điện giật nguy hiểm” và ngưỡng 50 mA/điện trở cơ thể cố định quá tuyệt đối. OSHA mô tả nguy cơ phụ thuộc điều kiện, đường đi và thời gian tiếp xúc. | P7-03/P7-05 sửa lời an toàn; dùng thực hành nguồn thấp áp cách ly, hạn dòng, tránh điện lưới. |
| `week1/day03.html:91` | Câu zigzag “phổ biến hơn trong tài liệu kỹ thuật” không có phạm vi/nguồn. | P7-03/P7-05 bỏ nhận xét phổ biến; minh họa cả hai quy ước. |
| D11-3, D14-1, D15-2, D16-1, D17-1, D23-1, D24-1, D32-1, D35-1, D38-1 | Sơ đồ mạch/bus/nguồn rủi ro cao chủ yếu đang trình bày bằng ký tự và danh sách nối dây. Chưa xác nhận lỗi điện hiện tại. | P7-04 đối chiếu datasheet đúng model và netlist, vẽ lại hoặc ghi lý do giữ; khóa hướng dẫn lắp phần cứng nếu chưa kiểm. |

### Nguồn dùng để mở hồ sơ claim

- [OSHA Basic Electricity Safety](https://www.osha.gov/sites/default/files/2019-04/Basic_Electricity_Materials.pdf) và [OSHA 1910.269 Appendix C](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.269AppC): điều kiện điện giật không thể gói thành một ngưỡng cố định phổ quát.
- [Texas Instruments, Grounding in mixed-signal systems, Part 1](https://www.ti.com/lit/an/slyt499/slyt499.pdf): tên chân AGND/DGND không tự quyết định bố trí ground bên ngoài.
- [Adafruit, Breadboard Tips & Tricks](https://learn.adafruit.com/breadboards-for-beginners/breadboard-tips-and-tricks): rail nguồn có thể bị ngắt; cần kiểm trên board thực.

Các nguồn trên xác minh nguyên tắc, không chứng thực pinout của một module không rõ mã và revision. Các claim chưa có nguồn chính xác giữ trạng thái `needs_source`/`needs_exact_part`/`needs_exact_module`. Không có thử nghiệm phần cứng trong P7-02.

## P7-03 — Sáu sơ đồ mẫu được thay và duyệt (2026-10-03)

### Tệp và nội dung

- D01-1…D01-4 tại `week1/day01.html`: thay bằng `d01-aa-series.svg`, `d01-current-loop.svg`, `d01-ground-reference.svg`, `d01-ac-dc-wave.svg`. Mỗi hình có alt, caption, liên kết mở SVG lớn và bản chữ mở bằng bàn phím. Pin ghi điện áp **danh định** theo mốc chọn; mũi tên dòng điện quy ước và electron đi ngược nhau trên cùng topology; GND mạch, chassis và PE phân biệt; AC ví dụ nguồn thấp áp cách ly, 50 Hz/T=20 ms. Đã sửa khẳng định DC phải có giá trị không đổi, an toàn điện áp thấp tuyệt đối và ngưỡng điện giật cố định.
- D02-1 tại `week1/day02.html`: `d02-breadboard-connectivity.svg` cho thấy nhóm a10–e10, f10–j10, cột 11 độc lập, rãnh giữa và rail có thể ngắt. Bản chữ chỉ cách đo thông mạch trên board thật. Ảnh breadboard 400 lỗ kế bên vẫn ghi đúng là loại 400 lỗ.
- D03-1 tại `week1/day03.html`: `d03-resistor-symbols.svg` thể hiện zigzag và hình chữ nhật có hai đầu nối; đã bỏ so sánh mức độ phổ biến không nguồn. Sáu SVG nguồn chỉnh sửa được, ghi bản quyền dự án trong `assets/images/lessons/SOURCES.md`.

### Rà soát độc lập và sửa lỗi

Reviewer `/root/p7_six_review` đọc hình học SVG và lời lân cận, chưa thấy lỗi cực tính/net ở sáu hình. Reviewer tìm thấy và đã sửa: ví dụ D02 nói sai rằng hàng d/e cùng cột thuộc hai nửa (thay bằng e/f); D01 áp một kiểu cổng VΩmA cho mọi đồng hồ và yêu cầu que đen luôn thấp thế (thay bằng cổng V trên máy cụ thể, COM là tham chiếu, tránh khe A/10A khi đo áp); đáy sóng AC sát trục thời gian (giảm biên độ hình minh họa). Bảng màu dây ở D02 nay là quy ước của bài học, không là chứng cứ về cực tính thực. GND của breadboard độc lập có thể liên hệ PE qua dụng cụ đo; văn bản đã sửa để người học kiểm thiết bị.

Nguồn nguyên tắc: [OpenStax về nguồn mắc nối tiếp](https://openstax.org/books/college-physics-ap-courses/pages/21-2-electromotive-force-terminal-voltage), [chiều dòng điện](https://openstax.org/books/university-physics-volume-2/pages/9-1-electrical-current), [AC](https://openstax.org/books/university-physics-volume-2/pages/15-1-ac-sources); [KiCad về hai biểu tượng điện trở](https://docs.kicad.org/8.0/en/getting_started_in_kicad/getting_started_in_kicad.html); [TI về AGND/DGND](https://www.ti.com/lit/an/slyt499/slyt499.pdf); [Adafruit về rail breadboard](https://learn.adafruit.com/breadboards-for-beginners/breadboard-tips-and-tricks); [OSHA về an toàn điện](https://www.osha.gov/sites/default/files/2019-04/Basic_Electricity_Materials.pdf). Nguồn không được dùng để suy pinout module khác model.

### Kết quả kiểm

- Sáu SVG parse XML, sáu HTML tham chiếu ảnh tương ứng; 80 ID trong `diagram-register.csv` còn duy nhất và trỏ đúng vị trí hiện hành: sáu ảnh mới, 74 khối ASCII còn mở cho P7-04.
- `python tools/check_visuals.py --require-all`: 56/56 bài có hình, 88 phần tử ảnh/89 asset, 74 ASCII, 0 lỗi nguồn/tệp. `python tools/check_links.py`: 59 trang, 580 liên kết nội bộ, 0 hỏng. Search index tái tạo và `--check`: 56 bài hiện hành.
- `python tools/qa_lesson_visuals.py --start 1 --end 3 --widths 320 390 1280`: 9 ca PASS. Thêm 12 ca Bài 1–3 ở 320/390 px × theme sáng/tối × cỡ chữ 24 px: ảnh tải, alt có, không tràn ngang. Đã xem screenshot thực tế của cả sáu ảnh ở chiều rộng 320 px.
- Chữ chú giải nhỏ trong SVG D01 giảm xuống khoảng 11–12 px ở màn 320 px; mỗi hình có liên kết mở SVG toàn cỡ và bản chữ chọn được. Nội dung khóa ở caption/bản chữ. Chưa chạy ERC, mô phỏng hay thử phần cứng; không coi rà soát hình học là chứng nhận sản phẩm điện.

## P7-05 — Đồng bộ điều hướng và chỉ mục (2026-10-03)

- So sánh từng `h1` của 56 trang với `assets/js/sidebar-data.js`: 48 nhãn menu cũ khác tiêu đề trang, nhiều nhãn trỏ tới chủ đề sai từ Bài 10–27. Đã cập nhật đúng tiêu đề hiện hành, giữ nguyên 56 URL. Trang chủ dùng cùng dữ liệu `CURRICULUM` để dựng danh sách bài.
- Thêm `tools/check_navigation.py` để bắt trùng/thiếu bài, URL sai, tiêu đề lệch và trang thiếu `h1`. Chế độ `--fix` chỉ cập nhật nhãn; liên kết URL không tự sửa.
- Kiểm lại nội dung an toàn của Bài 1 và nhận xét hai ký hiệu điện trở của Bài 3. Các phát biểu tuyệt đối đã sửa ở P7-03; chưa tìm thấy tái xuất hiện tại hai đoạn được nhắm.
- Cổng khi đóng P7-05: `python -X utf8 tools/check_navigation.py` PASS 56/56; `python -X utf8 tools/check_links.py` 59 trang/656 tham chiếu cục bộ, 0 lỗi; `python -X utf8 tools/build_search_index.py --check` 56 bài; `node --check assets/js/sidebar-data.js` PASS. P7-04 tiếp tục sửa HTML và đã chạy lại các cổng bên dưới.

## P7-04 — Tiến độ thay sơ đồ và rà kỹ thuật (2026-10-03, chưa nghiệm thu)

- Sổ `docs/curriculum/diagram-register.csv` có 80/80 ID duy nhất trỏ đến nguồn hiện hành: 70 SVG có liên kết phóng lớn và bản chữ, 10 tham chiếu HTML có thể chọn chữ. Không còn `.circuit-ascii`; `tools/check_diagram_register.py` và `tools/check_visuals.py --require-all` đều đạt. 60 SVG mới có dòng xuất xứ trong `assets/images/lessons/SOURCES.md`; tổng 153 tài sản được kiểm bằng manifest.
- Rà độc lập các nhóm sơ đồ/mã gần kề đã phát hiện và sửa khe hở net D11-3/D21-2; cực tụ D09-1; BOM D12/D15/D16; phân áp UART D22-3 theo nguồn 4,75–5,25 V và điện trở 5%; chọn diode LM2596 D32/D35; hướng GPS TX/RX D22; nối tụ VMOT–GND D38; chỉ báo LM358 D21; giới hạn MOSFET 3,3 V D18; mức logic module SD với Uno D24; ADC pin D41; khoảng đo HC-SR04 D40; topic MQTT D37; mã mẫu D28/D51/D53. Các thay đổi phần cứng chưa thử được lưu trong `.DHSYSTEM/debug/session-phase7-audit-corrections.json`.
- Trên bài có module/part chưa chốt, các bước lắp rủi ro được ràng buộc theo đúng mã/revision hoặc chuyển sang mô phỏng. D21 chưa có hysteresis nên chỉ thử khối NTC–LM358–LED; không lắp relay/quạt theo sơ đồ phân tích. D18 không dùng IRLZ44N trực tiếp từ GPIO 3,3 V nếu chưa có R_DS(on) được bảo đảm tại mức Gate đó. D27-2 không suy thứ tự chân PIR từ ảnh khi chưa biết PCB. D41 không tuyên bố module TP4056 bất kỳ có bảo vệ pin. Đây là giới hạn nghiệm thu thực tế, không phải giấy chứng nhận an toàn phần cứng.
- Bộ cổng hiện tại: `check_diagram_register.py` 80/80; `check_visuals.py --require-all` 56/56 bài có hình, 152 phần tử ảnh/153 tài sản, 0 ASCII, 0 lỗi; `check_links.py` 59 trang/709 tham chiếu, 0 hỏng; `check_navigation.py` 56/56; `build_search_index.py --check` 56 bài; `qa_lesson_visuals.py --widths 320 390 1280 --font-size 24` 168 ca PASS; 320 px dark/24 px 56 ca PASS. `node --check assets/js/sidebar-data.js` và `python -m compileall -q tools` PASS. Arduino-ESP32 sketch không biên dịch được trong môi trường này vì không có `arduino-cli` và board/library chính xác.
- **Cổng còn mở:** điện học 74 hình P7-04 vẫn ghi `not_verified_current_revision` trong sổ; các agent mới rà độc lập một phần, chưa có ERC/mô phỏng/đo phần cứng đầy đủ. Chưa có board/module chính xác và người duyệt kỹ thuật cho các bài cấp nguồn, LiPo, motor/relay, chuyển mức. P7-04/P7-06 và Phase 7 chưa thể đánh dấu PASS theo hợp đồng; Phase 8 chưa được mở theo phụ thuộc P8-01 → P7-06.

Nguồn chính đã đối chiếu ở các chỗ sửa: [Espressif giới hạn GPIO](https://docs.espressif.com/projects/esp-faq/en/latest/hardware-related/hardware-design.html), [TI LM358-N](https://www.ti.com/lit/ds/symlink/lm358-n.pdf), [TI LM2596](https://www.ti.com/lit/ds/symlink/lm2596.pdf), [Pololu A4988 carrier](https://www.pololu.com/product/1182), [Nichicon tụ phân cực](https://www.nichicon.co.jp/english/wp-content/uploads/CAT.8101.pdf), [ADI DS18B20](https://www.analog.com/media/en/technical-documentation/data-sheets/DS18B20.pdf), [ElecFreaks HC-SR04](https://www.elecfreaks.com/download/HC-SR04.pdf). Các URL xác nhận điều kiện trong phạm vi part nêu tại bài; không được dùng để suy module khác revision.
