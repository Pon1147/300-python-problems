"""Test cases cho Bài 013: Tính tổng chữ số"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from io import StringIO

import pytest


def test_basic():
    """Test với a = 1234."""
    from solution import solve

    sys.stdin = StringIO("1234\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "10"


def test_min():
    """Test với a = 1000 (giá trị nhỏ nhất)."""
    from solution import solve

    sys.stdin = StringIO("1000\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "1"


def test_max():
    """Test với a = 9999 (giá trị lớn nhất)."""
    from solution import solve

    sys.stdin = StringIO("9999\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "36"


def test_zeros():
    """Test với a = 1010."""
    from solution import solve

    sys.stdin = StringIO("1010\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "2"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
