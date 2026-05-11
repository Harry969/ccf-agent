# Corpus And Review Pack

The `kv` reference workflow has two useful stages before final rewriting:

1. Build a compact context brief from the local literature corpus.
2. Turn a draft into local judge targets for sentences, pseudocode, and equations.

This repository supports both stages with stdlib-only commands.

## Context Brief

Use `context-brief` when you have Markdown notes converted from PDFs:

```powershell
python -m ccf_agent.cli context-brief --source md_output --out build/context-brief.md --limit 12
```

The command extracts each file's title, headings, and first substantial paragraph. The brief is not a literature survey. It is a compact rhetorical map that helps the model imitate opener shape, equation placement, and definition cadence without copying claims.

Recommended use:

- include 6-12 examples,
- keep only examples from the same paper family,
- annotate opener intent by hand when the auto brief is too raw,
- never treat examples as factual evidence for the new paper.

## Logic-Judge Pack

Use `judge-pack` after a draft exists:

```powershell
python -m ccf_agent.cli judge-pack paper/sections/method.tex --out build/review-pack.md --context-examples examples/ccf-paper/context-examples.md --canonical-terms "state; transition; invariant; complexity"
```

The output file contains targets for:

- long or dense sentences,
- algorithm captions, input/output declarations, and pseudocode lines,
- displayed equations.

Paste `prompts/logic-judge.md` first, then the generated review pack. The judge returns verdicts; the writer rewrites only the targets marked `tighten` or `cut`.

## Why This Split Matters

The writer model is good at drafting, but it tends to defend its own text. The judge prompt is deliberately narrower: it cannot rewrite, it can only decide whether a local unit earns its place. This makes the loop auditable and keeps revisions small.
