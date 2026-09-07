#!/usr/bin/env python3
"""
Chạy test cho tất cả bài tập trong repository.

Usage:
    python run_tests.py                  # Chạy test tất cả
    python run_tests.py 04               # Chỉ chủ đề conditions
    python run_tests.py 04 easy          # Conditions + easy
    python run_tests.py 04 easy 019      # Problem 019 cụ thể
"""

import subprocess
import sys
from pathlib import Path


def find_test_files(
    base, filter_topic=None, filter_difficulty=None, filter_problem=None
):
    """Tìm tất cả test_solution.py phù hợp."""
    tests = []
    for topic in sorted(base.glob("0*")):
        if not topic.is_dir():
            continue
        topic_num = topic.name[:2]
        if filter_topic and filter_topic != topic_num:
            continue

        for difficulty in ["easy", "medium", "hard"]:
            if filter_difficulty and filter_difficulty != difficulty:
                continue

            diff_dir = topic / difficulty
            if not diff_dir.exists():
                continue

            for prob in sorted(diff_dir.iterdir()):
                if not prob.is_dir():
                    continue
                if filter_problem and filter_problem not in prob.name:
                    continue

                test_file = prob / "test_solution.py"
                if test_file.exists():
                    tests.append(test_file)

    return tests


def main():
    base = Path(__file__).parent
    args = sys.argv[1:]

    filter_topic = args[0] if len(args) > 0 else None
    filter_difficulty = args[1] if len(args) > 1 else None
    filter_problem = args[2] if len(args) > 2 else None

    tests = find_test_files(base, filter_topic, filter_difficulty, filter_problem)

    if not tests:
        print("Khong tim thay test nao ph hop le.")
        sys.exit(1)

    print(f"Tim thay {len(tests)} test file.")
    print(f"{'=' * 60}")

    # Chay tung test mot de tranh xung突 module name
    passed = 0
    failed = 0
    errors = 0

    for test_file in tests:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(test_file), "-v", "-q"],
            cwd=str(base),
            capture_output=False,
            check=True,
        )
        if result.returncode == 0:
            passed += 1
        elif result.returncode == 1:
            failed += 1
        else:
            errors += 1

    print(f"\n{'=' * 60}")
    print(f" Ket qua: {passed} pass, {failed} fail, {errors} error")


if __name__ == "__main__":
    main()
