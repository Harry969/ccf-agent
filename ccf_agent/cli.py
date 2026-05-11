from __future__ import annotations

import argparse
from pathlib import Path

from .config import load_config
from .harness import evaluate_file
from .prompt_builder import describe_prompt, write_paper, write_prompt


def _add_config(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--config", default="config/default.json", help="Path to a ccf-agent JSON config.")


def render_cmd(args: argparse.Namespace) -> int:
    config = load_config(args.config)
    out = Path(args.out)
    write_prompt(config, out)
    print(f"Rendered prompt bundle: {out}")
    if args.describe:
        print(describe_prompt(config))
    return 0


def init_paper_cmd(args: argparse.Namespace) -> int:
    config = load_config(args.config)
    out = Path(args.out)
    write_paper(config, out)
    print(f"Initialized LaTeX paper scaffold: {out}")
    return 0


def evaluate_cmd(args: argparse.Namespace) -> int:
    result = evaluate_file(args.path, require_latex=args.require_latex)
    if result.warnings:
        print("Warnings:")
        for warning in result.warnings:
            print(f"- {warning}")

    if result.missing:
        print("Missing signals:")
        for item in result.missing:
            print(f"- {item}")
        return 1

    print("Draft passes the lightweight harness.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ccf-agent")
    sub = parser.add_subparsers(dest="command", required=True)

    render = sub.add_parser("render", help="Render a model-ready prompt bundle.")
    _add_config(render)
    render.add_argument("--out", required=True, help="Output Markdown prompt file.")
    render.add_argument("--describe", action="store_true", help="Print prompt stats after rendering.")
    render.set_defaults(func=render_cmd)

    paper = sub.add_parser("init-paper", help="Create a LaTeX paper scaffold from config.")
    _add_config(paper)
    paper.add_argument("--out", required=True, help="Output directory for the paper scaffold.")
    paper.set_defaults(func=init_paper_cmd)

    evaluate = sub.add_parser("evaluate", help="Run the lightweight quality harness.")
    evaluate.add_argument("path", help="Markdown or LaTeX draft to evaluate.")
    evaluate.add_argument("--require-latex", action="store_true", help="Require full LaTeX document signals.")
    evaluate.set_defaults(func=evaluate_cmd)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
