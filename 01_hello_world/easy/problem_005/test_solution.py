"""Test cases cho Bài 005: Phép toán lũy thừa"""

import sys
from io import StringIO

import pytest


def test_basic():
    """Test với a = 2."""
    from solution import solve

    sys.stdin = StringIO("2\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "4\n32"


def test_zero():
    """Test với a = 0."""
    from solution import solve

    sys.stdin = StringIO("0\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "0\n0"


def test_one():
    """Test với a = 1."""
    from solution import solve

    sys.stdin = StringIO("1\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "1\n1"


def test_negative():
    """Test với a âm."""
    from solution import solve

    sys.stdin = StringIO("-3\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "9\n-243"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
