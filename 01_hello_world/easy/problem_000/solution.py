"""
Bài 000: A + B - C
Chủ đề: Nhập xuất cơ bản
Độ khó: Easy
"""
import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def solve():
    a = int(input())
    b, c = map(int, input().split())
    print(a + b - c)


def main():
    solve()


if __name__ == "__main__":
    main()
