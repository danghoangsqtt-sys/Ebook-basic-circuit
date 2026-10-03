# Hợp đồng biên soạn A01–A16 — Phase 8

Ngày lập: 2026-10-03. Đây là đặc tả **nội dung cần viết**, không phải xác nhận 16 trang đã xuất bản, đã mô phỏng hay đã đo trên phần cứng. Phạm vi là `advanced/a01.html`–`advanced/a16.html`, theo `.DHSYSTEM/CURRICULUM-PLAN.md` và [`syllabus.md`](syllabus.md); vị trí các bài D được đối chiếu với [`coverage-matrix.csv`](coverage-matrix.csv). Nếu ma trận hoặc phạm vi thay đổi, cập nhật hợp đồng trước khi viết bài liên quan.

## Quy ước chung và cổng nghiệm thu

- **Độc giả:** người mới đã học các bài D ghi ở mỗi mục. M0 = đơn vị, tỉ lệ, đại số một ẩn; M1 = hệ tuyến tính, hàm mũ, lượng giác cơ bản; M2 = giải tích, phương trình vi phân, số phức, **chỉ là nhánh mở rộng**. Không dùng M2 để khóa đáp án bắt buộc của M1.
- **Thời lượng tương đối:** 1 đơn vị (ĐV) = khoảng 45 phút học tập tập trung; phân bổ `đọc và ví dụ / tự làm giấy hoặc mô phỏng / bài tập và phản hồi`. Đây là ước lượng biên tập, không phải thời gian đã đo với học viên.
- **Đầu ra bài:** mục tiêu kiểm được; sơ đồ có net, dấu dòng/áp, cực tính và điều kiện; ví dụ giải từng bước; hoạt động tái lập được với dữ liệu vào, lệnh/thiết lập mô phỏng hoặc bảng tính tay và kết quả kỳ vọng; bài tập khác ví dụ cùng đáp án, bước giải/rubric; nguồn đặt sát claim và ghi trang/bảng/revision cho thông số part. Dữ liệu số trong ví dụ là giả định bài toán nếu không gắn part cụ thể.
- **Rubric chung:** mỗi bài 4 điểm: 1 điểm mô hình/sơ đồ và giả định đúng; 1 điểm công thức, dấu và đơn vị; 1 điểm số tính hoặc bảng/đồ thị đối chiếu; 1 điểm giải thích giới hạn, chọn part và quyết định kỹ thuật. Các dòng “đáp án” bên dưới cho mốc chấm tối thiểu; bài xuất bản phải có lời giải đầy đủ và tiêu chí theo từng bước, không chỉ một số cuối.
- **Nhánh số trước:** hoạt động bắt buộc làm được bằng giấy, bảng tính hoặc simulator với sơ đồ/nguồn chỉnh sửa được và kết quả kỳ vọng. Chưa có part/module/board/revision, BOM, nguồn giới hạn dòng, phép đo và reviewer nên mọi chỉ dẫn lắp/cấp điện là **kế hoạch có điều kiện**; không báo cáo đạt đo thật, ERC hay chạy mô phỏng nếu chưa có tệp bằng chứng. Pin Li-ion, adapter phía lưới, mạch chuyển mạch, tải cảm và phép đo oscilloscope cần duyệt riêng trước hướng dẫn phần cứng.
- **Nối với 56 bài cũ:** D01–D13 và D31/D54 giới thiệu khái niệm. A01–A16 chỉ đạt khi học viên **so sánh công nghệ, định lượng biên giới hạn, giải mạch nhiều ẩn hoặc liên hệ trường–mạch–layout**. Không lặp lại mã màu, định nghĩa Ohm, công thức τ đơn lẻ hay bảng tên linh kiện như toàn bộ bài mới. Không suy định mức package/module từ tên họ linh kiện.

## Ma trận tiên quyết và mức sâu

| Tuyến | Điều kiện vào | Đầu ra kiểm được | Nối bài cũ |
| --- | --- | --- | --- |
| A01 → A02 | D02,D03,D06; M0 | Chọn điện trở theo công suất/sai số, rồi biến đặc tính vật lý thành tín hiệu đo | D03 mã màu/SMD; D06 phép đo |
| A03 → A04 | D08,D09; M0→M1 | Phân loại tụ, rồi tính điện dung hữu hiệu và sai khác đáp ứng | D08 loại tụ; D09 RC; D54 decoupling |
| A05 → A06 → A07 | D04,D10–D13,D32,D41; M0→M1 | Chọn diode/từ/nguồn bằng giới hạn thật và mô hình tổn hao | D11,D12 diode; D10 RL; D13,D41 nguồn/pin |
| A01,A03,A05–A07 → A08 | M1 | Hồ sơ yêu cầu → datasheet → quyết định/BOM có thể kiểm lại | Gom việc chọn rời rạc trong D |
| A09 → A10 → A11,A12 | D05,D06; M1 | Giải DC tổng quát, đối chiếu hai phương pháp và nguồn tương đương | D05,D06 chỉ nhập môn |
| A09 + D09,D10 → A13 → A14 | M1; M2 tùy chọn | Dự báo quá độ và đáp ứng AC/RLC theo điều kiện đầu/pha | D09,D10 τ; D31 lọc |
| A03,A09 → A15; A06,A15,D54 → A16 | M1; M2 tùy chọn | Từ hình học/trường đến C,L và đường hồi dòng | D08,D10,D54 chỉ nêu ý tưởng |

