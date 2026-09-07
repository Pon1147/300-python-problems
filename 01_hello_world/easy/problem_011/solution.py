import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def solve():
    HS, T = map(int, input().split())

    full = HS // T
    residual = HS % T

    print(f"{full} {residual}")


def main():
    solve()


if __name__ == "__main__":
    main()
