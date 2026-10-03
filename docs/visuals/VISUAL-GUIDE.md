# Quy chuẩn hình minh họa giáo trình

Áp dụng cho 56 bài HTML. Mục tiêu là giúp người học **hiểu và lắp đúng mạch**; hình trang trí không thay cho ký hiệu điện hoặc chỉ dẫn đo. Danh mục từng bài ở `docs/brainstorm/visual-inventory-2026-10-02.md`; lỗi kỹ thuật cần xử lý ở `docs/qa/visual-technical-audit.md`.

## Chọn loại hình

| Loại | Dùng khi | Điều phải thể hiện |
| --- | --- | --- |
| Ảnh thiết bị thật | Nhận diện linh kiện, chân, cổng đo, thao tác thực tế | Model thực tế hoặc nhãn “ví dụ tương tự”, hướng nhìn, bộ phận được nói tới |
| Sơ đồ mạch SVG | Giải thích cách nối và chiều dòng/tín hiệu | Nút điện, GND, nguồn, cực tính, giá trị, mã linh kiện, diode/tụ phân cực và chú giải |
| Infographic | Quy tắc, so sánh, quy trình, chuỗi đo | Ý chính từ chính bài giảng; số liệu có điều kiện áp dụng |
| Sơ đồ khối | Hệ thống hoặc luồng điều khiển | Đầu vào, xử lý, đầu ra, nguồn, tín hiệu phản hồi và chiều mũi tên |
| Sơ đồ tư duy | Ôn tập hoặc định hướng | Tên nhánh khớp đề mục/bài; phân cấp rõ, ít chữ mỗi nhánh |

## Quy tắc kỹ thuật

1. Đọc toàn bộ đoạn giảng, sơ đồ ký tự và bước thực hành liên quan trước khi vẽ. Sơ đồ ký tự có lỗi trong audit **không** được chép nguyên sang SVG.
2. Với linh kiện có mã: dùng datasheet của đúng nhà sản xuất/package/module, ghi góc nhìn và số chân. Không coi thứ tự chân của một board là chuẩn cho tất cả board.
3. Sơ đồ nguồn và tải cảm phải thể hiện đường hồi dòng, tụ từ rail tới GND, diode flyback mắc ngược song song, bảo vệ quá áp/dòng và nguồn cấp phù hợp.
4. Đồ thị phải có trục, đơn vị, điều kiện đầu; không vẽ tỷ lệ/ngưỡng tuyệt đối nếu phụ thuộc linh kiện, tải hoặc cấu hình.
5. Hình mô tả nguyên tử, dòng điện hoặc hệ thống là *mô hình khái niệm* khi không đúng tỷ lệ/vị trí vật lý. Ghi giới hạn ngay ở chú thích.

## Bố cục và khả năng đọc

- Dùng `.figure` và `.figure-caption` có sẵn. Mỗi hình có số/tên, một đoạn giải thích ý nghĩa, nguồn và `alt` nêu thông tin chính. SVG nguồn có `<title>` và `<desc>`.
- Ảnh `<img>` có `width`, `height`, `loading="lazy"` nếu dưới màn hình đầu và `decoding="async"`. Caption theo cỡ chữ người đọc chọn; không dùng chữ chỉ để lấp khoảng trống.
- Thiết kế từ 320 px: nhãn trong hình cố gắng từ 15 px ở kích thước hiển thị; sơ đồ dày thông tin có bản SVG dọc qua `<picture>`. Không làm toàn trang cuộn ngang. Nếu vẫn quá rộng, cho cuộn trong riêng khung hình và ghi gợi ý cuộn.
- Dùng màu như hỗ trợ, luôn có nhãn chữ/ký hiệu. Kiểm tra cả theme tối và sáng, bàn phím, mức chữ 24 px và viewport 320/360/390/430 px.
- Ảnh raster được nén WebP phù hợp, mục tiêu dưới 800 KB. Giữ SVG là vector để đọc nét tại mức zoom cao.
- Sơ đồ tổng hợp cuối bài có nhãn trong SVG, alt mô tả quan hệ và bản chữ mở được bằng bàn phím; kiểm tra biên chữ SVG bằng `tools/qa_summary_visuals.py`.

