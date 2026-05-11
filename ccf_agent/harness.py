from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


REQUIRED_SIGNALS: dict[str, list[str]] = {
    "problem framing": ["problem", "task", "input", "output", "objective", "setting"],
    "baseline or difficulty": ["baseline", "brute force", "bottleneck", "challenge", "failure mode"],
    "core observation": ["observation", "key idea", "invariant", "lemma", "central insight"],
    "algorithm design": ["algorithm", "transition", "state", "data structure", "procedure", "pseudocode"],
    "correctness": ["correctness", "proof", "lemma", "therefore", "guarantee"],
    "complexity": ["complexity", "time", "space", "O("],
    "edge cases": ["edge", "implementation", "corner", "tie", "empty", "boundary"],
}

LATEX_SIGNALS = [r"\\section", r"\\begin\{abstract\}", r"\\end\{document\}"]
PLACEHOLDER_PATTERNS = ["TODO", "TBD", "{{", "}}", "lorem ipsum"]
WEAK_STYLE_PATTERNS = [
    "obviously",
    "clearly",
    "state of the art",
    "novel",
    "remarkable",
    "utilize",
    "subsequently",
]
DISPLAY_EQUATION_RE = re.compile(
    r"\\begin\{equation\}.*?\\end\{equation\}|\$\$.*?\$\$|\\\[.*?\\\]",
    re.DOTALL,
)
SECTION_RE = re.compile(r"\\(?:sub)*section\{")


@dataclass(frozen=True)
class CheckResult:
    ok: bool
    missing: list[str]
    warnings: list[str]


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def _sentence_word_count(sentence: str) -> int:
    return len(re.findall(r"[A-Za-z0-9_'-]+", sentence))


def _sentences(text: str) -> list[str]:
    compact = re.sub(r"\s+", " ", text)
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", compact) if part.strip()]


def _equation_warnings(text: str) -> list[str]:
    warnings: list[str] = []
    for index, match in enumerate(DISPLAY_EQUATION_RE.finditer(text), start=1):
        equation = match.group(0)
        if "\\begin{equation}" in equation and "\\label{" not in equation:
            warnings.append(f"display equation {index} has no label")
        if equation.startswith("$$") and "\\tag{" not in equation:
            warnings.append(f"display equation {index} uses $$ without a number tag")
        if equation.startswith("\\["):
            warnings.append(f"display equation {index} uses unnumbered \\[...\\]")
        if "\\begin{aligned}" in equation and "&=" not in equation and "& =" not in equation:
            warnings.append(f"display equation {index} has an aligned block without an equals anchor")
    return warnings


def _algorithm_warnings(text: str) -> list[str]:
    warnings: list[str] = []
    blocks = re.findall(r"\\begin\{algorithm\}.*?\\end\{algorithm\}", text, re.DOTALL)
    for index, block in enumerate(blocks, start=1):
        if "\\caption{" not in block:
            warnings.append(f"algorithm {index} has no caption")
        if "\\textbf{Input:}" not in block:
            warnings.append(f"algorithm {index} has no Input block")
        if "\\textbf{Output:}" not in block:
            warnings.append(f"algorithm {index} has no Output block")
        if "\\STATE \\textbf{return}" not in block and "\\State \\textbf{return}" not in block:
            warnings.append(f"algorithm {index} has no explicit return line")
        if "\\COMMENT{Eq.~" in block or "\\Comment{Eq.~" in block:
            warnings.append(f"algorithm {index} uses equation references in comments; prefer inline Eq.~ references")
    return warnings


def evaluate_text(text: str, *, require_latex: bool = False, minimum_sections: int | None = None) -> CheckResult:
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

    for marker in WEAK_STYLE_PATTERNS:
        if marker in compact:
            warnings.append(f"weak or overused style marker appears: {marker}")

    for sentence in _sentences(text):
        if _sentence_word_count(sentence) > 45:
            warnings.append("long sentence over 45 words; run the sentence judge")
            break

    if require_latex:
        for signal in LATEX_SIGNALS:
            if not re.search(signal, text):
                missing.append(f"LaTeX structure: {signal}")
        warnings.extend(_equation_warnings(text))
        warnings.extend(_algorithm_warnings(text))

    if minimum_sections is not None and minimum_sections > 0:
        section_count = len(SECTION_RE.findall(text))
        if section_count < minimum_sections:
            missing.append(f"section count: expected at least {minimum_sections}, found {section_count}")

    return CheckResult(ok=not missing, missing=missing, warnings=warnings)


def evaluate_file(
    path: str | Path,
    *,
    require_latex: bool | None = None,
    minimum_sections: int | None = None,
) -> CheckResult:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    should_require_latex = file_path.suffix.lower() == ".tex" if require_latex is None else require_latex
    return evaluate_text(text, require_latex=should_require_latex, minimum_sections=minimum_sections)
