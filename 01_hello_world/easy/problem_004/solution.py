"""
Bài 004: Phép toán chia
Chủ đề: Phép toán cơ bản
Độ khó: Easy
"""
import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def solve():
    a = int(input())
    print(f"{a / 3:.2f}")


def main():
    solve()


if __name__ == "__main__":
    main()
