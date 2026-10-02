# Kiểm định sơ đồ ký tự — Phase 4 / P4-02

Ngày: 2026-10-02. Phạm vi: toàn bộ 80 khối `circuit-ascii` trong 56 bài. Mức độ ở bảng là **ưu tiên kiểm tra** theo khả năng gây hiểu sai hoặc đấu mạch sai; không phải kết luận sơ đồ đã đúng. Các lỗi xác nhận nằm ở phần sau bảng.

## Quy tắc rà

- **Cao:** sơ đồ đấu nguồn, pinout, linh kiện phân cực, driver, chuyển mức hoặc mạch có nguy cơ hỏng linh kiện; phải so với nội dung và datasheet đúng model trước khi vẽ lại.
- **Vừa:** nguyên lý mạch/timing hoặc sơ đồ hệ thống; so giá trị, nút nối, chiều mũi tên và điều kiện áp dụng.
- **Thấp:** hình ký hiệu hoặc quy trình ít rủi ro; giữ văn bản nếu chính xác, thêm hình tổng quan để đọc dễ hơn.

## Danh mục đủ 80 khối

| ID | Vị trí | Nội dung | Ưu tiên | Hướng xử lý |
| --- | --- | --- | --- | --- |
| D01-1 | `week1/day01.html:173` | Hai pin AA nối tiếp: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D01-2 | `week1/day01.html:258` | Chiều dòng điện trong mạch đơn giản: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D01-3 | `week1/day01.html:316` | Các ký hiệu GND phổ biến: | Thấp | Giữ mô tả văn bản, bổ sung hình tổng quan |
| D01-4 | `week1/day01.html:350` | So sánh dạng sóng DC và AC: | Thấp | Giữ mô tả văn bản, bổ sung hình tổng quan |
| D01-5 | `week1/day01.html:375` | Mạch kín (có dòng):         Mạch hở (không có dòng): | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D02-1 | `week1/day02.html:101` | Sơ đồ cấu trúc breadboard 830 lỗ (nhìn từ trên xuống): | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D02-2 | `week1/day02.html:401` | Sơ đồ mạch trên breadboard: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D03-1 | `week1/day03.html:64` | Ký hiệu điện trở: | Thấp | Giữ mô tả văn bản, bổ sung hình tổng quan |
| D03-2 | `week1/day03.html:127` | Ví dụ: Nâu · Đen · Đỏ · Vàng kim | Thấp | Giữ mô tả văn bản, bổ sung hình tổng quan |
| D03-3 | `week1/day03.html:159` | Ví dụ: Nâu · Đen · Đen · Đỏ · Nâu | Thấp | Giữ mô tả văn bản, bổ sung hình tổng quan |
| D04-1 | `week1/day04.html:71` | LED 5mm thông dụng — nhìn từ bên cạnh: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D05-1 | `week1/day05.html:65` | Mạch nối tiếp 3 điện trở: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D05-2 | `week1/day05.html:99` | Mạch song song 3 điện trở: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D05-3 | `week1/day05.html:169` | Mạch hỗn hợp: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D06-1 | `week1/day06.html:74` | Mạch: 5V → R1(1kΩ) → R2(2kΩ) → R3(2kΩ) → GND | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D06-2 | `week1/day06.html:108` | Minh họa KCL tại node A: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D06-3 | `week1/day06.html:127` | Cầu chia áp cơ bản: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D06-4 | `week1/day06.html:161` | Cầu chia áp với tải R_load: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D06-5 | `week1/day06.html:189` | Cầu chia áp LDR — Cảm biến ánh sáng: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D07-1 | `week1/day07.html:143` | Sơ đồ mạch Mini Project: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D08-1 | `week2/day08.html:68` | Cấu tạo tụ điện cơ bản: | Thấp | Giữ mô tả văn bản, bổ sung hình tổng quan |
| D08-2 | `week2/day08.html:131` | Tụ hóa 100µF/25V — nhận dạng: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D08-3 | `week2/day08.html:199` | Decoupling capacitor — vị trí đặt: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D09-1 | `week2/day09.html:64` | Mạch RC nạp tụ: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D10-1 | `week2/day10.html:63` | Đặc tính cuộn cảm: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D10-2 | `week2/day10.html:146` | Mạch điều khiển relay đúng cách: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D11-1 | `week2/day11.html:64` | Cấu tạo diode và ký hiệu: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D11-2 | `week2/day11.html:122` | Mạch chỉnh lưu bán sóng: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D11-3 | `week2/day11.html:139` | Cầu diode 4 linh kiện: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D12-1 | `week2/day12.html:65` | Diode Zener — hướng cắm: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D12-2 | `week2/day12.html:129` | Bảo vệ GPIO ESP32 khỏi quá áp: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D13-1 | `week2/day13.html:86` | Sơ đồ chân LM7805 (TO-220): | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D13-2 | `week2/day13.html:136` | Sơ đồ chân AMS1117 (SOT-223): | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D14-1 | `week2/day14.html:73` | Mạch nguồn DC hoàn chỉnh: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D15-1 | `week3/day15.html:71` | NPN Transistor BC547 — Ký hiệu và sơ đồ chân: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D15-2 | `week3/day15.html:141` | Mạch switch NPN cơ bản: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D16-1 | `week3/day16.html:73` | Mạch relay driver BC337 — sơ đồ chuẩn: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D16-2 | `week3/day16.html:120` | Mạch buzzer với NPN switch: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D17-1 | `week3/day17.html:63` | Mạch khuếch đại CE cơ bản: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D18-1 | `week3/day18.html:69` | So sánh MOSFET NMOS và BJT NPN: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D18-2 | `week3/day18.html:124` | NMOS Switch chuẩn điều khiển motor DC: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D19-1 | `week3/day19.html:48` | PWM — 3 ví dụ duty cycle khác nhau: | Thấp | Giữ mô tả văn bản, bổ sung hình tổng quan |
| D19-2 | `week3/day19.html:101` | PWM → Analog qua RC filter: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D20-1 | `week3/day20.html:63` | Ký hiệu Op-Amp và chân LM358 (DIP-8): | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D20-2 | `week3/day20.html:107` | Inverting Amplifier: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D20-3 | `week3/day20.html:130` | Voltage Follower — A_V = 1, không đảo pha: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D20-4 | `week3/day20.html:141` | Comparator: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D21-1 | `week3/day21.html:73` | Mạch phân áp NTC + R_ref: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D21-2 | `week3/day21.html:88` | Hệ thống Báo Nhiệt Tự Động: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D22-1 | `week4/day22.html:62` | Kết nối UART giữa 2 thiết bị: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D22-2 | `week4/day22.html:90` | Frame UART 8N1 (8 data bits, No parity, 1 Stop bit): | Thấp | Giữ mô tả văn bản, bổ sung hình tổng quan |
| D22-3 | `week4/day22.html:113` | Level Shifter đơn giản 5V→3.3V: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D23-1 | `week4/day23.html:68` | Kết nối I2C — nhiều thiết bị chung bus: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D23-2 | `week4/day23.html:103` | Frame I2C — ghi 1 byte vào thiết bị: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D24-1 | `week4/day24.html:62` | SPI — 4 dây cơ bản: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D26-1 | `week4/day26.html:93` | Hardware debounce (RC filter): | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D27-1 | `week4/day27.html:61` | Kết nối DHT22 — 4 chân (nhìn mặt phẳng có lưới): | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D27-2 | `week4/day27.html:136` | HC-SR501 — 3 chân: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D28-1 | `week4/day28.html:66` | Sơ đồ task / luồng xử lý: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D30-1 | `week5/day30.html:65` | Layout oscilloscope cơ bản (DSO/analog): | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D31-1 | `week5/day31.html:57` | RC Low Pass Filter:               RC High Pass Filter: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D31-2 | `week5/day31.html:87` | Band Pass Filter = HPF + LPF nối tiếp: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D32-1 | `week5/day32.html:48` | Buck Converter — nguyên lý: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D33-1 | `week5/day33.html:46` | Quy trình từ ý tưởng đến PCB hoàn chỉnh: | Thấp | Giữ mô tả văn bản, bổ sung hình tổng quan |
| D35-1 | `week5/day35.html:69` | Mạch LM2596S-5V chuẩn từ datasheet: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D37-1 | `week6/day37.html:125` | Kiến trúc MQTT: | Thấp | Giữ mô tả văn bản, bổ sung hình tổng quan |
| D38-1 | `week6/day38.html:47` | Kết nối A4988 driver với NEMA 17: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D39-1 | `week6/day39.html:45` | H-Bridge — 4 switch tạo thành chữ "H": | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D40-1 | `week6/day40.html:45` | Nguyên lý HC-SR04: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D41-1 | `week6/day41.html:68` | Module TP4056 + BMS tích hợp (module xanh/đỏ): | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D42-1 | `week6/day42.html:67` | Sơ đồ hệ thống Robot WiFi: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D43-1 | `week7/day43.html:44` | Vòng đời thiết kế hệ thống nhúng (V-Model): | Thấp | Giữ mô tả văn bản, bổ sung hình tổng quan |
| D44-1 | `week7/day44.html:44` | Cấu trúc thư mục dự án Arduino/PlatformIO: | Thấp | Giữ mô tả văn bản, bổ sung hình tổng quan |
| D45-1 | `week7/day45.html:44` | Thứ tự test module — bottom-up: | Thấp | Giữ mô tả văn bản, bổ sung hình tổng quan |
| D46-1 | `week7/day46.html:61` | Thêm Test Point (TP) trong KiCad: | Thấp | Giữ mô tả văn bản, bổ sung hình tổng quan |
| D51-1 | `week8/day51.html:45` | Vòng điều khiển PID: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D53-1 | `week8/day53.html:44` | BLE GATT Hierarchy: | Vừa | Đối chiếu nội dung, quyết định giữ hoặc vẽ lại |
| D54-1 | `week8/day54.html:49` | Tại sao cần decoupling: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D54-2 | `week8/day54.html:84` | Ground loop gây nhiễu: | Cao | Kiểm tra và vẽ lại sơ đồ kỹ thuật |
| D55-1 | `week8/day55.html:31` | Lộ trình sau khóa học cơ bản: | Thấp | Giữ mô tả văn bản, bổ sung hình tổng quan |

