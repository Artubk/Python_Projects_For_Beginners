# Python_Projects_For_Beginners
Python Projects For Beginners. It have 56 projects for beginners

#-----------------------------------------------------------------------------#

Project 1: Number Guessing Game
- Dự đoán số được chọn ngẫu nhiên trong khoảng (a, b)

#-----------------------------------------------------------------------------#

Project 2: Caculate Mean, Median and Mode
- Tính giá trị trung bình, trung vị
- Mode: dùng set để tìm ra số xuất hiện nhiều nhất trong một List

#-----------------------------------------------------------------------------#

Project 3: Password Authentication System (He thong xac thuc mat khau)
- Database: luu tru username va password
- Su dung thu vien getpass de nhap mat khau thay vi dung input()
- Thu vien getpass se khong lam lo mat khau khi nhap vao
- Ngoai ra co the dung thu vien pwinput de hien thi mat khau dang "*******"

Run in Pycharm by Terminal:

python Python_for_Beginner_96_Projects.py

#-----------------------------------------------------------------------------#

Project 4: Send Automatic Emails
- Đầu tiên cần lấy mật khẩu ứng dụng bằng cách truy cập vào: myaccount.google.com >> Bảo mật >> Xác minh 2 bước >> Mật khẩu ứng dụng >> Chọn mục Thư và Máy tính dùng window
- User: nhập tên người muốn được gửi thư
- Email: nhập email người muốn được gửi thư
- Your Gmail Account: nhập email của bạn
- Your App Password: nhập app password vừa lấy được

#-----------------------------------------------------------------------------#

Project 5: Age Calculator
- Tính tuổi dựa trên ngày sinh bạn nhập vào và ngày hiện tại trên máy tính
- Tuổi được tính theo công thức: Age = Days / 365.25

#-----------------------------------------------------------------------------#

Project 6: Group Anagrams
- Cho một chuỗi các từ
- Trả về kết quả các từ được ghép lại từ các chữ giống nhau

#-----------------------------------------------------------------------------#

Project 7: Find Missing Number
- Khởi tạo một List number từ 1 đến n, trong List này sẽ thiếu một vài số
- Trả về kết quả những số bị thiếu trong List

#-----------------------------------------------------------------------------#

Project 8: Group Elements of Same Indices
- Khởi tạo một List, VD: inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
- Trả về kết quả một List_new với các phần tử có cùng chỉ số là một nhóm. VD: outputLists = [10, 40, 70] [20, 50, 80] [30, 60, 90]

#-----------------------------------------------------------------------------#

Project 9: Calculate Execution Time of a Python Program (Tính thời gian chạy một chương trình)
- Sử dụng thư viện time để tính thời gian chạy chương trình
- Thời gian chạy chương trình trên môi trường khác nhau là khác nhau
- Để đo lường thời gian chính xác nên sử dụng các công cụ đo lường thời gian chuyên dụng hoặc thử chạy mã nhiều lần và tính trung bình thời gian thực thi.

#-----------------------------------------------------------------------------#

Project 10: Count Number of Words in a Column
- Dùng thư viện pandas để thao tác với dữ liệu dạng bảng
- Câu lệnh .head() để in ra 5 dòng đầu tiên của dữ liệu

#-----------------------------------------------------------------------------#

Project 11: Rock Paper Scissors Game (đá, giấy, kéo)
- Người chơi 1 sẽ ra kéo, búa, bao trước
- Người chơi 2 là máy sẽ dùng hàm ramdom để ra ngẫu nhiên kéo, búa, bao

#-----------------------------------------------------------------------------#

Project 12: Print Emojis
- Dùng thư viện "pip install emoji" để in biểu tượng cảm xúc
- Biểu tượng cảm xúc sẽ được ghi trong ký tự "::". Ví dụ: 📚 (:books:)

#-----------------------------------------------------------------------------#

Project 13: Correct Spellings (sửa lỗi chính tả)
- Dùng thư viện "pip install pyspellchecker"
- Nhập vào từ bàn phím từ tiếng Anh cần sửa lỗi chính tả
- Trả về Correct hoặc từ sau khi đã sửa lỗi chính tả

#-----------------------------------------------------------------------------#

Project 14: Scraping GitHub Profile (lấy avatar trong github)
- Dùng thư viện "pip install beautifulsoup4", "pip install requests"

#-----------------------------------------------------------------------------#

