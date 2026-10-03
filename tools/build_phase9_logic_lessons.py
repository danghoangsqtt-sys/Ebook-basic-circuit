"""Deterministically author the five P9-01 logic lessons and their original SVGs.

The mathematical exercises and source boundaries live in this file; run it after
editing them, then rebuild the search index. No remote assets are downloaded.
"""

from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TI00 = "https://www.ti.com/lit/ds/symlink/sn74hc00.pdf"
TI151 = "https://www.ti.com/lit/ds/symlink/sn74hc151.pdf"
TI74 = "https://www.ti.com/lit/ds/symlink/sn74hc74.pdf"
TI161 = "https://www.ti.com/lit/ds/symlink/sn74hc161.pdf"
MIT5 = "https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c5/c5s1/"
MIT6 = "https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c6/c6s1/"


LESSONS = [
    {
        "id": "a17", "title": "Nhị Phân & Mức Logic", "subtitle": "Bit là ký hiệu; điện áp ở chân IC cần ngưỡng của chính part và điều kiện cấp nguồn.",
        "base": "D01, D06", "units": "4", "figure_alt": "Bốn trọng số nhị phân 8, 4, 2, 1 cho số 1101 bằng 13; bên phải là ba vùng điện áp đầu vào của SN74HC00 tại VCC 4,5 V: không quá 1,35 V, vùng chưa bảo đảm, và từ 3,15 V.",
        "figure_text": "Bên trái là mã số trừu tượng. Bên phải chỉ là ngưỡng <em>đầu vào</em> của TI SN74HC00 khi VCC=4,5 V, không phải dạng sóng hay mức ra đo được.",
        "source": f'<a href="{TI00}" target="_blank" rel="noopener">TI SNx4HC00 Rev. H, §6.3 Recommended Operating Conditions</a>',
        "transcript": "Bốn ô từ trái sang phải có trọng số 8, 4, 2, 1; hàng bit 1, 1, 0, 1 cho tổng 13. Thang bên phải tách 0 đến 1,35 V là vùng nhận thấp được bảo đảm, trên 1,35 đến dưới 3,15 V là vùng không được bảo đảm 0/1, từ 3,15 đến 4,5 V là vùng nhận cao được bảo đảm, với VCC=4,5 V và các điều kiện vận hành của datasheet.",
        "objectives": ["Đổi số nguyên không dấu giữa hệ 10 và hệ 2 bằng trọng số lũy thừa 2.", "Phân biệt bit/giá trị Boolean với điện áp đầu vào chân IC.", "Dùng VIL,max/VIH,min đúng VCC và VOH,min/VOL,max ở đúng tải để phân loại mức và tính biên nhiễu."],
        "body": f'''
<h2>1. Bit không tự có điện áp</h2>
<p>Một bit nhận 0 hoặc 1 trong phép tính. Chuỗi <code>1101₂</code> có bốn vị trí theo thứ tự <code>2³, 2², 2¹, 2⁰</code>: <code>1×8+1×4+0×2+1×1=13₁₀</code>. Muốn đổi 13 từ hệ 10, chọn 8 còn 5, chọn 4 còn 1, bỏ 2, chọn 1. Bit cao bên trái là MSB; số bit phải được nêu trước khi bàn tràn hay số âm. Ví dụ này là số <strong>không dấu</strong>.</p>
<h2>2. Từ bit sang đầu vào NAND thật</h2>
<p><a href="{TI00}" target="_blank" rel="noopener">TI SNx4HC00 Rev. H, §6.3</a> quy định SN74HC00 làm việc với <code>VCC=2–6 V</code>. Riêng <code>VCC=4,5 V</code>, <code>VIL,max=1,35 V</code> và <code>VIH,min=3,15 V</code>. Do đó <code>1,0 V</code> ở chân vào thuộc mức thấp được bảo đảm; <code>3,3 V</code> thuộc mức cao được bảo đảm; <code>2,0 V</code> ở khoảng giữa, <strong>không được datasheet bảo đảm sẽ đọc 0 hay 1</strong>. Không gọi vùng này là một mức logic thứ ba của cổng NAND.</p>
<p>Ngưỡng đầu vào không phải điện áp đầu ra, và một giá trị <code>3,3 V</code> chỉ được phân loại theo giả định nó thực sự xuất hiện tại chân vào IC đang cấp 4,5 V. Khi nối hai IC thật, còn phải kiểm <code>VOH,min/VOL,max</code> của bên phát ở đúng tải, ngưỡng bên nhận, nguồn chung và điều kiện nhiệt. Không suy từ bài này rằng GPIO 3,3 V của một board bất kỳ đã tương thích.</p>
<p><strong>Ví dụ biên nhiễu cùng họ HC:</strong> cho một ngõ ra SN74HC00 lái một đầu vào SN74HC00, cả hai ở <code>VCC=4,5 V</code>, nhiệt độ <code>−40…85 °C</code>. Ở điều kiện tải datasheet <code>IOH=−20 µA</code>, <code>IOL=20 µA</code>, <a href="{TI00}" target="_blank" rel="noopener">TI §6.5</a> bảo đảm <code>VOH,min=4,4 V</code> và <code>VOL,max=0,1 V</code>. Ghép với ngưỡng §6.3: <code>NMH=VOH,min−VIH,min=4,4−3,15=1,25 V</code>; <code>NML=VIL,max−VOL,max=1,35−0,1=1,25 V</code>. Đây là <em>biên DC theo các điều kiện đã nêu</em>, không là lượng nhiễu thực đo, không bao gồm xung nhanh/crosstalk, và sẽ phải tính lại với tải/part khác.</p>
<h2>3. Hoạt động bảng tính</h2>
<div class="callout callout-practice"><div class="callout-header">🔬 Giấy/bảng tính</div><p>Lập cột trọng số <code>8,4,2,1</code> và điền <code>1101</code>; tính tổng. Với VCC=4,5 V của SN74HC00, đặt ba cột <code>Vin=1,0; 2,0; 3,3 V</code>, so từng giá trị với <code>1,35</code> và <code>3,15 V</code>, ghi thấp / chưa bảo đảm / cao. Ghi tên part và mục datasheet cạnh bảng; không cần cấp nguồn hay chạm mạch.</p></div>
<div class="table-wrap"><table><caption>Kết quả theo TI SN74HC00 tại VCC=4,5 V</caption><thead><tr><th>Vin</th><th>Kết luận đầu vào</th><th>Lý do</th></tr></thead><tbody><tr><td>1,0 V</td><td>Thấp được bảo đảm</td><td>≤1,35 V</td></tr><tr><td>2,0 V</td><td>Chưa bảo đảm</td><td>&gt;1,35 V và &lt;3,15 V</td></tr><tr><td>3,3 V</td><td>Cao được bảo đảm</td><td>≥3,15 V</td></tr></tbody></table></div>
<div class="callout callout-warning"><div class="callout-header">⚠️ Giới hạn mạch thật</div><p>Không đưa điện áp vào chân vượt giới hạn vận hành của part. Bài này không có BOM, sơ đồ nối nguồn/decoupling, đặc tính ngõ ra, phép đo hay chứng nhận tương thích hai họ logic.</p></div>''',
        "exercise": "Đổi <code>22₁₀</code> sang nhị phân không dấu rồi tính ngược. Tại đầu vào SN74HC00 cấp <code>4,5 V</code>, phân loại <code>1,2 V</code>, <code>2,0 V</code> và <code>3,2 V</code>. Vì sao không thể gọi 2,0 V là 0 chắc chắn? Nếu tải ra ở điều kiện <code>IOH=−4 mA</code>, datasheet §6.5 cho <code>VOH,min=3,84 V</code> ở −40…85 °C, tính lại NMH khi lái cùng họ ở VCC=4,5 V.",
        "answer": "<ol><li>1 điểm: <code>22=16+4+2</code>, nên <code>10110₂</code> (5 bit).</li><li>1 điểm: tính ngược <code>1×16+0×8+1×4+1×2+0×1=22</code>.</li><li>1 điểm: 1,2 V thấp, 2,0 V chưa bảo đảm, 3,2 V cao theo ngưỡng 1,35/3,15 V của SN74HC00 ở VCC=4,5 V.</li><li>1 điểm: 2,0 V nằm giữa VIL,max và VIH,min; bảng chân trị lý tưởng không gán điện áp này thành 0.</li><li>1 điểm: tại IOH=−4 mA, <code>NMH=3,84−3,15=0,69 V</code> theo VOH,min tại điều kiện tải/nhiệt đã nêu; không dùng biên 1,25 V của tải nhẹ.</li></ol>",
        "checks": ["Tôi đổi đúng trọng số và ghi số bit/không dấu", "Tôi nêu part và VCC khi dùng ngưỡng điện áp", "Tôi giữ vùng chưa bảo đảm thay vì đoán 0/1"],
    },
    {
        "id": "a18", "title": "Boolean & Cổng Logic", "subtitle": "Bảng chân trị là hợp đồng chức năng; NAND thật còn có điều kiện điện và thời gian.",
        "base": "A17", "units": "4", "figure_alt": "Hai đầu vào A và B đi vào cổng NAND, đầu ra Y bằng NOT của A AND B. Bảng bốn hàng 00, 01, 10, 11 cho Y lần lượt 1, 1, 1, 0.",
        "figure_text": "Một NAND hai đầu vào ở cấp Boolean; bóng tròn ở ngõ ra là phép phủ định, không diễn tả ngưỡng điện hoặc delay.",
        "source": f'<a href="{TI00}" target="_blank" rel="noopener">TI SNx4HC00 Rev. H, §1 và sơ đồ logic §8</a>',
        "transcript": "A và B đi vào phép AND rồi đảo để ra Y. Với A B bằng 00, 01, 10, 11, phép AND lần lượt 0,0,0,1, nên NAND Y là 1,1,1,0. Hình chỉ chức năng của một cổng, chưa chỉ số chân và nguồn.",
        "objectives": ["Lập đủ 2²=4 hàng cho hai biến Boolean A,B.", "Tính AND, OR, NOT và NAND theo từng hàng, không nhầm NAND với NOR.", "Kiểm định luật De Morgan bằng bảng chân trị thay vì chỉ thuộc công thức."],
        "body": f'''
<h2>1. Phép logic và bốn hàng bắt buộc</h2>
<p>Với hai bit A,B có <code>2²=4</code> đầu vào. <code>A·B</code> chỉ là 1 khi cả hai là 1; <code>A+B</code> là OR, không phải cộng số nguyên, nên <code>1+1=1</code> trong đại số Boolean. <code>¬A</code> đảo từng bit. NAND là <code>Y=¬(A·B)</code>; <a href="{TI00}" target="_blank" rel="noopener">SN74HC00 của TI</a> chứa bốn NAND hai đầu vào, nhưng bảng dưới chỉ áp cho trạng thái đầu vào hợp lệ sau khi tín hiệu ổn định.</p>
<div class="table-wrap"><table><caption>Bảng chân trị đủ bốn tổ hợp</caption><thead><tr><th>A</th><th>B</th><th>A·B</th><th>A+B</th><th>¬A</th><th>¬(A·B)</th></tr></thead><tbody><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td></tr></tbody></table></div>
<h2>2. De Morgan và hình cổng</h2>
<p>De Morgan cho <code>¬(A·B)=¬A+¬B</code>. Kiểm theo bốn hàng: vế phải là 1 nếu ít nhất một đầu vào bằng 0, nên cùng chuỗi <code>1,1,1,0</code> với NAND. Dấu tròn ở ngõ ra hình A18-1 biểu diễn đảo <em>kết quả AND</em>, không phải chỉ đảo A. Công thức đối ngẫu <code>¬(A+B)=¬A·¬B</code> sẽ được kiểm ở bài tập.</p>
<h2>3. Hoạt động tái lập</h2>
<div class="callout callout-practice"><div class="callout-header">🔬 Giấy/bảng tính</div><p>Tạo hai cột A,B đúng thứ tự 00,01,10,11. Tính từng cột AND, OR, NOT A, NAND; thêm hai cột <code>¬A</code>, <code>¬B</code> rồi OR chúng. So sánh cột NAND và <code>¬A+¬B</code> từng hàng. Nếu dùng bảng tính, lưu công thức 0/1 và ảnh chụp bảng, không gọi đó là đo IC.</p></div>
<div class="callout callout-warning"><div class="callout-header">⚠️ Giới hạn của bảng Boolean</div><p>Bảng chân trị không chứa thời gian truyền, xung glitch, dòng ngõ ra hay mức điện áp. Mạch SN74HC00 thật cần VCC/decoupling, đầu vào hợp lệ và tải trong giới hạn datasheet; sơ đồ biểu tượng chưa là netlist lắp thử.</p></div>''',
        "exercise": "Chứng minh <code>F=¬(A+B)</code> bằng <code>G=¬A·¬B</code> với cả bốn hàng. F là loại cổng nào? Nếu A=B=1, tại sao không dùng phép cộng số nguyên 1+1=2?",
        "answer": "<ol><li>1 điểm: liệt kê đủ 00,01,10,11.</li><li>1 điểm: F lần lượt <code>1,0,0,0</code>.</li><li>1 điểm: G cũng <code>1,0,0,0</code>, nên F=G; F là NOR.</li><li>1 điểm: dấu + là OR Boolean; 1 OR 1 = 1, sau đảo thành 0, không có giá trị 2.</li></ol>",
        "checks": ["Tôi có đủ bốn hàng không lặp/thiếu", "Tôi phân biệt AND, OR, NAND, NOR", "Tôi không dùng bảng Boolean để suy điện áp hoặc delay"],
    },
    {
        "id": "a19", "title": "Mạch Tổ Hợp & Bộ Chọn Kênh", "subtitle": "Một mux 2:1 chọn A hoặc B theo S; đầu ra chỉ phụ thuộc bộ đầu vào đang xét.",
        "base": "A18", "units": "4", "figure_alt": "Mux hai ngõ dữ liệu A, B và ngõ chọn S. Nhánh A qua AND với NOT S, nhánh B qua AND với S, hai nhánh qua OR cho Y bằng NOT S AND A OR S AND B.",
        "figure_text": "Sơ đồ hai nhánh AND và một OR cho mux 2:1 trừu tượng; không phải wiring/pinout của IC 8:1 SN74HC151.",
        "source": f'<a href="{TI151}" target="_blank" rel="noopener">TI SNx4HC151 Rev. F, §1 và §8 (mux 8:1 có thật)</a>',
        "transcript": "A đi qua cổng AND thứ nhất với NOT S; B đi qua AND thứ hai với S; hai kết quả OR để thành Y. Khi S=0 thì nhánh B bị khóa và Y=A. Khi S=1 thì nhánh A bị khóa và Y=B. Không có phần tử nhớ trong hình.",
        "objectives": ["Diễn dịch và dựng Y=¬S·A+S·B từ hai AND, một OR, một NOT.", "Lập đủ 2³=8 hàng bảng chân trị và so từng hàng với quy tắc chọn.", "Phân biệt biểu thức tổ hợp với latch/flip-flop có trạng thái."],
        "body": f'''
<h2>1. Ghép cổng thành mux 2:1</h2>
<p>Đầu vào dữ liệu A,B và chọn S tạo <code>Y=(¬S·A)+(S·B)</code>. Nếu <code>S=0</code>, <code>¬S=1</code> nên <code>Y=A</code>; nếu <code>S=1</code> thì <code>Y=B</code>. Đây là hàm tổ hợp: với bộ S,A,B đang giữ ổn định, không cần biết giá trị Y ở chu kỳ trước. Xét đủ <code>2³=8</code> bộ đầu vào, không chỉ hai trường hợp S.</p>
<div class="table-wrap"><table><caption>Bảng chân trị mux 2:1, thứ tự S A B</caption><thead><tr><th>S</th><th>A</th><th>B</th><th>¬S·A</th><th>S·B</th><th>Y</th></tr></thead><tbody><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td></tr></tbody></table></div>
<h2>2. Đọc datasheet IC mux thật</h2>
<p><a href="{TI151}" target="_blank" rel="noopener">TI SN74HC151 Rev. F, §7.1</a> là bộ chọn 8:1, có ba địa chỉ chọn; strobe <code>G</code> phải ở mức <strong>thấp</strong> để cho phép chọn dữ liệu. Khi G cao, đầu ra chuẩn Y bị ép thấp còn W đảo bị ép cao, bất kể địa chỉ. Hình A19-1 là <strong>mô hình 2:1 tự dựng</strong>, không sao chép sơ đồ chân hoặc nói rằng A/B/S nối trực tiếp vào một con SN74HC151 là chạy được. Nếu chọn IC này cho lab, phải chốt package, pinout, G, mức nguồn, đầu ra Y/W và điều kiện timing theo bản datasheet tương ứng.</p>
<h2>3. Hoạt động bảng tính</h2>
<div class="callout callout-practice"><div class="callout-header">🔬 Giấy/bảng tính</div><p>Sinh tám hàng S,A,B từ 000 đến 111; tính <code>¬S·A</code>, <code>S·B</code> rồi OR. Thêm cột kỳ vọng <code>IF(S=0,A,B)</code>; hai cột phải khớp tám hàng. Đổi thứ tự cột để xem vì sao thiếu hàng dễ che lỗi. Chưa có waveform hoặc mô phỏng độ trễ.</p></div>
<div class="callout callout-warning"><div class="callout-header">⚠️ Giới hạn thời gian</div><p>Khi S/A/B đổi gần nhau, các cổng có delay khác nhau và Y có thể có xung ngắn. Bảng trạng thái ổn định không chứng minh mạch không glitch hoặc điện áp ngõ ra hợp lệ cho tải; cần model/time test của thiết kế cụ thể.</p></div>''',
        "exercise": "Thiết kế <code>F=¬S·A+S·¬B</code> bằng một mux chọn A khi S=0 và chọn <code>¬B</code> khi S=1. Lập đủ tám hàng S,A,B và ghi F. F có cần trạng thái trước đó không?",
        "answer": "<ol><li>1 điểm: hai nhánh đúng <code>¬S·A</code> và <code>S·¬B</code>.</li><li>2 điểm: theo 000,001,010,011,100,101,110,111, F là <code>0,0,1,1,1,0,1,0</code>; không thiếu hàng.</li><li>1 điểm: F chỉ phụ thuộc S,A,B hiện tại, không có trạng thái nhớ; bảng không đánh giá glitch.</li></ol>",
        "checks": ["Tôi xác định hai nhánh bằng giá trị S", "Tôi thử đủ tám hàng và so biểu thức", "Tôi không nhầm mux trừu tượng với pinout SN74HC151"],
    },
    {
        "id": "a20", "title": "Latch, Flip-Flop & Bộ Đếm", "subtitle": "Latch theo mức; D flip-flop chốt tại cạnh; bộ đếm cần điều kiện clock và điều khiển xác định.",
        "base": "A19", "units": "4", "figure_alt": "D flip-flop lấy mẫu D ở ba cạnh lên của CLK; D trước các cạnh là 1, 0, 1 và Q sau các cạnh là 1, 0, 1. Bên cạnh là chu trình đếm mod-4 00, 01, 10, 11 rồi về 00.",
        "figure_text": "Hai mô hình đồng bộ độc lập. DFF lý tưởng lấy mẫu ở cạnh lên; chuỗi mod-4 chỉ là trạng thái logic, không phải sơ đồ chân HC161.",
        "source": f'<a href="{TI74}" target="_blank" rel="noopener">TI SNx4HC74 Rev. F</a>; <a href="{TI161}" target="_blank" rel="noopener">TI SN74HC161 Rev. D</a>; <a href="{MIT5}" target="_blank" rel="noopener">MIT 6.004 §5.1</a>',
        "transcript": "Ba cạnh lên của clock được đánh số một, hai, ba; ngay trước chúng D ổn định lần lượt 1,0,1; Q ngay sau cạnh lấy lần lượt 1,0,1 trong mô hình lý tưởng. Một máy đếm hai bit riêng đi 00 rồi 01,10,11 và quay 00 nếu mọi cạnh đều được phép đếm.",
        "objectives": ["Phân biệt latch mở trong một mức enable với flip-flop lấy mẫu ở cạnh clock.", "Điền Q sau từng cạnh từ D ngay trước cạnh khi reset/preset bất hoạt.", "Trace bộ đếm nhị phân mod-4 trừu tượng và nhận ra điều kiện enable/reset của IC thật."],
        "body": f'''
<h2>1. Khi nào đầu ra có thể đổi?</h2>
<p>Latch D nhạy mức: khi enable ở mức hoạt động, Q có thể theo D; khi đóng, giữ giá trị. D flip-flop kích <em>cạnh lên</em> lấy giá trị D quanh cạnh rồi giữ Q đến cạnh tiếp theo, trừ tác động bất đồng bộ. <a href="{MIT5}" target="_blank" rel="noopener">MIT 6.004 §5.1</a> giải thích latch, register và setup/hold. <a href="{TI74}" target="_blank" rel="noopener">SN74HC74 Rev. F</a> là DFF cạnh lên có ngõ preset/clear bất đồng bộ, nên không được áp mô hình cạnh lên nếu preset/clear đang tác động.</p>
<h2>2. Ví dụ ba cạnh</h2>
<p>Giả sử Q ban đầu 0, preset/clear bất hoạt, D đã ổn định trước mỗi cạnh lên và giữ đủ lâu sau cạnh. D trước các cạnh số 1,2,3 là <code>1,0,1</code>; Q <em>sau</em> từng cạnh là <code>1,0,1</code>. Nếu D đổi giữa hai cạnh mà không có ngõ bất đồng bộ, Q của DFF lý tưởng giữ nguyên; latch đang mở có thể đổi theo D. Khi dựng timing thật phải xét setup/hold và clock-to-Q, bài A21 sẽ làm rõ.</p>
<div class="table-wrap"><table><caption>Hai trace lý tưởng riêng</caption><thead><tr><th>Cạnh lên</th><th>D ổn định trước cạnh</th><th>Q DFF sau cạnh</th><th>Counter mod-4 sau cạnh (ban đầu 00)</th></tr></thead><tbody><tr><td>1</td><td>1</td><td>1</td><td>01</td></tr><tr><td>2</td><td>0</td><td>0</td><td>10</td></tr><tr><td>3</td><td>1</td><td>1</td><td>11</td></tr><tr><td>4</td><td>chưa cho</td><td>chưa xác định từ đề</td><td>00</td></tr></tbody></table></div>
<p>Bộ đếm mod-4 hai bit tăng theo <code>00→01→10→11→00</code>. <a href="{TI161}" target="_blank" rel="noopener">SN74HC161 Rev. D</a> là bộ đếm <strong>bốn bit</strong> đồng bộ có ngõ enable, load và clear; chuỗi hai bit ở hình không đồng nghĩa IC tự chạy mod-4 nếu chưa cấu hình ngõ điều khiển.</p>
<h2>3. Hoạt động giấy/bảng tính</h2>
<div class="callout callout-practice"><div class="callout-header">🔬 Trace cạnh clock</div><p>Vẽ bốn cạnh lên, cho Q ban đầu 0, D ổn định trước cạnh là 1,0,1,0. Điền Q sau từng cạnh; ở một dòng khác cộng một bit vào trạng thái counter hai bit và bỏ carry ở ngoài 2 bit. So với bảng trên cho ba cạnh đầu. Ghi rõ đây là mô hình chức năng, chưa kiểm cửa sổ setup/hold của part.</p></div>
<div class="callout callout-warning"><div class="callout-header">⚠️ Giới hạn IC thật</div><p>Không để preset/clear, load hay enable nổi và không suy clock tối đa từ trace. Chọn datasheet theo VCC/nhiệt/tải và kiểm pulse width, setup/hold, reset trước lab thật.</p></div>''',
        "exercise": "Q ban đầu 0; preset/clear bất hoạt. D ổn định trước ba cạnh lên lần lượt <code>0,1,1</code>. Ghi Q sau từng cạnh. Bộ đếm hai bit ban đầu 00, được phép đếm ở cả ba cạnh: trạng thái sau mỗi cạnh là gì? Một lần đổi D giữa cạnh 2 và 3 có làm Q DFF đổi ngay không?",
        "answer": "<ol><li>1 điểm: Q DFF sau ba cạnh <code>0,1,1</code>.</li><li>1 điểm: counter từ 00 cho <code>01,10,11</code>.</li><li>1 điểm: D đổi giữa hai cạnh không đổi Q ngay trong mô hình DFF cạnh lên khi ngõ bất đồng bộ bất hoạt.</li><li>1 điểm: muốn áp lên HC74/HC161 thật còn phải nêu các điều kiện control và setup/hold; trạng thái logic không là timing guarantee.</li></ol>",
        "checks": ["Tôi nêu Q ban đầu và thời điểm lấy D", "Tôi phân biệt latch với DFF cạnh lên", "Tôi không gán mod-4 mặc định cho HC161 bốn bit"],
    },
    {
        "id": "a21", "title": "FSM, Clock & Kiểm Timing", "subtitle": "Trạng thái đổi ở cạnh hợp lệ; timing cần điều kiện cả setup, hold, clock và đầu vào bất đồng bộ.",
        "base": "A20", "units": "5", "figure_alt": "FSM Moore ba trạng thái G xanh, Y vàng, R đỏ. Với advance bằng 1 ở cạnh clock: G sang Y, Y sang R, R sang G; advance bằng 0 giữ trạng thái. Bên dưới là ngân sách setup giả định: 20 cộng 30 cộng 15 bằng 65 ns nhỏ hơn chu kỳ 100 ns.",
        "figure_text": "FSM đèn ba trạng thái trừu tượng; màu trong tên trạng thái chỉ là nhãn output, không phải mạch điều khiển đèn giao thông an toàn. Mọi thời gian trong hình là giả định bài toán.",
        "source": f'<a href="{MIT6}" target="_blank" rel="noopener">MIT 6.004 §6.1 FSM, async/metastability</a>; <a href="{MIT5}" target="_blank" rel="noopener">MIT §5.1 setup/hold</a>',
        "transcript": "Có ba trạng thái G, Y, R với output Moore tương ứng xanh, vàng, đỏ. Tại mỗi cạnh lên, advance 0 giữ trạng thái; advance 1 cho G sang Y, Y sang R, R sang G. Đường thời gian giả định gồm clock-to-Q tối đa 20 ns, logic tổ hợp tối đa 30 ns và setup 15 ns, tổng 65 ns, để so với chu kỳ 100 ns; hình không đưa dữ liệu hold/min delay.",
        "objectives": ["Lập bảng chuyển trạng thái Moore đủ ba trạng thái và hai giá trị advance.", "Trace trạng thái sau từng cạnh, tách output theo trạng thái khỏi input tức thời.", "Kiểm điều kiện setup của đường register→logic→register với các delay giả định và nêu các điều kiện chưa được kiểm."],
        "body": f'''
<h2>1. Máy trạng thái Moore ba trạng thái</h2>
<p>Chọn trạng thái khởi đầu <code>G</code> (xanh). Output Moore phụ thuộc <em>trạng thái hiện tại</em>: G bật nhãn xanh, Y nhãn vàng, R nhãn đỏ. Tại cạnh lên, <code>advance=0</code> giữ trạng thái; <code>advance=1</code> đi <code>G→Y→R→G</code>. Đây là mô hình học toán, không phải bộ điều khiển đèn giao thông an toàn: không có pha all-red, interlock, giám sát lỗi hoặc thời gian thực.</p>
<div class="table-wrap"><table><caption>Bảng chuyển trạng thái đủ 3×2 hàng</caption><thead><tr><th>Trạng thái hiện tại</th><th>Output Moore</th><th>advance=0 → sau cạnh</th><th>advance=1 → sau cạnh</th></tr></thead><tbody><tr><td>G</td><td>Xanh</td><td>G</td><td>Y</td></tr><tr><td>Y</td><td>Vàng</td><td>Y</td><td>R</td></tr><tr><td>R</td><td>Đỏ</td><td>R</td><td>G</td></tr></tbody></table></div>
<p>Ví dụ từ G với advance ổn định trước bốn cạnh là <code>1,0,1,1</code>: sau các cạnh nhận <code>Y,Y,R,G</code>; output tương ứng vàng, vàng, đỏ, xanh. Nếu đầu vào đổi giữa hai cạnh, trạng thái chưa đổi; nếu đổi quá sát cạnh có thể vi phạm timing, không được tự gán hàng nào là chắc.</p>
<h2>2. Kiểm đường setup, giữ riêng các điều kiện khác</h2>
<p>Với hai register trên cùng clock lý tưởng, bỏ qua skew/jitter trong <strong>ví dụ giả định</strong>, cần <code>T ≥ tCQ,max + tcomb,max + tsetup</code>. Cho <code>20 ns + 30 ns + 15 ns = 65 ns</code>; nếu <code>T=100 ns</code> thì còn biên setup <code>35 ns</code>. Nếu <code>T=60 ns</code>, thiếu <code>5 ns</code>, nên <strong>không đạt</strong> điều kiện setup trong model. Các trị 20/30/15 ns không lấy từ SN74HC74 hoặc một board nào. <a href="{MIT5}" target="_blank" rel="noopener">MIT 6.004 §5.1</a> tách yêu cầu setup và hold.</p>
<p>Để kết luận mạch thật, còn cần bất đẳng thức <strong>hold</strong> dùng <em>minimum</em> clock-to-Q/logic contamination delay và clock skew, độ rộng xung clock, reset và điều kiện điện. Trong một mô hình riêng <strong>không skew</strong>, điều kiện là <code>tCQ,min+tcomb,min ≥ thold</code>; nếu giả sử <code>2+3 ≥ 4 ns</code> thì biên hold là <code>1 ns</code>. Ba số này cũng chỉ là giả định dạy cách kiểm; đường của ví dụ setup không hề có min delay, nên <strong>hold của nó vẫn chưa kiểm</strong>. Đầu vào <code>advance</code> bất đồng bộ có thể đến sát cạnh; <a href="{MIT6}" target="_blank" rel="noopener">MIT §6.1</a> giải thích metastability. Bộ đồng bộ nhiều tầng giảm xác suất lan truyền nếu thiết kế đúng, không thể cam kết thời gian giải quyết hữu hạn cho mọi sự kiện; nếu là nút bấm còn cần xử lý dội phím và xác định một lần bấm ứng với mấy cạnh.</p>
<h2>3. Hoạt động bảng trạng thái/timing</h2>
<div class="callout callout-practice"><div class="callout-header">🔬 Giấy/bảng tính</div><p>Viết sáu hàng (G,Y,R)×(0,1), đánh dấu output từng trạng thái, sau đó trace từ G theo <code>1,0,1,1</code>. Tạo bảng T=60, 65, 100 ns, cột <code>T−(20+30+15)</code> lần lượt −5, 0, 35 ns; ghi 65 ns là đúng ranh giới toán học trong giả định, không có margin. Thêm cột “hold/clock/async” là <em>chưa kiểm</em>, không điền PASS.</p></div>
<div class="callout callout-warning"><div class="callout-header">⚠️ Không phải lab điều khiển đèn thật</div><p>Hình FSM không chứa transistor/relay/nguồn, phần mềm MCU hoặc chứng nhận an toàn. Các output chỉ là nhãn. Nếu hiện thực, phải chọn nền tảng/part/revision, sơ đồ, clock/reset, synchronizer/debounce, timing path, và kiểm điều kiện lỗi; P9-04 mới xét lab tích hợp.</p></div>''',
        "exercise": "Từ G, advance ổn định trước bốn cạnh là <code>1,1,0,1</code>. Ghi trạng thái và output sau từng cạnh. Cùng đường giả định <code>tCQ,max=20 ns</code>, <code>tcomb,max=30 ns</code>, <code>tsetup=15 ns</code>: chu kỳ <code>T=60 ns</code> đạt setup không? Có được kết luận hold và đầu vào bất đồng bộ đều an toàn không?",
        "answer": "<ol><li>1 điểm: trạng thái sau bốn cạnh là <code>Y,R,R,G</code>.</li><li>1 điểm: output Moore là vàng, đỏ, đỏ, xanh.</li><li>1 điểm: tổng max+setup <code>65 ns</code>; T=60 ns thiếu 5 ns, không đạt setup trong giả định không skew/jitter.</li><li>1 điểm: chưa thể kết luận hold vì thiếu minimum delay/skew; max setup không thay thế kiểm hold.</li><li>1 điểm: advance bất đồng bộ có nguy cơ metastability; cần đồng bộ/debounce theo thiết kế cụ thể, không thể bảo đảm tuyệt đối bằng trace này.</li></ol>",
        "checks": ["Tôi trace đúng trạng thái sau cạnh và output Moore", "Tôi tính setup bằng max delay và nói rõ giả định", "Tôi để hold/async chưa kiểm khi thiếu dữ liệu"],
    },
]


