"""Test cases cho Bài 006: Căn bậc 2"""

import sys
from io import StringIO

import pytest


def test_perfect_square():
    """Test với số chính phương."""
    from solution import solve

    sys.stdin = StringIO("16\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "4.00"


def test_non_square():
    """Test với số không phải chính phương."""
    from solution import solve

    sys.stdin = StringIO("10\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "3.16"


def test_zero():
    """Test với a = 0."""
    from solution import solve

    sys.stdin = StringIO("0\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "0.00"


def test_one():
    """Test với a = 1."""
    from solution import solve

    sys.stdin = StringIO("1\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "1.00"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
