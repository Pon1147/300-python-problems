# Hướng dẫn đóng góp bài tập

## Cấu trúc 1 bài tập

Mỗi bài tập nằm trong thư mục:

```
{topic_number}_{topic_name}/{difficulty}/problem_XXX/
├── README.md          # Mô tả bài tập
├── solution.py        # Lời giải mẫu
└── test_solution.py   # Test cases
```

## Viết README.md

```markdown
# Bài XXX: [Tên bài]

## Mô tả

[Mô tả ngắn gọn bài tập bằng tiếng Việt]

## Yêu cầu

1. [Yêu cầu 1]
2. [Yêu cầu 2]

## Ví dụ

**Input:**
```

4

```

**Output:**
```

1 2 3 4

```

## Gợi ý
- [Gợi ý nhỏ, không cho đáp án]

## Kiến thức cần biết
- [Kiến thức liên quan]
```

## Viết solution.py

```python
"""Lời giải cho Bài XXX: [Tên bài]"""


def solve():
    """Hàm giải chính"""
    # Code của bạn ở đây
    pass


if __name__ == "__main__":
    solve()
```

## Viết test_solution.py

```python
"""Test cases cho Bài XXX: [Tên bài]"""
import pytest
from solution import solve


def test_example_1():
    """Test với ví dụ 1"""
    # Sử dụng monkeypatch để giả lập input
    ...


def test_example_2():
    """Test với ví dụ 2"""
    ...


def test_edge_case():
    """Test trường hợp đặc biệt"""
    ...
```

## Kiểm tra trước khi commit

```bash
# Chạy test cho bài mới
python -m pytest 04_conditions/easy/problem_010/test_solution.py -v

# Chạy tất cả test
python -m pytest tests/ -v
```

## Gửi đóng góp

1. Fork repository
2. Tạo branch mới (`git checkout -b feature/bai-123`)
3. Commit thay đổi (`git commit -m 'Add: Bài 123 - Tên bài'`)
4. Push lên (`git push origin feature/bai-123`)
5. Tạo Pull Request
