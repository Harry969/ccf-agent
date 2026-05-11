# Advanced Harness

The default Python harness catches missing section-level signals. The advanced harness is a prompt-based review layer for paper-quality details that deterministic keyword checks cannot see.

It is inspired by the `kv` reference workflow:

```text
opus4.7-max thinking + few-shot + harness + context prompt
+ personal writing style skill + ccf agent writes paper
```

## Three Review Modes

1. Sentence judge: checks whether each sentence contributes new logical load.
2. Pseudocode-line judge: checks symbol binding, algorithm grain, comments, I/O form, and return shape.
3. Equation form judge: checks numbering, declaration placement, alignment, notation weight, and packing.

The prompt template is in `prompts/logic-judge.md`.

You can generate concrete targets automatically:

```powershell
python -m ccf_agent.cli judge-pack paper/sections/method.tex --out build/review-pack.md
```

## Why This Exists

A paper section can pass a coarse harness while still feeling weak. Typical failures:

- a sentence repeats the previous one,
- a claim appears before the premise that supports it,
- an equation introduces symbols before declaring them,
- pseudocode uses a symbol not listed in the input block,
- a caption is a slogan rather than the object being computed,
- terminology drifts from the canonical noun phrases.

The advanced judge catches these local failures one target at a time.

## Caller Protocol

Pass the logic-judge prompt first, then append a concrete instance:

```text
TARGET:
<sentence, pseudocode line, or equation>

SURROUNDING CONTEXT:
<paragraph or declaration window>

SECTION:
<section title>

CANONICAL TERMS:
<semicolon-separated terms and symbols>

JUDGE MODE:
sentence | pseudocode | equation
```

Batching is fine. For a first paragraph, send all sentences and request one verdict block per sentence. For an algorithm, send the caption, input, output, and body lines as separate targets.

## How It Fits The Agent Loop

1. Generate a draft with the main prompt bundle.
2. Run the deterministic harness.
3. Generate `build/review-pack.md` with `ccf-agent judge-pack`.
4. Run the advanced judge on dense sentences in each technical subsection.
5. Run the pseudocode judge on algorithm blocks.
6. Run the equation judge on new displayed equations.
7. Rewrite only the spans marked `tighten` or `cut`.

The judge should not rewrite directly. Keeping judgment separate from rewriting makes the workflow easier to audit.
