# Nguồn hình tuyến chuyên sâu

Các SVG trong thư mục này là sơ đồ tự vẽ từ nội dung bài học, giữ net, cực tính và nhãn để người đọc kiểm lại phép tính. Chúng không sao chép hình trong PDF của hãng. Link datasheet bên dưới là nguồn đối chiếu thông số/công nghệ, không xác nhận mạch đã lắp hoặc đo.

| Hình | Xuất xứ và kiểm chứng |
| --- | --- |
| `a01.svg` | Tự vẽ vòng nguồn DC–R, phép tính worst-case từ A01. Đối chiếu giới hạn part với [Vishay Doc. 28952](https://www.vishay.com/docs/28952/mcr0201at-mca1206at.pdf); sơ đồ 12 V/1 kΩ là ví dụ lý tưởng, không phải mạch hãng. |
| `a02.svg` | Tự vẽ cầu chia áp R cố định–NTC và điểm Vout từ A02; tải đồng hồ chỉ được phân tích trong chữ. Đường R/T tra [TDK B57891M](https://www.tdk-electronics.tdk.com/inf/50/db/ntc/NTC_Leaded_disks_M891.pdf); trị tải đo là giả định bài toán. |
| `a03.svg` | Tự vẽ lưu đồ chọn họ tụ theo nhiệm vụ từ A03; so công nghệ với [Murata FAQ](https://www.murata.com/support/faqs/capacitor/ceramiccapacitor/char/0017) và [Nichicon](https://www.nichicon.co.jp/english/products/pdf/aluminum.pdf). Cực tính và giới hạn phải đọc riêng cho part được chọn. |
| `a04.svg` | Tự vẽ mạch nguồn bước–R–C lý tưởng từ A04; đối chiếu DC-bias MLCC với [Murata](https://ds.murata.com/simsurfing_data/pdf/en-us/mlcc/sim_mlcc_measuringcond_e.pdf). ESR/leakage được bàn trong chữ, chưa được vẽ thành phần tử tương đương; phần trăm điện dung hiệu dụng trong hình là giả định, không lấy từ part thật. |
