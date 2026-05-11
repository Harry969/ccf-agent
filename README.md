# ccf-agent

`ccf-agent` is an open template for drafting competition-algorithm and top-conference-style paper sections with a reusable agent stack:

```text
strong reasoning model + few-shot examples + harness + context prompt
+ personal writing style skill + configurable LaTeX paper template
```

The first reference recipe is:

```text
opus4.7-max thinking + few-shot + harness + context prompt
+ personal writing style skill + ccf agent writes the paper
```

The project is intentionally model-agnostic. You can point it at any model/API in your own runner, while this repository provides the prompts, context contract, LaTeX skeleton, examples, and quality harness.

## What It Generates

- A complete conference paper scaffold in LaTeX.
- Algorithm chapters with problem framing, observations, method, proof, complexity, and implementation notes.
- Prompt bundles that combine user context, few-shot examples, style skill, model profile, and output contract.
- Context briefs distilled from local Markdown literature notes.
- Logic-judge review packs extracted from drafts for sentence, pseudocode, and equation review.
- Lightweight checks for missing technical sections, placeholder leakage, and LaTeX structure.
- Advanced prompt-based review for sentence logic, pseudocode lines, and equation form.

## Quick Start

Render a prompt bundle from the example configuration:

```powershell
python -m ccf_agent.cli render --config examples/ccf-paper/config.json --out build/prompt.md
```

Create a starter LaTeX paper from the same configuration:

```powershell
python -m ccf_agent.cli init-paper --config examples/ccf-paper/config.json --out build/paper
```

Run the harness on the included sample output:

```powershell
python harness/evaluate.py examples/ccf-paper/expected-output.tex
```

Build a compact context brief from local paper notes:

```powershell
python -m ccf_agent.cli context-brief --source path\to\md_notes --out build\context-brief.md --limit 12
```

Create review targets for the logic judge:

```powershell
python -m ccf_agent.cli judge-pack examples/ccf-paper/expected-output.tex --out build/review-pack.md --context-examples examples/ccf-paper/context-examples.md
```

Or use the console script after installing locally:

```powershell
pip install -e .
ccf-agent render --config examples/ccf-paper/config.json --out build/prompt.md
ccf-agent init-paper --config examples/ccf-paper/config.json --out build/paper
ccf-agent evaluate examples/ccf-paper/expected-output.tex
```

## Repository Layout

```text
ccf-agent/
  ccf_agent/                 # stdlib-only CLI and prompt renderer
  config/
    default.json             # model/profile/template defaults
  docs/
    workflow.md              # end-to-end agent workflow
    customization.md         # how users replace context/style/model/API
    advanced-harness.md      # sentence/pseudocode/equation judging workflow
    corpus-and-review-pack.md # context brief and judge-pack commands
    vision.md                # project philosophy
  examples/
    ccf-paper/               # complete paper-writing example
    few-shot/                # focused algorithm-section example
  harness/
    evaluate.py              # standalone quality checks
  paper/
    main.tex                 # editable paper scaffold
    sections/
  prompts/
    *.md                     # system, context, paper, algorithm, review prompts
    logic-judge.md
  skills/
    personal-writing-style.md
  templates/
    latex/
```

## Configuration

All user-facing behavior starts from JSON configuration. The default example is `examples/ccf-paper/config.json`.

You can customize:

- `model`: provider, model name, temperature, max tokens, and thinking profile.
- `context`: target venue, audience, paper goal, constraints, terminology, and source files.
- `style`: personal writing style skill and forbidden expressions.
- `latex`: template, title, authors, abstract seed, sections, and bibliography path.
- `few_shot`: examples that define pacing and technical density.
- `review`: canonical terms, context examples, and judge modes.
- `harness`: checks that must pass before a draft is considered usable.

No secret keys are stored in this repository. Put API keys in your own environment or orchestration layer.

## Agent Loop

1. Collect paper context: problem, contribution, method, experiments, target venue, and author style.
2. Optionally build a context brief from local Markdown notes with `ccf-agent context-brief`.
3. Render a prompt bundle with `ccf-agent render`.
4. Ask the chosen model to draft or revise a LaTeX section.
5. Save the generated `.tex` into the paper scaffold.
6. Run `ccf-agent evaluate` or `python harness/evaluate.py`.
7. Create a review pack with `ccf-agent judge-pack`.
8. Run `prompts/logic-judge.md` on dense paragraphs, pseudocode, and equations.
9. Iterate with `prompts/review.md` until the harness and human review agree.

## License

MIT. Use it as a base for your own paper-writing agent, prompt harness, or model comparison workflow.