## Nguồn và lưu trữ

- Ảnh ngoài chỉ CC0 hoặc miền công cộng **trên trang tệp cụ thể**. Ghi tác giả, trang tệp, giấy phép, ngày xác minh, xử lý và bài sử dụng trong `assets/images/lessons/SOURCES.md`.
- Không lưu ảnh chỉ vì nó xuất hiện trên Google/YouTube hoặc trên một website có giấy phép mở. Nếu không xác minh được tác quyền hay model, dùng ảnh tự chụp của tác giả hoặc sơ đồ tự vẽ.
- Không gán giấy phép CC0 của ảnh ngoài cho toàn giáo trình. Dự án vẫn giữ bản quyền riêng theo quyết định chủ dự án.

## Kiểm tra trước khi đưa vào bài

1. Đối chiếu hình với nội dung và nguồn kỹ thuật, sau đó cập nhật văn bản nếu hình phơi bày lỗi bài giảng.
2. Chạy `python tools/check_visuals.py --require-all`, `python tools/check_links.py`, `python tools/build_search_index.py --check` sau khi tạo lại chỉ mục từ HTML đã sửa.
3. Chạy `python tools/qa_lesson_visuals.py` và `python tools/qa_summary_visuals.py`; xem thêm hình ở điện thoại và desktop, kiểm tra chữ trong hình, caption, đường dẫn ảnh và không tràn ngang. Ghi kết quả trong tài liệu QA của tuần/Phase.

## Rubric thay 80 khối ASCII — Phase 7

Sổ kiểm hiện hành là `docs/curriculum/diagram-register.csv`; phát biểu cần nguồn là `docs/curriculum/technical-claims.csv`. ID cũ chỉ dùng để truy vết vị trí. Mức ưu tiên trong audit Phase 4 là dữ liệu lịch sử, không phải kết luận lỗi của HTML hiện tại.

| Dạng | Cổng kỹ thuật trước xuất bản | Cổng hiển thị và bản chữ |
| --- | --- | --- |
| Schematic/ký hiệu | Mọi dây nối có nút rõ; ký hiệu chuẩn, cực tính, giá trị, rail nguồn và đường hồi; đối chiếu netlist với lời và datasheet đúng part/package | SVG nét rõ ở 320 px, không phụ thuộc màu; caption mô tả dòng đi và giới hạn mô hình |
| Waveform/timing | Trục có biến/đơn vị, mức 0, biên độ/tần số/chu kỳ có điều kiện; các cạnh và thời điểm nhất quán với lời | Chữ và mốc thời gian đọc được khi phóng to; bản chữ nêu từng pha |
| Breadboard/pinout/vật lý | Tách kết nối a–e/f–j, rãnh và rail; pinout ghi hướng nhìn, part/module và revision; rail thực đo thông mạch | Hình có chú thích chân và mô tả vị trí theo hàng/cột, không chỉ theo màu dây |
| Luồng/hệ thống | Mũi tên phân biệt nguồn, dữ liệu, điều khiển và phản hồi; thứ tự có điều kiện rõ | Nội dung các khối có thể đọc theo văn bản tuyến tính bằng trình đọc màn hình |
| Bảng tra/công thức văn bản | Ưu tiên HTML/table thay ảnh; đơn vị, ký hiệu và phép tính kiểm độc lập | Cho phép chọn chữ, đổi cỡ chữ và tìm kiếm nội dung |

Một sơ đồ chỉ được đánh `verified` sau khi so với đoạn giảng, phép tính hoặc mô phỏng liên quan, nguồn kỹ thuật khi cần, và kiểm ở màn 320 px. Nếu thiếu model/revision, ghi `needs_exact_part` hoặc `needs_exact_module`, dùng ví dụ mô phỏng và không hướng dẫn cắm chân trên phần cứng chưa xác định. Các hình thử nghiệm phải giữ nguồn SVG chỉnh sửa được và bản chữ tương đương.
