# Phiếu chuẩn bị nghiệm thu Pico non-W + TMP36GT9Z

Trạng thái 2026-10-04: **chưa có board, part, dụng cụ, phép đo hoặc reviewer được xác nhận**. Phiếu này là trình tự thu thập bằng chứng cho P9-04/A29–A32; không chứng minh mạch đã hoạt động. Chỉ người có thiết bị thật và người duyệt kỹ thuật mới điền kết quả.

## 1. Chốt đúng mẫu trước khi nối

| Mục | Phải ghi và giữ bằng chứng |
| --- | --- |
| Board | Ảnh hai mặt, marking Pico **non-W**, revision, nguồn USB dùng, firmware MicroPython/phiên bản, SHA-256 của đúng file đã nạp |
| Sensor | Ảnh marking TMP36GT9Z và package TO-92, lô/mã mua; [ADI Rev. H Fig. 4](https://www.analog.com/media/en/technical-documentation/data-sheets/tmp35_36_37.pdf) ghi **bottom view** pin 1 `+VS`, pin 2 `VOUT`, pin 3 `GND` |
| Tụ và dây/carrier | Mã tụ 0,1 µF, điện áp/dung sai/package, vị trí trên carrier, ảnh mặt trên/mặt dưới và đánh dấu góc nhìn chân sensor |
| Dụng cụ | ID đồng hồ đo áp, ngày hiệu chuẩn, độ phân giải/uncertainty; ID chuẩn nhiệt và uncertainty/k; setup đo và thời gian ổn định |
| Người duyệt | Họ tên, ngày, chữ ký, revision schematic/PCB được duyệt; ghi mục chưa thử |

Theo [Raspberry Pi Pico documentation](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) và [pinout chính thức](https://pip-assets.raspberrypi.com/categories/610-raspberry-pi-pico/documents/RP-008309-DS-1-Pico-R3-A4-Pinout.pdf?disposition=inline), board non-W dùng pin 36 `3V3(OUT)`, pin 33 `AGND`, pin 31 `GP26/ADC0` và LED onboard `GP25`. Pico W có đường LED khác, nên không được thay board theo tên gần giống. [MicroPython RP2 v1.26](https://docs.micropython.org/en/v1.26.0/rp2/quickref.html) cho `ADC(Pin(26)).read_u16()` 0…65535 qua API, trong khi ADC phần cứng là 12 bit.

## 2. Rà net và nguồn khi chưa cấp điện

Schematic CAD và ERC/DRC chưa có. Khi dựng CAD, reviewer độc lập so từng net với bảng này và ký bản revision; không gọi SVG là schematic đã ERC.

| Net | Điểm cần nối | Kiểm bằng dụng cụ khi chưa cấp điện |
| --- | --- | --- |
| `+3V3` | Pico 36 → TMP36 pin 1 + C1 đầu 1 | Thông mạch đúng điểm; không ngắn với AGND/TEMP_V |
| `TEMP_V` | TMP36 pin 2 → Pico 31 GP26/ADC0 | Thông mạch đúng điểm; không dính `+3V3` hoặc AGND |
| `AGND` | TMP36 pin 3 + C1 đầu 2 → Pico 33 | Đường hồi liên tục; không ngắn `+3V3` |
| `LED_GP25` | Chỉ là LED onboard Pico non-W | Không đưa ra chân carrier tưởng tượng |

Trước khi cấp USB: chụp góc nhìn part, so pin 1/2/3 theo **bottom view**, kiểm không đảo cực tụ nếu dùng loại có cực (bài này định dùng gốm không cực), kiểm không có dây 5 V vào `GP26`. Ghi reviewer chấp nhận net/nguồn rồi mới thử có điện. Nếu CAD/part/reviewer chưa đủ, dừng ở bước này.

## 3. Thu thập phép đo có điều kiện

Sau khi mạch đã được duyệt và lắp đúng revision, ghi điều kiện môi trường, setup nguồn, firmware, dụng cụ và uncertainty. Đo `VBUS`, `VSYS`, `3V3(OUT)`, `ADC_VREF` (pin 35) và `TEMP_V` với cùng mốc AGND; đo nhiệt chuẩn, ghi giá trị lúc khởi động và sau ổn định. Không suy `ADC_VREF` bằng đúng 3,300 V từ tên rail.

Ở các điểm nhiệt tăng rồi giảm qua 27/28/29/30/31 °C, đợi sensor và chuẩn cùng ổn định theo setup đã ghi. Với **mỗi lần đọc đồng bộ**, lưu raw `read_u16`, `TEMP_V` đo bởi DMM, `ADC_VREF` đo, nhiệt chuẩn, uncertainty chuẩn và trạng thái LED quan sát. Lưu ảnh/log nguồn cùng thời gian. Mốc đúng 28/30 °C có thể đổi phía sau lượng tử hóa; chấm LED theo nhiệt **firmware tính từ raw**, không theo nhiệt đặt danh định. Chạy đủ chiều tăng/giảm để thấy nhánh giữ hysteresis.

Điền một dòng mỗi mẫu vào [CSV trống](pico-tmp36-measurements-template.csv). `run_id` tách lần khởi động mới; `sample_index` bắt đầu 0 và liên tục, `timestamp_utc` là thời điểm ISO 8601 UTC tăng theo lần đọc. Ghi cửa sổ lấy mẫu/độ lệch thời gian giữa DMM, chuẩn và raw trong nhật ký đo; chỉ ghép chúng khi nhiệt đã ổn định. SHA-256 phải là file firmware đã nạp; `firmware_reference_v` là tham số thực sự đưa vào `run` (mặc định 3,3 V), không phải phép đo `adc_vref_v`. `reference_u_c` là độ bất định ±°C của chuẩn trong điều kiện đo; ghi coverage factor/k và chứng chỉ trong nhật ký ngoài CSV. `led_observed` ghi 0/1 từ mắt hoặc log độc lập. Không điền số mô phỏng vào CSV đo.

Chạy:

```text
python tools/analyze_phase10_measurements.py docs/qa/pico-tmp36-measurements-template.csv
```

Với file mới chỉ có header, kết quả phải là `no_data`, `hardware_accepted: false`. Với CSV đo thật, công cụ tính nhiệt từ VOUT theo đường **danh định** ADI (`T=(VOUT−0,500)/0,010`), nhiệt từ raw theo VREF đo, nhiệt firmware theo tham số firmware, sai khác với chuẩn và LED dự kiến theo hysteresis. `analysis_only` chỉ có nghĩa là bản ghi hợp lệ và không có cờ cơ bản; **không phải PASS độ chính xác, ERC, an toàn hay board**. `review_required` yêu cầu điều tra cờ như LED lệch, VOUT vượt VREF hoặc VREF ngoài miền mô hình. Reviewer đối chiếu sai khác với uncertainty đầy đủ của chuẩn, DMM, sensor, ADC và điều kiện nhiệt trước khi kết luận.

## 4. Phiếu kết luận của reviewer

| Trường | Điền khi có bằng chứng thật |
| --- | --- |
| Board/part/firmware/dụng cụ và revision | chưa có |
| Schematic CAD, ERC, PCB DRC và ảnh đối chiếu net | chưa có |
| File CSV đo thật, log nguồn và báo cáo sai khác | chưa có |
| Uncertainty budget, điểm fit và điểm kiểm độc lập | chưa có |
| Lỗi mở, cách xử lý, phép thử lặp lại | chưa có |
| Reviewer, ngày, chữ ký và phạm vi được duyệt | chưa có |

Chỉ cập nhật [sổ phần cứng](curriculum-hardware-pending.md) và trạng thái P10-04 sau khi các trường cần thiết có chứng cứ kiểm lại được. Không suy bằng chứng vật lý từ kết quả host fake hoặc CSV tổng hợp của test.
