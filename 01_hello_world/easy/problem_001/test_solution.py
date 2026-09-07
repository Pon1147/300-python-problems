import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

"""Test cases cho BÃ i 001: PhÃ©p toÃ¡n cá»™ng"""
import sys
from io import StringIO

import pytest


def test_positive():
    """Test vá»›i a dÆ°Æ¡ng."""
    from solution import solve
    sys.stdin = StringIO("10\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "2035"


def test_zero():
    """Test vá»›i a = 0."""
    from solution import solve
    sys.stdin = StringIO("0\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "2025"


def test_negative():
    """Test vá»›i a Ã¢m."""
    from solution import solve
    sys.stdin = StringIO("-100\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "1925"


def test_large():
    """Test vá»›i a lá»›n."""
    from solution import solve
    sys.stdin = StringIO("1000000000\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "1000002025"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

