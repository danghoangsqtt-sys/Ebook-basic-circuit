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
