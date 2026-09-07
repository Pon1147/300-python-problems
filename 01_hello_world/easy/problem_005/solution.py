"""
Bài 005: Phép toán lũy thừa
Chủ đề: Phép toán cơ bản
Độ khó: Easy
"""
import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def solve():
    a = int(input())
    print(a ** 2)
    print(a ** 5)


def main():
    solve()


if __name__ == "__main__":
    main()
