# Sổ đối chiếu nguồn gốc A09–A16

Kiểm ngày 2026-10-03. Tệp này đối chiếu các **ví dụ do dự án tự dựng** trong `advanced-phase8-syllabus.md` với nguồn giáo khoa gốc/ứng dụng kỹ thuật gốc. Các nguồn chứng minh định luật và miền áp dụng, **không** phải biên bản đã mô phỏng, đo mạch hoặc phê duyệt part cụ thể. Giữ sơ đồ, bảng và câu chữ của bài học do dự án tự tạo; không sao chép hình/bài tập của nguồn.

## A09 — Mô hình mạch DC và KCL/KVL

- [OpenStax University Physics Vol. 2, §10.3 “Kirchhoff's Rules”, mục *Kirchhoff's Rules*, *Problem-Solving Strategy*, Fig. 10.24–10.25](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules): xác nhận tổng dòng tại nút bằng 0, tổng biến thiên áp quanh vòng bằng 0, phương trình độc lập và quy ước dấu. [MIT 6.002, Lecture 2 “Basic circuit analysis method”](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/resources/6002_l2/) xác nhận phương pháp phân tích mạch lumped. Nguồn **không** xác nhận một mạch 5 V/1 kΩ đã được lắp hoặc mô phỏng; các số sau là phép tính riêng.
- Ví dụ: `2 kΩ || 2 kΩ = 1 kΩ`; `I=5 V/(1+1) kΩ=2,5 mA`; `VX=2,5 V`; mỗi nhánh `2,5 V/2 kΩ=1,25 mA`. `Pnguồn=5 V·2,5 mA=12,5 mW`; điện trở nối tiếp `I²·1 kΩ=6,25 mW`; mỗi nhánh `VX²/2 kΩ=3,125 mW`; tổng tiêu tán `12,5 mW`. **Đạt** trong mô hình nguồn và dây lý tưởng.
- Bài tập: `1 kΩ || 3 kΩ=750 Ω`; `I=5/1,75 kΩ=20/7 mA≈2,857 mA`; `VX=15/7 V≈2,143 V`; `I1=15/7 mA≈2,143 mA`, `I3=5/7 mA≈0,714 mA`; KCL `15/7+5/7=20/7 mA`. **Đạt**.

## A10 — Phương pháp nút và vòng

- [MIT 6.002, Lecture 2 “Basic circuit analysis method”](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/resources/6002_l2/) và [Lecture 3, trang PDF 2–4, tóm tắt node method/ma trận dẫn nạp](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/5ec9a8524891d6940e4572e1c97b0cf1_6002_l3.pdf); [OpenStax §10.3, *Problem-Solving Strategy*](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules). Hỗ trợ lập KCL/KVL và số phương trình độc lập. Chúng **không** chứng minh kết quả của sơ đồ A10 nếu không xác định đúng cực nguồn và topology; bài học phải vẽ rõ 10 V→2 kΩ→A, A→ground, A→B, B→ground.
- Ví dụ, nhân KCL với `2 kΩ`: tại A `(VA−10)+VA+(VA−VB)=0`, tại B `(VB−VA)+VB=0`; hệ `3VA−VB=10`, `−VA+2VB=0` → `VA=4 V`, `VB=2 V`. Dòng nguồn `(10−4)/2 kΩ=3 mA`; dòng A→B `(4−2)/2 kΩ=1 mA`; dòng A→ground `2 mA`; dòng B→ground `1 mA`. **Đạt**.
- Bài tập đổi A→ground thành `1 kΩ`: `4VA−VB=10`, `−VA+2VB=0` → `VA=20/7 V≈2,857 V`, `VB=10/7 V≈1,429 V`. Dòng nguồn `25/7 mA≈3,571 mA`, nhánh A→ground `20/7 mA`, nhánh A→B `5/7 mA`; cân bằng KCL. **Đạt**. Supernode/supermesh là phần mở rộng phương pháp, không suy ra từ số liệu ví dụ.

## A11 — Chồng chất và nguồn phụ thuộc

