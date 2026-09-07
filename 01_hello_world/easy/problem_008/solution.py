"""
Bài 008: Tính giá trị biểu thức 1
Chủ đề: Phép toán cơ bản
Độ khó: Easy
"""
import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def solve():
    a = int(input())
    b = int(input())

    P = 21 * a + 5 * b - 2009
    Q = (21 * a**2 - 5 * b) / (2009 * b**2)
    R = (21 * a + 5 * b**2) / (2009 * b + 15)

    print(f"{P} {Q:.4f}")
    print(f"{R:.6f}")


def main():
    solve()


if __name__ == "__main__":
    main()
