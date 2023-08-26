# Data Preprocessing Pipeline
- Cài đặt các thư viện trong requirements.txt sử dụng python 3.7

Các bước trong quy trình tiền xử lý trên bất kỳ tập dữ liệu cụ thể nào, gồm có 5 bước chính:

1. Quy trình bắt đầu bằng việc xác định các đặc trưng số và đặc trưng phân loại trong tập dữ liệu.
2. Tiếp theo, quy trình xử lý các giá trị thiếu có mặt trong các đặc trưng số. Nó điền vào các giá trị thiếu này bằng giá trị trung bình của mỗi đặc trưng số tương ứng (bạn có thể điều chỉnh bước này theo cách bạn muốn điền vào các giá trị thiếu của một đặc trưng số). Điều này đảm bảo rằng dữ liệu thiếu không gây trở ngại cho phân tích và tính toán tiếp theo.
3. Quy trình sau đó xác định và xử lý các giá trị ngoại lệ trong các đặc trưng số bằng phương pháp Khoảng giữa (Interquartile Range - IQR). Tính toán các phân vị và khoảng giữa xác định ranh giới trên và ranh giới dưới cho các giá trị ngoại lệ. Bất kỳ giá trị nào nằm ngoài các ranh giới này sẽ được thay thế bằng giá trị trung bình của đặc trưng số tương ứng. Bước này giúp ngăn chặn ảnh hưởng của các giá trị cực đại đối với các phân tích và xây dựng mô hình tiếp theo.
4. Sau khi xử lý các giá trị thiếu và ngoại lệ, quy trình chuẩn hóa các đặc trưng số. Quá trình này đảm bảo rằng tất cả các đặc trưng số đóng góp một cách bình đẳng cho phân tích tiếp theo, tránh các sai lệch do các độ lớn khác nhau.
5. Quy trình tiếp tục xử lý các giá trị thiếu trong các đặc trưng phân loại. Nó điền vào các giá trị thiếu này bằng giá trị mode, đại diện cho danh mục xuất hiện phổ biến nhất.

Bằng cách tuân theo quy trình này, các chuyên gia dữ liệu có thể tự động hóa và hợp lý hóa quy trình chuẩn bị dữ liệu để phân tích, đảm bảo chất lượng, độ tin cậy và tính nhất quán của dữ liệu.
