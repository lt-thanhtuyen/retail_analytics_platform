# Báo cáo phân tích chất lượng dữ liệu — Ngày 4

## 1. Tổng quan dữ liệu

- Tổng số dòng: 1.067.371.
- Tổng số cột: 8.
- Số dòng trùng sau lần xuất hiện đầu tiên: 34.335.
- Khoảng thời gian giao dịch: từ 01/12/2009 07:45 đến 09/12/2011 12:50.
- Số ngày không chuyển đổi được: 0.

## 2. Giá trị thiếu

| Cột | Số giá trị thiếu | Tỷ lệ |
|---|---:|---:|
| Description | 4.382 | 0,41% |
| Customer ID | 243.007 | 22,77% |

Các cột còn lại không có giá trị thiếu trong lần kiểm tra này.

Customer ID bị thiếu không tự động làm giao dịch mất tính hợp lệ. Những dòng này vẫn có thể đóng góp vào doanh thu nếu đáp ứng các quy tắc nghiệp vụ khác, nhưng không được tính là khách hàng duy nhất.

## 3. Các trường hợp bất thường

| Trường hợp | Số dòng |
|---|---:|
| Hóa đơn hủy | 19.494 |
| Quantity âm | 22.950 |
| Price bằng 0 | 6.202 |
| Price âm | 5 |

Các nhóm có thể giao nhau, vì vậy không cộng trực tiếp các số liệu trên để suy ra tổng số dòng bất thường duy nhất.

## 4. Kết quả kiểm tra giao nhau

- Hóa đơn hủy và Quantity âm: 19.493 dòng.
- Hóa đơn hủy và Price bằng 0: 0 dòng.
- Hóa đơn hủy và Price âm: 0 dòng.
- Quantity âm và Price không dương: 3.457 dòng.

19.493 trong số 19.494 dòng thuộc hóa đơn hủy cũng có Quantity âm. Đây là mối liên hệ mạnh trong dữ liệu hiện tại, nhưng hai điều kiện vẫn được theo dõi riêng.

## 5. Phạm vi giá trị số

| Cột | Nhỏ nhất | Trung vị | Lớn nhất |
|---|---:|---:|---:|
| Quantity | -80.995 | 3 | 80.995 |
| Price | -53.594,36 | 2,10 | 38.970,00 |

Các giá trị cực trị cần được điều tra trước khi chốt công thức KPI. Chỉ từ thống kê tổng quan, chưa thể kết luận chúng đều là lỗi dữ liệu.

## 6. Quyết định nghiệp vụ liên quan

- Giữ hóa đơn hủy để phân tích riêng và loại khỏi các KPI bán hàng thông thường.
- Phân tích Quantity âm riêng; không mặc định tất cả đều là hàng trả lại.
- Giữ Price không dương để điều tra nhưng loại khỏi doanh thu bán hàng thông thường.
- Không loại giao dịch chỉ vì thiếu Customer ID.
- Đánh dấu và điều tra bản ghi trùng trước khi quyết định loại bỏ.

## 7. Công việc tiếp theo

1. Kiểm tra các giá trị cực trị của Quantity và Price.
2. Xác định tiêu chí xử lý bản ghi trùng chính xác.
3. Hoàn thiện định nghĩa KPI và các điều kiện lọc.
4. Chuẩn bị thiết kế schema MySQL sau khi các quy tắc được xác minh.

