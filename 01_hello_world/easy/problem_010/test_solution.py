"""Test cases cho Bài 010: Phép chia lấy phần nguyên và lấy phần dư"""

import sys
from io import StringIO

import pytest


def test_basic():
    """Test với a = 10, b = 3."""
    from solution import solve

    sys.stdin = StringIO("10 3\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "3 1"


def test_divisible():
    """Test với a chia hết cho b."""
    from solution import solve

    sys.stdin = StringIO("10 2\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "5 0"


def test_equal():
    """Test với a = b."""
    from solution import solve

    sys.stdin = StringIO("5 5\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "1 0"


def test_large():
    """Test với giá trị lớn."""
    from solution import solve

    sys.stdin = StringIO("1000000000 3\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "333333333 1"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
