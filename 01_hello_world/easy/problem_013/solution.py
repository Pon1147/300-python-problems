"""
Bài 013: Tính tổng chữ số
Chủ đề: Phép toán cơ bản
Độ khó: Easy
"""

import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def solve():
    a = int(input())

    total = 0
    for _ in range(4):
        total += a % 10
        a //= 10
    print(total)


def main():
    solve()


if __name__ == "__main__":
    main()
