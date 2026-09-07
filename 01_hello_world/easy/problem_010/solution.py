"""
Bài 010: Phép chia lấy phần nguyên và lấy phần dư
Chủ đề: Phép toán cơ bản
Độ khó: Easy
"""
import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def solve():
    a, b = map(int, input().split())
    P = a // b
    Q = a % b
    print(f"{P} {Q}")


def main():
    solve()


if __name__ == "__main__":
    main()
