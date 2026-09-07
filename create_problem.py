#!/usr/bin/env python3
"""
Script tạo mới một bài tập với đầy đủ file template.

Usage:
    python create_problem.py <topic_number> <difficulty> <problem_number> "<title>"

Examples:
    python create_problem.py 04 easy 020 "Chia het cho 3"
    python create_problem.py 10 medium 150 "Doan so bi mat"
    python create_problem.py 05 hard 200 "Dem so lan"
"""

import sys
import os
from pathlib import Path


TOPICS = {
    "01": "hello_world",
    "02": "variables_types",
    "03": "input_output",
    "04": "conditions",
    "05": "loops",
    "06": "functions",
    "07": "lists",
    "08": "strings",
    "09": "dictionaries",
    "10": "math_games",
    "11": "nested_loops",
    "12": "file_operations",
    "13": "text_analysis",
    "14": "turtle_graphics",
    "15": "2d_arrays",
    "16": "sorting",
    "17": "recursion",
    "18": "oop_basics",
    "19": "error_handling",
    "20": "games_projects",
}

DIFFICULTY_LABELS = {
    "easy": "Easy",
    "medium": "Medium",
    "hard": "Hard",
}


def read_template(filename):
    """Đọc nội dung template từ thư mục templates/."""
    template_path = Path(__file__).parent / "templates" / filename
    if not template_path.exists():
        print(f"Loi: Khong tim thay template {filename}")
        sys.exit(1)
    return template_path.read_text(encoding="utf-8")


def fill_template(content, replacements):
    """Thay thế các placeholder trong template."""
    for key, value in replacements.items():
        content = content.replace(f"{{{key}}}", str(value))
    return content


def create_problem(topic_num, difficulty, problem_num, title):
    """Tạo mới một bài tập."""
    # Validate
    topic_key = topic_num.zfill(2)
    if topic_key not in TOPICS:
        print(f"Loi: Chu de '{topic_num}' khong hop le.")
        print("Cac chu de co san:")
        for k, v in sorted(TOPICS.items()):
            print(f"  {k} - {v}")
        sys.exit(1)

    if difficulty not in DIFFICULTY_LABELS:
        print(f"Loi: Do kho '{difficulty}' khong hop le.")
        print("Cac do kho: easy, medium, hard")
        sys.exit(1)

    topic_name = TOPICS[topic_key]
    topic_dir = f"{topic_key}_{topic_name}"
    difficulty_lower = difficulty.lower()
    problem_id = f"problem_{problem_num.zfill(3)}"

    # Đường dẫn
    base_dir = Path(__file__).parent / topic_dir / difficulty_lower / problem_id
    if base_dir.exists():
        print(f"Loi: Thu muc {base_dir} da ton tai!")
        sys.exit(1)

    # Tạo thư mục
    base_dir.mkdir(parents=True, exist_ok=True)

    # Thay thế vào templates
    replacements = {
        "number": problem_num.zfill(3),
        "title": title,
        "topic": topic_name.replace("_", " ").title(),
        "difficulty": DIFFICULTY_LABELS[difficulty_lower],
        "description": "[Viết mô tả bài tập tại đây]",
        "requirement_1": "[Yêu cầu 1]",
        "requirement_2": "[Yêu cầu 2]",
        "example_1_input": "[input]",
        "example_1_output": "[output]",
        "example_2_input": "[input]",
        "example_2_output": "[output]",
        "hint_1": "[Gợi ý]",
        "concept_1": "[Kiến thức 1]",
        "concept_2": "[Kiến thức 2]",
        "bonus_challenge": "[Thử thách thêm]",
    }

    # Viết README.md
    readme_content = read_template("problem_README.md")
    (base_dir / "README.md").write_text(
        fill_template(readme_content, replacements), encoding="utf-8"
    )

    # Viết solution.py
    sol_content = read_template("problem_solution.py")
    sol_replacements = {**replacements, "number": problem_num.zfill(3)}
    (base_dir / "solution.py").write_text(
        fill_template(sol_content, sol_replacements), encoding="utf-8"
    )

    # Viết test_solution.py
    test_content = read_template("problem_test.py")
    test_replacements = {**replacements, "number": problem_num.zfill(3)}
    (base_dir / "test_solution.py").write_text(
        fill_template(test_content, test_replacements), encoding="utf-8"
    )

    # Thông báo thành công
    print(f"\n{'='*50}")
    print(f"Da tao thanh cong bai tap:")
    print(f"  Chu de : {topic_dir}")
    print(f"  Do kho : {DIFFICULTY_LABELS[difficulty_lower]}")
    print(f"  So hieu : {problem_id}")
    print(f"  Tieu de : {title}")
    print(f"  Duong dan: {base_dir}")
    print(f"{'='*50}")
    print(f"\nCac file duoc tao:")
    print(f"  {base_dir}/README.md")
    print(f"  {base_dir}/solution.py")
    print(f"  {base_dir}/test_solution.py")
    print(f"\nHay chinh sua noi dung cho cac file nay!")


def main():
    if len(sys.argv) < 5:
        print(__doc__)
        sys.exit(1)

    topic_num = sys.argv[1]
    difficulty = sys.argv[2]
    problem_num = sys.argv[3]
    title = sys.argv[4]

    create_problem(topic_num, difficulty, problem_num, title)


if __name__ == "__main__":
    main()