- [MIT 6.002 Lecture 3, trang PDF 6–9 “Superposition” và trang 20–21 “Norton”](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/5ec9a8524891d6940e4572e1c97b0cf1_6002_l3.pdf): tính tuyến tính, chồng điện áp/dòng trong mạng tuyến tính. [MIT 6.002 Lecture 9a transcript, trang PDF 2–3, đoạn “dependent sources”](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/9f06a403e4b1ecccb8763350561b7a06_6_0022007L09a.pdf) và [MIT 6.200, *Dependent Sources*, trang PDF 4 và 8](https://circuits.mit.edu/_static/S23/handouts/lec05a/lecture05a.pdf): khi tắt từng **nguồn độc lập**, giữ nguồn phụ thuộc trong mạch. `g·VX` cần được định nghĩa là điện áp **giữa node X và ground**, không xem điện thế của một node không có mốc tham chiếu là biến điều khiển. Nguồn này không cho một giá trị `g` hoặc bảo đảm mọi mạch có nghiệm duy nhất; mạch phụ thuộc phải kiểm riêng topology và điều kiện nghiệm.
- Ví dụ: KCL `(VX−10)/1k+(VX−5)/1k+VX/1k=0` → `VX=5 V`. Với nguồn 5 V triệt thành short, đóng góp 10 V là `10/3 V`; với nguồn 10 V triệt, đóng góp 5 V là `5/3 V`; tổng `5 V`. **Đạt**. Không cộng các công suất riêng vì `P=V²/R` phi tuyến theo V.
- Bài tập nguồn 10 V→6 V: `6/3+5/3=11/3 V≈3,667 V`. **Đạt**. Điều kiện “triệt nguồn áp = short/nguồn dòng = open” chỉ cho **nguồn lý tưởng độc lập** trong phân tích tuyến tính; trở trong của nguồn thật cần giữ theo mô hình.

## A12 — Thévenin và Norton

- [MIT 6.002 Lecture 3, trang PDF 14–21, phương pháp Thévenin/Norton](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/5ec9a8524891d6940e4572e1c97b0cf1_6002_l3.pdf) hỗ trợ nguồn tương đương hai cực và `IN=VTH/RTH`. [MIT 6.200, *Dependent Sources*, trang PDF 4–6](https://circuits.mit.edu/_static/S23/handouts/lec05a/lecture05a.pdf) xác nhận phương pháp nguồn thử cho nguồn phụ thuộc tuyến tính và chỉ ra khi `VTH=IN=0` không thể lấy tỷ số `VTH/IN` để tìm `RTH`. [OpenStax §10.3](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules) hỗ trợ nghiệm đối chiếu qua KCL/KVL. Điều kiện cực đại `RL=RTH` và biểu thức công suất ở đây được suy ra trực tiếp từ `P_L=VTH²·RL/(RTH+RL)²`, với `RTH>0`, tải thuần trở và nguồn DC lý tưởng; không dùng làm bảo đảm công suất liên tục/nhiệt của mạch thật.
- Ví dụ: `VTH=12·4/(2+4)=8 V`; `RTH=2 kΩ||4 kΩ=4/3 kΩ`; `IN=8/(4/3 kΩ)=6 mA`. Với `RL=4 kΩ`, `VL=8·4/(4+4/3)=6 V`; `IL=1,5 mA`. `Pmax=8²/[4·(4/3 kΩ)]=12 mW` tại `RL=4/3 kΩ`. **Đạt**.
- Bài tập `RL=2 kΩ`: `VL=8·2/(2+4/3)=4,8 V`, `IL=4,8/2 kΩ=2,4 mA`. Kiểm mạch gốc: `4 kΩ||2 kΩ=4/3 kΩ`, node chia áp `12·(4/3)/(2+4/3)=4,8 V`. **Đạt**. Với nguồn phụ thuộc, không triệt nguồn phụ thuộc khi tìm điện trở nhìn vào; dùng nguồn thử và `Vtest/Itest` khi cần.

## A13 — Quá độ RC/RL và điều kiện đầu

- [OpenStax §10.5 “RC Circuits”, phương trình 10.8–10.9, Fig. 10.39](https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits): nạp/xả mũ và `τRC=RC`. [OpenStax §14.4 “RL Circuits”, phương trình 14.24–14.27](https://openstax.org/books/university-physics-volume-2/pages/14-4-rl-circuits): dòng RL, `τL=L/R`, mức 63% tại một `τ`. [ADI ADALM2000 “Transient Response of an RL Circuit”, Procedure](https://wiki.analog.com/university/courses/electronics/rl_transient_response) hỗ trợ hoạt động so đáp ứng thực/đồ thị; đây là hoạt động với ADALM2000, không phải biên bản đo của dự án. Ba nguồn không cung cấp ESR/DCR của linh kiện được chọn, nên mọi sai khác thực nghiệm chỉ là giả thuyết đến khi có datasheet/đo.
- Ví dụ: `10 kΩ·100 µF=1 s`; `vC(1s)=5(1−e⁻¹)=3,16060 V≈3,16 V`. `100 mH/10 Ω=0,01 s=10 ms`. **Đạt** với RC/RL bậc một, nguồn bước lý tưởng, ban đầu `vC(0−)=0`, `iL(0−)=0`.
- Bài tập: `2 kΩ·10 µF=20 ms`; `vC(20ms)=3(1−e⁻¹)=1,89636 V≈1,90 V`; `vC(0+)=0` nếu ban đầu xả hết và không có xung lý tưởng vô hạn. **Đạt**.

## A14 — AC, trở kháng và RLC

- [OpenStax §15.2 “Simple AC Circuits”, mục Capacitor/Inductor](https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits): `XC=1/(ωC)`, `XL=ωL`, quan hệ pha và RMS. [OpenStax §15.3 “RLC Series Circuits with AC”, phương trình trở kháng series](https://openstax.org/books/university-physics-volume-2/pages/15-3-rlc-series-circuits-with-ac): `|Z|=√[R²+(ωL−1/ωC)²]`. **Bổ sung bắt buộc khi giải thích băng thông:** [OpenStax §15.5 “Resonance in an AC Circuit”, phương trình 15.17–15.19, Example 15.5](https://openstax.org/books/university-physics-volume-2/pages/15-5-resonance-in-an-ac-circuit) mới có `ω0`, `Q` và `Δω=R/L`; §15.3 một mình không đủ cho băng thông. [ADI ADALM2000 “Resonance in RLC Circuits”, Procedure](https://wiki.analog.com/university/courses/electronics/rlc_resonance) chỉ hỗ trợ cách quét/đọc đáp ứng, không kiểm mạch của dự án.
- Ví dụ: `L=0,01 H`, `C=1×10⁻⁷ F`: `f0=1/(2π√LC)=5032,92 Hz≈5,03 kHz`; tại cộng hưởng `I=1 Vrms/100 Ω=10 mArms`. `Δf=R/(2πL)=1591,55 Hz≈1,59 kHz` là băng thông **toàn phần** giữa hai điểm nửa công suất của mô hình series RLC lý tưởng, không là sai số quanh `f0`. **Đạt**.
- Bài tập `C=400 nF`: `f0=2516,46 Hz≈2,52 kHz`, đúng bằng nửa tần số cũ; `Δf=1591,55 Hz` nếu R,L không đổi trong model. **Đạt**. Điện áp từng L/C có thể lớn hơn nguồn tại cộng hưởng, vì vậy không suy dòng/điện áp linh kiện cho hardware từ mô hình thiếu ESR, DCR, tổn hao, sai số tụ/cảm và mức điện áp cho phép.

## A15 — Điện trường đến điện dung

- [OpenStax §8.1 “Capacitors and Capacitance”, mục Parallel-Plate Capacitor, Fig. 8.5 và phương trình 8.3](https://openstax.org/books/university-physics-volume-2/pages/8-1-capacitors-and-capacitance): `V=Ed`, `C=ε0A/d` trong xấp xỉ bản rộng, chân không/không khí gần đúng. [OpenStax §8.3 “Energy Stored in a Capacitor”, phương trình 8.10](https://openstax.org/books/university-physics-volume-2/pages/8-3-energy-stored-in-a-capacitor): `U=½CV²`. Nguồn không chứng minh chính xác điện dung một tụ công nghiệp nhiều lớp hoặc hiệu ứng rìa của hình học A15; cần model/tài liệu riêng nếu khẳng định phần đó.
- Ví dụ lấy `ε0=8,854187817×10⁻¹² F/m`: `C=ε0·0,01/0,001=88,5419 pF≈88,5 pF`; `E=5/0,001=5000 V/m=5 kV/m`; `U=½·88,5419 pF·(5 V)²=1,10677 nJ≈1,11 nJ`. **Đạt**.
- Bài tập giữ `A,V` và gấp đôi `d`: `C=44,2709 pF≈44,3 pF`; `E=2,5 kV/m`; `U=0,553387 nJ≈0,553 nJ` ở ba chữ số có nghĩa. **Đạt** sau khi đáp án đề cương được sửa từ `≈0,554 nJ` thành `≈0,553 nJ`. Kết luận năng lượng giảm một nửa chỉ đúng ở **V cố định**; khi Q cố định, `U=Q²/(2C)` tăng gấp đôi.

## A16 — Từ trường, cảm ứng và đường hồi dòng

- [OpenStax §13.1 “Faraday's Law”, phương trình 13.1–13.3, Fig. 13.4 và Example 13.1](https://openstax.org/books/university-physics-volume-2/pages/13-1-faradays-law): `Φ=∫B·n dA`, `e=−dΦ/dt`; với một vòng cố định, trường đều vuông góc, `|e|=A|dB/dt|`. [OpenStax §14.2 “Self-Inductance and Inductors”, phương trình 14.10](https://openstax.org/books/university-physics-volume-2/pages/14-2-self-inductance-and-inductors): `e=−L dI/dt` cho tự cảm, **không** cho điện cảm của vòng PCB A16 nếu chưa biết geometry/môi trường.
- [TI SCAA082A Rev. A (Aug. 2017), **High-Speed Layout Guidelines**, §1.6 “Return Current and Loop Areas”, Fig. 6a–6d](https://www.ti.com/lit/pdf/SCAA082A): đường hồi ở DC theo điện trở thấp, ở tần số cao theo trở kháng thấp; **Fig. 6c** là khe ground plane buộc return path đi vòng; **Fig. 6d** là phương án bắc cầu 0 Ω qua khe. Đề cương đã sửa tên nguồn và chú thích hai hình; *Practical PCB Design Rules* là tên §2, không phải tên tài liệu. TI nói diện tích vòng lớn gây thêm rủi ro bức xạ/EMI, nhưng **không** cho hệ số từ trường `0,1 T/s`, trị số emf hoặc cam kết rằng giảm khoảng cách luôn đạt EMC.
- [ADI AN-1368 “Ferrite Bead Demystified”, Fig. 1, mục *DC Bias Current Considerations*](https://www.analog.com/en/resources/app-notes/an-1368.html): ví dụ lọc nguồn mixed-signal và biến thiên trở kháng bead do DC bias/tần số. Đây **không** là nguồn chứng minh phép tính vòng dây hoặc quy tắc return path; chỉ dùng khi bài mở rộng sang lọc nguồn, và không biến ferrite thành giải pháp thay ground plane liên tục.
- Ví dụ: `A1=0,100 m·0,010 m=0,001 m²`, `|e1|=0,001·0,1=0,0001 V=0,1 mV`; `A2=0,100·0,002=0,0002 m²`, `|e2|=0,0002·0,1=0,00002 V=0,02 mV`. **Đạt** cho trường đều cùng hướng, một vòng cố định; không là số đo PCB thật.
- Bài tập: `A=0,050 m·0,004 m=2×10⁻⁴ m²`, `|e|=2×10⁻⁴·0,2=4×10⁻⁵ V=40 µV`. **Đạt**. Để nói dấu emf cần định hướng pháp tuyến và chiều đi quanh vòng theo Lenz; chỉ cho `|dB/dt|` thì chỉ suy được độ lớn, không suy dấu tuyệt đối. Nếu góc 90° giữa `B` và **pháp tuyến diện tích**, từ thông bằng 0; nếu góc 90° với mặt phẳng vòng thì từ thông cực đại.

## Kết quả tích hợp và quy tắc cho bài học

1. A14: đề cương đã thêm OpenStax §15.5 cho băng thông; khi viết bài đặt nguồn này ngay cạnh `Δf=R/(2πL)`.
2. A15: đề cương đã sửa đáp án thành `≈0,553 nJ`. Khi tính tiếp, dùng giá trị chưa làm tròn; `1,11 nJ/2=0,555 nJ` không phải `0,553 nJ` vì làm tròn quá sớm.
3. A16: đề cương đã sửa tên TI thành **High-Speed Layout Guidelines** và phân biệt Fig. 6c/6d; tách AN-1368 sang tiểu mục ferrite/lọc nguồn nếu có.
4. A09–A16: thêm sơ đồ tự vẽ với cực tính, node, đường đi/hồi; nhãn “tính theo mô hình” cho số ví dụ. Chỉ đánh dấu “đã mô phỏng/đo” sau khi lưu netlist, phiên bản phần mềm, điều kiện đo và kết quả thật.
