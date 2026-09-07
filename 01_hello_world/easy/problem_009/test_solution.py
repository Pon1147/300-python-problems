"""Test cases cho Bài 009: Tính giá trị biểu thức 2"""

import sys
from io import StringIO

import pytest


def test_basic():
    """Test với a = 2, b = 1, c = 1."""
    from solution import solve

    sys.stdin = StringIO("2 1 1\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    output = captured.getvalue().strip()
    parts = output.split()
    assert len(parts) == 2


def test_larger_values():
    """Test với giá trị lớn hơn."""
    from solution import solve

    sys.stdin = StringIO("10 5 3\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    output = captured.getvalue().strip()
    parts = output.split()
    assert len(parts) == 2


def test_negative_b():
    """Test với b âm."""
    from solution import solve

    sys.stdin = StringIO("5 -10 2\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    output = captured.getvalue().strip()
    parts = output.split()
    assert len(parts) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
