# Lược đồ dữ liệu cục bộ

Website không có database, Kafka hoặc API tự xây trong phạm vi hiện tại. Vì vậy không tạo `database-schema.sql`, `kafka-topics.yaml` hay `api-contracts.yaml` giả.

- `reader-preferences.schema.json`: cỡ chữ lưu trên thiết bị.
- `highlight-record.schema.json`: dấu đánh dấu gắn với bài và đoạn trích.
- `search-index.schema.json`: chỉ mục tĩnh tạo từ 56 bài.

Các schema là hợp đồng cho bước triển khai; mã đọc dữ liệu cần kiểm tra phiên bản và xử lý dữ liệu cũ/sai một cách an toàn.
