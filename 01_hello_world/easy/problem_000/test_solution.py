"""Test cases cho Bài 000: A + B - C"""

import sys
from io import StringIO

import pytest


def test_basic_case():
    """Test với giá trị dương."""
    from solution import solve

    sys.stdin = StringIO("3\n5 2\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "6"


def test_negative_a():
    """Test với a âm."""
    from solution import solve

    sys.stdin = StringIO("-3\n5 2\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "0"


def test_all_zeros():
    """Test với tất cả bằng 0."""
    from solution import solve

    sys.stdin = StringIO("0\n0 0\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "0"


def test_negative_result():
    """Test với kết quả âm."""
    from solution import solve

    sys.stdin = StringIO("1\n2 10\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "-7"


def test_negative_b_c():
    """Test với b, c âm."""
    from solution import solve

    sys.stdin = StringIO("5\n-3 -2\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "4"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
