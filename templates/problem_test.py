"""
Test cases cho Bài {number}: {title}
"""
import sys
from pathlib import Path

# Thêm folder hiện tại vào sys.path để import solution.py
sys.path.insert(0, str(Path(__file__).parent))

import pytest
from unittest.mock import patch
import io


# ---------- Test cases ----------

def test_example_1():
    """Test với ví dụ 1"""
    # TODO: Thêm test case
    pass


def test_example_2():
    """Test với ví dụ 2"""
    # TODO: Thêm test case
    pass


def test_edge_case():
    """Test trường hợp đặc biệt"""
    # TODO: Thêm test case cho edge case
    pass


# ---------- Chạy test ----------

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
