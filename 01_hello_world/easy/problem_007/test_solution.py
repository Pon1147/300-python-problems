"""Test cases cho Bài 007: Nghịch đảo"""

import sys
from io import StringIO

import pytest


def test_basic():
    """Test với a = 3."""
    from solution import solve

    sys.stdin = StringIO("3\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "0.33333"


def test_one():
    """Test với a = 1."""
    from solution import solve

    sys.stdin = StringIO("1\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "1.00000"


def test_negative():
    """Test với a âm."""
    from solution import solve

    sys.stdin = StringIO("-4\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "-0.25000"


def test_decimal():
    """Test với a là số thập phân."""
    from solution import solve

    sys.stdin = StringIO("0.5\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "2.00000"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
