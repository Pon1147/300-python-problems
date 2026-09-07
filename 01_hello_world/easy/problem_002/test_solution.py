"""Test cases cho Bài 002: Phép toán trừ"""
import sys
from io import StringIO

import pytest


def test_positive():
    """Test với a dương."""
    from solution import solve
    sys.stdin = StringIO("5\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "3"


def test_zero():
    """Test với a = 0."""
    from solution import solve
    sys.stdin = StringIO("0\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "-2"


def test_negative():
    """Test với a âm."""
    from solution import solve
    sys.stdin = StringIO("-10\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "-12"


def test_large():
    """Test với a lớn."""
    from solution import solve
    sys.stdin = StringIO("1000000000\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "999999998"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
