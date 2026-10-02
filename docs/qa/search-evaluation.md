# P2-02 — Đánh giá tìm kiếm nội bộ

## Bộ truy vấn nghiệm thu

Chạy qua `EbookSearch.search()` trên Bài 1, 28 và 56 bằng `tools/qa_browser.py`. Kết quả đầu phải có tiêu đề, đề mục và đoạn trích; URL dẫn tới tệp bài thật.

| Truy vấn | Kiểu | Bài đầu kỳ vọng | Kết quả |
| --- | --- | --- | --- |
| `điện áp` | Tiếng Việt có dấu | Bài 1 | PASS |
| `dien ap` | Tiếng Việt không dấu | Bài 1 | PASS |
| `voltage` | Thuật ngữ Anh | Bài 1 | PASS |
| `resistor` | Thuật ngữ Anh | Bài 3 | PASS |
| `capacitor` | Thuật ngữ Anh | Bài 8 | PASS |
| `sensor` | Thuật ngữ Anh | Bài 27 | PASS |
| `pcb` | Thuật ngữ viết tắt | Bài 33 | PASS |

Từ đồng nghĩa được biên tập trong `assets/js/search.js` dựa trên thuật ngữ có sẵn trong giáo trình: điện áp/voltage/volt, dòng điện/current/ampere, điện trở/resistor/resistance, tụ điện/capacitor/capacitance, vi điều khiển/microcontroller/MCU, mạch in/PCB và cảm biến/sensor. Truy vấn không có kết quả trả danh sách rỗng và giao diện đưa gợi ý rút ngắn. Kết quả tối đa 8 bài, ưu tiên tiêu đề rồi đề mục và nội dung; đoạn trích được cắt theo vị trí sau khi chuẩn hóa dấu tiếng Việt.

`python tools/build_search_index.py --check` và `python tools/check_links.py` đạt. Chromium qua bộ truy vấn ở ba bài; WebKit kiểm tra luồng tìm và mở kết quả. Giới hạn: bộ truy vấn là mẫu biên tập, chưa đo độ chính xác trên toàn bộ truy vấn tự do của người đọc.
