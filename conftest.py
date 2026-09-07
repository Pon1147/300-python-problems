import sys
from pathlib import Path


def pytest_configure(config):
    """Thêm thư mục chứa test file vào sys.path trước khi import."""
    # Khi chạy từ root, thêm root vào path
    root = Path(__file__).parent.resolve()
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
