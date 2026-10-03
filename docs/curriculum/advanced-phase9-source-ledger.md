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
