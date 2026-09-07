"""
Bài 006: Căn bậc 2
Chủ đề: Phép toán cơ bản
Độ khó: Easy
"""
import sys
import math

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def solve():
    a = float(input())
    print(f"{math.sqrt(a):.2f}")


def main():
    solve()


if __name__ == "__main__":
    main()
