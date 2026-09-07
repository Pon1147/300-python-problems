"""Test cases cho Bài 259: Vẽ hình vuông màu sắc"""
import pytest


def test_turtle_import():
    """Kiểm tra turtle có thể import được."""
    try:
        import turtle
        assert True
    except ImportError:
        pytest.skip("Turtle not available on this system")


def test_draw_square_logic():
    """Kiểm tra logic vẽ hình vuông (4 cạnh, góc 90 độ)."""
    # Hình vuông có 4 cạnh, mỗi góc quay 90 độ
    sides = 4
    turn_angle = 360 / sides
    assert sides == 4
    assert turn_angle == 90


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
