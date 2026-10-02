# DH-AUDIT — Phase 1 — 2026-10-02

## Tier 1 — Trạng thái DHSYSTEM: PASS

TRACKER, PHASE-STATE, HANDOFF cùng ghi Phase 1 đang audit sau khi P1-01–P1-08 PASS. Các tag checkpoint task có trong Git; tag hoàn tất phase được tạo khi audit/debug khép lại. Không có sai lệch trạng thái cần sửa.

## Tier 2 — Tài liệu: LOW → RESOLVED

`.DHSYSTEM/ARCHITECTURE.md` còn gọi ranh giới module là “dự kiến”, Search UI là “module mới” và Phase 1 như chưa triển khai. `dh-debug` đã đối chiếu với các tệp hiện có và cập nhật câu chữ. README, CHANGELOG, báo cáo QA và bốn sidecar Mermaid khớp triển khai; không có URL placeholder trong tài liệu đã quét.

## Tier 3 — Website tĩnh: PASS trong phạm vi đã thử

`check_links.py` kiểm tra 57 trang/470 tham chiếu, không có file, fragment hoặc đường dẫn thoát thư mục bị hỏng. Chỉ mục tìm kiếm 56 bài còn hiện hành; toàn bộ JS qua `node --check`. Chromium qua toàn bộ 56 bài ở 320 px, các bài đại diện ở viewport 160–430 px và các luồng tương tác. WebKit qua mẫu tương ứng. Xem `docs/qa/phase1-results.md`.

Guardrail cho các phase kế: sau khi sửa bài, chạy lại `build_search_index.py` rồi `--check`; giữ `check_links.py` và `qa_browser.py` xanh; kiểm tra nội dung động bằng `textContent` hoặc DOM an toàn; thử lưu trữ trên HTTP. Điện thoại thật và screen reader thật chưa có trong môi trường kiểm thử.

## Tier 4 — Không áp dụng

Đây là dự án giáo trình, không phải kho nguồn DHSYSTEM.

---

# DH-AUDIT — Phase 2 — 2026-10-02

## Tier 1 — Trạng thái DHSYSTEM: PASS

TRACKER, PHASE-STATE và HANDOFF cùng ghi Phase 2 đã xong P2-01/P2-02, P2-03 quyết định hoãn tính năng và đang audit. Tag Phase 1 đã có; tag Phase 2 được tạo khi audit/debug khép lại.

## Tier 2 — Tài liệu: LOW → RESOLVED

Kiến trúc chưa ghi thư viện dấu xuyên bài, luồng đối chiếu neo và từ đồng nghĩa tìm kiếm. `dh-debug` đã cập nhật `ARCHITECTURE.md` cùng bốn sidecar Mermaid. README, CHANGELOG, báo cáo QA của thư viện và bộ truy vấn tìm kiếm đã có.

## Tier 3 — Website tĩnh: PASS trong phạm vi đã thử

58 trang/479 tham chiếu HTML nội bộ, 0 lỗi. Chỉ mục 56 bài còn mới; JS qua `node --check`. Chromium kiểm tra 56 bài ở 320 px, thư viện dấu ở 320–430 px, tạo dấu từ hai bài, lọc/tìm/xóa/mở, trạng thái mất neo; WebKit kiểm tra mẫu. Bảy truy vấn Anh–Việt trả bài đầu đúng ở Bài 1/28/56. Dấu mất neo không tạo URL nhảy vào vị trí không chắc chắn. Không có thiết bị điện thoại thật trong môi trường thử.

## Tier 4 — Không áp dụng

Đây là dự án giáo trình, không phải kho nguồn DHSYSTEM.
---

# DH-AUDIT — Phase 3 — 2026-10-02

## Tier 1 — Trạng thái DHSYSTEM: PASS

TRACKER, PHASE-STATE và HANDOFF cùng ghi P3-01 PASS, P3-02 quyết định hoãn backend và Phase 3 đang audit. Tag hoàn tất Phase 1/2 có trong Git; Phase 3 được gắn tag sau khi audit/debug khép lại.

## Tier 2 — Tài liệu: LOW → RESOLVED

Kiến trúc chưa ghi trang xuất/nhập, định dạng JSON version 1 và luồng xem trước/xác nhận/khôi phục khi ghi lỗi. `dh-debug` đã cập nhật `ARCHITECTURE.md` và bốn sidecar Mermaid. README, CHANGELOG, báo cáo `docs/qa/import-export.md` và schema đã có. Schema và mã đều giới hạn trường/kiểu/độ dài; mã kiểm tra ID dấu trùng trong khi schema dùng `uniqueItems` cho bản ghi.

## Tier 3 — Website tĩnh: PASS trong phạm vi đã thử

59 trang/487 tham chiếu nội bộ, 0 link hoặc fragment hỏng. Chỉ mục tìm kiếm 56 bài còn mới; toàn bộ JavaScript qua `node --check`. Chromium kiểm tra 56 bài ở 320 px và các luồng đọc, thư viện, sao lưu; WebKit kiểm tra mẫu. Xuất→nhập khôi phục dấu/cỡ chữ/theme/tiến độ/checklist. JSON hỏng, thiếu trường, version cũ, ngày sai, quote quá dài đều bị từ chối trước ghi; xung đột ID được báo; lỗi ghi mô phỏng đã rollback dữ liệu cũ. Rà mã thấy `Date.parse` tự chuẩn hóa ngày không tồn tại (ví dụ 31/02); `dh-debug` đã thêm kiểm tra ngày theo lịch và ca hồi quy. Chưa thử trên điện thoại thật.

## Tier 4 — Không áp dụng

Đây là dự án giáo trình, không phải kho nguồn DHSYSTEM.
