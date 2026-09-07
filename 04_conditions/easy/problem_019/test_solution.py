"""Test cases cho Bài 019: Kiểm tra số dương hay âm"""

import pytest
from solution import check_number


def test_positive():
    """Số dương -> So duong"""
    assert check_number(5) == "So duong"
    assert check_number(1) == "So duong"
    assert check_number(100) == "So duong"


def test_negative():
    """Số âm -> So am"""
    assert check_number(-3) == "So am"
    assert check_number(-1) == "So am"
    assert check_number(-100) == "So am"


def test_zero():
    """Số 0 -> So 0"""
    assert check_number(0) == "So 0"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
