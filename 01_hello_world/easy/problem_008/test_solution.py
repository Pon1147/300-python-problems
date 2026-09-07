"""Test cases cho Bài 008: Tính giá trị biểu thức 1"""

import sys
from io import StringIO

import pytest


def test_basic():
    """Test với a = 1, b = 1."""
    from solution import solve

    sys.stdin = StringIO("1\n1\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    output = captured.getvalue().strip()
    lines = output.split("\n")
    assert len(lines) == 2
    assert lines[0] == "-1983 0.0080"
    assert abs(float(lines[1]) - 0.012846) < 0.000001


def test_larger_values():
    """Test với giá trị lớn hơn."""
    from solution import solve

    sys.stdin = StringIO("10\n5\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    output = captured.getvalue().strip()
    lines = output.split("\n")
    assert len(lines) == 2


def test_negative():
    """Test với giá trị âm."""
    from solution import solve

    sys.stdin = StringIO("-1\n-1\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    output = captured.getvalue().strip()
    lines = output.split("\n")
    assert len(lines) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