Project 15: Visualizing Linear Relationships
- Visualization data là biểu diễn data trên biểu đồ, giúp trực quan hóa dữ liệu
- Thư viện dùng là: matplotlib, seaborn

#-----------------------------------------------------------------------------#

Project 16: Generate Text
- Tự động tạo ra văn bản dựa vào pipeline có sẵn
- pip install transformers
- do_sample=True: Tham số này cho phép mô hình tạo ra đầu ra dựa trên phân phối xác suất của các từ, thay vì chỉ chọn từ có xác suất cao nhất.
- top_k=50: Tham số này chỉ định rằng chỉ có các từ có xác suất cao nhất trong top 50 sẽ được xem xét khi mô hình tạo ra câu mới. Điều này giúp đảm bảo tính đa dạng trong đầu ra.
- temperature=0.9: Tham số này điều chỉnh mức độ sáng tạo của đầu ra. Giá trị càng cao sẽ tạo ra đầu ra ngẫu nhiên hơn, trong khi giá trị càng thấp sẽ tạo ra đầu ra gần với các từ có xác suất cao nhất.
- max_length=100: Tham số này giới hạn độ dài tối đa của câu mới tạo ra. Trong trường hợp này, câu mới không vượt quá 100 từ.
- num_return_sentences=2: Tham số này chỉ định số lượng câu mới mà mô hình sẽ tạo ra.

#-----------------------------------------------------------------------------#

Project 17: Scrape Table from a Website
- Cài đặt thư viện: pandas, lmxl
- Để save data dùng câu lệnh sau:
data.to_csv("programming.csv")

#-----------------------------------------------------------------------------#

Project 18: Extract Text From PDF
- Trích xuất văn bản từ PDF, thường được dùng trong các file CV.pdf
- Cài đặt thư viện: pip install pypdf2

#-----------------------------------------------------------------------------#

Project 19: Reverse a String
- Nhập vào từ bàn phím một string
- Kết quả trả về một Reverse string

#-----------------------------------------------------------------------------#

Project 20: SequenceMatcher
- Nhập vào hai Sequence
- Kết quả trả về mức độ matcher của 2 sequence

#-----------------------------------------------------------------------------#

Project 21: QR Code
- Tạo mã QR Code từ link cho trước
pip install PyQRCode
pip install pypng

#-----------------------------------------------------------------------------#

Project 22: Decode a QR Code
- Lấy link từ QR Code cho trước
pip install pyzbar
pip install pillow

#-----------------------------------------------------------------------------#

Project 23: Create Dummy Data (tạo data giả)
pip install faker
pip install pandas

#-----------------------------------------------------------------------------#

Project 24: Remove Cuss Words
- Thay thế Cuss words bằng ký tự ****
pip install better_profanity

#-----------------------------------------------------------------------------#

Project 25: Find Duplicate Values
- Tạo vòng lặp duyệt qua hết values
- Vòng lập 2 duyệt từ (value+1) để tìm values trùng nhau và đẩy chúng vào duplicates

#-----------------------------------------------------------------------------#

Project 26: Detect Questions
import nltk
nltk.dowload()
- Cài đặt package "punkt"
- Đoạn code trả về kết quả câu đó có phải câu hỏi không dựa vào question_words đã được thêm sẵn

#-----------------------------------------------------------------------------#

Project 27: Voice Recorder
- Để ghi âm ta cài thư viện:
pip install sounddevice
- Để lưu file ghi âm về định dạng tệp cụ thể:
pip install SciPy

#-----------------------------------------------------------------------------#

Project 28: Reading and Writing CSV Files
- Sử dụng thư viện pandas để đọc và ghi file .csv

#-----------------------------------------------------------------------------#

Project 29: Box Plot
- Sử dụng thư viện pandas và plotly.express
- Biểu đồ hộp thể hiện: 75%, 50%, 25%, max, min, median

#-----------------------------------------------------------------------------#

Project 30: Send Instagram Messages
pip install instabot

#-----------------------------------------------------------------------------#

Project 31: LCM(Least Common Multiple)
- Trả về bộ số nhỏ nhất của 2 hay nhiều số

#-----------------------------------------------------------------------------#

Project 32: Price Elasticity of Demand
- Tính sự thay đổi lượng cầu khi giá thay đổi
- Dựa vào công thức sau:
Percentage Change in Quantity Demanded / Percentage Change in the Price

#-----------------------------------------------------------------------------#

