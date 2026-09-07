# 🐣 300 Bài Code Thiếu Nhi

Bộ sưu tập 300 bài tập Python dành cho trẻ em, được thiết kế để học lập trình một cách vui vẻ và hiệu quả.

## 📚 Cấu trúc bài học

Bài học được chia thành **20 chủ đề**, mỗi chủ đề có **3 cấp độ**:

| Cấp độ    | Số bài   | Phù hợp với             |
| --------- | -------- | ----------------------- |
| 🟢 Easy   | ~150 bài | Người mới bắt đầu       |
| 🟡 Medium | ~100 bài | Đã có kiến thức cơ bản  |
| 🔴 Hard   | ~50 bài  | Muốn thử thách bản thân |

## 🗂️ Danh sách chủ đề

| #   | Chủ đề                       | Easy    | Medium | Hard   | Tổng    |
| --- | ---------------------------- | ------- | ------ | ------ | ------- |
| 01  | Hello World & In ra màn hình | 8       | 5      | 3      | 16      |
| 02  | Biến & Kiểu dữ liệu          | 8       | 5      | 3      | 16      |
| 03  | Nhập/xuất (Input/Output)     | 8       | 5      | 3      | 16      |
| 04  | Điều kiện (if/elif/else)     | 13      | 8      | 4      | 23      |
| 05  | Vòng lặp (for/while)         | 13      | 8      | 4      | 23      |
| 06  | Hàm (Functions)              | 9       | 5      | 3      | 17      |
| 07  | Danh sách (Lists)            | 9       | 5      | 3      | 17      |
| 08  | Chuỗi (Strings)              | 9       | 5      | 3      | 17      |
| 09  | Từ điển (Dictionaries)       | 8       | 4      | 3      | 15      |
| 10  | Trò chơi toán học            | 9       | 5      | 3      | 17      |
| 11  | Vòng lặp lồng nhau           | 7       | 4      | 3      | 14      |
| 12  | Thao tác file                | 6       | 3      | 3      | 12      |
| 13  | Phân tích văn bản            | 6       | 3      | 3      | 12      |
| 14  | Vẽ hình với Turtle           | 9       | 4      | 3      | 15      |
| 15  | Mảng 2 chiều                 | 6       | 3      | 3      | 11      |
| 16  | Sắp xếp                      | 4       | 3      | 3      | 10      |
| 17  | Đệ quy (Recursion)           | 4       | 3      | 3      | 10      |
| 18  | Lập trình hướng đối tượng    | 4       | 3      | 3      | 10      |
| 19  | Xử lý lỗi                    | 4       | 3      | 2      | 9       |
| 20  | Dự án & Trò chơi             | 7       | 4      | 3      | 13      |
|     | **Tổng cộng**                | **151** | **97** | **52** | **300** |

## 🚀 Bắt đầu

### Yêu cầu

- Python 3.10+
- pip (package manager)

### Cài đặt

```bash
# Clone repository
git clone <your-repo-url>
cd 300-python-problems

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy bài tập đầu tiên
python 01_hello_world/easy/problem_001/solution.py

# Chạy test cho tất cả bài
python -m pytest tests/
```

## 📖 Cách sử dụng

Mỗi bài tập có cấu trúc:

```bash
04_conditions/easy/problem_010/
├── README.md          # Mô tả bài tập
├── solution.py        # Lời giải mẫu
└── test_solution.py   # Test cases
```

**Quy trình học:**

1. Đọc `README.md` để hiểu yêu cầu
2. Tự viết code vào `solution.py`
3. Chạy `python -m pytest test_solution.py` để kiểm tra
4. So sánh với `solution.py` nếu cần

## 🎯 Lộ trình học gợi ý

### Giai đoạn 1: Người mới (Bài 1-50)

`01_hello_world` → `02_variables_types` → `03_input_output` → `04_conditions` (easy)

### Giai đoạn 2: Cơ bản (Bài 51-150)

`04_conditions` → `05_loops` → `06_functions` → `07_lists` → `08_strings` (easy+medium)

### Giai đoạn 3: Nâng cao (Bài 151-250)

`09_dictionaries` → `10_math_games` → `14_turtle_graphics` → các bài medium/hard

### Giai đoạn 4: Thành thạo (Bài 251-300)

`15_2d_arrays` → `16_sorting` → `17_recursion` → `18_oop_basics` → `20_games_projects`

## 🏷️ Quy ước đặt tên file

- `solution.py` - Lời giải mẫu
- `test_solution.py` - Test cases (dùng pytest)
- `README.md` - Mô tả bài tập (tiếng Việt)
- `input.txt` / `output.txt` - Dữ liệu đầu vào/ra (nếu có)

## 📝 Thử nghiệm

```bash
# Chạy test cho 1 bài
python -m pytest 04_conditions/easy/problem_010/test_solution.py -v

# Chạy test cho toàn bộ chủ đề
python -m pytest 05_loops/ -v

# Chạy test cho tất cả
python -m pytest tests/ -v
```

## 🤝 Đóng góp

Mỗi bài mới cần có:

1. `README.md` - Mô tả bằng tiếng Việt, ví dụ minh họa
2. `solution.py` - Lời giải đúng
3. `test_solution.py` - Ít nhất 3 test cases

Xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết chi tiết.

## 📄 License

MIT
