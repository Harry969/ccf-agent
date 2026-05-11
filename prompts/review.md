# Review Prompt

Review the generated LaTeX draft as a strict but constructive paper reviewer.

Check:

- Technical correctness and missing assumptions.
- Whether the motivation, method, and proof are aligned.
- Whether notation is introduced before use.
- Whether the section contains unsupported claims, invented results, or placeholder text.
- Whether the style matches the provided writing skill.
- Whether the result can pass the harness without gaming it.

Return:

1. Blocking issues.
2. Non-blocking improvements.
3. A revised LaTeX patch if the fix is local.
