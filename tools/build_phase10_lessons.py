"""Publish A29–A32 design-project lessons; source remains this script and ledger."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PICO = "https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf"
TMP = "https://www.analog.com/media/en/technical-documentation/data-sheets/tmp35_36_37.pdf"
MP = "https://docs.micropython.org/en/v1.26.0/rp2/quickref.html"


def source(url, label):
    return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'


COMMON = '<p>Xem <a href="../docs/projects/pico-tmp36-design.md">hồ sơ bốn chặng</a> và <a href="../docs/labs/pico-tmp36-monitor.md">lab P9-04</a> để đọc BOM, netlist, bảng đo và giới hạn. Hình A29–A32 là sơ đồ khối tự vẽ, không là sơ đồ CAD/ERC, layout sản xuất hoặc phép đo board.</p>'

LESSONS = [
    {
        "id": "a29", "title": "Từ Yêu Cầu Đến Sơ Đồ Khối", "base": "A09;A22;A25;A28", "units": "5",
        "subtitle": "Viết yêu cầu có phép kiểm và truy vết thành net, BOM, phép tính và bằng chứng.",
        "alt": "Ba khối USB/Pico, TMP36 và firmware/hysteresis/LED; đường nguồn 3V3, tín hiệu TEMP_V và hồi AGND được nêu rõ.",
        "caption": "Chặng A29 đặt ranh giới hệ; nối thật phải dùng bottom view TO-92 và đúng pinout Pico non-W.",
        "transcript": "USB cấp Pico non-W; 3V3(OUT) của board cấp TMP36 và tụ bypass. TMP36 đưa VOUT về GP26/ADC0; firmware đổi mã và điều khiển LED GP25 tích hợp. AGND là đường hồi. Hình không diễn tả một PCB đã thiết kế.",
        "objectives": ["Chuyển câu cần đo nhiệt thành phạm vi 20–40 °C, chu kỳ 1 s và hai ngưỡng có điều kiện kiểm.", "Truy vết ba net nguồn/tín hiệu/hồi, BOM và phép tính danh định từ yêu cầu.", "Tách cổng mô hình host khỏi phép đo và ký duyệt phần cứng."],
        "body": f'''<h2>1. Yêu cầu có thể chấm</h2><p>Đồ án là bộ báo nhiệt phòng <strong>theo mô hình</strong>: mỗi giây log raw ADC và nhiệt danh định, LED trên Pico non-W bật khi T_est≥30 °C, tắt khi T_est≤28 °C, giữ ở giữa. Không có radio, nguồn lưới, Li-ion hay tải ngoài. Dải kích thích giấy 20–40 °C tương ứng TMP36 danh định 0,70–0,90 V theo {source(TMP,'ADI TMP36 Rev. H')}; điều đó chưa chứng minh accuracy của một mẫu thực.</p>
<h2>2. Từ khối tới schematic/net</h2><p>Trên {source(PICO,'Pico datasheet §2')}, pin 36 là 3V3(OUT), pin 31 GP26/ADC0, pin 33 AGND, LED GP25 thuộc board non-W. Theo ADI Fig. 4 <strong>bottom view</strong>, TMP36GT9Z TO-92 có chân 1 +VS, 2 VOUT, 3 GND. Net học tập: +3V3 nối pin 36→U1.1/C1.1; TEMP_V nối U1.2→pin 31; AGND nối U1.3/C1.2→pin 33. C1 gốm 0,1 µF đặt sát U1 theo ADI Fig. 24. BOM B1 Pico, U1 TMP36GT9Z, C1; board/revision/footprint thực chưa có.</p>
<h2>3. Ngân sách và kế hoạch chứng cứ</h2><p>Ở 3,3 V danh định, TMP36 nằm trên mức nguồn tối thiểu 2,7 V là 0,6 V; chưa đo rail nên đây không là headroom đã chứng minh. Dòng TMP36 dưới 50 µA theo bảng ADI; tổng dòng Pico chưa biết. Chạy mô phỏng P9-04 để kiểm trace; bảng đo tương lai cần VREF/VOUT/raw, chuẩn nhiệt, timestamp, model/revision và T_est−T_chuẩn từng điểm. Điền “chưa đo” cho hiện tại.</p>{COMMON}''',
        "exercise": "Viết ba yêu cầu đo được; ghi net +3V3/TEMP_V/AGND với số chân, BOM ba mục, tính VOUT ở 20 và 40 °C; nêu hai bằng chứng thiếu trước khi nhận thiết kế vật lý.",
        "answer": "<ol><li>2 điểm: dải kích thích 20–40 °C, mẫu mỗi 1 s, LED on≥30/off≤28 °C theo T_est.</li><li>2 điểm: Pico 36→TMP36.1/C1; TMP36.2→Pico31; TMP36.3/C1→Pico33, góc nhìn đáy.</li><li>2 điểm: Pico/TMP36GT9Z/C1 0,1 µF; VOUT 0,70/0,90 V danh định.</li><li>2 điểm: thiếu rail/VREF/chuẩn nhiệt và marking/reviewer/ERC/đo thật; không chấm fake ADC là đo.</li></ol>",
        "checks": ["Tôi ghi yêu cầu có ngưỡng và thời gian", "Tôi đọc bottom view trước khi ghi pin", "Tôi giữ trạng thái chưa đo"],
        "source": f'{source(PICO,"Pico datasheet")}, {source(TMP,"ADI TMP36 Rev. H")}',
    },
    {
        "id": "a30", "title": "Thiết Kế Nguồn Thấp Áp Cho Hệ", "base": "A07;A08;A29", "units": "5",
        "subtitle": "Theo đường USB–VSYS–3V3 có sẵn trên Pico và tính tải cảm biến có điều kiện.",
        "alt": "Nguồn USB đi qua diode D1, VSYS và SMPS có sẵn trên Pico tới 3V3 OUT cấp TMP36; C1 bypass giữa rail và AGND.",
        "caption": "D1/SMPS là thành phần của Pico board, không phải BOM carrier; không mở adapter lưới.",
        "transcript": "USB đi tới VBUS Pico, qua diode D1 trên board tới VSYS và bộ nguồn chuyển mạch trên board để tạo 3V3 OUT. Rail đó cấp TMP36 và tụ C1 0,1 microfarad hồi về AGND. ADC_VREF lấy từ rail được lọc. Không có nguồn pin hoặc điện lưới trong bài.",
        "objectives": ["Truy đường cấp USB tới 3V3(OUT) theo đúng board datasheet.", "Tính công suất tải TMP36 từ giới hạn dòng và phân biệt với tổng dòng board chưa biết.", "Thiết kế phiếu đo rail/VREF/ripple mà không gọi mô hình nguồn lý tưởng là đo thật."],
        "body": f'''<h2>1. Đường nguồn đã có trên board</h2><p>{source(PICO,'Pico datasheet §4.5')} mô tả USB VBUS qua diode D1 tới VSYS, rồi nguồn board tạo 3,3 V; pin 36 3V3(OUT) cấp sensor, pin 33 AGND làm hồi. Không đưa 5 V USB tới GP26 hoặc TMP36. Không cấp ngược 3V3(OUT), không thêm nguồn VSYS thứ hai trong chặng này. Giá trị USB 5 V là danh định, rail thật phụ thuộc adapter/cáp/tải. ADC_VREF lấy từ 3,3 V đã lọc trên Pico, không tự nhận là chính xác 3,300 V.</p>
<h2>2. Schematic, BOM và ngân sách</h2><p>Schematic net: VBUS→D1→VSYS→SMPS nằm <em>trong B1 Pico</em>; 3V3(OUT) pin 36→U1 pin 1/C1; AGND pin 33→U1 pin 3/C1; U1 pin 2→GP26 pin 31. BOM ngoài board chỉ U1 TMP36GT9Z và C1 gốm 0,1 µF (mã/footprint/định mức điện áp chưa chốt). {source(TMP,'ADI Rev. H')} ghi sensor dưới 50 µA, nên ở 3,3 V <code>P_U1&lt;3,3×50 µA=0,165 mW</code> theo điều kiện datasheet. Pico khuyên tải 3V3(OUT) dưới 300 mA tùy VSYS/tải RP2040; không dùng 50 µA để suy tổng dòng hệ đã đo.</p>
<h2>3. Mô hình và phép đo tương lai</h2><p>Mô hình P9-04 đặt rail/VREF chính xác 3,300 V, không mô phỏng D1/SMPS/ripple/ESR. Muốn nghiệm thu thật phải ghi model USB, PCB/firmware, đo VBUS/VSYS/3V3/ADC_VREF khi không/có U1, xem ripple với ground/probe được duyệt và báo sai khác điều kiện. Chưa có dữ liệu nên không có hiệu suất/nhiệt nguồn được xác nhận.</p>{COMMON}''',
        "exercise": "Vẽ đường nguồn từ USB tới TMP36, phân biệt D1/SMPS thuộc board hay BOM mới; tính P sensor tối đa theo 50 µA ở 3,3 V; liệt kê ba rail hoặc điểm đo còn thiếu và giải thích vì sao 0,165 mW không là công suất cả hệ.",
        "answer": "<ol><li>2 điểm: USB→D1→VSYS→SMPS→3V3(OUT)→TMP36, AGND hồi, D1/SMPS sẵn trên Pico.</li><li>2 điểm: B1/U1/C1; không thêm nguồn lưới hoặc Li-ion.</li><li>2 điểm: 0,165 mW là cận theo dòng sensor, chưa tính RP2040/SMPS/LED/USB.</li><li>2 điểm: đo VBUS, VSYS, 3V3, ADC_VREF/ripple và điều kiện tải; chưa có số thực.</li></ol>",
        "checks": ["Tôi phân biệt đường nguồn board và carrier", "Tôi tính riêng tải sensor", "Tôi không nhận VREF lý tưởng là số đo"],
        "source": f'{source(PICO,"Pico datasheet §4.5")}, {source(TMP,"ADI TMP36 Rev. H")}',
    },
    {
        "id": "a31", "title": "Khối Cảm Biến, ADC & MCU", "base": "A23;A25;A28;A30", "units": "6",
        "subtitle": "Đổi raw thành nhiệt danh định, giữ hysteresis và kiểm ngân sách sai số theo giả định.",
        "alt": "TMP36 VOUT đi tới GP26 ADC0, phần mềm đổi mã sang nhiệt rồi qua FSM hai ngưỡng tới LED GP25; raw và VREF cần được giữ.",
        "caption": "Dòng dữ liệu/điều khiển, không là đường cấp điện; net điện ở hồ sơ đồ án.",
        "transcript": "TMP36 phát VOUT analog tới GP26 ADC0; mã read_u16 và VREF giả định tạo nhiệt danh định. FSM bật LED GP25 khi từ 30 độ C trở lên, tắt khi từ 28 độ C trở xuống, giữ trạng thái ở giữa. Log raw, nhiệt và trạng thái. Không có sensor thứ hai hoặc bộ chuẩn.",
        "objectives": ["Tính raw/T_est từ VOUT TMP36 bằng API MicroPython và phân biệt 12 bit silicon với 16 bit API.", "Kiểm trace LED on/hold/off từ mã đã lượng tử hóa.", "Lập ngân sách sai số giả định và phiếu validation độc lập, không gắn accuracy đo thật."],
        "body": f'''<h2>1. Schematic và BOM giữ đúng ranh giới</h2><p>B1 Pico non-W pin 36 cấp U1 TMP36GT9Z pin 1; U1 pin 2→B1 pin 31 GP26/ADC0, U1 pin 3/C1→B1 pin 33 AGND; C1 0,1 µF sát U1. Fig. 4 ADI nhìn <em>từ đáy</em>. LED GP25 thuộc board, không lộ ở header. {source(MP,'MicroPython RP2 quick reference v1.26')} dùng <code>ADC(Pin(26)).read_u16()</code>. API trả 0…65535 nhưng RP2040 ADC silicon là 12 bit; mã API không chứng minh 16 bit accuracy.</p>
<h2>2. Phép tính và ngưỡng</h2><p>Theo {source(TMP,'ADI TMP36 Rev. H')}, <code>V=0,500+0,010T</code> danh định. Mô hình host dùng 3,300 V chính xác: tại 25 °C, V=0,750 V→raw=14894→T_est≈24,9984 °C. Nếu T_est≥30 thì on; ≤28 thì off; ở giữa giữ. Mẫu kích thích 30 °C lượng tử thành 29,9986 °C nên chưa bật. Trace tám mẫu [25,29,30,31,29,28,27,31] °C là LED <code>0,0,0,1,1,0,0,1</code>. Chạy <code>python tools/verify_phase9_sensor_lab.py</code> để kiểm fake ADC/LED; đó không đo ADC thật.</p>
<h2>3. Ngân sách sai số có nhãn giả định</h2><p>Giả sử VREF lệch +1% mà phần mềm vẫn dùng 3,300 V, tại VOUT≈0,75 V thành phần sai lệch có cỡ 0,75 °C; nửa bước ADC 12 bit lý tưởng là <code>3,3/4096/2/0,010≈0,0403 °C</code>. Đây là giả định và lượng tử lý tưởng, chưa gồm sai số sensor theo grade/điều kiện, phi tuyến ADC, nhiễu, tự gia nhiệt và chuẩn nhiệt. Không cộng thông số <em>typical</em> thành mức bảo đảm. Bước đo thật: raw/VREF/VOUT/chuẩn ở 27–31 °C theo hai chiều, kiểm điểm validation độc lập và log <code>T_est−T_chuẩn</code>. Chưa có phép đo đó.</p>{COMMON}''',
        "exercise": "Tính VOUT và mã API danh định tại 25 °C; giải thích vì sao kích thích 30 °C có thể chưa bật LED; dự đoán trạng thái ở 31→29→28 °C; nêu ba nguồn sai số không có trong mô hình.",
        "answer": "<ol><li>2 điểm: 0,750 V, raw 14894, T_est≈24,9984 °C theo VREF 3,300 V.</li><li>2 điểm: 30 °C thành 29,9986 °C sau lượng tử nên chưa vượt ngưỡng; chấm theo T_est.</li><li>2 điểm: 31 bật, 29 giữ bật, 28 tắt theo mã thực của kịch bản.</li><li>2 điểm: VREF/ADC/sensor/chuẩn nhiệt/tiếp xúc hoặc noise chưa kiểm.</li></ol>",
        "checks": ["Tôi giữ raw và VREF", "Tôi chấm hysteresis từ số đã giải mã", "Tôi không coi bước API là accuracy"],
        "source": f'{source(TMP,"ADI TMP36 Rev. H")}, {source(PICO,"Pico datasheet")}, {source(MP,"MicroPython RP2 ADC")}',
    },
    {
        "id": "a32", "title": "Tích Hợp PCB & Báo Cáo Sai Khác", "base": "A29;A30;A31;D34", "units": "6",
        "subtitle": "Chốt net/footprint cần duyệt, đặt tụ gần cảm biến và giữ kết quả mô hình tách đo thật.",
        "alt": "Carrier thấp áp với Pico, TMP36 và tụ C1; ba net +3V3, TEMP_V, AGND, các cổng ERC/DRC/đo và ký duyệt được chỉ ra là còn chờ.",
        "caption": "Bố cục khái niệm của carrier; chưa chọn footprint và chưa chạy ERC/DRC/EMC.",
        "transcript": "Pico board cắm lên carrier. Đường 3V3 từ chân 36 tới chân 1 TMP36 và một đầu tụ C1; VOUT chân 2 tới GP26 chân 31; AGND chân 3 và đầu còn lại C1 tới Pico chân 33. Tụ được đặt gần sensor và TEMP_V ngắn. Danh sách chờ gồm footprint, ERC, DRC, số đo và reviewer.",
        "objectives": ["Liệt kê net PCB và kiểm số chân theo package/góc nhìn, không xuất Gerber từ hình minh họa.", "Giải thích vị trí bypass/đường hồi và giữ ngân sách nguồn/sai số xuyên A29–A31.", "Lập báo cáo sai khác có điều kiện, bằng chứng ERC/DRC/đo/reviewer còn chờ."],
        "body": f'''<h2>1. Netlist carrier và BOM</h2><p>Carrier chỉ dự kiến ba net: <code>+3V3={{B1.36,U1.1,C1.1}}</code>, <code>TEMP_V={{U1.2,B1.31}}</code>, <code>AGND={{U1.3,C1.2,B1.33}}</code>. GP25→LED onboard nằm trong Pico. B1 là Pico non-W, U1 TMP36GT9Z TO-92, C1 gốm 0,1 µF. Chưa chọn part number/footprint của C1 hay loại header; marking U1 và PCB B1 chưa đối chiếu mẫu. {source(TMP,'ADI TMP36 Rev. H Fig. 4')} ghi TO-92 từ đáy; việc gán pad PCB phải kiểm ở đúng góc nhìn. Netlist chữ và <a href="../assets/images/labs/pico-tmp36-monitor.svg">hình net lab</a> không thay CAD schematic có ERC.</p>
<h2>2. Layout số và ngân sách</h2><p>C1 sát chân +VS/GND U1 theo ADI Fig. 24, TEMP_V ngắn và có đường hồi AGND rõ; giữ khỏi vùng đường nguồn/switching của board trong bố trí dự kiến. {source(PICO,'Pico datasheet')} cho AGND/pinout và nguồn board, không chứng minh một layout mới đã đạt EMI. Ngân sách nguồn như A30: U1 dưới 50 µA, P_U1 dưới 0,165 mW ở 3,3 V; ngân sách sai số như A31 còn VREF/ADC/sensor/chuẩn chưa đo. Mô hình host dự đoán 25 °C→0,75 V/code14894/LED off, 31 °C→0,81 V/LED on, 29 °C sau đó giữ on.</p>
<h2>3. Cổng chế tạo và báo cáo sai khác</h2><p>Trước cấp điện: xác định đúng part/footprint/board marking và schematic revision, dựng KiCad, kiểm net với người độc lập, chạy ERC/DRC rồi ký duyệt; kiểm thông mạch/ngắn khi chưa cấp nguồn. Sau đó mới đo 3V3/VREF/VOUT/raw/nhiệt chuẩn/LED và báo <code>T_est−T_chuẩn</code> cùng uncertainty, setup, firmware, ngày, người duyệt. Hiện tất cả mục này là <strong>pending</strong>; không có Gerber, PCB, ERC, DRC, phép đo hoặc chữ ký. Mô phỏng host không thể thay bước này.</p>{COMMON}''',
        "exercise": "Ghi ba net và BOM, chỉ ra vị trí C1 và một lỗi footprint TO-92 có thể xảy ra; nêu bốn bằng chứng cần trước khi công bố mạch thật, và điền hàng báo cáo sai khác khi chưa có board.",
        "answer": "<ol><li>2 điểm: ba net đúng B1.36/U1.1/C1.1, U1.2/B1.31, U1.3/C1.2/B1.33.</li><li>2 điểm: C1 gần sensor, TEMP_V ngắn/hồi AGND, không lấy Fig. 4 bottom view thành top view.</li><li>2 điểm: footprint/part/board, ERC/DRC, đo rail/nhiệt/ADC, reviewer ký là các cổng còn chờ.</li><li>2 điểm: báo cáo hiện ghi chưa đo/chưa tính/chưa ký, không điền 0 như phép đo.</li></ol>",
        "checks": ["Tôi kiểm pad theo góc nhìn package", "Tôi giữ sơ đồ khối tách CAD/ERC", "Tôi không điền kết quả đo giả"],
        "source": f'{source(TMP,"ADI TMP36 Rev. H")}, {source(PICO,"Pico datasheet")}',
    },
]


FIGURES = {
    "a29": ("USB / Pico", "3V3 → TMP36", "ADC → FSM → LED"),
    "a30": ("USB → VSYS", "SMPS → 3V3 OUT", "TMP36 + C1 → AGND"),
    "a31": ("TMP36 VOUT", "GP26 ADC0 / raw", "FSM → LED GP25"),
    "a32": ("B1 Pico + U1 TMP36", "+3V3 / TEMP_V / AGND", "ERC / DRC / đo: chờ"),
}


def svg(item):
    a, b, c = FIGURES[item["id"]]
    title = f'{item["id"].upper()} — {item["title"]}'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="480" viewBox="0 0 900 480" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(item['alt'])}</desc><rect width="900" height="480" rx="24" fill="#0f172a"/><text x="35" y="50" fill="#e2e8f0" font-family="Arial" font-size="25" font-weight="bold">{escape(title)}</text><g font-family="Arial" font-size="18" text-anchor="middle"><rect x="40" y="130" width="245" height="180" rx="16" fill="#164e63"/><rect x="327" y="130" width="245" height="180" rx="16" fill="#14532d"/><rect x="614" y="130" width="245" height="180" rx="16" fill="#713f12"/><text x="162" y="230" fill="white">{escape(a)}</text><text x="449" y="230" fill="white">{escape(b)}</text><text x="736" y="230" fill="white">{escape(c)}</text></g><path d="M285 220H327M572 220H614" stroke="#93c5fd" stroke-width="4"/><text x="45" y="405" fill="#cbd5e1" font-family="Arial" font-size="18">Mô hình học tập · xem netlist, điều kiện và giới hạn trong bài</text></svg>\n'''


def render(item, previous, following):
    ident = item["id"]
    objectives = "".join(f"<li>{escape(value)}</li>" for value in item["objectives"])
    checks = "".join(f'<div class="checklist-item"><input type="checkbox" id="{ident}c{i}"><label for="{ident}c{i}">{escape(value)}</label></div>' for i, value in enumerate(item["checks"], 1))
    prev_link = f'<a href="{previous[0]}.html" class="lesson-nav-btn"><div><div class="nav-label">← Bài trước</div><div class="nav-title">{escape(previous[1])}</div></div></a>'
    next_link = f'<a href="{following[0]}.html" class="lesson-nav-btn"><div><div class="nav-label">Bài tiếp →</div><div class="nav-title">{escape(following[1])}</div></div></a>' if following else ""
    html = f'''<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>{ident.upper()}: {escape(item['title'])} — Giáo Trình Điện Tử Thực Hành</title><meta name="description" content="{escape(item['subtitle'])}"><link rel="stylesheet" href="../assets/css/style.css"></head><body><header class="site-header"><a href="../index.html" class="logo"><div class="logo-icon">⚡</div><div><div class="logo-text">Điện Tử Thực Hành</div><div class="logo-sub">Giáo trình nâng cao</div></div></a><button class="btn-menu" aria-label="Menu"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg></button><nav class="header-nav"><a href="../index.html">Trang chủ</a><a href="../week4/day25.html">Bài nền D25</a></nav><div class="header-progress"><span class="progress-label">Lộ trình nâng cao · {ident.upper()}</span></div></header><div class="app-layout"><aside class="sidebar" id="sidebar"></aside><main class="main-content"><article class="content-area"><div class="lesson-header"><div class="lesson-meta"><span class="tag tag-week">Phase 10</span><span class="tag tag-day">{ident.upper()}</span><span class="tag tag-difficulty-beginner">M1 · {item['units']} ĐV</span></div><h1 class="lesson-title">{escape(item['title'])}</h1><p class="lesson-subtitle">{escape(item['subtitle'])}</p><div class="lesson-stats"><span class="lesson-stat">⏱ {item['units']} ĐV đọc/bảng/bài tập</span><span class="lesson-stat">📚 Tiên quyết: {escape(item['base'])}</span></div></div><div class="objectives-box"><div class="objectives-title">🎯 Mục tiêu kiểm được</div><ul class="objectives-list">{objectives}</ul></div><figure class="figure figure--overview"><div class="figure-scroll" tabindex="0" role="region" aria-label="Sơ đồ có thể cuộn ngang"><img src="../assets/images/advanced/{ident}.svg" width="900" height="480" loading="lazy" decoding="async" alt="{escape(item['alt'])}"></div><figcaption class="figure-caption"><div class="figure-number">{ident.upper()}-1 — {escape(item['title'])}</div><div class="figure-text">{item['caption']}</div><div class="figure-source">Hình tự vẽ; đối chiếu {item['source']}. <a href="../assets/images/advanced/{ident}.svg" target="_blank" rel="noopener">Mở hình lớn</a>.</div></figcaption></figure><details class="summary-transcript"><summary>Đọc hình bằng chữ</summary><p>{item['transcript']}</p></details>{item['body']}<div class="section-divider"><span class="section-divider-label">Bài tập độc lập</span></div><div class="exercise-section"><div class="exercise-title">📝 Tự giải trước khi xem đáp án</div><p>{item['exercise']}</p><div class="answer-section"><button class="answer-toggle">👁 Xem lời giải và rubric</button><div class="answer-content">{item['answer']}</div></div></div><div class="checklist"><div class="checklist-title">✅ Tự kiểm {ident.upper()}</div>{checks}</div><div class="lesson-nav">{prev_link}{next_link}</div></article></main></div><script src="../assets/js/sidebar-data.js"></script><script src="../assets/js/main.js"></script><script>renderSidebar('{ident}.html');</script></body></html>\n'''
    return (html.replace('<body>', '<body><a class="skip-link" href="#lesson-main">\u0110i t\u1edbi n\u1ed9i dung ch\u00ednh</a>', 1)
                .replace('<main class="main-content">', '<main class="main-content" id="lesson-main" tabindex="-1">', 1))


def main():
    for index, item in enumerate(LESSONS):
        previous = ("a28", "A28: Sai Số, Hiệu Chuẩn & Lọc Cảm Biến") if index == 0 else (LESSONS[index - 1]["id"], f"{LESSONS[index - 1]['id'].upper()}: {LESSONS[index - 1]['title']}")
        following = (LESSONS[index + 1]["id"], f"{LESSONS[index + 1]['id'].upper()}: {LESSONS[index + 1]['title']}") if index < len(LESSONS) - 1 else None
        (ROOT / "advanced" / f"{item['id']}.html").write_text(render(item, previous, following), encoding="utf-8")
        (ROOT / "assets/images/advanced" / f"{item['id']}.svg").write_text(svg(item), encoding="utf-8")
        print(item["id"], "published")


if __name__ == "__main__":
    main()