Project 33: Find the Most Frequent Words in a File
- Trả về kết quả là các từ được dùng nhiều nhất trong file

#-----------------------------------------------------------------------------#

Project 34: Find the Number of Capital Letters in a File
- Tìm số lượng chữ in hoa trong file
- Dùng .isupper(), ngoài ra có thể tìm chữ in thường bằng .islower()
- 
#-----------------------------------------------------------------------------#

Project 35: Index of Maximum Value in a Python List
- Trả về index của giá trị lớn nhất trong 1 list

#-----------------------------------------------------------------------------#

Project 36: Index of Minimum Value in a Python List
- Trả về index của giá trị nhỏ nhất trong 1 list

#-----------------------------------------------------------------------------#

Project 37: Animated Scatter Plot
- Sử dụng data do chính thư viện plotly cung cấp
- GDP bình quân đầu người trên từng quốc giá
- Trục x là GDP, trục y là tuổi thọ
- Sử dụng thư viện plotly.express

#-----------------------------------------------------------------------------#

Project 38: Create Font Art
- Tạo font chữ
pip install pyfiglet

#-----------------------------------------------------------------------------#

Project 39: Collage Maker
- Ghép 2 images lại
- Chuyển 2 images thành 2 array rồi vstack, sau đó hiển thị

#-----------------------------------------------------------------------------#

Project 40: Phone Number Details
pip install phonenumbers
- Từ 1 số điện thoại, hiển thị:
timezone.time_zones_for_number(number): Múi giờ
carrier.name_for_number(number, "en"): Tên nhà mạng
geocoder.description_for_number(number, "en"): Mô tả địa lý của quốc gia

#-----------------------------------------------------------------------------#

Project 41: Print a Calendar
- In lịch, sử dụng thư viện calendar

#-----------------------------------------------------------------------------#

Project 42: Internet Speed Test
pip install speedtest-cli
- Test tốc độ mạng download và upload

#-----------------------------------------------------------------------------#

Project 43: Text to Handwriting
pip install pywhatkit
pip install opencv-python==4.5.5.64
- Tạo chữ viết tay từ Text

#-----------------------------------------------------------------------------#

Project 44: Shutdown Computer
- Sử dụng thư viện os để truy cập hệ thống
- Có thể tắt máy tính, restart, đặt lời nhắc trước khi tắt máy, cài đặt thời gian tắt máy

#-----------------------------------------------------------------------------#

Project 45: Defang IP Address
- Mã hóa địa chỉ IP bằng việc thay dấu "." bằng "[.]"
- Việc tạo một Defang IP giúp địa chỉ IP khó nhận dạng hơn khi IP được chia sẻ công khai

#-----------------------------------------------------------------------------#

Project 46: Count Character Occurrences
- Đếm ký tự

#-----------------------------------------------------------------------------#

Project 47: Pyramid Pattern
- Tạo mô hình kim tự tháp

#-----------------------------------------------------------------------------#

Project 48: Plotting Annotations
- Thêm chú thích vào hình vẽ

#-----------------------------------------------------------------------------#

Project 49: Create Acronyms
- Tạo từ viết tắt bằng cách tìm những chữ cái viết hoa sau khoảng trắng

#-----------------------------------------------------------------------------#

Project 50: Alarm Clock
- Cài đặt giờ theo cấu truc: HH:MM:SS AM or HH:MM:SS PM

pip install playsound
web dowload free Alarm Clock: https://notification-sounds.com/alarm-clock-sound-download/

#-----------------------------------------------------------------------------#

Project 51: Email Slicer
- Từ your email trích xuất ra thông tin your user name và your domain

#-----------------------------------------------------------------------------#

Project 52: Generate Password
- Tự động tạo mật khẩu ngẫu nhiên theo độ dài của password

#-----------------------------------------------------------------------------#

Project 53. Create a Quiz Game
- Tạo một game với những câu hỏi đã được chuẩn bị sẵn đáp án
- Người chơi sẽ trả lời câu hỏi và sẽ được trả lời sai 3 lần

#-----------------------------------------------------------------------------#

Project 54. Print Colored Text
- In ra màn hình màu nền và màu chữ

#-----------------------------------------------------------------------------#

Project 55. BMI Calculator
- Tính chỉ số sức khỏe BMI = Weight/(Height*Height)

#-----------------------------------------------------------------------------#

Project 56: Treemap
- Vẽ Treemap bằng grapth_objects

#-----------------------------------------------------------------------------#
