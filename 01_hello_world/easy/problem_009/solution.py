"""
Bài 009: Tính giá trị biểu thức 2
Chủ đề: Phép toán cơ bản
Độ khó: Easy
"""
import sys
import math

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def solve():
    a, b, c = map(int, input().split())

    P = (21 * a**2 + 5 * b**2) / (2009 * c**2 + 15)
    Q = math.sqrt(a**2 - 2 * b) / (3 * c**2 + 4)

    print(f"{P:.4f} {Q:.4f}")


def main():
    solve()


if __name__ == "__main__":
    main()
