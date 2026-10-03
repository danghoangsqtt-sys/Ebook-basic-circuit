# Cổng xác minh phần cứng còn chờ — giáo trình điện tử

Ngày lập: 2026-10-03. Giáo trình hiện dùng nhánh phân tích/mô phỏng khi chưa có board, module và dụng cụ cụ thể. Các hình và phép tính giúp học nguyên lý; chúng không chứng nhận mạch lắp thật. Chưa chạy ERC cho sơ đồ điện đầy đủ, chưa chạy mô phỏng mạch có kết quả lưu, chưa biên dịch sketch trên target đã chốt và chưa đo phần cứng. Không đánh dấu bất kỳ mục nào dưới đây là đã thử.

| Bài / ID | Dữ liệu cần chốt trước khi lắp hoặc cấp điện | Bằng chứng nghiệm thu phần cứng cần lưu |
| --- | --- | --- |
| D12, D13-1/2, D14-1 | Mã/package Zener, LM7805, AMS1117; tụ ổn định, nguồn/tải, tản nhiệt và diode bảo vệ của nguồn hai rail | Datasheet đúng part và revision; tính công suất/dung sai/nhiệt; schematic ERC; phép đo không tải/có tải và nhiệt ở điều kiện ghi rõ; không thử đảo cực trước khi duyệt |
| D16-1, D19-1, D21-1/2 | Mã cuộn relay, transistor/MOSFET, motor/quạt, nguồn và GPIO; hysteresis comparator | Dòng cuộn/stall, khả năng cấp dòng GPIO, diode hồi dòng, tổn hao, hai ngưỡng chuyển và phép đo trên đúng mạch; reviewer kỹ thuật ký |
| D18-1/2 | Mã MOSFET và mức gate thực của board | R_DS(on) được bảo đảm ở V_GS dùng thật, nhiệt và dòng tải; không dùng V_GS(th) làm bằng chứng đóng hoàn toàn |
| D22-3, D24-1, D27-2 | Module GPS/SIM, SD, PIR đúng PCB/revision và rail I/O | Pinout module, nguồn/mức logic, dung sai mạch chuyển mức và phép đo trên module cụ thể |
| D23-1/2 | Board Uno/host, OLED và BME280/SHT31 đúng breakout/revision | Rail I²C, pull-up từng board, mức VDDIO, địa chỉ và điện dung bus; dùng host 3,3 V hoặc chuyển mức hai chiều đã xác minh |
| D28-1 | Board ESP32, DHT22, OLED, SD, buzzer, nguồn 3,3 V và rail/mạch chuyển mức đúng module | Ngân sách dòng đỉnh, dropout và nhiệt nguồn, lỗi đọc cảm biến/SD, cấu hình target và log test với dữ liệu tham chiếu; code mẫu chưa biên dịch trên board thật |
| D30-1 | Model adapter, oscilloscope và probe | Xác nhận điểm GND DUT được phép nối PE của scope, băng thông/AC coupling/tải; phép đo ripple có log thay vì ngưỡng chung |
| D32-1, D35-1 | Mã IC/module buck, diode, cuộn cảm, tụ, PCB và nguồn/tải | BOM/footprint/net, ERC/DRC, giới hạn dòng, đo đầu ra trước khi nối tải, hiệu suất/ripple/nhiệt và reviewer nguồn |
| D38-1, D39-1, D42-1 | Carrier A4988/L298N/TB6612FNG, motor, servo, pin/boost, ESP32 và cảm biến đúng revision | Pinout, điện trở sense và giới hạn dòng, dòng kẹt trục, bảo vệ và nhiệt, mức GPIO/ECHO, ngân sách dòng đỉnh, thử lỗi/reset |
| D41-1, D42-1 | Cell lithium, mạch sạc, bảo vệ xả và power-path đúng PCB/revision | Datasheet cell, dòng sạc R_PROG, bảo vệ ngắn mạch/quá xả, phương án cấp tải khi sạc, thử nghiệm dưới giám sát và reviewer pin |
| Bài 34, 46, 47, 49 | PCB/đồ án, nguồn, tải và test plan cụ thể | Ngưỡng dòng lấy từ thiết kế đã kiểm; kiểm thông mạch theo net, test cấp nguồn, log chạy bền, demo thật và phần sai khác so với mô phỏng |
| Bài 36, D40-1 | Module DS3231, loại pin dự phòng, HC-SR04/VL53L0X đúng revision | Kiểm PCB RTC có đường sạc trước khi dùng CR2032 sơ cấp; kiểm nguồn/mức ECHO và đặc tính đo khoảng cách theo môi trường/target |

Chủ sở hữu bước tiếp theo: người triển khai với thiết bị thực và người duyệt kỹ thuật có chuyên môn. Trước khi có các bằng chứng này, bài học chỉ đạt phạm vi số; checklist được diễn đạt theo phân tích/mô phỏng hoặc điều kiện cần kiểm, không được dùng làm xác nhận đã lắp hay an toàn điện.
