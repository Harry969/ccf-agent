from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
EQUATION_RE = re.compile(
    r"\\begin\{equation\}.*?\\end\{equation\}|\$\$.*?\$\$|\\\[.*?\\\]",
    re.DOTALL,
)
PSEUDOCODE_RE = re.compile(
    r"^.*(?:\\STATE|\\State|\\FOR|\\For|\\IF|\\If|\\RETURN|\\Return|\\caption\{|\\textbf\{Input:|\\textbf\{Output:).*$",
    re.MULTILINE,
)


@dataclass(frozen=True)
class ReviewTarget:
    mode: str
    label: str
    target: str
    context: str


def _compact(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _window(text: str, start: int, end: int, radius: int = 700) -> str:
    left = max(0, start - radius)
    right = min(len(text), end + radius)
    return _compact(text[left:right])


def _sentence_targets(text: str, limit: int) -> list[ReviewTarget]:
    targets: list[ReviewTarget] = []
    offset = 0
    for sentence in SENTENCE_RE.split(_compact(text)):
        if not sentence or len(sentence) < 45:
            offset += len(sentence) + 1
            continue
        lowered = sentence.lower()
        if any(marker in lowered for marker in ["\\begin", "\\end", "\\state", "\\caption"]):
            offset += len(sentence) + 1
            continue
        targets.append(
            ReviewTarget(
                mode="sentence",
                label=f"sentence-{len(targets) + 1}",
                target=sentence,
                context=_window(text, offset, offset + len(sentence)),
            )
        )
        offset += len(sentence) + 1
        if len(targets) >= limit:
            break
    return targets


def _equation_targets(text: str, limit: int) -> list[ReviewTarget]:
    targets: list[ReviewTarget] = []
    for match in EQUATION_RE.finditer(text):
        targets.append(
            ReviewTarget(
                mode="equation",
                label=f"equation-{len(targets) + 1}",
                target=match.group(0).strip(),
                context=_window(text, match.start(), match.end()),
            )
        )
        if len(targets) >= limit:
            break
    return targets


def _pseudocode_targets(text: str, limit: int) -> list[ReviewTarget]:
    targets: list[ReviewTarget] = []
    for match in PSEUDOCODE_RE.finditer(text):
        line = match.group(0).strip()
        targets.append(
            ReviewTarget(
                mode="pseudocode",
                label=f"pseudocode-{len(targets) + 1}",
                target=line,
                context=_window(text, match.start(), match.end(), radius=900),
            )
        )
        if len(targets) >= limit:
            break
    return targets


def collect_review_targets(text: str, *, per_mode_limit: int = 8) -> list[ReviewTarget]:
    return [
        *_sentence_targets(text, per_mode_limit),
        *_pseudocode_targets(text, per_mode_limit),
        *_equation_targets(text, per_mode_limit),
    ]


def render_review_pack(
    draft_path: str | Path,
    *,
    canonical_terms: str = "",
    context_examples: str = "",
    per_mode_limit: int = 8,
) -> str:
    path = Path(draft_path)
    text = path.read_text(encoding="utf-8")
    targets = collect_review_targets(text, per_mode_limit=per_mode_limit)
    parts = [
        "# Logic Judge Review Pack",
        f"Draft: {path}",
        "",
        "Use this file with `prompts/logic-judge.md`. Return one verdict block per target.",
        "",
        "## Canonical Terms",
        canonical_terms.strip() or "TODO: add paper-specific terms and symbols.",
    ]
    if context_examples.strip():
        parts.extend(["", "## Context Examples", context_examples.strip()])

    for target in targets:
        parts.extend(
            [
                "",
                f"## Target: {target.label}",
                f"JUDGE MODE: {target.mode}",
                "",
                "TARGET:",
                target.target,
                "",
                "SURROUNDING CONTEXT:",
                target.context,
            ]
        )
    return "\n".join(parts).rstrip() + "\n"