def svg_shell(number: str, title: str, desc: str, contents: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="480" viewBox="0 0 900 480" role="img" aria-labelledby="title desc">
<title id="title">{escape(number)} — {escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<rect width="900" height="480" rx="24" fill="#0f172a"/><text x="36" y="48" fill="#e2e8f0" font-family="Arial,sans-serif" font-size="25" font-weight="700">{escape(number)} · {escape(title)}</text>
{contents}
<text x="36" y="450" fill="#cbd5e1" font-family="Arial,sans-serif" font-size="17">Mô hình học tập · nguồn và giả định ghi tại caption bài học</text></svg>'''


FIGURES = {
    "a17": '''<rect x="36" y="78" width="386" height="320" rx="16" fill="#1e293b"/><text x="60" y="114" fill="#93c5fd" font-size="21" font-family="Arial">1101₂ = 13₁₀</text><g fill="#e2e8f0" font-size="32" font-family="Arial"><text x="76" y="190">1</text><text x="165" y="190">1</text><text x="254" y="190">0</text><text x="343" y="190">1</text></g><g fill="#cbd5e1" font-size="20" font-family="Arial"><text x="68" y="235">8</text><text x="157" y="235">4</text><text x="246" y="235">2</text><text x="335" y="235">1</text><text x="65" y="310">8 + 4 + 0 + 1 = 13</text></g><rect x="454" y="78" width="410" height="320" rx="16" fill="#1e293b"/><text x="474" y="115" fill="#93c5fd" font-size="20" font-family="Arial">SN74HC00 · VCC=4,5 V</text><rect x="476" y="150" width="366" height="58" fill="#14532d"/><rect x="476" y="208" width="366" height="58" fill="#713f12"/><rect x="476" y="266" width="366" height="58" fill="#1d4ed8"/><g fill="white" font-family="Arial" font-size="20"><text x="494" y="187">0–1,35 V · LOW bảo đảm</text><text x="494" y="245">(1,35;3,15) V · chưa bảo đảm</text><text x="494" y="303">3,15–4,5 V · HIGH bảo đảm</text></g><text x="478" y="365" fill="#cbd5e1" font-family="Arial" font-size="16">Ngưỡng đầu vào, không phải mức ra</text>''',
    "a18": '''<rect x="36" y="78" width="390" height="320" rx="16" fill="#1e293b"/><g stroke="#93c5fd" stroke-width="4" fill="none"><path d="M70 196H170 M70 276H170 M328 236H380"/><path d="M170 155H236 Q310 155 310 236 Q310 317 236 317 H170Z"/></g><circle cx="321" cy="236" r="11" fill="#0f172a" stroke="#93c5fd" stroke-width="4"/><g fill="white" font-family="Arial" font-size="24"><text x="55" y="184">A</text><text x="55" y="267">B</text><text x="388" y="244">Y</text><text x="174" y="360">Y = ¬(A·B)</text></g><rect x="458" y="78" width="406" height="320" rx="16" fill="#1e293b"/><g font-family="Arial" font-size="24" fill="#e2e8f0"><text x="510" y="133">A B</text><text x="710" y="133">Y</text><text x="510" y="185">0 0</text><text x="710" y="185">1</text><text x="510" y="237">0 1</text><text x="710" y="237">1</text><text x="510" y="289">1 0</text><text x="710" y="289">1</text><text x="510" y="341">1 1</text><text x="710" y="341">0</text></g>''',
    "a19": '''<rect x="36" y="78" width="828" height="320" rx="16" fill="#1e293b"/><g fill="#0f172a" stroke="#93c5fd" stroke-width="3"><rect x="110" y="136" width="255" height="78" rx="12"/><rect x="110" y="240" width="255" height="78" rx="12"/><rect x="510" y="185" width="135" height="78" rx="12"/></g><g stroke="#93c5fd" stroke-width="4" fill="none"><path d="M365 175H440V205H510 M365 279H440V244H510 M645 224H748"/></g><g font-family="Arial" font-size="22" fill="white"><text x="132" y="169">AND nhánh A</text><text x="132" y="196">¬S · A</text><text x="132" y="273">AND nhánh B</text><text x="132" y="300">S · B</text><text x="554" y="233">OR</text><text x="757" y="233">Y</text></g><text x="118" y="360" font-family="Arial" font-size="20" fill="#cbd5e1">S=0 chọn A; S=1 chọn B · Y = ¬S·A + S·B</text>''',
    "a20": '''<rect x="36" y="78" width="414" height="320" rx="16" fill="#1e293b"/><text x="60" y="119" font-family="Arial" font-size="22" fill="#93c5fd">DFF · cạnh lên</text><path d="M84 270H385" stroke="#e2e8f0" stroke-width="3"/><g stroke="#38bdf8" stroke-width="4"><path d="M130 285V180 M240 285V180 M350 285V180"/></g><g font-family="Arial" font-size="20" fill="#e2e8f0"><text x="114" y="318">1</text><text x="224" y="318">2</text><text x="334" y="318">3</text><text x="80" y="165">D trước:</text><text x="125" y="225">1</text><text x="235" y="225">0</text><text x="345" y="225">1</text><text x="80" y="365">Q sau: 1 → 0 → 1</text></g><rect x="476" y="78" width="388" height="320" rx="16" fill="#1e293b"/><text x="500" y="119" font-family="Arial" font-size="22" fill="#93c5fd">Đếm mod-4 lý tưởng</text><g font-family="Arial" font-size="29" fill="white"><text x="535" y="207">00 → 01</text><text x="535" y="263">↑         ↓</text><text x="535" y="319">11 ← 10</text></g>''',
    "a21": '''<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="strokeWidth"><path d="M0 0L10 5L0 10Z" fill="#93c5fd"/></marker></defs><rect x="36" y="78" width="828" height="320" rx="16" fill="#1e293b"/><g fill="#14532d" stroke="#86efac" stroke-width="3"><circle cx="172" cy="204" r="60"/></g><g fill="#713f12" stroke="#fde68a" stroke-width="3"><circle cx="450" cy="204" r="60"/></g><g fill="#7f1d1d" stroke="#fca5a5" stroke-width="3"><circle cx="728" cy="204" r="60"/></g><g fill="white" font-family="Arial" font-size="29" text-anchor="middle"><text x="172" y="213">G</text><text x="450" y="213">Y</text><text x="728" y="213">R</text></g><g stroke="#93c5fd" stroke-width="4" fill="none" marker-end="url(#arrow)"><path d="M232 204H382"/><path d="M510 204H660"/><path d="M728 265V321H172V270"/></g><g fill="#e2e8f0" font-family="Arial" font-size="19"><text x="280" y="188">advance=1</text><text x="558" y="188">advance=1</text><text x="360" y="315">advance=1 · quay về G</text><text x="93" y="112">advance=0: mỗi trạng thái giữ nguyên tại cạnh</text><text x="133" y="370">Setup giả định: 20 + 30 + 15 = 65 ns ≤ T 100 ns</text></g>''',
}


def render(lesson: dict[str, object], index: int) -> str:
    lesson_id = str(lesson["id"])
    title = str(lesson["title"])
    prev_id = f"a{16 + index:02}"
    prev_title = "Từ Trường, Cảm Ứng & Đường Hồi Dòng" if index == 0 else str(LESSONS[index - 1]["title"])
    next_nav = (f'<a href="a{18 + index:02}.html" class="lesson-nav-btn"><div><div class="nav-label">Bài tiếp →</div><div class="nav-title">A{18 + index:02}: {escape(str(LESSONS[index + 1]["title"]))}</div></div></a>' if index < 4 else "")
    objectives = "".join(f"<li>{item}</li>" for item in lesson["objectives"])
    checks = "".join(f'<div class="checklist-item"><input type="checkbox" id="{lesson_id}c{i}"><label for="{lesson_id}c{i}">{escape(item)}</label></div>' for i, item in enumerate(lesson["checks"], 1))
    return f'''<!DOCTYPE html>
<html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>{lesson_id.upper()}: {escape(title)} — Giáo Trình Điện Tử Thực Hành</title><meta name="description" content="{escape(str(lesson['subtitle']))}"><link rel="stylesheet" href="../assets/css/style.css"></head>
<body><header class="site-header"><a href="../index.html" class="logo"><div class="logo-icon">⚡</div><div><div class="logo-text">Điện Tử Thực Hành</div><div class="logo-sub">Giáo trình nâng cao</div></div></a><button class="btn-menu" aria-label="Menu"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg></button><nav class="header-nav"><a href="../index.html">Trang chủ</a><a href="../week4/day22.html">Bài nền D22</a></nav><div class="header-progress"><span class="progress-label">Lộ trình nâng cao · {lesson_id.upper()}</span></div></header>
<div class="app-layout"><aside class="sidebar" id="sidebar"></aside><main class="main-content"><article class="content-area">
<div class="lesson-header"><div class="lesson-meta"><span class="tag tag-week">Phase 9</span><span class="tag tag-day">{lesson_id.upper()}</span><span class="tag tag-difficulty-beginner">M1 · {lesson['units']} ĐV</span></div><h1 class="lesson-title">{escape(title)}</h1><p class="lesson-subtitle">{escape(str(lesson['subtitle']))}</p><div class="lesson-stats"><span class="lesson-stat">⏱ {lesson['units']} ĐV đọc/bảng/bài tập</span><span class="lesson-stat">📚 Tiên quyết: {escape(str(lesson['base']))}</span></div></div>
<div class="objectives-box"><div class="objectives-title">🎯 Mục tiêu kiểm được</div><ul class="objectives-list">{objectives}</ul></div>
<figure class="figure figure--overview"><div class="figure-scroll" tabindex="0" role="region" aria-label="Sơ đồ có thể cuộn ngang"><img src="../assets/images/advanced/{lesson_id}.svg" width="900" height="480" loading="lazy" decoding="async" alt="{escape(str(lesson['figure_alt']))}"></div><figcaption class="figure-caption"><div class="figure-number">{lesson_id.upper()}-1 — {escape(title)}</div><div class="figure-text">{lesson['figure_text']}</div><div class="figure-source">Hình tự vẽ; đối chiếu {lesson['source']}. <a href="../assets/images/advanced/{lesson_id}.svg" target="_blank" rel="noopener">Mở hình lớn</a>.</div></figcaption></figure>
<details class="summary-transcript"><summary>Đọc hình bằng chữ</summary><p>{lesson['transcript']}</p></details>
{lesson['body']}
<div class="section-divider"><span class="section-divider-label">Bài tập độc lập</span></div><div class="exercise-section"><div class="exercise-title">📝 Tự giải trước khi xem đáp án</div><p>{lesson['exercise']}</p><div class="answer-section"><button class="answer-toggle">👁 Xem lời giải và rubric</button><div class="answer-content">{lesson['answer']}</div></div></div>
<div class="checklist"><div class="checklist-title">✅ Tự kiểm {lesson_id.upper()}</div>{checks}</div>
<div class="lesson-nav"><a href="{prev_id}.html" class="lesson-nav-btn"><div><div class="nav-label">← Bài trước</div><div class="nav-title">{prev_id.upper()}: {escape(prev_title)}</div></div></a>{next_nav}</div>
</article></main></div><script src="../assets/js/sidebar-data.js"></script><script src="../assets/js/main.js"></script><script>renderSidebar('{lesson_id}.html');</script></body></html>
'''


def main() -> None:
    for index, lesson in enumerate(LESSONS):
        lesson_id = str(lesson["id"])
        (ROOT / "advanced" / f"{lesson_id}.html").write_text(render(lesson, index), encoding="utf-8")
        figure = svg_shell(lesson_id.upper(), str(lesson["title"]), str(lesson["figure_alt"]), FIGURES[lesson_id])
        (ROOT / "assets/images/advanced" / f"{lesson_id}.svg").write_text(figure + "\n", encoding="utf-8")
        print(f"Wrote {lesson_id}.html and {lesson_id}.svg")


if __name__ == "__main__":
    main()
