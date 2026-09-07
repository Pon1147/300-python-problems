"""Test cases cho Bài 014: Tính tổng hàng đơn vị"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from io import StringIO

import pytest


def test_basic():
    """Test với a = 123, b = 456."""
    from solution import solve

    sys.stdin = StringIO("123 456\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "9"


def test_zeros():
    """Test với a = 0, b = 0."""
    from solution import solve

    sys.stdin = StringIO("0 0\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "0"


def test_large():
    """Test với số lớn."""
    from solution import solve

    sys.stdin = StringIO("1000000000 999999999\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "9"


def test_same_units():
    """Test với cùng hàng đơn vị."""
    from solution import solve

    sys.stdin = StringIO("27 37\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "14"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
