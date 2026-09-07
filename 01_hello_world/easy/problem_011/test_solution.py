"""Test cases cho Bài 011: Chia táo"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from io import StringIO

import pytest


def test_basic():
    """Test với T = 10, HS = 3."""
    from solution import solve

    sys.stdin = StringIO("10 3\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "3 1"


def test_exact_division():
    """Test với chia hết."""
    from solution import solve

    sys.stdin = StringIO("10 2\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "5 0"


def test_one_tao():
    """Test với 1 táo."""
    from solution import solve

    sys.stdin = StringIO("1 5\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "0 1"


def test_large():
    """Test với giá trị lớn."""
    from solution import solve

    sys.stdin = StringIO("1000000000 3\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "333333333 1"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
