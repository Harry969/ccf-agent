# Algorithm Chapter Prompt

Write a CCF-style algorithm chapter or paper method section in LaTeX.

## Required Sections

1. Problem framing: restate the task, input, output, constraints, and objective.
2. Baseline and bottleneck: explain the direct solution and why it fails.
3. Core observation: state the invariant, monotonicity, exchange argument, recurrence, or structural property.
4. Algorithm design: define states, transitions, maintained data, and full procedure.
5. Correctness proof: connect each step of the algorithm to the observation.
6. Complexity analysis: define all variables and give time and space bounds.
7. Implementation details and edge cases: identify mistakes that can break a correct idea.

## Quality Bar

- The core observation must be concrete enough that a reader could rederive the algorithm from it.
- The proof must match the described algorithm, not a different idealized version.
- Complexity must name the variables it depends on.
- Avoid writing only code comments. The output is a paper/chapter section, not a solution note.
- Keep paragraphs connected; the section should feel like a guided derivation.
