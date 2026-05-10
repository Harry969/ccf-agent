from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_SIGNALS = {
    "problem": ["问题", "题目", "输入", "输出"],
    "baseline": ["朴素", "直接", "瓶颈", "复杂度"],
    "observation": ["核心观察", "关键", "状态", "性质"],
    "algorithm": ["算法", "步骤", "转移", "维护"],
    "correctness": ["正确性", "证明", "不会漏", "最优"],
    "complexity": ["时间复杂度", "空间复杂度", "O("],
    "edge_cases": ["边界", "实现", "容易出错", "注意"],
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", "", text)


def evaluate(text: str) -> list[str]:
    compact = normalize(text)
    missing: list[str] = []

    for section, signals in REQUIRED_SIGNALS.items():
        if not any(signal in compact for signal in signals):
            missing.append(section)

    return missing


def main() -> int:
    parser = argparse.ArgumentParser(description="Check an algorithm chapter draft.")
    parser.add_argument("chapter", type=Path, help="Markdown chapter file to check")
    args = parser.parse_args()

    text = args.chapter.read_text(encoding="utf-8")
    missing = evaluate(text)

    if missing:
        print("Missing signals:")
        for item in missing:
            print(f"- {item}")
        return 1

    print("Chapter passes the lightweight structure check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

