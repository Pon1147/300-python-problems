"""
Bài 012: Tìm chữ số
Chủ đề: Phép toán cơ bản
Độ khó: Easy
"""

import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def solve():
    a = int(input())
    units = a % 10  # hàng đơn vị
    tens = a // 10  # hàng chục
    print(f"{units} {tens}")


def main():
    solve()


if __name__ == "__main__":
    main()
