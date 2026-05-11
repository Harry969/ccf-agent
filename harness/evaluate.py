from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from ccf_agent.harness import evaluate_file


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a CCF/paper draft.")
    parser.add_argument("draft", type=Path, help="Markdown or LaTeX draft to check.")
    parser.add_argument("--require-latex", action="store_true", help="Require full LaTeX document structure.")
    args = parser.parse_args()

    result = evaluate_file(args.draft, require_latex=args.require_latex or args.draft.suffix == ".tex")

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


if __name__ == "__main__":
    raise SystemExit(main())
