"""Test cases cho Bài 004: Phép toán chia"""
import sys
from io import StringIO

import pytest


def test_divisible():
    """Test với a chia hết cho 3."""
    from solution import solve
    sys.stdin = StringIO("9\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "3.00"


def test_not_divisible():
    """Test với a không chia hết cho 3."""
    from solution import solve
    sys.stdin = StringIO("10\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "3.33"


def test_negative():
    """Test với a âm."""
    from solution import solve
    sys.stdin = StringIO("-10\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "-3.33"


def test_zero():
    """Test với a = 0."""
    from solution import solve
    sys.stdin = StringIO("0\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "0.00"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
