"""Test cases cho Bài 012: Tìm chữ số"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from io import StringIO

import pytest


def test_basic():
    """Test với a = 35."""
    from solution import solve

    sys.stdin = StringIO("35\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "5 3"


def test_edge_min():
    """Test với a = 10 (giá trị nhỏ nhất)."""
    from solution import solve

    sys.stdin = StringIO("10\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "0 1"


def test_edge_max():
    """Test với a = 99 (giá trị lớn nhất)."""
    from solution import solve

    sys.stdin = StringIO("99\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "9 9"


def test_other():
    """Test với a = 72."""
    from solution import solve

    sys.stdin = StringIO("72\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "2 7"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
