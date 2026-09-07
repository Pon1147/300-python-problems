"""
Bài 259: Vẽ hình vuông màu sắc
Chủ đề: Vẽ hình với Turtle
Độ khó: Easy
"""
import sys

# Xử lý encoding tiếng Việt trên Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

import turtle


def draw_colored_square():
    """Vẽ hình vuông màu đỏ viền, nền vàng nhạt."""
    t = turtle.Turtle()
    t.speed(3)

    # Đặt màu viền đỏ, nền vàng nhạt
    t.color("red", "lightyellow")
    t.begin_fill()

    # Vẽ hình vuông 4 cạnh
    for _ in range(4):
        t.forward(100)
        t.right(90)

    t.end_fill()
    t.hideturtle()

    # Click để đóng
    turtle.done()


def solve():
    """Hàm giải chính."""
    draw_colored_square()


def main():
    """Hàm main."""
    print("=== Bài 259: Ve hinh vuong mau sac ===")
    print("Cua so ve huan se mo. Click de dong.")
    solve()


if __name__ == "__main__":
    main()
