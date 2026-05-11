from __future__ import annotations

from datetime import date
from pathlib import Path
from textwrap import indent
from typing import Any

from .config import AgentConfig, ROOT


def _format_mapping(title: str, value: dict[str, Any]) -> str:
    lines = [f"## {title}"]
    for key, item in value.items():
        if isinstance(item, list):
            lines.append(f"- {key}:")
            for entry in item:
                lines.append(f"  - {entry}")
        elif isinstance(item, dict):
            lines.append(f"- {key}:")
            for child_key, child_value in item.items():
                lines.append(f"  - {child_key}: {child_value}")
        else:
            lines.append(f"- {key}: {item}")
    return "\n".join(lines)


def _read_repo_file(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def render_prompt(config: AgentConfig) -> str:
    model = config.get("model", {})
    context = config.get("context", {})
    style = config.get("style", {})
    latex = config.get("latex", {})
    few_shot = config.get("few_shot", {})
    review = config.get("review", {})

    sections = [
        "# CCF Agent Prompt Bundle",
        f"Generated: {date.today().isoformat()}",
        _format_mapping("Model Profile", model),
        _format_mapping("Paper Context", context),
        _format_mapping("LaTeX Contract", latex),
        "## System Prompt\n" + _read_repo_file("prompts/system.md").strip(),
        "## Orchestrator Prompt\n" + _read_repo_file("prompts/orchestrator.md").strip(),
        "## Context Prompt\n" + _read_repo_file("prompts/context.md").strip(),
        "## Paper Writer Prompt\n" + _read_repo_file("prompts/paper-writer.md").strip(),
        "## Algorithm Chapter Prompt\n" + _read_repo_file("prompts/algorithm-chapter.md").strip(),
    ]

    style_path = style.get("path")
    style_text = config.read_text(style_path) or _read_repo_file("skills/personal-writing-style.md")
    sections.append("## Personal Writing Style Skill\n" + style_text.strip())

    few_shot_path = few_shot.get("path")
    if few_shot_path:
        sections.append("## Few-Shot Example\n" + config.read_text(few_shot_path).strip())

    user_context_path = context.get("source")
    if user_context_path:
        sections.append("## User Context Source\n" + config.read_text(user_context_path).strip())

    context_examples_path = review.get("context_examples")
    if context_examples_path:
        sections.append("## Rhetorical Context Examples\n" + config.read_text(context_examples_path).strip())

    canonical_terms = review.get("canonical_terms")
    if canonical_terms:
        sections.append("## Canonical Terms\n" + "\n".join(f"- {term}" for term in canonical_terms))

    if review:
        sections.append(_format_mapping("Review Protocol", review))

    final_contract = latex.get("output_contract", "Return compilable LaTeX only.")
    sections.append("## Final Output Contract\n" + final_contract.strip())

    return "\n\n".join(section for section in sections if section.strip()) + "\n"


def render_paper_files(config: AgentConfig) -> dict[Path, str]:
    latex = config.get("latex", {})
    template_path = latex.get("template", "templates/latex/conference-paper.tex")
    template = config.read_text(template_path)

    title = latex.get("title", "Untitled Paper")
    authors = latex.get("authors", "Anonymous Authors")
    abstract = latex.get("abstract_seed", "TODO: summarize the motivation, method, and main result.")
    sections = latex.get("sections", [])

    section_inputs = []
    for item in sections:
        name = item["name"]
        file_name = item.get("file", f"sections/{name.lower().replace(' ', '-')}.tex")
        section_inputs.append(r"\input{" + file_name.replace("\\", "/").removesuffix(".tex") + "}")

    rendered_main = (
        template.replace("{{TITLE}}", title)
        .replace("{{AUTHORS}}", authors)
        .replace("{{ABSTRACT}}", abstract)
        .replace("{{SECTION_INPUTS}}", "\n".join(section_inputs))
    )

    files: dict[Path, str] = {Path("main.tex"): rendered_main}

    section_template = config.read_text("templates/latex/section.tex")
    for item in sections:
        name = item["name"]
        file_name = item.get("file", f"sections/{name.lower().replace(' ', '-')}.tex")
        seed = item.get("seed", "TODO")
        body = section_template.replace("{{SECTION_TITLE}}", name).replace("{{SECTION_SEED}}", seed)
        files[Path(file_name)] = body

    return files


def write_prompt(config: AgentConfig, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_prompt(config), encoding="utf-8")


def write_paper(config: AgentConfig, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for relative_path, content in render_paper_files(config).items():
        target = out_dir / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")


def describe_prompt(config: AgentConfig) -> str:
    prompt = render_prompt(config)
    lines = prompt.splitlines()
    return "\n".join(
        [
            f"Prompt lines: {len(lines)}",
            f"Prompt characters: {len(prompt)}",
            "First section:",
            indent("\n".join(lines[:12]), "  "),
        ]
    )
