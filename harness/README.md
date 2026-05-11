# Harness

The harness is a lightweight guardrail for generated paper sections.

It checks whether a draft contains signals for:

- problem framing,
- baseline or bottleneck,
- core observation,
- algorithm design,
- correctness,
- complexity,
- implementation details and edge cases,
- LaTeX structure when the input is a `.tex` file.

Run:

```powershell
python harness/evaluate.py examples/ccf-paper/expected-output.tex
```

The harness is intentionally simple and deterministic. It should be easy to extend with model-based review, compilation checks, citation checks, or project-specific rubrics.
