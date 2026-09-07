#!/usr/bin/env python3
"""
Script liệt kê tất cả bài tập trong repository và trạng thái hoàn thành.

Usage:
    python list_problems.py                  # Liệt kê tất cả
    python list_problems.py 04               # Chỉ chủ đề conditions
    python list_problems.py easy             # Chỉ level easy
    python list_problems.py 04 easy          # Conditions + easy
"""

import os
import sys
from pathlib import Path


TOPICS = {
    "01": "Hello World & In ra man hinh",
    "02": "Bien & Kieu du lieu",
    "03": "Nhap/xuat (Input/Output)",
    "04": "Dieu kien (if/elif/else)",
    "05": "Vong lap (for/while)",
    "06": "Ham (Functions)",
    "07": "Danh sach (Lists)",
    "08": "Chuoi (Strings)",
    "09": "Tu dien (Dictionaries)",
    "10": "Tro choi toan hoc",
    "11": "Vong lap long nhau",
    "12": "Thao tac file",
    "13": "Phan tich van ban",
    "14": "Ve hinh voi Turtle",
    "15": "Manh 2 chieu",
    "16": "Sap xep",
    "17": "De quy (Recursion)",
    "18": "Lap trinh huong doi tuong",
    "19": "Xu ly loi",
    "20": "Du an & Tro choi",
}

DIFFICULTY_ORDER = {"easy": 0, "medium": 1, "hard": 2}


def get_problem_status(problem_dir):
    """Kiểm tra trạng thái hoàn thành của 1 bài."""
    has_readme = (problem_dir / "README.md").exists()
    has_solution = (problem_dir / "solution.py").exists()
    has_test = (problem_dir / "test_solution.py").exists()

    if has_readme and has_solution and has_test:
        return "[X]"  # Done
    elif has_solution:
        return "[~]"  # In progress
    else:
        return "[ ]"   # Not started


def list_problems(filter_topic=None, filter_difficulty=None):
    """Liệt kê bài tập."""
    base = Path(__file__).parent
    topics_dir = base

    total = 0
    done = 0
    in_progress = 0

    for topic_folder in sorted(topics_dir.glob("0*")):
        if not topic_folder.is_dir():
            continue
        topic_num = topic_folder.name[:2]

        # Filter topic
        if filter_topic and filter_topic != topic_num:
            continue

        topic_name = TOPICS.get(topic_num, topic_folder.name)
        print(f"\n{'='*60}")
        print(f" #{topic_num} {topic_name}")
        print(f"{'='*60}")

        for difficulty in ["easy", "medium", "hard"]:
            # Filter difficulty
            if filter_difficulty and filter_difficulty != difficulty:
                continue

            diff_label = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}[difficulty]
            diff_dir = topic_folder / difficulty

            if not diff_dir.exists():
                continue

            print(f"\n  [{diff_label}]")
            problems = sorted(diff_dir.iterdir())
            for prob_dir in problems:
                if not prob_dir.is_dir():
                    continue
                total += 1
                status = get_problem_status(prob_dir)
                if status == "[X]":
                    done += 1
                elif status == "[~]":
                    in_progress += 1

                print(f"    {status} {prob_dir.name}")

    print(f"\n{'='*60}")
    print(f" Tong cong: {total} bai")
    print(f"  Da hoan thanh: {done}")
    print(f"  Dang lam: {in_progress}")
    print(f"  Con lai: {total - done - in_progress}")


def main():
    filter_topic = sys.argv[1] if len(sys.argv) > 1 else None
    filter_difficulty = sys.argv[2] if len(sys.argv) > 2 else None

    list_problems(filter_topic, filter_difficulty)


if __name__ == "__main__":
    main()
