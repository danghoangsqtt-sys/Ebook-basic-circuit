# Đồ án tăng dần A29–A32: bộ báo nhiệt Pico/TMP36 thấp áp

Ngày soạn 2026-10-04. Bốn chặng cùng một hệ nhằm kiểm được luồng yêu cầu → sơ đồ → ngân sách → mô phỏng → phép đo → sai khác. Chưa có PCB/board/sensor/chuẩn nhiệt thật hoặc người duyệt kỹ thuật. Các sơ đồ dưới đây là **netlist học tập**, không phải tệp KiCad đã qua ERC/DRC hay thiết kế được chứng nhận để cấp điện.

**Nguồn hãng trực tiếp:** [Raspberry Pi Pico datasheet §2, §4.5](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf) cho pinout, ADC_VREF, rail và nguồn USB→D1→VSYS→SMPS; [Raspberry Pi Pico board docs](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) cho pin 31/33/36 và LED non-W GP25; [ADI TMP36 Rev. H Fig. 4, Fig. 24, ordering table](https://www.analog.com/media/en/technical-documentation/data-sheets/tmp35_36_37.pdf) cho pin TO-92 nhìn đáy, 0,1 µF bypass, 2,7–5,5 V và điện áp danh định; [MicroPython RP2 ADC v1.26](https://docs.micropython.org/en/v1.26.0/rp2/quickref.html) cho `ADC(Pin(26)).read_u16()`. Sơ đồ/hình do dự án tự tạo, không sao chép hình hãng. Board reference Rev3 và TMP36GT9Z là mã để học; revision/marking part thật chưa xác nhận.

## A29 — yêu cầu và sơ đồ khối

**Yêu cầu kiểm được:** cảm nhận nhiệt độ mô hình 20…40 °C, mỗi giây có một bản ghi raw ADC/nhiệt danh định/trạng thái; LED onboard bật khi T_est≥30 °C, tắt khi T_est≤28 °C, giữ ở giữa; hệ dùng USB Pico không W, không có radio/tải ngoài/nguồn điện lưới. Đây là mục tiêu cho *mô hình*; độ chính xác nhiệt thật chưa có chuẩn để chốt.

**Sơ đồ khối và schematic net:** `USB → D1/VSYS/SMPS Pico → +3V3 → TMP36 +VS`; `TMP36 VOUT → GP26/ADC0 → hàm đổi số → FSM hysteresis → GP25/LED onboard`; `TMP36 GND → AGND Pico`; C1 `0,1 µF` giữa +3V3–AGND sát sensor. Bản net/bản chữ và SVG ở [lab P9-04](../labs/pico-tmp36-monitor.md). TMP36 TO-92 Fig. 4 là **bottom view**: 1 +VS, 2 VOUT, 3 GND. Không suy thứ tự mặt trước.

| BOM A29 | Model | Số lượng | Chưa chốt vật lý |
| --- | --- | ---: | --- |
| B1 | Pico RP2040 non-W, hình Rev3 reference | 1 | PCB marking/firmware thực |
| U1 | TMP36GT9Z TO-92 theo ADI Rev. H | 1 | Marking/grade/supplier thực |
| C1 | Gốm 0,1 µF | 1 | Mã/footprint/voltage/temp thật |

**Ngân sách A29:** nguồn TMP36 2,7…5,5 V, ở rail danh định 3,3 V còn khoảng 0,6 V trên mức min; khoảng này **không** chứng minh rail thực ổn định. Ở 20/40 °C, VOUT danh định 0,70/0,90 V, trong dải ADC giả định 0…3,3 V. Dòng sensor dưới 50 µA theo datasheet, tiêu thụ Pico/USB chưa đo. **Mô phỏng/đối chiếu:** `python tools/simulate_phase9_sensor_lab.py`, `python tools/verify_phase9_sensor_lab.py` xác nhận chuỗi phần mềm theo ADC lý tưởng. **Bước đo tương lai:** kiểm USB/3V3/VREF trước sensor, đo VOUT ở 20/30/40 °C với chuẩn nhiệt được chọn, lưu raw/timestamp. **Báo cáo sai khác:** điền `Vđo−Vdanh định`, `T_est−T_chuẩn` tại từng điểm; hiện ghi “chưa đo”, không điền 0.

## A30 — thiết kế nguồn thấp áp

**Yêu cầu:** chỉ cấp Pico bằng micro-USB theo hướng dẫn hãng, dùng `3V3(OUT)` pin 36 để cấp TMP36. Không mở adapter điện lưới, không cấp ngược 3V3(OUT), không nối nguồn phụ vào VSYS trong bài này. Pin 33 AGND là hồi sensor/ADC. Pico datasheet §4.5 mô tả USB VBUS qua diode D1 tới VSYS, rồi nguồn board tạo 3,3 V; giá trị USB 5 V là danh định, không suy rail chính xác khi tải.

**Schematic net/khối:** `USB VBUS → D1 (trên Pico) → VSYS (trên Pico) → SMPS (trên Pico) → 3V3(OUT) pin 36 → U1 +VS pin 1`; `C1 0,1 µF` nối 3V3–AGND gần U1; `U1 GND pin 3 → AGND pin 33`; `U1 VOUT pin 2 → GP26 pin 31`; LED onboard từ GP25. D1/SMPS là phần **có sẵn trên board**, không phải linh kiện thêm vào PCB carrier.

| BOM A30 | Model | Vai trò |
| --- | --- | --- |
| B1/U1/C1 | như A29 | Pico tạo rail; U1 là tải duy nhất bên ngoài; C1 bypass |
| J1 | Cổng micro-USB trên Pico | không thiết kế adapter hoặc jack nguồn riêng |

**Ngân sách nguồn:** ADI ghi TMP36 supply current <50 µA; ở 3,3 V, `P_U1 <3,3×50 µA=0,165 mW` theo giới hạn dòng trong điều kiện datasheet. Pico datasheet khuyên tải ngoài ở 3V3(OUT) <300 mA tùy VSYS và tải RP2040; 50 µA chỉ là một tải rất nhỏ, **không** là tổng dòng board hay phép chứng nhận nguồn. Board/firmware/USB có thể tạo ripple và offset ADC. **Mô phỏng số:** `python tools/simulate_phase10_design.py` xuất 10 kịch bản nguồn tham chiếu lý tưởng 3,300/3,333 V và điện áp sensor; chưa mô hình D1, SMPS, tụ ESR hoặc quá độ. **Đo tương lai:** với board thật, đo VBUS/VSYS/3V3/ADC_VREF và nhiệt nguồn ở không tải/có sensor; dùng probe/ground đúng setup và ghi uncertainty. **Sai khác:** so từng rail với dự đoán có điều kiện; hiện chưa có kết quả.

## A31 — sensor, ADC và firmware MCU

**Yêu cầu:** tính nhiệt danh định từ raw code, lưu raw, bật/tắt LED theo hai ngưỡng và không dùng dữ liệu tổng hợp A28 để nhận là hiệu chuẩn sensor thật. GP26/ADC0 là pin 31; LED GP25 là nội bộ Pico non-W. Mã ở [`labs/pico_tmp36_monitor.py`](../../labs/pico_tmp36_monitor.py).

**Schematic/BOM:** các net A30 được giữ; U1 pin 2 đi thẳng tới GP26/ADC0, không có cầu chia hay level shifter trong mô hình vì VOUT danh định 0,10…1,75 V cho −40…125 °C và rail sensor 3,3 V. Khi thiết kế thật phải kiểm cả điện áp lỗi/điều kiện cực trị và đặc tính ADC. BOM là B1/U1/C1, không có cảm biến thứ hai hoặc LED ngoài.

**Phép tính:** `V=0,500+0,010T` (V) danh định ADI. `ADC_u16=round(V/3,300×65535)` trong mô hình; tại 25 °C → 0,750 V → code 14894 → T_est≈24,9984 °C. API 16 bit biểu diễn không có nghĩa ADC silicon 16 bit; RP2040 ADC là 12 bit. Nếu **giả định bài tập** VREF thực lệch +1% nhưng code giải theo 3,300 V, cỡ sai lệch ở 0,75 V là khoảng 7,5 mV/0,75 °C; nửa bước ADC 12 bit lý tưởng là `3,3/4096/2/0,01≈0,0403 °C`. Những số này chưa gồm sai số sensor, phi tuyến ADC, noise, tự gia nhiệt, tiếp xúc nhiệt và chuẩn. Không ghép số typical của sensor vào một bảo đảm toàn hệ.

**Mô phỏng:** tám kích thích P9-04 cho LED `0,0,0,1,1,0,0,1`; mốc kích thích 30 °C lượng tử hóa thành T_est≈29,9986 °C, không bật, nên phải chấm theo raw giải mã. **Đo tương lai:** ghi raw VREF/VOUT/chuẩn nhiệt và trạng thái LED ở 27/28/29/30/31 °C sau ổn định nhiệt; kiểm cả tăng/giảm và thời gian trễ. **Sai khác:** `T_est−T_chuẩn` theo từng hướng; chưa có điểm đo thật.

## A32 — PCB carrier tích hợp và báo cáo

**Yêu cầu thiết kế số:** tạo carrier/phiếu layout cho Pico non-W và TMP36, chỉ đưa ra pin 31,33,36 của Pico; C1 sát U1; giữ TEMP_V ngắn và cách đường nguồn/switching, đường hồi sensor về AGND. Trên bản in cần đánh rõ **góc nhìn đáy TO-92**; footprint thực phải kiểm với part được mua. Không định tuyến GP25 ra header vì LED là onboard. Không tạo điện lưới, cell Li-ion hoặc tải motor trong carrier.

**Schematic net/BOM A32:** net `+3V3={B1.36,U1.1,C1.1}`, `TEMP_V={U1.2,B1.31}`, `AGND={U1.3,C1.2,B1.33}`; GP25→LED là net có sẵn trên B1. BOM B1 Pico non-W, U1 TMP36GT9Z, C1 gốm 0,1 µF, cơ cấu carrier/đầu nối **chưa chốt mã/footprint**; không tự nhận bản vẽ này là tệp KiCad/ERC hoàn chỉnh. [SVG sơ đồ P9-04](../../assets/images/labs/pico-tmp36-monitor.svg) là hình đọc; file layout/gerber chỉ lập sau khi part/board được xác nhận.

**Ngân sách:** nguồn và sai số giữ từ A30/A31. Dự đoán số học 25 °C → 0,750 V → code 14894, LED off; 31 °C → 0,810 V → LED on; 29 °C sau đó → giữ on. C1 chọn theo khuyến nghị bypass ADI, giá trị thực theo dung sai/DC bias chưa chọn; không tuyên bố EMI đã đạt. **Mô phỏng:** kiểm model host, không có SPICE/field/EMC/PCB thermal. **Bước đo/reviewer:** chọn part/supplier/footprint và board marking; dựng CAD schematic, chạy ERC rồi DRC; độc lập so từng net và góc nhìn chân; sau duyệt mới lắp/cấp USB, ghi rail/VREF/raw/nhiệt chuẩn/LED và kiểm lỗi mở/ngắn/đảo. Người duyệt, ngày ký và báo cáo sai khác phần cứng: **pending**.

## Mẫu báo cáo sai khác (không điền giá trị giả)

| Mẫu/board/firmware | Điểm chuẩn, điều kiện | VREF/VOUT/raw đo | T_est và trạng thái | Sai khác so mô hình/chuẩn | Người duyệt |
| --- | --- | --- | --- | --- | --- |
| chưa có | chưa có | chưa đo | chưa đo | chưa tính | chưa ký |

Khi có dữ liệu, giữ ảnh board/marking, datasheet revision, schematic/ERC/DRC, nguồn USB, phiên bản MicroPython, setup DMM/chuẩn nhiệt và uncertainty. Rubric riêng ở A29–A32 không cho điểm “đã chạy thật” từ log mô hình.
