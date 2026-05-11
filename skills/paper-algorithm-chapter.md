# Skill: paper-algorithm-chapter

Write a rigorous algorithm or method chapter for a top-conference or CCF-style paper.

Use this skill when the user wants a section covering:

- preliminaries,
- observation,
- core mechanism,
- equations,
- pseudocode or pipeline,
- correctness,
- complexity,
- implementation notes.

## Reference Shape

Mirror the KV reference structure when the paper is algorithmic:

1. Problem framing.
2. Baseline and bottleneck.
3. Core observation.
4. Algorithm design.
5. Correctness.
6. Complexity.
7. Implementation details and edge cases.

For each subsection:

- open with a gap-first, observation-recall, constraint-first, defect-diagnosis, or phenomenon-plus-need-plus-handle opener;
- declare notation before the first display equation;
- keep equation declarations local and explicit;
- use pseudocode only when the procedure needs a reusable plan;
- end with a complexity or implementation consequence.

## Default Shape

1. Start with a one-paragraph overview of the pipeline or algorithm.
2. Split the method into one subsection per constructed object.
3. In each subsection, open with one of the context-example opener families.
4. Introduce notation before equations.
5. Place the equation immediately after the definition window.
6. Explain the consequence of the equation after it appears.
7. Summarize the procedure with object-named pseudocode.
8. End with local complexity or an implementation consequence.

## Style Constraints

- Write in restrained technical English.
- Prefer concrete nouns over slogans.
- Prefer short declarative sentences before formulas.
- Use `Author note` only for missing facts, not for uncertainty that can be resolved from context.
- Do not invent experiments, citations, or numeric results.

## Algorithm Block Rules

- Caption names the object or role.
- Input and Output are flush-left.
- Inputs are semicolon-separated.
- Output is one object or a clearly justified tuple.
- Use tensor-op grain, phase grain, recurrence grain, or mixed grain deliberately.
- Every symbol is declared in Input or in a previous line.
- Return line matches the Output object.
- If a block is a sub-procedure, name it with `\textsc{FunctionName}` and keep the parent algorithm's symbols consistent with the callee.

## Equation Rules

- Number or label method-section display equations.
- Declare symbols before use.
- Use trailing `where` clauses only when they stay local and short.
- Pack only parallel definitions.
- Avoid nested subscript depth unless the domain requires it.
- If a subsection has no displayed equation, say so by keeping the math inside the algorithm block instead of inventing one.

## Review Loop

After drafting, run:

1. deterministic harness,
2. sentence judge on dense first paragraphs,
3. pseudocode-line judge on algorithm blocks,
4. equation judge on displayed equations.

Only rewrite targets marked `tighten` or `cut`.

## Coverage Note

This skill is the genericized version of the `kv` chapter skill. It keeps the chapter-level rhetorical spine while removing project-specific names and bilingual wording.