## Lỗi kỹ thuật được xác nhận

Các phát hiện dưới đây đến từ việc đọc sơ đồ cùng đoạn giảng và bài thực hành. **P0** cần sửa trước khi dùng sơ đồ để lắp mạch; **P1** có thể dẫn tới hiểu sai hoặc đấu sai; **P2** là sai lệch trình bày/độ chính xác cần sửa trong đợt hình. Số dòng là tại baseline trước khi chỉnh bài.

| Mức | Vị trí | Vấn đề xác nhận | Hướng sửa khi minh họa |
| --- | --- | --- | --- |
| P0 | `week1/day07.html:125–150` | LED xanh dương với điện trở 10 Ω từ GPIO 3,3 V có thể kéo dòng quá lớn, trái mục tiêu 10 mA của bài. | Tính lại R từ Vf/If và dòng chân cho phép; ghi ví dụ với trị số an toàn, kiểm tra thực tế. |
| P0 | `week2/day09.html:64–75` | Dây song song vẽ nối tắt tụ trong mạch nạp RC. | Vẽ R nối tiếp C, Vout đo trên C; đối chiếu đồ thị nạp/xả. |
| P0 | `week2/day11.html:139–150` | Cầu bốn diode sai nút/chiều nên không thành bộ chỉnh lưu cầu. | Dựng lại bốn diode với hai đầu AC và hai đầu DC tách biệt; vẽ hai đường dẫn mỗi bán kỳ. |
| P0 | `week2/day12.html:65–77` | Zener ổn áp bị vẽ nối tiếp tải thay vì mắc ngược song song từ Vout xuống GND. | Vẽ điện trở nối tiếp đầu vào, Zener và tải song song; kiểm tra dòng/công suất. |
| P0 | `week2/day13.html:95–102,136–145` | Tụ lọc nằm trên đường nguồn như phần tử nối tiếp; sơ đồ AMS1117 ghi nhầm thứ tự chân. | Tụ từ rail đến GND; pin 1 GND/ADJ, pin 2 và tab VOUT, pin 3 VIN theo package đúng mã. |
| P0 | `week2/day14.html:73–87` | Nhánh sau diode về GND tạo ngắn mạch; tụ nguồn vẽ nối tiếp. | Lập lại schematic nguồn theo từng nút, không dùng sơ đồ cũ làm mẫu lắp. |
| P0 | `week3/day15.html:71–87,141–155` | Pin BC547 tự mâu thuẫn trong chú giải; mạch LED switch không xác định rõ tải giữa VCC và collector. | Pinout theo datasheet/nhà sản xuất đúng mã; vẽ LED + R trên nhánh tải, B qua R, E về GND. |
| P0 | `week3/day16.html:73–94,171` và `week3/day18.html:124–139` | Diode flyback được vẽ nối tiếp relay/motor; Bài 16 còn hướng dẫn tháo diode rồi đóng relay nhiều lần. | Đặt diode ngược song song cuộn/tải cảm, bỏ bước thử thiếu bảo vệ. |
| P0 | `week3/day17.html:63–81` | Sơ đồ common emitter nối Vin vào collector, bias R1/R2 không neo nguồn, C_E nối tiếp R_E. | Vẽ lại đầu vào qua tụ vào base, bias hai rail, collector load và bypass song song R_E. |
| P0 | `week3/day21.html:73–84,126–132` | Với hướng NTC hiện vẽ, V_sensor giảm khi nóng nhưng vào IN(+), nên logic output ngược mô tả; relay driver cũng nối collector sai. | Chọn lại vị trí NTC hoặc đổi hai đầu vào so sánh; dựng mạch tải theo nhánh thật. |
| P0 | `week4/day23.html:68–78` | Nét dọc trong sơ đồ I²C có thể chập SDA với SCL. | Vẽ hai bus tách biệt, pull-up riêng và GND chung. |
| P0 | `week4/day24.html:62–77` | Nét dọc trong sơ đồ SPI có thể chập MOSI/MISO/SCK/CS; thiết bị thứ hai thiếu nhánh tín hiệu. | Vẽ từng net tách biệt và CS riêng từng thiết bị. |
| P0 | `week5/day32.html:48–60` | Sơ đồ buck đặt L xuống GND, thiếu nút chuyển mạch và đường hồi dòng qua diode. | Vẽ switch–L–Vout và diode freewheel đúng nút; gắn nhãn hai pha. |
| P0 | `week5/day35.html:69–87` | LM2596: L nối tắt VIN→VOUT, diode sai đường/cực, nhãn pin 1/2 đảo; bài thực hành yêu cầu chép sơ đồ này. | Thay bằng sơ đồ tự vẽ đối chiếu [datasheet TI](https://www.ti.com/lit/ds/symlink/lm2596.pdf): pin 1 VIN, 2 OUTPUT, 3 GND, 4 FB, 5 ON/OFF. |
| P0 | `week6/day38.html:47–60` | A4988 RST nối EN sai chức năng, thiếu tụ bulk VMOT; công thức Vref giả định Rsense chung cho mọi board. | Theo module thực tế: RST/SLP đúng mức, EN active-low, tụ VMOT; tính Vref theo điện trở sense của board. |
| P0 | `week6/day42.html:58,67–80` | Danh sách dùng LiPo một cell nhưng sơ đồ có thêm pin 2S/7,4 V; ECHO HC-SR04 được vẽ thẳng tới GPIO ESP32 3,3 V. | Chốt một sơ đồ nguồn nhất quán; hạ mức ECHO và ghi GND chung. |
| P1 | `week1/day01.html:173–183,258–269` | Hai pin AA đặt cực + ở junction 1,5 V nhưng chú thích 3 V; sơ đồ dòng electron thiếu nhất quán. | Sửa cực pin, điểm GND và hai chiều dòng theo một vòng kín. |
| P1 | `week1/day04.html:71–88`, `week2/day11.html:64–76` | Ký hiệu diode/LED dạng tam giác dễ lẫn với mũi tên chiều dòng. | Dùng ký hiệu diode/LED chuẩn; mũi tên ánh sáng tách khỏi ký hiệu và chú thích. |
| P1 | `week2/day12.html:129–139` | Nói Zener 3,3 V đảm bảo GPIO không vượt 3,3 V là quá chắc vì dung sai/đường đặc tính. | Ghi giới hạn áp dụng và phương án chuyển mức phù hợp. |
| P1 | `week3/day20.html:107–115` | Khuếch đại đảo dùng nguồn đơn 0–5 V, chân (+) ở GND nhưng ví dụ Vin dương cần Vout âm. | Thêm điểm bias giữa nguồn hoặc nguồn hai cực; kiểm tra miền điện áp. |
| P1 | `week4/day26.html:93–105` | Tụ debounce đặt ở phía GND của switch thay vì nút GPIO trong sơ đồ. | Vẽ RC tại đầu vào GPIO, giá trị và pull-up đúng. |
| P1 | `week4/day27.html:136–145` | Dãy chân PIR thiếu hướng nhìn; thứ tự phụ thuộc module. | Dùng ảnh đúng module, nhãn chân nhìn trực tiếp trên board. |
| P1 | `week5/day31.html:57–66,87–100` | Giải thích LPF nhầm điện áp rơi trên tụ; sơ đồ band-pass thiếu R shunt nên HPF không hoạt động. | Sửa lời giảng và hai tầng RC đúng nút. |
| P1 | `week6/day39.html:45–74` | H-bridge không vẽ motor nối vào hai nút giữa; bảng L298N nhầm coast/brake. | Thêm motor đúng vị trí và đối chiếu bảng trạng thái trong datasheet ST. |
| P1 | `week6/day40.html:45–57`, `week6/day41.html:68–83` | Chưa nêu mức ECHO 5 V với ESP32; TP4056 và BMS/điện áp cắt được mô tả như mọi module đều giống nhau. | Ghi biến thể module, hạ mức ECHO và phân biệt mạch sạc với bảo vệ pin. |
| P1 | `week7/day46.html:61–72` | Hướng dẫn thêm TestPoint trực tiếp trên PCB mà thiếu symbol/net trong schematic. | TestPoint symbol → net → footprint → Update PCB. |
| P1 | `week8/day51.html:45–68,102–110` | Nhãn Output lẫn tín hiệu PID u với đại lượng sau plant y; ví dụ lò 100°C dùng BME280 (tối đa 85°C) và GPIO9 ESP32 WROOM dành cho flash. | Vẽ r/e/u/y và feedback âm; chọn cảm biến ≥100°C, GPIO hợp lệ và driver heater. |
| P1 | `week8/day54.html:84–110` | Sơ đồ “ground loop” không cho thấy đoạn return chung gây common-impedance coupling. | Vẽ Z_shared, dòng motor và sụt áp tại ADC; tránh coi star ground là quy tắc chung. |
| P2 | `week1/day02.html:101–122` | Sơ đồ 830 lỗ đánh đến 30; vùng rail/chỗ ngắt khó đọc. | Vẽ topology có nhãn a–e/f–j và đoạn rail theo board thật. |
| P2 | `week3/day19.html:48–60` | Tỷ lệ PWM và khẳng định 50% duty = nửa tốc motor quá tuyệt đối. | Vẽ theo thời gian đúng và ghi tốc độ phụ thuộc tải/motor. |
| P2 | `week7/day43.html:44–49`, `week7/day44.html:84–150`, `week8/day53.html:44–114` | V-model sai chiều/nhãn; ví dụ “non-blocking” còn delay/I/O chặn; hình BLE thêm LED WRITE mà code chỉ có TEMP. | Sửa từng hình để khớp quy trình và mã hiện có. |


## Nguồn kỹ thuật ưu tiên

- [onsemi BC546/BC547 datasheet](https://www.onsemi.com/download/data-sheet/pdf/bc546-d.pdf) cho pinout transistor Bài 15.
- [TI LM358-N datasheet](https://www.ti.com/lit/ds/symlink/lm358-n.pdf) cho giới hạn điện áp vào/ra và nguồn đơn Bài 20–21.
- [Allegro A4988 datasheet](https://www.allegromicro.com/~/media/files/datasheets/a4988-datasheet.pdf) và [tài liệu board Pololu](https://www.pololu.com/product/1182) cho Bài 38.
- [ST L298 datasheet](https://www.st.com/resource/en/datasheet/l298.pdf) cho trạng thái cầu H Bài 39.
- [Bosch BME280 datasheet](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf) và [Espressif GPIO FAQ](https://docs.espressif.com/projects/esp-faq/en/latest/software-framework/peripherals/gpio.html) cho Bài 51.
- [Adafruit HC-SR04 pinout](https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/pinouts) cho mức ECHO Bài 40/42.
- [TI LM2596 datasheet](https://www.ti.com/lit/ds/symlink/lm2596.pdf) cho sơ đồ nguồn Bài 35; phải khớp đúng phiên bản điện áp cố định và giá trị linh kiện theo điều kiện thiết kế.
- [Espressif ESP32 Hardware Design Guidelines](https://documentation.espressif.com/esp-hardware-design-guidelines/en/latest/esp32/index.html) và datasheet board/module cụ thể cho mạch GPIO, UART/I2C và nguồn ESP32.
