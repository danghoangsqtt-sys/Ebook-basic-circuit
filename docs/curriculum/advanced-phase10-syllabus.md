# Đề cương Phase 10 — A29–A32

Ngày 2026-10-04. Cùng một đồ án báo nhiệt Pico non-W/TMP36GT9Z được tăng dần qua bốn bước, mỗi bài có sơ đồ khối, netlist, BOM, phép tính, mô phỏng host, phiếu đo/sai khác và rubric. Bài là nhánh nội dung số; CAD/ERC/DRC, board và người duyệt còn chờ. Đọc [hồ sơ đồ án](../projects/pico-tmp36-design.md) cùng từng bài.

| Bài | Tiên quyết và mục tiêu | Ví dụ/hoạt động | Bài độc lập/rubric | Cổng vật lý |
| --- | --- | --- | --- | --- |
| A29 Từ yêu cầu đến sơ đồ khối | A09/A22/A25/A28; viết dải 20–40 °C, log 1 s, hysteresis 30/28 °C; ánh xạ net/BOM | Tính 0,70/0,90 V ở 20/40 °C; sơ đồ hệ Pico/TMP36 | Viết yêu cầu và ba net/số chân; rubric 8 điểm | Marking board/TO-92, rail và chuẩn đo chưa có |
| A30 Nguồn thấp áp | A07/A08/A29; theo USB→D1→VSYS→SMPS→3V3; tách tải sensor khỏi toàn board | Tính P_U1<0,165 mW ở 3,3 V/50 µA theo ADI | Net nguồn/BOM/phiếu đo; 8 điểm | VBUS/VSYS/3V3/VREF/ripple chưa đo |
| A31 Sensor/MCU | A23/A25/A28/A30; raw ADC, công thức danh định, FSM hysteresis và budget sai số có giả định | 25 °C→0,750 V→14894; trace 8 mẫu | Tính code/trace/sai số còn thiếu; 8 điểm | ADC/chuẩn nhiệt/firmware thật chưa thử |
| A32 Carrier PCB | A29–A31/D34; netlist, placement C1/AGND/TEMP_V và cổng chế tạo | Ba net B1/U1/C1; mẫu báo sai khác chưa đo | Ghi net/footprint/cổng ERC/DRC/reviewer; 8 điểm | Chưa có KiCad PCB/gerber/ERC/DRC/đo hoặc chữ ký |

Nguồn hãng theo từng claim ở [sổ nguồn Phase 10](advanced-phase10-source-ledger.md). Hình là sơ đồ khối tự vẽ có bản chữ, không là chứng nhận mạch in.
