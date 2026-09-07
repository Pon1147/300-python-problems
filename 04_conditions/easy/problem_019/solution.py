"""
Bài 019: Kiểm tra số dương hay âm
Chủ đề: Điều kiện (if/elif/else)
Độ khó: Easy
"""
import sys

# Xử lý encoding tiếng Việt trên Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def check_number(n):
    """Kiểm tra số là dương, âm hay bằng 0.

    Args:
        n: Số nguyên cần kiểm tra

    Returns:
        str: 'So duong', 'So am', hoặc 'So 0'
    """
    if n > 0:
        return "So duong"
    elif n < 0:
        return "So am"
    else:
        return "So 0"


def solve():
    """Nhận input và in kết quả."""
    n = int(input())
    print(check_number(n))


def main():
    """Hàm main."""
    print("=== Bài 019: Kiểm tra so duong hay am ===")
    solve()


if __name__ == "__main__":
    main()
