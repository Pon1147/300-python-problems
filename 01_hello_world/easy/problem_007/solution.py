"""
Bài 007: Nghịch đảo
Chủ đề: Phép toán cơ bản
Độ khó: Easy
"""
import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def solve():
    a = float(input())
    print(f"{1 / a:.5f}")


def main():
    solve()


if __name__ == "__main__":
    main()