## A01 — Họ điện trở cố định

- **Đạt khi:** nhận biết và so sánh film, wirewound, thick/thin-film SMD và shunt theo dung sai, TCR, công suất, xung và package; loại một ứng viên bằng điều kiện định mức, không bằng tên công nghệ.
- **Vào/thời lượng:** D02,D03; M0; **3 ĐV** (1/1/1).
- **Ví dụ mẫu:** nguồn 12 V đặt liên tục trên 1 kΩ ±5%: tại 950 Ω, `Pmax = 12²/950 = 0,152 W`. Tính công suất tại biên thấp rồi yêu cầu đối chiếu **đường giảm định mức theo nhiệt độ, điện áp làm việc và xung của part cụ thể** trước chọn, không mặc nhiên gọi mọi điện trở 0,25 W là đạt.
- **Hoạt động tái lập:** lập bảng ba công nghệ bằng datasheet nhà sản xuất, ghi nominal/tolerance/TCR/power/temp/package; tính `Rmin,Rmax,Pmax` bằng giấy/bảng tính cho 5, 9, 12 V. Nếu có thiết bị sau này, đo điện trở ở trạng thái **ngắt điện** và lưu nhiệt độ, sai số đồng hồ.
- **Bài tập/đáp án:** 680 Ω ±10% chịu 9 V DC lý tưởng: `Rmin=612 Ω`, `Pmax=81/612=0,132 W`; rubric đòi dùng biên thấp, đơn vị W và chưa duyệt part cho tới khi đọc derating.
- **Nguồn gốc và phạm vi:** [Vishay, *Resistors 101—Product Overview*](https://www.vishay.com/docs/49873/49873_sg2113.pdf), bảng công nghệ điện trở và thông số so sánh; [Vishay, *12 Things to Know About Resistors in Pulse Load Applications*, mục 8](https://www.vishay.com/docs/48516/_ms9702509-2401-vishaychecklistpulseload.pdf) chỉ cho khác biệt khả năng xung, không làm định mức cho part khác. D03 đã dạy mã màu; A01 kiểm **lựa chọn và biên**.

## A02 — Điện trở chức năng và phép đo

- **Đạt khi:** phân biệt biến trở, NTC/PTC, LDR và shunt theo đại lượng–đường đặc tính–tự nung nóng–tải đo; thiết kế bảng hiệu chuẩn tối thiểu hai điểm và dự báo chiều thay đổi điện áp.
- **Vào/thời lượng:** A01,D06,D25 (D25 có thể đọc bổ trợ); M0, M1 tùy chọn cho nội suy; **3 ĐV** (1/1/1).
- **Ví dụ mẫu:** chia áp 3,3 V với điện trở cố định 100 kΩ trên, NTC `B57891M0104J000` 100 kΩ ở 25 °C dưới: `Vout=1,65 V`. Khi nhiệt tăng, NTC giảm R nên `Vout` giảm. Tính lý tưởng chưa gồm sai số R25, self-heating hay ADC.
- **Hoạt động tái lập:** lấy bảng R/T **R/T số 4003** trong datasheet TDK, chép ba mốc 25/35/45 °C, tính `Vout=3,3R_NTC/(100k+R_NTC)` và vẽ đồ thị; lưu mã part và nguồn dữ liệu. Nhánh đo thật chỉ khi chọn mạch/ADC cụ thể, kiểm mức áp và chống tự nung nóng.
- **Bài tập/đáp án:** tại NTC 50 kΩ giả định trong cùng chia áp, `Vout=1,10 V`; nhiệt tăng so với 25 °C vì R giảm. Rubric cần nêu đây là **giả định**, không gán 50 kΩ cho một nhiệt độ của TDK khi chưa đọc bảng.
- **Nguồn gốc và phạm vi:** [TDK/EPCOS B57891M, Jan 2018, tr. 2–3 (ordering/R25/B) và tr. 8 (bảng R/T số 4003)](https://www.tdk-electronics.tdk.com/inf/50/db/ntc/NTC_Leaded_disks_M891.pdf) chứng minh R25, dung sai, B và đường R/T của **dòng B57891M**; không chứng minh chân module bán lẻ hay hiệu chuẩn hệ ADC. D06/D25 có ví dụ đo; A02 thêm **đường đặc tính và ngân sách sai số**.

## A03 — Các họ tụ điện

- **Đạt khi:** nhận biết ceramic Class 1/Class 2, film, nhôm điện phân/polymer, supercap theo cực tính, điện áp, dung sai, nhiệt và nhiệm vụ; chọn họ cho ba tình huống có giải thích, không suy mọi tụ cùng C là thay thế được.
- **Vào/thời lượng:** D08; M0; **3 ĐV** (1/1/1).
- **Ví dụ mẫu:** tụ lý tưởng 100 µF ở 10 V giữ `E=½CV²=0,005 J`; năng lượng bằng nhau không nói được ESR, cực tính, tuổi thọ hay dòng ripple. Bài phải gắn sơ đồ cực tính nếu minh họa điện phân.
- **Hoạt động tái lập:** bảng chọn ba chức năng (định thời, bulk nguồn, ghép AC) từ các catalog hãng, chép C danh định, điện áp, nhiệt, cực tính và thuộc tính cần xem tiếp; với hai mức 5/10 V tính năng lượng mô hình lý tưởng.
- **Bài tập/đáp án:** 47 µF tại 6 V có `E=0,846 mJ` lý tưởng; rubric cần đổi µF và ghi công thức, đồng thời từ chối kết luận “an toàn xả” chỉ từ năng lượng danh định.
- **Nguồn gốc và phạm vi:** [Murata FAQ về Class 1 C0G và Class 2 X5R/X7R](https://www.murata.com/support/faqs/capacitor/ceramiccapacitor/char/0017) cho đặc tính và ứng dụng MLCC; [Nichicon, *General Descriptions of Aluminum Electrolytic Capacitors*](https://www.nichicon.co.jp/english/series_items/catalog_pdf/e-aluminum.pdf) cho cấu trúc, cực tính, điện rò/ESR. D08 đã liệt kê loại; A03 buộc **chọn theo ứng dụng**.

## A04 — Tụ trong mạch thực

- **Đạt khi:** tính điện dung hữu hiệu và sai lệch τ dưới DC bias; giải thích ESR, leakage, ripple và giảm định mức bằng đồ thị của **part được chọn**; phân biệt số liệu typical với giới hạn guaranteed.
- **Vào/thời lượng:** A03,D09; M1; **3 ĐV** (1/1/1).
- **Ví dụ mẫu:** mô hình 10 µF danh định, giả định còn 60% dưới bias: `Ceff=6 µF`; với 10 kΩ, `τ` đổi từ 100 ms sang 60 ms. **60% là dữ liệu bài toán**, không là đặc tính của mọi X5R.
- **Hoạt động tái lập:** dùng đường C–V của một mã MLCC từ công cụ/datasheet hãng, ghi điện áp và nhiệt độ; lập bảng `Ceff(V)` rồi vẽ hai đường nạp RC trong simulator hoặc bảng tính `v=V(1−e^(−t/RC))`; lưu dữ liệu nguồn và model.
- **Bài tập/đáp án:** 4,7 µF còn 70% với 2 kΩ: `Ceff=3,29 µF`, `τ=6,58 ms`; rubric yêu cầu gắn tỷ lệ 70% là giả định và kiểm đường cong mã part trước thiết kế.
- **Nguồn gốc và phạm vi:** [Murata FAQ, mục DC-bias của MLCC](https://www.murata.com/en-us/support/faqs/capacitor/ceramiccapacitor/char/0005); [Murata *MLCC measuring conditions*, Fig. 3](https://ds.murata.com/simsurfing_data/pdf/en-us/mlcc/sim_mlcc_measuringcond_e.pdf) là **đồ thị minh họa**, không dùng làm Ceff cho mọi part; [Nichicon mô tả ESR/leakage](https://www.nichicon.co.jp/english/series_items/catalog_pdf/e-aluminum.pdf). D09 đã có τ lý tưởng; A04 thêm điều kiện thực.

## A05 — Các họ diode

- **Đạt khi:** lập ma trận chỉnh lưu/switching/Schottky/Zener/TVS/LED/photodiode theo vai trò, `VR`, `IF`, `VF`, công suất, phục hồi hoặc xung khi có; tránh dùng LED hay Zener như diode chỉnh lưu chung.
- **Vào/thời lượng:** D04,D11,D12; M0–M1; **3 ĐV** (1/1/1).
- **Ví dụ mẫu:** LED mô hình `VF=2 V`, nguồn 5 V, R=330 Ω cho `I=(5−2)/330=9,09 mA`, `PR≈27,3 mW`. `VF=2 V` chỉ là **giả định bài toán**; chọn LED/R thật phải xét dải VF, dòng, nhiệt và cực tính từ datasheet.
- **Hoạt động tái lập:** vẽ cùng hai cực thử với diode lý tưởng và diode switching 1N4148 bằng model được ghi tên; quét DC hoặc bảng `IF–VF`, so tính gần đúng với đường typical ở 25 °C; ghi rõ model không đại diện mọi diode.
- **Bài tập/đáp án:** nguồn 3,3 V, LED VF giả định 2,1 V, R=220 Ω: `I≈5,45 mA`, `PR≈6,55 mW`; rubric yêu cầu kiểm dòng LED và công suất R theo **giới hạn datasheet**, không kết luận đủ từ VF giả định.
- **Nguồn gốc và phạm vi:** [Vishay 1N4148, Doc. 81857 Rev. 1.6 (07-Nov-2024), bảng maximum ratings/electrical characteristics và Fig. 1–3](https://www.vishay.com/docs/81857/1n4148.pdf) cho **1N4148 switching**, không làm bằng chứng cho LED/Zener/TVS hoặc module. D11,D12 đã giới thiệu diode; A05 kiểm **đọc đặc tính và đối chiếu loại**.

## A06 — Cuộn cảm, biến áp và ferrite bead

- **Đạt khi:** đọc L, DCR, `Isat`, dòng nhiệt và đường L–I của cuộn cảm; phân biệt chức năng trữ năng lượng của inductor, ghép từ của transformer, suy hao cao tần của ferrite bead; giải thích cần đường thoát dòng khi ngắt tải cảm.
- **Vào/thời lượng:** D10,D32; M1; **3 ĐV** (1/1/1).
- **Ví dụ mẫu:** L lý tưởng 10 mH ở 0,1 A lưu `E=½LI²=50 µJ`. Khi ngắt dòng, `v=L·di/dt`; không gán một đỉnh áp thật nếu chưa biết điện dung ký sinh, đường clamp và tốc độ chuyển mạch.
- **Hoạt động tái lập:** tạo bảng datasheet cho một inductor Würth và một ferrite bead, chép DCR, dòng rated và điều kiện đo; mô phỏng RL 10 mH/100 Ω với bước 5 V (`τ=0,1 ms`) và hai trường hợp clamp lý tưởng/không clamp, ghi giới hạn model.
- **Bài tập/đáp án:** L=2 mH, I=0,2 A giữ `E=40 µJ`; với R=20 Ω, `τ=L/R=0,1 ms`. Rubric đòi không đồng nhất `Isat` với dòng nhiệt và không khuyên ngắt cuộn dây thật khi chưa có clamp.
- **Nguồn gốc và phạm vi:** [Würth 7687714471 datasheet, rev. 2019-05-06, tr. 1 bảng electrical properties và tr. 2 đường L–I typical](https://www.we-online.com/components/products/datasheet/7687714471.pdf) chỉ cho **part đó** và phân biệt `IR` theo tăng nhiệt với `ISAT` theo giảm L; [ADI AN-1368, Fig. 2, 7–9](https://www.analog.com/en/resources/app-notes/an-1368.html) cho tính phụ thuộc tần số/DC bias của ferrite bead và giới hạn mô hình. D10 có RL nhập môn; A06 tách **ba loại phần tử từ**.

## A07 — Adapter, bộ ổn áp và pin

- **Đạt khi:** vẽ ranh giới nguồn ngoài thấp áp cách ly → ổn áp → tải; tính ngân sách điện áp, dòng, công suất và nhiệt; phân biệt nhãn adapter, đặc tính regulator, thông số cell và mạch bảo vệ/charger.
- **Vào/thời lượng:** D13,D41; M1; **3 ĐV** (1/1/1).
- **Ví dụ mẫu:** mô hình linear 9→5 V, tải 0,2 A: `Pd≈(9−5)×0,2=0,8 W` **chưa cộng dòng tĩnh**. Tính `ΔT≈Pd·θJA` chỉ khi có package/PCB và θJA tương ứng; không suy “0,8 W là dùng được” từ công suất đầu ra.
- **Hoạt động tái lập:** lập bảng kịch bản 7,5/9/12 V, tải 0,1/0,2 A, tính tổn hao mô hình; đối chiếu dải input/output, dropout, giới hạn nhiệt của một mã regulator. Nhánh battery chỉ lập ngân sách dung lượng/dòng trên giấy; không hướng dẫn sạc hoặc đấu cell khi chưa chốt cell/charger/protection.
- **Bài tập/đáp án:** 12→5 V tại 0,1 A cho `Pd≈0,7 W`, hiệu suất lý tưởng theo tỉ số áp `≈41,7%` nếu bỏ qua dòng tĩnh; rubric yêu cầu ghi giả định và kiểm headroom/nhiệt với part thực.
- **Nguồn gốc và phạm vi:** [TI LM7800 product/datasheet](https://www.ti.com/product/LM7800) cho họ LM7800, yêu cầu đọc đúng **biến thể, package và revision** trước ghi giới hạn; [OpenStax University Physics Vol. 2 §10.1](https://openstax.org/books/university-physics-volume-2/pages/10-1-electromotive-force) cho suất điện động và điện trở trong cell. D13,D41 đã nhắc regulator/LiPo; A07 xây **budget và ranh giới an toàn**, không xác nhận mạch pin cũ.

## A08 — Chọn linh kiện bằng datasheet

- **Đạt khi:** biến yêu cầu thành bảng giới hạn có đơn vị/điều kiện, trích đúng part/package/revision/bảng/đường cong, đánh dấu guaranteed/typical, quyết định chọn/loại và BOM còn điều kiện mở.
- **Vào/thời lượng:** A01,A03,A05,A06,A07; M1; **3 ĐV** (1/1/1).
- **Ví dụ mẫu:** bài toán giả định cần chặn áp ngược 30 V: ứng viên diode có `VR(max)=20 V` bị loại ngay, dù `IF` đủ; ứng viên 40 V chỉ **qua một cổng**, vẫn phải kiểm dòng, công suất/nhiệt, xung, package và điều kiện môi trường. Các số 20/40 V là ứng viên giả định, không gán cho mã part.
- **Hoạt động tái lập:** tạo hồ sơ hai ứng viên cho từng chức năng R/C/diode/L/regulator bằng các nguồn của A01–A07: cột claim, URL, revision, trang/bảng, điều kiện, kết luận, khoảng chưa biết. Kết quả là bảng nguồn–quyết định có thể kiểm độc lập.
- **Bài tập/đáp án:** nguồn max 12 V, tụ ứng viên 10 V và 16 V: **loại 10 V**, 16 V mới qua điều kiện áp danh định và còn phải kiểm Ceff, ripple, nhiệt/derating; rubric chấm cổng loại theo worst-case và không tuyên bố part 16 V đã đạt toàn mạch.
- **Nguồn gốc và phạm vi:** [Vishay 1N4148 Rev. 1.6, bảng maximum ratings so với electrical characteristics](https://www.vishay.com/docs/81857/1n4148.pdf); [Murata FAQ DC-bias](https://www.murata.com/en-us/support/faqs/capacitor/ceramiccapacitor/char/0005); [Würth 7687714471 datasheet](https://www.we-online.com/components/products/datasheet/7687714471.pdf). Nguồn dùng để dạy **cách trích giới hạn**, không xem ba part trên là BOM mặc định. D03/D08/D11/D13 có ví dụ chọn rời; A08 yêu cầu hồ sơ chứng minh.

## A09 — Mô hình mạch DC và KCL/KVL

- **Đạt khi:** đặt node chuẩn, mũi tên dòng và cực tính nhất quán; giải mạch nhiều nhánh, kiểm KCL, KVL và bảo toàn công suất; nêu giả định nguồn/lõi dây lý tưởng.
- **Vào/thời lượng:** D05,D06; M1; **3 ĐV** (1/1/1).
- **Ví dụ mẫu:** 5 V qua 1 kΩ đến node X; từ X có hai nhánh 2 kΩ xuống ground. `Rparallel=1 kΩ`, `VX=2,5 V`, `Isrc=2,5 mA`, mỗi nhánh `1,25 mA`; công suất nguồn `12,5 mW`, các R lần lượt `6,25+3,125+3,125=12,5 mW`.
- **Hoạt động tái lập:** vẽ netlist/ASCII không mơ hồ và bảng node/dòng/công suất; giải tay rồi chạy DC operating point trong simulator **nếu có**, lưu netlist, version và bảng so; nếu không có, đối chiếu bằng hai phương pháp KCL và tương đương nối tiếp/song song.
- **Bài tập/đáp án:** thay hai nhánh bằng 1 kΩ và 3 kΩ: `Rparallel=750 Ω`, `VX≈2,143 V`, dòng nguồn `≈2,857 mA`, dòng hai nhánh `≈2,143 mA` và `≈0,714 mA`; rubric buộc tổng dòng nhánh bằng dòng nguồn trong sai số làm tròn.
- **Nguồn gốc và phạm vi:** [OpenStax University Physics Vol. 2 §10.3, Kirchhoff's Rules](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules), định luật nút/vòng và quy ước dấu; [MIT 6.002 Lecture 2](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/lecture-notes/), quy trình phân tích lumped circuit. D06 giới thiệu luật; A09 kiểm **giải và kiểm năng lượng**.

## A10 — Phương pháp nút và vòng

- **Đạt khi:** viết đủ hệ phương trình độc lập cho mạch có hai ẩn, giải nút và vòng/loop cùng một mạch, đối chiếu dòng/áp; nhận diện trường hợp cần supernode/supermesh và ghi cách mở rộng.
- **Vào/thời lượng:** A09; M1; **4 ĐV** (1/2/1).
- **Ví dụ mẫu:** 10 V→2 kΩ→A; A→ground 2 kΩ; A→B 2 kΩ; B→ground 2 kΩ. KCL rút gọn `3VA−VB=10`, `−VA+2VB=0`, nên `VA=4 V`, `VB=2 V`; kiểm dòng qua A–B bằng `1 mA` và tổng nguồn `3 mA`.
- **Hoạt động tái lập:** từ sơ đồ/netlist cố định, lập cả ma trận dẫn nạp nút và hai vòng độc lập trên giấy; chạy phép giải tuyến tính trong bảng tính hoặc simulator, đối chiếu node A/B và dòng từng nhánh. Mở rộng một nguồn áp giữa hai node để học viên **chỉ khoanh supernode**, chưa cần bài số phức.
- **Bài tập/đáp án:** đổi điện trở A–ground từ 2 kΩ thành 1 kΩ, còn lại giữ: `4VA−VB=10`, `−VA+2VB=0`, nên `VA=20/7≈2,857 V`, `VB=10/7≈1,429 V`; rubric yêu cầu hệ và dòng kiểm KCL, không chỉ nghiệm máy.
- **Nguồn gốc và phạm vi:** [MIT 6.002 Lecture 2, *Basic circuit analysis method*](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/lecture-notes/) và [OpenStax §10.3](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules) cho cách lập các phương trình độc lập. Đây là độ sâu chưa có trong D05/D06.

## A11 — Chồng chất và nguồn phụ thuộc

- **Đạt khi:** cộng **điện áp/dòng**, không cộng công suất, của mạch tuyến tính; triệt nguồn áp độc lập thành short, nguồn dòng độc lập thành open khi thích hợp; **giữ nguồn phụ thuộc** khi xét từng nguồn độc lập; nêu không áp dụng trực tiếp cho diode phi tuyến.
- **Vào/thời lượng:** A10; M1; **3 ĐV** (1/1/1).
- **Ví dụ mẫu:** node X nối tới 10 V qua 1 kΩ, tới 5 V qua 1 kΩ, xuống ground qua 1 kΩ: `VX=5 V`. Xét 10 V riêng được `10/3 V`, xét 5 V riêng được `5/3 V`; tổng 5 V. Nguồn phụ thuộc được giới thiệu bằng một biến điều khiển riêng, không triệt nó.
- **Hoạt động tái lập:** lập ba bản netlist (đủ nguồn, chỉ nguồn 1, chỉ nguồn 2), lưu bảng `VX` và dòng tải; vẽ thêm sơ đồ có nguồn dòng `g·VX`, yêu cầu chỉ ra nguồn nào phải giữ khi phân tích, rồi thử với các giá trị g không gây nghiệm suy biến.
- **Bài tập/đáp án:** cùng mạch nhưng nguồn 10 V đổi 6 V: đóng góp `6/3=2 V` và `5/3≈1,667 V`, tổng `11/3≈3,667 V`; rubric cần phép triệt nguồn đúng và giải thích công suất tải phải tính từ kết quả tổng.
- **Nguồn gốc và phạm vi:** [MIT 6.002 Lecture 3, *Superposition, Thévenin and Norton*](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/resources/6002_l3/) cho tuyến chồng chất; [MIT 6.002 Lecture 9a transcript, đoạn dependent sources](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/9f06a403e4b1ecccb8763350561b7a06_6_0022007L09a.pdf) nói giữ nguồn phụ thuộc khi tắt nguồn độc lập. Không có đề mục độc lập tương ứng trong D theo ma trận.

## A12 — Thévenin và Norton

- **Đạt khi:** xác định đúng hai cực nhìn từ tải, tìm `Vth`, `Rth`, `In`, kiểm trên ít nhất hai tải; với nguồn phụ thuộc dùng nguồn thử khi cần, không tự động triệt nó; tính công suất tải và điều kiện cực đại trong mô hình tuyến tính.
- **Vào/thời lượng:** A09,A10; M1; **4 ĐV** (1/2/1).
- **Ví dụ mẫu:** nguồn 12 V, R trên 2 kΩ và R dưới 4 kΩ, lấy cực node chia áp–ground: `Vth=8 V`, `Rth=2k||4k=1,333 kΩ`, `In=6 mA`. Tải 4 kΩ nhận `VL=6 V`; tại `RL=Rth`, `Pmax=Vth²/(4Rth)=12 mW` theo mô hình lý tưởng.
- **Hoạt động tái lập:** giải mạch gốc và tương đương với tải 1/4/8 kΩ bằng bảng tính hay simulator DC, so VL và IL theo sai số làm tròn; dùng test source 1 V ở đầu ra của một sơ đồ có nguồn phụ thuộc để minh họa quy tắc `Rin=Vtest/Itest`.
- **Bài tập/đáp án:** cùng nguồn chia áp, tải 2 kΩ: `VL=8×2/(2+4/3)=4,8 V`, `IL=2,4 mA`; rubric yêu cầu chỉ ra tải mắc **sau** khi tính điện áp hở mạch và kiểm lại trực tiếp trên sơ đồ gốc.
- **Nguồn gốc và phạm vi:** [MIT 6.002 Lecture 3](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/resources/6002_l3/) cho nguồn tương đương; [OpenStax §10.3](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules) cho phép giải đối chiếu bằng KCL/KVL. D không có bài riêng cho định lý này theo ma trận.

## A13 — Quá độ RC/RL và điều kiện đầu

- **Đạt khi:** xác định đại lượng liên tục ngay trước/sau chuyển mạch (`vC`, `iL`), giá trị cuối, `τ` và 10/63/90% ở mô hình bậc một; giải thích sai khác do ESR/DCR hoặc nguồn/tải khi mở rộng; M2 chỉ là nhánh dẫn xuất.
- **Vào/thời lượng:** A09,D09,D10; M1, M2 tùy chọn; **4 ĐV** (1/2/1).
- **Ví dụ mẫu:** nạp RC lý tưởng từ 0 bằng bước 5 V, R=10 kΩ, C=100 µF: `τ=1 s`, `vC(1s)=5(1−e⁻¹)≈3,16 V`. So thêm RL 100 mH/10 Ω có `τL=10 ms`; hai τ xuất phát từ đại lượng trạng thái khác nhau.
- **Hoạt động tái lập:** lập bảng tại `t=0, τ, 2τ, 5τ` bằng công thức; mô phỏng transient với bước thời gian ≤τ/20 nếu có simulator, lưu netlist và đồ thị, nêu điều kiện đầu và ideal switch. Nhánh đo thật chỉ sau khi chọn part, nguồn thấp áp, giới hạn dòng và cách đo phù hợp.
- **Bài tập/đáp án:** RC 3 V, 2 kΩ, 10 µF: `τ=20 ms`, `vC(20ms)≈1,90 V`, `vC(0⁺)=0` nếu ban đầu xả hết; rubric yêu cầu nêu điều kiện đầu thay vì áp công thức máy móc.
- **Nguồn gốc và phạm vi:** [OpenStax §10.5 RC Circuits](https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits) cho phương trình nạp/xả; [OpenStax §14.4 RL Circuits](https://openstax.org/books/university-physics-volume-2/pages/14-4-rl-circuits) cho RL; [ADI ADALM2000 RL transient activity](https://wiki.analog.com/university/courses/electronics/rl_transient_response) cho cách so đồ thị/thời hằng. D09,D10 có τ; A13 buộc **điều kiện đầu, hai hệ và đối chiếu**.

## A14 — AC, trở kháng và RLC

- **Đạt khi:** dùng đồ thị biên độ/pha và `XL=2πfL`, `XC=1/(2πfC)` để nhận cộng hưởng; dự báo tần số cộng hưởng, dòng và băng thông series RLC lý tưởng; nhánh M2 dùng phasor và `Z=R+j(ωL−1/ωC)`.
- **Vào/thời lượng:** A13,D31; M1 cho kết quả bắt buộc, M2 tùy chọn; **4 ĐV** (1/2/1).
- **Ví dụ mẫu:** series R=100 Ω, L=10 mH, C=100 nF, nguồn 1 Vrms: `f0=1/(2π√LC)≈5,03 kHz`, tại cộng hưởng `I≈10 mArms` trong mô hình lý tưởng; băng thông `R/(2πL)≈1,59 kHz`. Ghi rõ điện áp trên L/C có thể vượt nguồn và model không chứa ESR/ký sinh.
- **Hoạt động tái lập:** quét 0,1–20 kHz trong simulator AC hoặc bảng tính `|Z|=√(R²+(XL−XC)²)` và `I=Vrms/|Z|`; lưu model, biên độ/pha, chỉ ra đỉnh dòng và hai tần số −3 dB nếu model hỗ trợ.
- **Bài tập/đáp án:** giữ R,L nhưng đổi C=400 nF: `f0≈2,52 kHz` (một nửa), băng thông lý tưởng vẫn `≈1,59 kHz`; rubric yêu cầu đơn vị Hz, giải thích `f0∝1/√C` và không áp nhận xét này cho part thật khi ký sinh chi phối.
- **Nguồn gốc và phạm vi:** [OpenStax §15.2 Simple AC Circuits](https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits), `XL/XC` và pha; [OpenStax §15.3 RLC Series Circuits with AC](https://openstax.org/books/university-physics-volume-2/pages/15-3-rlc-series-circuits-with-ac), trở kháng series; [OpenStax §15.5 Resonance in an AC Circuit](https://openstax.org/books/university-physics-volume-2/pages/15-5-resonance-in-an-ac-circuit), độ rộng băng thông và hệ số Q; [ADI ADALM2000 RLC resonance activity](https://wiki.analog.com/university/courses/electronics/rlc_resonance), phép quét đáp ứng. D31 dạy lọc; A14 nối **pha–cộng hưởng–giới hạn model**.

## A15 — Điện trường đến điện dung

- **Đạt khi:** vẽ hướng trường/điện thế của hai bản cực, tính `E≈V/d`, `C≈εA/d`, năng lượng; chỉ ra giả định tấm rộng, trường đều, fringing nhỏ và điện môi tuyến tính; nối biến hình học với sai khác tụ thực.
- **Vào/thời lượng:** A03,A09; M1, M2 tùy chọn cho tích phân/điều kiện biên; **3 ĐV** (1/1/1).
- **Ví dụ mẫu:** hai bản trong không khí, diện tích mỗi bản `A=0,01 m²`, cách `d=1 mm`, ở 5 V: `C≈ε0A/d≈88,5 pF`, `E≈5 kV/m`, `U≈1,11 nJ`. Đây là bản cực lý tưởng, không dự báo chính xác tụ công nghiệp.
- **Hoạt động tái lập:** bảng tính hai cột `d=0,5/1/2 mm` giữ A,V, vẽ `C(d),E(d)` và mô tả vì sao khi d giảm thì cả hai tăng; nếu dùng FEM, lưu geometry, vật liệu, mesh, boundary conditions và so kết quả với xấp xỉ phẳng.
- **Bài tập/đáp án:** giữ A,V, tăng d gấp đôi: `C≈44,3 pF`, `E≈2,5 kV/m`, `U≈0,553 nJ`; rubric cần giải thích điều kiện **V không đổi**, phân biệt với trường hợp điện tích không đổi.
- **Nguồn gốc và phạm vi:** [OpenStax University Physics Vol. 2 §8.1 Capacitors and Capacitance](https://openstax.org/books/university-physics-volume-2/pages/8-1-capacitors-and-capacitance), mô hình bản cực và điện môi; [§8.3 Energy Stored in a Capacitor](https://openstax.org/books/university-physics-volume-2/pages/8-3-energy-stored-in-a-capacitor), năng lượng. D08 chỉ nêu trường trong tụ; A15 kiểm **định lượng hình học và miền áp dụng**.

## A16 — Từ trường, cảm ứng và đường hồi dòng

- **Đạt khi:** vẽ một vòng dòng đi–về kín, xác định thông lượng từ qua diện tích vòng và dấu/độ lớn emf cảm ứng trong mô hình trường đều; so sánh hai đường hồi dòng, liên hệ với L, nhiễu và layout mà không biến quy tắc gần đường hồi thành bảo đảm EMC tổng quát.
- **Vào/thời lượng:** A06,A15,D54; M1, M2 tùy chọn cho tích phân thông lượng; **4 ĐV** (1/2/1).
- **Ví dụ mẫu:** vòng chữ nhật dài 100 mm, dây đi–về cách 10 mm có `A≈0,001 m²`; nếu `|dB/dt|=0,1 T/s` vuông góc, `|emf|≈0,1 mV`. Thu khoảng cách còn 2 mm cho `A≈0,0002 m²`, `|emf|≈0,02 mV` theo **mô hình trường đều cùng hướng**, không là số đo PCB thật.
- **Hoạt động tái lập:** trên sơ đồ nguồn thấp áp–tải, tô đường đi và hồi dòng, xác định diện tích vòng cho hai layout giả định; lập bảng emf tại ba `dB/dt` và một trường hợp góc 90° để thấy thông lượng bằng 0. Nếu dùng trường solver, lưu kích thước, đường dòng, hướng trường, biên và so với phép tính; đo thật cần part/PCB/đầu dò và reviewer.
- **Bài tập/đáp án:** vòng dài 50 mm, khoảng cách 4 mm, `|dB/dt|=0,2 T/s` vuông góc: `A=2×10⁻⁴ m²`, `|emf|=40 µV`; rubric buộc đổi mm→m, hướng thông lượng và nêu đây là xấp xỉ một vòng.
- **Nguồn gốc và phạm vi:** [OpenStax §13.1 Faraday's Law](https://openstax.org/books/university-physics-volume-2/pages/13-1-faradays-law), thông lượng/emf; [§14.2 Self-Inductance and Inductors](https://openstax.org/books/university-physics-volume-2/pages/14-2-self-inductance-and-inductors), dòng biến thiên và tự cảm; [TI *High-Speed Layout Guidelines*, SCAA082A Rev. A, §1.6, Fig. 6c–6d](https://www.ti.com/lit/pdf/SCAA082A), Fig. 6c cho đường hồi đi vòng quanh khe plane và Fig. 6d cho cầu 0 Ω ở khe để rút ngắn đường hồi; [ADI AN-1368, Fig. 1 và phần DC-bias/resonance](https://www.analog.com/en/resources/app-notes/an-1368.html), ví dụ lọc nguồn và giới hạn ferrite. D54 đã nói return path; A16 chứng minh bằng **mô hình trường → vòng mạch → quyết định layout**.

## Cổng triển khai P8-02–P8-06

1. Trước viết từng bài, chốt nguồn **mã part và revision hiện hành** cho mọi thông số định mức; các nguồn giáo khoa chứng minh định luật/mô hình chứ không chứng minh một module. Claim có điều kiện cần ghi nhiệt, bias, dòng, tần số, package và phương pháp đo. Không chép nguyên hình/bảng có bản quyền; tự vẽ từ dữ liệu được trích dẫn.
2. Mỗi trang A01–A16 phải có ít nhất một sơ đồ nguồn chỉnh sửa được và SVG/alt rõ net/cực tính; ví dụ mẫu và bài tập ở đây là **hợp đồng tối thiểu**. Nếu bài dùng số khác, vẫn cần độ sâu tương đương, lời giải và rubric có thể tái kiểm. Hoạt động số phải có tệp dữ liệu/netlist hoặc bảng tính lưu được; chưa chạy thì ghi “kỳ vọng”, không ghi “đã kiểm”.
3. Kiểm sau P8-02/P8-03/P8-04/P8-05 bằng audit nội dung, nguồn, phép tính, sơ đồ, mobile; debug lỗi được xác nhận. P8-06 chỉ đạt phạm vi số khi 16/16 bài, điều hướng/search/link/ảnh, bài tập/lời giải và claim qua rubric; trạng thái phần cứng thật còn theo [`curriculum-hardware-pending.md`](../qa/curriculum-hardware-pending.md), không được suy từ mô phỏng.
