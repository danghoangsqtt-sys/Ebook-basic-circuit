# Rà soát từ góc nhìn người học và mobile

Ngày: 2026-10-02. Hai lượt rà soát chỉ đọc được thực hiện sau bản kế hoạch đầu tiên; các điểm bên dưới đã được đưa vào ROADMAP và bản mẫu giao diện.

| Phát hiện | Điều chỉnh kế hoạch |
| --- | --- |
| Lộ trình 4 nhóm trong bản mẫu chưa mở được từng bài | Trang đầu mẫu có mục lục 8 tuần/56 bài; P1-02 yêu cầu mở trực tiếp bài bất kỳ |
| Người đọc mobile có thể mất danh sách bài khi sidebar bị ẩn | P1-03 yêu cầu menu 8 tuần/56 bài, chỉ báo bài hiện tại và kiểm tra focus |
| Dấu đã tô khó tìm lại ngay trong Phase 1 | P1-07 có danh sách dấu của bài hiện tại; P2-01 mở rộng thư viện xuyên bài |
| Người mới thiếu đường dẫn chuẩn bị và an toàn | Trang đầu mẫu liên kết tới Bài 1; P1-02 yêu cầu xác minh và dẫn tới nội dung chuẩn bị/an toàn có thật |
| Chọn chữ bằng bàn phím và mobile có nhiều khác biệt | P1-06 quy định Shift+Arrow, Tab, Escape, Context Menu/Shift+F10; thử iOS Safari và Android Chrome |
| Dấu màu đơn thuần khó tiếp cận | P1-07 yêu cầu danh sách bằng chữ, trạng thái neo, thao tác bằng bàn phím/screen reader |
| Chọn cả câu dài có thể làm tìm kiếm rỗng | P1-05 rút từ khóa có nghĩa và cung cấp gợi ý sửa truy vấn |

Không có phát hiện nào làm đổi ba phase hoặc đòi thêm backend.

## Rà soát kế hoạch tái biên soạn — 2026-10-03

Hai lượt review chỉ đọc: góc nhìn người mới học và góc nhìn kỹ thuật điện tử. Chúng đánh giá bản brainstorm và mã nguồn hiện có; **chưa xác nhận** sơ đồ hoặc bài mới đã đúng. Đã đưa các điểm dưới đây vào `CURRICULUM-PLAN.md`.

| Phát hiện | Điều chỉnh kế hoạch |
| --- | --- |
| Số bài, độc giả, mức toán và thiết bị chưa chốt | P7-01 xác nhận trước khi viết A01–A32; lab có nhánh mô phỏng nếu chưa có board |
| 80 ASCII được audit ở bản lịch sử, trạng thái lỗi có thể đã thay đổi | P7-02 tái kiểm trên HTML hiện hành, ghi ID/dòng/trạng thái mới; không tự coi lỗi cũ vẫn mở |
| Sáu hình cần đúng quan hệ điện, không chỉ đẹp | P7-03 yêu cầu nguồn sửa được, SVG, net/cực tính/đơn vị/nguồn, alt và reviewer; sáu ID D01-1…D01-4, D02-1, D03-1 |
| Giáo trình có nhiều nhắc đến linh kiện nhưng thiếu tuyến chọn/đo | P8-02/P8-03 đòi nhận biết, datasheet, đo/mô phỏng, bài tập và lời giải theo từng họ |
| Lý thuyết mạch cần chứng minh học được | P8-04 buộc ví dụ giải độc lập, điều kiện áp dụng, đối chiếu mô phỏng/đo và đáp án cho từng phương pháp |
| Cảm biến, board và đồ án có rủi ro phụ thuộc part cụ thể | P9-02…P10-03 yêu cầu mã/revision, giới hạn I/O, hiệu chuẩn, ngân sách nguồn/sai số, BOM, phép đo và người duyệt cho mạch rủi ro |
| Một số câu an toàn Bài 1 và nhận xét ký hiệu Bài 3 có thể gây hiểu sai | P7-05 soát với điều kiện và nguồn; không giữ lời khẳng định tổng quát thiếu căn cứ |

Ví dụ chuỗi hai pin trong `week1/day01.html` hiện có nút 0/1,5/3 V và cực tính nhất quán theo giả định danh định. Lý do đưa vào P7-03 là **khó đọc và cần minh họa kỹ thuật**, không mặc định gọi đó là lỗi đấu nối; QA cũ có thể nói về phiên bản trước. Ngược lại, phần GND và lời an toàn phải được duyệt kỹ thuật theo nội dung hiện hành.
