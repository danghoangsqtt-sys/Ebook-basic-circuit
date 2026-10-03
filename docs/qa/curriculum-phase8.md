# QA Phase 8 — Linh kiện, phân tích mạch và trường

Ngày mở: 2026-10-03. Phạm vi đang thực hiện là nội dung số, phép tính và hoạt động mô phỏng **dự kiến**. Phase 7 đã qua audit trong phạm vi này; cổng phần cứng thật ở [`curriculum-hardware-pending.md`](curriculum-hardware-pending.md) vẫn mở. Không ghi bài mới đã xuất bản, mô phỏng đã chạy hoặc mạch đã đo khi chưa có tệp bằng chứng.

## P8-01 — Khóa hợp đồng A01–A16

- [`advanced-phase8-syllabus.md`](../curriculum/advanced-phase8-syllabus.md) có đúng 16 mã A01–A16, mỗi mã một mục duy nhất. Mỗi mục có outcome kiểm được, tiên quyết/M0–M2, thời lượng tương đối, ví dụ giải bằng số, hoạt động giấy/bảng tính/simulator có dữ liệu kỳ vọng, bài tập khác ví dụ với đáp án/rubric và nguồn gốc có URL cùng phạm vi áp dụng.
- Ma trận tiên quyết nối A01–A16 với 56 bài D trong [`syllabus.md`](../curriculum/syllabus.md) và [`coverage-matrix.csv`](../curriculum/coverage-matrix.csv). A01–A08 mở rộng lựa chọn linh kiện/datasheet; A09–A16 mở rộng giải mạch nhiều ẩn, quá độ, AC và trường–layout. Các phần này không coi việc nêu tên linh kiện hay công thức một bước ở bài D là đã dạy đủ năng lực mới.
- Nguồn thông số linh kiện là tài liệu hãng Vishay, TDK, Murata, Nichicon, Würth, TI và ADI; định luật/mô hình tham chiếu OpenStax/MIT. Ví dụ số không gắn part được gắn nhãn **giả định bài toán**. Không suy giới hạn của một IC sang module/PCB khác.
- Kiểm cấu trúc bằng Python: 16/16 heading đúng thứ tự A01–A16; mỗi mục có đủ sáu trường bắt buộc và ít nhất một URL HTTPS — PASS. Agent biên soạn đã kiểm lại ví dụ số và vị trí bảng nguồn; đây là review tĩnh, chưa phải review trang xuất bản.

**Kết luận P8-01:** PASS cho đặc tả nội dung số. Bước kế tiếp P8-02 viết A01–A04; bài mới chỉ được tính là hoàn thành khi có HTML/SVG, nguồn sát claim, lời giải, chỉ mục/liên kết/hiển thị và audit/debug riêng.
