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
