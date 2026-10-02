# Hiện trạng trước Phase 1 — 02/10/2026

## Phạm vi và cách đo

- Kho hiện có `index.html` và đúng 56 bài: `week1/day01.html` đến `week8/day56.html`, 7 bài mỗi tuần.
- Chạy `python tools/check_links.py` từ thư mục dự án. Script đọc `href`/`src` của 57 trang, chuẩn hóa đường dẫn nội bộ và kiểm tra tệp đích; URL ngoài và fragment đơn được bỏ qua. Script chỉ kiểm tra sự tồn tại của tệp, chưa kiểm tra ID fragment hoặc link tạo động bằng JavaScript.
- Phục vụ các trang bằng HTTP tại `127.0.0.1` và đo `document.documentElement.clientWidth`/`scrollWidth` sau khi tải xong bằng Playwright Chromium 148, viewport cao 800 CSS px. Đây là phép đo viewport trong trình duyệt desktop, chưa phải kiểm thử iOS Safari hoặc Android Chrome trên thiết bị thật.

## Liên kết nội bộ

Script thấy **479 tham chiếu nội bộ**, **73 tham chiếu hỏng**, quy về **4 tệp đích thiếu**:

| Đích thiếu | Số tham chiếu | Ví dụ nguồn |
| --- | ---: | --- |
| `front/components.html` | 60 | `index.html:300`; thanh đầu trang của 56 bài |
| `appendix/glossary.html` | 6 | `index.html:301`; `week1/day01.html:30` |
| `front/guide.html` | 5 | `index.html:299` |
| `front/preface.html` | 2 | `index.html:298` |

Lệnh hiện trả **exit code 1**. Các đích trên là đường dẫn đã chuẩn hóa; một đích có thể được ghi bằng đường dẫn tương đối khác nhau ở trang chủ và trang bài. P1-08 sẽ thay các link này bằng đích thật hoặc bỏ đi sau khi đối chiếu nội dung.

## Tràn ngang tại bốn viewport

Giá trị ô là `scrollWidth` của toàn trang, đơn vị CSS px. Số trong ngoặc là phần vượt quá viewport; dấu `0` nghĩa là không có cuộn ngang toàn trang.

| Trang | 320 | 360 | 390 | 430 |
| --- | ---: | ---: | ---: | ---: |
| Trang đầu `index.html` | 320 (0) | 360 (0) | 390 (0) | 430 (0) |
| Bài 1 `week1/day01.html` | 714 (+394) | 714 (+354) | 714 (+324) | 714 (+284) |
| Bài 28 `week4/day28.html` | 494 (+174) | 494 (+134) | 494 (+104) | 494 (+64) |
| Bài 56 `week8/day56.html` | 495 (+175) | 495 (+135) | 495 (+105) | 495 (+65) |

Trang đầu không cuộn ngang theo phép đo trên, nhưng **menu đầu trang vẫn vượt mép phải**: tại 320 px, cạnh phải `<nav>` là khoảng 440 px; tại 430 px vẫn là 440 px. Vì header `position: fixed`, các link ngoài viewport không làm tăng `scrollWidth` của tài liệu. Đây là lỗi điều hướng mobile dù chỉ số cuộn toàn trang bằng 0.

Ở cả ba bài mẫu, `.main-content` là flex item có `min-width: auto`, nở theo nội dung rộng thay vì co theo viewport. Ở 320 px, chiều rộng `<main>` lần lượt khoảng 714/494/495 px. `.a11y-toolbar` trong header cũng vươn tới khoảng 472 px. P1-03 cần giữ bảng/sơ đồ cuộn trong khung riêng và cho vùng bài co đúng kích thước; P1-02 cần menu trang đầu dùng được trên màn hình hẹp.

## Khối nội dung đại diện cần giữ đọc được

| Trang | Khối có trong HTML | Rủi ro khi thu hẹp |
| --- | --- | --- |
| Trang đầu | ảnh bìa, lưới 8 tuần, header nhiều link | menu vượt mép; các nút/lưới cần xếp lại |
| Bài 1 | 8 bảng, 5 khối `.circuit-ascii` | bảng và sơ đồ dài đẩy vùng bài rộng; kiểm tra cuộn riêng |
| Bài 28 | 3 bảng, 1 `pre`, 1 khối `.circuit-ascii` | code/sơ đồ và bảng dài |
| Bài 56 | 2 bảng | bảng và khối tổng kết dài |

Các số đếm là thẻ/khối trong HTML, gồm cả nội dung có thể được ẩn mặc định. Nghiệm thu sau khi sửa cần kiểm tra thêm zoom 200%, thao tác menu bằng bàn phím và trình duyệt điện thoại thật theo hợp đồng P1-02/P1-03.

## Kiểm tra script bằng fixture riêng

Tạo thư mục tạm với 56 bài rỗng và trang đầu chứa link hợp lệ, URL ngoài, fragment đơn, query string và `missing%20file.html`. Script báo đúng một đích thiếu và exit code 1. Sau khi thêm tệp đích vào fixture, script exit code 0. Không chỉnh sửa bài thật để thử.
