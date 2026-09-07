import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

"""Test cases cho BÃ i 002: PhÃ©p toÃ¡n trá»«"""
import sys
from io import StringIO

import pytest


def test_positive():
    """Test vá»›i a dÆ°Æ¡ng."""
    from solution import solve
    sys.stdin = StringIO("5\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "3"


def test_zero():
    """Test vá»›i a = 0."""
    from solution import solve
    sys.stdin = StringIO("0\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "-2"


def test_negative():
    """Test vá»›i a Ã¢m."""
    from solution import solve
    sys.stdin = StringIO("-10\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "-12"


def test_large():
    """Test vá»›i a lá»›n."""
    from solution import solve
    sys.stdin = StringIO("1000000000\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "999999998"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

