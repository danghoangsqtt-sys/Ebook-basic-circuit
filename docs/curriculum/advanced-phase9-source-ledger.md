# Sổ nguồn Phase 9 — logic số A17–A21

Kiểm ngày 2026-10-04. Nguồn ở đây là tài liệu hãng/trường xuất bản trực tiếp. Hình bài học là tự vẽ, không sao chép sơ đồ datasheet. Khi dùng linh kiện thật phải chọn mã đặt hàng, package và điều kiện nhiệt/nguồn/tải của chính thiết kế.

| Nguồn chính | Vị trí, claim được phép | Không được suy |
| --- | --- | --- |
| [TI SNx4HC00 Rev. H](https://www.ti.com/lit/ds/symlink/sn74hc00.pdf) | §6.3: SN74HC00 VCC 2–6 V; tại 4,5 V, VIL,max=1,35 V và VIH,min=3,15 V. §6.5 ở −40…85 °C: VOH,min=4,4 V tại IOH=−20 µA; VOL,max=0,1 V tại IOL=20 µA; VOH,min=3,84 V tại IOH=−4 mA. §1/§8: bốn NAND hai đầu vào. | 2,0 V là 0/1 bảo đảm; 1,25 V noise margin ở mọi tải/họ logic; kết quả DC là đo nhiễu thực hay bảo đảm timing. |
| [TI SNx4HC151 Rev. F](https://www.ti.com/lit/ds/symlink/sn74hc151.pdf) | §7.1: chọn dữ liệu 8:1 bằng ba address, strobe G thấp cho phép; G cao ép Y thấp/W cao. Dùng như ví dụ IC mux có thật. | Hình mux 2:1 trong A19 là pinout của IC 8:1 hoặc một wiring có thể lắp trực tiếp. |
| [TI SNx4HC74 Rev. F](https://www.ti.com/lit/ds/symlink/sn74hc74.pdf) | §1/§8: DFF hai kênh kích cạnh lên, preset/clear bất đồng bộ. §6.7 có các giới hạn setup/hold/pulse theo VCC/nhiệt. | Giá trị thời gian giả định ở A21 là thông số bảo đảm của SN74HC74. Không bỏ qua preset/clear khi lập mạch thực. |
| [TI SN74HC161 Rev. D](https://www.ti.com/lit/ds/symlink/sn74hc161.pdf) | §1/§8: bộ đếm nhị phân đồng bộ 4 bit với điều kiện enable/load/clear. | Chuỗi mod-4 giản lược ở A20 là sơ đồ chân hoặc trạng thái mặc định của HC161. |
| [MIT 6.004 2017, §5.1 annotated slides](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c5/c5s1/) | Phân biệt latch/register, setup/hold và kỷ luật đồng bộ một clock. | Chỉ thỏa setup là đã bảo đảm hold hoặc tính toàn vẹn clock. |
| [MIT 6.004 2017, §6.1 annotated slides](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c6/c6s1/) | Máy trạng thái hữu hạn, đầu vào bất đồng bộ có thể vi phạm setup/hold và metastability. | Hai tầng đồng bộ luôn loại bỏ hoàn toàn metastability hoặc có thời gian giải quyết bị chặn cứng. |

Ví dụ tính trong giáo trình dùng giả định riêng; datasheet xác nhận loại linh kiện và thông số nêu đích danh, không chứng nhận mô phỏng/hardware chưa thực hiện.

## P9-02 — CPU/board/ngoại vi A22–A24

| Nguồn chính | Vị trí, claim được phép | Không được suy |
| --- | --- | --- |
| [Raspberry Pi Pico board datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf) | §1 mô tả Pico board dựa RP2040 và Fig. 1 ghi board Rev3; 2 MB flash trên board, 26 GPIO đa chức năng 3,3 V được đưa ra chân. | Một board thực của học viên là Rev3 chỉ vì hình reference là Rev3; Pico W có cùng LED/GPIO path. |
| [Raspberry Pi RP2040 datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf) | §2.6.2 có 264 kB SRAM on-chip chia sáu bank; bản chip mô tả dual Cortex-M0+, bus fabric, QSPI/XIP và ngoại vi. | 2 MB flash của board là SRAM trong chip, hoặc mọi board RP2040 đều có 2 MB flash. |
| [Raspberry Pi Pico board documentation](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) và [C SDK blink guide](https://www.raspberrypi.com/documentation/microcontrollers/c_sdk.html) | Pico non-W có LED GP25; Pico W có LED trên wireless chip WL_GPIO0; Pico đời đầu có 2 MB flash, 264 kB SRAM RP2040, 26 GPIO board. | `Pin(25)` là LED board trên Pico W hoặc ESP32-C6; board header nào cũng có GP25. |
| [MicroPython RP2 quick reference](https://docs.micropython.org/en/latest/rp2/quickref.html) và [`machine.Pin`](https://docs.micropython.org/en/latest/library/machine.Pin.html) | `Pin(id, Pin.OUT)`, `value(1/0)`, `time.sleep_ms`; dùng làm ngữ nghĩa code lab. | Host fake Pin phản ánh mức/độ chính xác thời gian của chip thật; đọc lại Pin.OUT luôn cho điện áp thực. |
| [Espressif ESP32-C6-DevKitC-1 v1.2 user guide](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32c6/esp32-c6-devkitc-1/user_guide.html) | Board dựa WROOM-1(U) 8 MB flash, có Wi-Fi 6/BLE/802.15.4, RGB LED điều khiển từ GPIO8; header và hardware revision details. Schematic v1.2/v1.3/v1.4 phụ thuộc PW batch. | GPIO8 là LED đơn được lái như GP25; sơ đồ v1.2 áp cho mọi batch v1.2; nêu ADC accuracy cho batch chưa biết. |
| [Espressif ESP32-C6 Series datasheet v1.5](https://documentation.espressif.com/esp32-c6_datasheet_en.html) | Features/§4: HP CPU 32-bit RISC-V tối đa 160 MHz, LP CPU tối đa 20 MHz; đây là đặc tính silicon của ESP32-C6 trong module DevKitC. | Tần số thực của một firmware luôn bằng max, hay số GPIO trong chip bằng số chân đưa ra header board. |

Tham chiếu vendor đang được dùng để so kiến trúc và so điều kiện board, không chứng nhận lab đã chạy trên thiết bị. `labs/pico_gpio_blink.py` chỉ là mã tự viết theo API MicroPython và nhánh host test kiểm thứ tự lệnh.

## P9-03 — cảm biến A25–A28

| Nguồn chính | Claim có điều kiện | Không được suy |
| --- | --- | --- |
| [ADI TMP35/36/37 Rev. H](https://www.analog.com/media/en/technical-documentation/data-sheets/tmp35_36_37.pdf) | TMP36 2,7–5,5 V, −40…125 °C, 750 mV ở 25 °C, 10 mV/°C danh định; ±1 °C ở 25 °C và ±2 °C toàn dải là **typical** trong giới thiệu. Grade F/G có max khác trong bảng; đáp ứng nhiệt phụ thuộc package/môi trường. | 0,5–1 ms turn-on là đáp ứng nhiệt; slope/accuracy typical thành bảo đảm cho mẫu thật. Pin TO-92 hình nhìn từ đáy không là góc nhìn mặt trước. |
| [ADI DS18B20 Rev. 6](https://www.analog.com/media/en/technical-documentation/data-sheets/ds18b20.pdf) | VDD 3–5,5 V khi cấp riêng, −55…125 °C; ±0,5 °C trong −10…85 °C; 12-bit LSB 0,0625 °C, conversion tối đa 750 ms. Cần Convert T/CRC; +85 °C sau bật nguồn có thể là khởi đầu. | LSB là accuracy; 750 ms là đáp ứng nhiệt hoặc chu kỳ update bảo đảm của toàn hệ; parasite power chạy không cần strong pull-up. |
| [TI OPT3001 Rev. C](https://www.ti.com/lit/ds/symlink/opt3001.pdf) | VDD 1,6–3,6 V; I²C; 83.865,6 lux full-scale max, LSB 0,01 lux ở range thấp nhất; tích phân 100/800 ms và auto-range có thể kéo dài. | 0,01 lux là accuracy trong mọi range/phổ/góc/cover glass; tích phân là độ trễ toàn hệ cố định. |
| [TI DRV5032 Rev. H](https://www.ti.com/lit/ds/symlink/drv5032.pdf) | VCC 1,65–5,5 V; Hall switch, BOP/BRP/driver/5–80 Hz tùy suffix. | Một ngưỡng/driver/tốc độ dùng cho mọi hậu tố; output là số đo B liên tục. |
| [Bosch BMP280 DS001 Rev. 1.26](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf) | Table 2/Table 13: 300–1100 hPa, VDD 1,71–3,6 V, VDDIO 1,2–3,6 V, I²C/SPI; output resolution 0,0016 hPa ở ultra-high-resolution; absolute accuracy **typical** ±1 hPa ở 950–1050 hPa, 0…40 °C; thời đo **typical** 5,5 ms ở ultra-low-power preset. | 0,0016 hPa là accuracy; ±1 hPa hoặc 5,5 ms áp cho mọi áp suất/mode/nhiệt. |
| [ST LSM6DSOX datasheet Table 2](https://www.st.com/resource/en/datasheet/lsm6dsox.pdf) | IMU 3-axis accel/3-axis gyro; ±2/4/8/16 g, ±125/250/500/1000/2000 dps; analog supply 1,71–3,6 V, I²C/SPI/I3C theo mode. Sensitivity **typical** 0,061 mg/LSB tại ±2 g; ODR có cấu hình 104 Hz. | Sensitivity là accuracy vị trí; ODR 104 Hz là latency hệ bảo đảm; chọn dải mà không xét bias, noise, ODR, hướng lắp. |
| [ST VL53L1X Rev. 8](https://www.st.com/resource/en/datasheet/vl53l1x.pdf) | ToF, AVDD 2,6–3,5 V; I²C I/O mặc định 1,8 V, mode 2,8 V cần cấu hình; cận gần bảo đảm 4 cm, tầm xa phụ thuộc reflectance/ambient/FoV/timing budget/cover glass. | Mặc định chịu I²C 3,3 V, mọi mục tiêu đạt 4 m/±20 mm/100 ms; breakout không rõ schematic tự có level shifter. |

Số liệu A28 ở 0/25/50 °C và 0,510/0,762/1,005 V là **dữ liệu tổng hợp của bài học**. Datasheet ADI chỉ hỗ trợ mô hình danh định TMP36, không phải chứng thư phép đo hay chuẩn hiệu chuẩn. Họ LDR/reed/PIR/IR/siêu âm được so về cơ chế, chưa chọn mã part và không nhận thông số số học.
