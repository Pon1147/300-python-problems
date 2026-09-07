import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

"""Test cases cho BÃ i 007: Nghá»‹ch Ä‘áº£o"""

import sys
from io import StringIO

import pytest


def test_basic():
    """Test vá»›i a = 3."""
    from solution import solve

    sys.stdin = StringIO("3\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "0.33333"


def test_one():
    """Test vá»›i a = 1."""
    from solution import solve

    sys.stdin = StringIO("1\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "1.00000"


def test_negative():
    """Test vá»›i a Ã¢m."""
    from solution import solve

    sys.stdin = StringIO("-4\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "-0.25000"


def test_decimal():
    """Test vá»›i a lÃ  sá»‘ tháº­p phÃ¢n."""
    from solution import solve

    sys.stdin = StringIO("0.5\n")
    captured = StringIO()
    sys.stdout = captured
    solve()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "2.00000"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

