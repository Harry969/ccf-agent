from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


REQUIRED_SIGNALS: dict[str, list[str]] = {
    "problem framing": ["problem", "task", "input", "output", "题目", "问题", "输入", "输出"],
    "baseline or difficulty": ["baseline", "brute force", "bottleneck", "朴素", "瓶颈"],
    "core observation": ["observation", "key idea", "invariant", "核心观察", "关键性质"],
    "algorithm design": ["algorithm", "transition", "state", "data structure", "算法", "状态", "转移"],
    "correctness": ["correctness", "proof", "lemma", "正确性", "证明"],
    "complexity": ["complexity", "time", "space", "O(", "复杂度"],
    "edge cases": ["edge", "implementation", "corner", "边界", "实现"],
}

LATEX_SIGNALS = [r"\\section", r"\\begin\{abstract\}", r"\\end\{document\}"]
PLACEHOLDER_PATTERNS = ["TODO", "TBD", "{{", "}}", "lorem ipsum"]


@dataclass(frozen=True)
class CheckResult:
    ok: bool
    missing: list[str]
    warnings: list[str]


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def evaluate_text(text: str, *, require_latex: bool = False) -> CheckResult:
    compact = _normalize(text)
    missing = [
        section
        for section, signals in REQUIRED_SIGNALS.items()
        if not any(signal.lower() in compact for signal in signals)
    ]

    warnings: list[str] = []
    for marker in PLACEHOLDER_PATTERNS:
        if marker.lower() in compact:
            warnings.append(f"placeholder marker remains: {marker}")

    if require_latex:
        for signal in LATEX_SIGNALS:
            if not re.search(signal, text):
                missing.append(f"LaTeX structure: {signal}")

    return CheckResult(ok=not missing, missing=missing, warnings=warnings)


def evaluate_file(path: str | Path, *, require_latex: bool | None = None) -> CheckResult:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    should_require_latex = file_path.suffix.lower() == ".tex" if require_latex is None else require_latex
    return evaluate_text(text, require_latex=should_require_latex)
