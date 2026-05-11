from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,4})\s+(.+)$", re.MULTILINE)


@dataclass(frozen=True)
class CorpusEntry:
    path: Path
    title: str
    first_paragraph: str
    headings: list[str]


def _compact(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _first_paragraph(text: str) -> str:
    for block in re.split(r"\n\s*\n", text):
        cleaned = _compact(re.sub(r"^#+\s+.*$", "", block, flags=re.MULTILINE))
        if len(cleaned) >= 120 and not cleaned.startswith("<!--"):
            return cleaned
    return ""


def read_corpus_entries(source: str | Path, *, limit: int = 30) -> list[CorpusEntry]:
    root = Path(source)
    files = sorted(root.rglob("*.md")) if root.is_dir() else [root]
    entries: list[CorpusEntry] = []
    for file_path in files:
        try:
            text = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = file_path.read_text(encoding="utf-8", errors="ignore")
        headings = [match.group(2).strip() for match in HEADING_RE.finditer(text)]
        title = headings[0] if headings else file_path.stem.replace("_", " ")
        paragraph = _first_paragraph(text)
        if not paragraph:
            continue
        entries.append(CorpusEntry(path=file_path, title=title, first_paragraph=paragraph, headings=headings[:8]))
        if len(entries) >= limit:
            break
    return entries


def render_context_brief(source: str | Path, *, limit: int = 12) -> str:
    entries = read_corpus_entries(source, limit=limit)
    parts = [
        "# Context Brief",
        f"Source: {Path(source)}",
        "",
        "This brief is meant to be pasted into the context prompt. It keeps the local rhetorical fingerprint without copying whole papers into the model call.",
    ]
    for index, entry in enumerate(entries, start=1):
        opener = entry.first_paragraph[:900].rstrip()
        if len(entry.first_paragraph) > len(opener):
            opener += "..."
        parts.extend(
            [
                "",
                f"## C{index}. {entry.title}",
                f"- File: `{entry.path}`",
                f"- Headings: {', '.join(entry.headings[:5]) if entry.headings else 'n/a'}",
                "- Opener sample:",
                "",
                f"> {opener}",
                "",
                "- Extraction notes:",
                "  - Identify the opener intent before reusing this example.",
                "  - Borrow rhetorical shape, not claims, numbers, or citations.",
                "  - Add canonical terms for the current paper before drafting.",
            ]
        )
    return "\n".join(parts).rstrip() + "\n"
