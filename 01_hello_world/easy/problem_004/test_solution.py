import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

"""Test cases cho BÃ i 004: PhÃ©p toÃ¡n chia"""
import sys
from io import StringIO

import pytest


def test_divisible():
    """Test vá»›i a chia háº¿t cho 3."""
    from solution import solve
    sys.stdin = StringIO("9\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "3.00"


def test_not_divisible():
    """Test vá»›i a khÃ´ng chia háº¿t cho 3."""
    from solution import solve
    sys.stdin = StringIO("10\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "3.33"


def test_negative():
    """Test vá»›i a Ã¢m."""
    from solution import solve
    sys.stdin = StringIO("-10\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "-3.33"


def test_zero():
    """Test vá»›i a = 0."""
    from solution import solve
    sys.stdin = StringIO("0\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "0.00"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

