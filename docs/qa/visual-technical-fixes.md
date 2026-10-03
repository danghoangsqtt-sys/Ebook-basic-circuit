# Bản sửa kỹ thuật từ audit hình — P4-04

Ngày: 2026-10-02. Đối chiếu với 31 nhóm lỗi trong [báo cáo audit](visual-technical-audit.md). Mỗi dòng dưới đây được kết luận sau khi đọc lại sơ đồ, lời giảng và bài thực hành; kiểm tra liên kết/HTML chỉ xác nhận cấu trúc trang, không thay thế kiểm định điện tử.

## Bài 43–54

| Nhóm audit | Kết quả sửa | Cơ sở kiểm tra |
| --- | --- | --- |
| P1 Bài 46 TestPoint | Đã sửa chuỗi thao tác: đặt symbol trên schematic, nối net, gán footprint rồi cập nhật PCB; pad dùng để đo đúng net. | [KiCad: Update PCB from Schematic](https://docs.kicad.org/7.0/en/pcbnew/pcbnew.html) đồng bộ net/footprint từ schematic. |
| P1 Bài 51 PID/heater | Đã phân biệt r, e, u (PWM) và y (nhiệt độ); đổi ví dụ sang PT100 với mạch đo, GPIO25 và driver heater. | [Bosch BME280](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf) có dải nhiệt độ tới 85°C; [Espressif GPIO](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html) liệt kê GPIO25 và cảnh báo GPIO6–11 thường nối flash. |
| P1 Bài 54 đường hồi dòng | Đã vẽ nút GND chung, Z_shared và dòng motor gây sụt áp mốc ADC; giải thích cách đo/xác nhận và sửa đường hồi dòng; bỏ khẳng định star ground áp dụng chung. | Phép sụt áp trên trở kháng chung ΔV = I_motor × Z_shared; đối chiếu các nút và chiều dòng trong hình mới. |
| P2 Bài 43/44/53 | Đã sửa V-model theo cặp thiết kế/kiểm thử, làm rõ giới hạn blocking của ví dụ <code>millis()</code>, và ghi rõ LED WRITE là bài tập mở rộng chưa có trong mã BLE mẫu. | Đọc chéo hình, chú giải và đoạn mã cùng bài. |

## Đối chiếu 31 nhóm phát hiện

Trạng thái “Đã sửa” nghĩa là sơ đồ và đoạn giảng tương ứng đã được đối chiếu trong HTML. Các sơ đồ mới ở Phase 5 vẫn phải kiểm định riêng trước khi xuất bản.

| # | Mức/bài | Trạng thái và thay đổi | Cơ sở kiểm tra |
| ---: | --- | --- | --- |
| 1 | P0 Bài 7 | Đã sửa: bỏ R=10Ω ở nhánh LED xanh; dùng 150Ω với giới hạn độ sáng và tính dòng theo Vf. | (3,3−2,8)/150≈3,3mA; không yêu cầu LED xanh đạt 10mA ở rail 3,3V. |
| 2 | P0 Bài 9 | Đã sửa: R nối tiếp, C từ Vc xuống GND, không còn dây song song nối tắt. | Đọc nút Vc, nguồn, GND và chiều nạp tụ. |
| 3 | P0 Bài 11 | Đã sửa: bốn diode là bốn nhánh giữa AC1/AC2 và DC+/DC−; có đường dẫn cho hai bán kỳ. | Kiểm tra từng đường AC1→D1→tải→D4→AC2 và chiều ngược tương ứng. |
| 4 | P0 Bài 12 | Đã sửa: R_s nối tiếp nguồn, Zener ngược song song tải từ Vout xuống GND; có điều kiện dòng/công suất. | K anode/cathode và phương trình I_Z=I_R−I_load. |
| 5 | P0 Bài 13 | Đã sửa: tụ LM7805/AMS1117 từ từng rail xuống GND; AMS1117 SOT-223 đúng chân 1 GND, 2 OUT/tab, 3 IN theo đúng mã. | [Datasheet AMS1117](https://www.advanced-monolithic.com/pdf/ds1117.pdf) và sơ đồ chân package. |
| 6 | P0 Bài 14 | Đã sửa: sơ đồ nguồn tách VIN_REG, +5V, +3,3V và GND; mọi tụ song song rail; hạn dòng tải thử và bước đo trước khi cấp ESP32. | Rà từng nút/đường hồi và công suất nhiệt của hai IC ổn áp. |
| 7 | P0 Bài 15 | Đã sửa: pinout BC547 theo onsemi C–B–E khi nhìn mặt chữ; LED+R là nhánh tải từ +5V đến collector, emitter GND. | [onsemi BC547](https://www.onsemi.com/download/data-sheet/pdf/bc546-d.pdf). |
| 8 | P0 Bài 16/18 | Đã sửa: diode flyback ngược song song cuộn relay/motor; bỏ thao tác tháo diode để thử; ghi đường hồi dòng sau khi ngắt. | Cathode ở rail dương, anode ở collector/drain; kiểm tra bài thực hành. |
| 9 | P0 Bài 17 | Đã sửa: Vin qua C_in vào base, cầu R1/R2 neo +12V/GND, R_C ở collector, C_E song song R_E; chỉnh công thức gain. | Kiểm tra điểm phân cực B/C/E và đường AC. |
| 10 | P0 Bài 21 | Đã sửa: NTC làm V_sensor giảm khi nóng và nối IN(−); V_ref ở IN(+); relay là nhánh cuộn +5V→C, diode song song; LED là nhánh riêng. | [TI LM358-N](https://www.ti.com/lit/ds/symlink/lm358-n.pdf) cho miền common-mode/output và dòng điều khiển. |
| 11 | P0 Bài 23 | Đã sửa: SDA/SCL là hai net độc lập, mỗi net pull-up riêng và GND chung. | Kiểm tra đường bus theo tên net; rail logic ESP32 3,3V. |
| 12 | P0 Bài 24 | Đã sửa: MOSI/MISO/SCK riêng, chia sẻ giữa hai slave; CS riêng mỗi thiết bị. | Đối chiếu master/slave và chiều MISO. |
| 13 | P0 Bài 32 | Đã sửa: Q_sw→SW→L→Vout, diode cathode ở SW/anode GND, C_out từ Vout xuống GND. | Kiểm tra đường dòng pha ON/OFF và nút SW. |
| 14 | P0 Bài 35 | Đã sửa: LM2596 pin 1 VIN, pin 2 OUTPUT/SW, diode cathode SW, FB từ Vout sau L; bước KiCad yêu cầu kiểm tra mã/package. | [TI LM2596](https://www.ti.com/lit/ds/symlink/lm2596.pdf). |
| 15 | P0 Bài 38 | Đã sửa: SLP/RST giữ HIGH, EN active LOW, tụ bulk VMOT–GND, Vref tính từ R_sense của carrier cụ thể và dòng motor. | [Pololu A4988 carrier](https://www.pololu.com/product/1182), [Allegro A4988](https://www.allegromicro.com/~/media/files/datasheets/a4988-datasheet.pdf). |
| 16 | P0 Bài 42 | Đã sửa: robot dùng một cell LiPo 1S→bảo vệ→boost 5V; ECHO HC-SR04 qua chia áp 10kΩ/15kΩ tới GPIO, GND chung. | [Adafruit HC-SR04](https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/pinouts), [ESP32-WROOM-32](https://documentation.espressif.com/esp32-wroom-32_datasheet_en.html); 5V×15/(10+15)=3,0V. |
| 17 | P1 Bài 1 | Đã sửa cực hai pin AA và mốc 0/1,5/3V; vòng dòng quy ước và electron được mô tả riêng. | Kiểm tra hai suất điện động nối tiếp và chiều dòng vòng kín. |
| 18 | P1 Bài 4/11 | Đã sửa nhãn A/K và vạch cathode, tách mũi tên phát sáng khỏi ký hiệu LED; bỏ ký hiệu tam giác gây hiểu nhầm trong chế độ đo diode. | Đối chiếu ký hiệu và vạch thực trên linh kiện. |
| 19 | P1 Bài 12 | Đã bỏ khẳng định Zener 3,3V kẹp GPIO chính xác; ví dụ chuyển tín hiệu 5V bằng chia áp 10kΩ/15kΩ có ghi điều kiện rail/tốc độ. | [ESP32-WROOM-32](https://documentation.espressif.com/esp32-wroom-32_datasheet_en.html) cho điện áp đầu vào. |
| 20 | P1 Bài 20 | Đã đặt nguồn LM358 ±9V cho ví dụ Vout âm; nguồn đơn có Vref và giới hạn miền vào/ra. | [TI LM358-N](https://www.ti.com/lit/ds/symlink/lm358-n.pdf). |
| 21 | P1 Bài 26 | Đã đặt tụ debounce tại nút GPIO xuống GND, song song công tắc; pull-up ngoài 10kΩ rõ ràng. | Kiểm tra hai nhánh GPIO→switch→GND và GPIO→C→GND. |
| 22 | P1 Bài 27 | Đã bỏ thứ tự chân PIR áp dụng mọi board; yêu cầu đọc nhãn và đo mức OUT của module thực trước khi vào ESP32. | Khác biệt pinout/điện áp theo biến thể module. |
| 23 | P1 Bài 31 | Đã sửa lời giải thích LPF và thêm R1 shunt vào tầng HPF của band-pass; ghi tương tác giữa hai tầng. | X_C=1/(2πfC); kiểm tra Vout lấy trên C ở LPF và R ở HPF. |
| 24 | P1 Bài 39 | Đã đặt motor giữa hai nút cầu H và đổi bảng L298N: EN HIGH, IN bằng nhau hãm; EN LOW thả trôi. | [ST L298](https://www.st.com/resource/en/datasheet/l298.pdf). |
| 25 | P1 Bài 40/41 | Đã thêm chia áp ECHO 10kΩ/15kΩ và GND chung; TP4056 là IC sạc 1S, mạch bảo vệ tùy module/IC; sửa phép tính thời gian pin theo Wh. | [ESP32-WROOM-32](https://documentation.espressif.com/esp32-wroom-32_datasheet_en.html), [TP4056](https://www.toppwr.com/uploadfile/file/20230304/640301eae1260.pdf). |
| 26 | P1 Bài 46 | Đã sửa quy trình TestPoint schematic→footprint→Update PCB. | [KiCad PCB Editor](https://docs.kicad.org/7.0/en/pcbnew/pcbnew.html). |
| 27 | P1 Bài 51 | Đã phân biệt r/e/u/y trong vòng PID, chọn cảm biến ≥100°C và GPIO25, ghi driver heater. | [Bosch BME280](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf), [Espressif GPIO](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html). |
| 28 | P1 Bài 54 | Đã thể hiện Z_shared trên đường hồi motor/ADC, sụt áp theo I×Z; bỏ quy tắc star ground tuyệt đối. | Rà đường hồi dòng và nút mốc ADC trong sơ đồ. |
| 29 | P2 Bài 2 | Đã thay hình ASCII giả định 30 cột bằng ví dụ 63 cột, hai nhóm a–e/f–j và rail có thể ngắt; bài đo continuity sửa theo nút thật. | Kiểm tra topology board 830 lỗ; ảnh 400 lỗ được ghi đúng model riêng. |
| 30 | P2 Bài 19 | Đã vẽ PWM theo 8 ô cùng chu kỳ và bỏ khẳng định duty 50%=nửa tốc motor. | Đối chiếu T_on/T và V_avg=D×V_high. |
| 31 | P2 Bài 43/44/53 | Đã sửa V-model, giới hạn blocking của <code>millis()</code>, và BLE GATT khớp code chỉ có TEMP; LED WRITE ghi là phần mở rộng. | Đọc chéo hình, chú giải và mã trong từng bài. |

## Kiểm tra cấu trúc

- `python tools/check_links.py`: 59 trang, 490 tham chiếu nội bộ, 0 hỏng.
- `python tools/check_visuals.py`: 56/56 bài, 80 khối ASCII còn trong bài, 0 lỗi tài sản/alt/nguồn; chỉ 2 bài hiện có hình, sẽ mở rộng ở Phase 5.
- `python tools/build_search_index.py`: tạo lại chỉ mục từ 56 bài đã sửa.
- `python tools/build_search_index.py --check`: 56 bài, chỉ mục còn mới.
- `python tools/qa_browser.py --quick`: Chromium PASS, gồm 4 viewport trang đầu, 24 trường hợp bài/viewport và các luồng đọc, thư viện, sao lưu.
- Audit lại phát hiện đáp án Bài 12 vẫn khuyên Zener 3,3/3,6V như bảo vệ GPIO chắc chắn và chọn R_s=68Ω dù không đạt I_Z ở tải lớn; đã sửa cả bốn câu hỏi/đáp án theo miền tải và dung sai. Bài 18 đã làm rõ V_GS(th) không thay thế R_DS(on) trong mục tiêu, bảng linh kiện và đáp án.

Giới hạn: đây là kiểm tra tài liệu, phép tính và mô phỏng trình duyệt; chưa kiểm tra phần cứng thật hoặc độc lập nghiệm thu điện tử toàn bộ 56 bài. Trước khi lắp mạch cần đối chiếu datasheet của đúng linh kiện/module đang có và đo rail thực tế.
