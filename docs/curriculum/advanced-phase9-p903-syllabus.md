# Đề cương Phase 9 — cảm biến A25–A28 (P9-03)

Khóa phạm vi ngày 2026-10-04. Mỗi bài 1 ĐV ≈25 phút. Các part là **IC trần** theo nguồn hãng, chưa phải breakout/BOM. Các họ LDR, reed, PIR, IR phản xạ và siêu âm chỉ là đối chứng công nghệ khi chưa có mã part nên không nhận trị số dải, sai số hoặc timing.

| Bài | Mục tiêu và tiên quyết | Ví dụ/hoạt động | Bài độc lập/rubric | Nguồn/giới hạn |
| --- | --- | --- | --- | --- |
| A25 Bản đồ cảm biến | A08,D27,D40; lập bảy hàng đại lượng–nguyên lý–nguồn/I/O–dải–sai số/độ phân giải–đáp ứng | TMP36, DS18B20, OPT3001, DRV5032, BMP280, LSM6DSOX, VL53L1X; đối chiếu marking/package/module | Chọn nhiệt và từ, ghi mỗi trường và điểm chưa biết; 4 điểm | Datasheet hãng trong sổ nguồn; một số trường là phụ thuộc mode/package nên không suy số chung |
| A26 Nhiệt, ánh sáng, từ | A25; so TMP36 analog/DS18B20 1-Wire và OPT3001/LDR, DRV5032/reed theo nhu cầu | TMP36 760 mV ⇒ 26 °C danh định; phân biệt LSB DS18B20 với ±0,5 °C và conversion 750 ms max | Tính nhiệt, chọn lux số, giải thích Hall switch; 4 điểm | ADI/TI, chưa nối sensor thật; LDR/reed chưa chọn part |
| A27 Áp suất, chuyển động, khoảng cách | A25; chọn BMP280, LSM6DSOX, VL53L1X theo đại lượng và điều kiện, so PIR/IR/siêu âm ở mức công nghệ | Bảng phân biệt BMP280 0,0016 hPa output resolution ở mode ultra-high-resolution với ±1 hPa accuracy typical có điều kiện; IMU range/ODR, ToF reflectance/timing/I/O 1,8 V | Tình huống mục tiêu 3 m tối và khí áp; 4 điểm | Bosch/ST; không cam kết độ chính xác ngoài điều kiện hoặc nối I²C 3,3 V vào chip trần ToF |
| A28 Sai số/hiệu chuẩn/lọc | A25–A27,D25; fit hai điểm, kiểm trên điểm độc lập, lập ngân sách và giữ raw data | **Dữ liệu tổng hợp:** (0 °C,0,510 V), (50 °C,1,005 V) fit; (25 °C,0,762 V) kiểm. Fit 9,9 mV/°C, offset 0,510 V; lỗi trước +1,2 °C, sau +0,4545 °C tại đúng điểm kiểm | Tính fit, sai số, ±2 mV giả định ⇒ ±0,2 °C theo slope danh định; lọc trung bình; 5 điểm | TMP36 danh định từ ADI; không có phép đo/chuẩn thật, không xác nhận accuracy trên phần cứng |

Cổng P9-03: bốn trang/hình nguồn/bản chữ/rubric, ma trận và search/nav; kiểm tính toán độc lập, audit các claim datasheet theo điều kiện và phân biệt silicon/breakout. Cổng phần cứng chờ mã đặt hàng/package, module/schematic, chuẩn đo và log từ thiết bị thật.
