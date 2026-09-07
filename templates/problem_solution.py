"""
Bài {number}: {title}
Chủ đề: {topic}
Độ khó: {difficulty}
"""
import sys

# Xử lý encoding tiếng Việt trên Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def solve():
    """Hàm giải chính cho bài tập."""
    # TODO: Viết code giải bài tập tại đây
    pass


def main():
    """Hàm main - gọi solve() khi chạy script."""
    print(f"=== Bài {number}: {title} ===")
    solve()


if __name__ == "__main__":
    main()
