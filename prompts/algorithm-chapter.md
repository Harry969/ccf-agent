# Algorithm Chapter Prompt

Write a CCF-style algorithm chapter or paper method section in LaTeX.

## Chapter Contract

The section should read like a derivation, not like a checklist. It must expose why the method exists, what object it builds, and why the object is enough for the rest of the paper.

## Required Sections

1. Problem framing: restate the task, input, output, constraints, and objective.
2. Baseline and bottleneck: explain the direct solution and why it fails.
3. Core observation: state the invariant, monotonicity, exchange argument, recurrence, or structural property.
4. Algorithm design: define states, transitions, maintained data, and full procedure.
5. Correctness proof: connect each step of the algorithm to the observation.
6. Complexity analysis: define all variables and give time and space bounds.
7. Implementation details and edge cases: identify mistakes that can break a correct idea.

## Opener Shapes

Use one of these, depending on the subsection:

- gap-first: state the old habit, then the limitation, then the new handle;
- observation-recall: tie back to an earlier figure or empirical fact, then define the quantity that measures it;
- constraint-first: name the hard constraint before the construction;
- defect-diagnosis: isolate the failure mode of the previous representation, then announce the repair;
- phenomenon + need + handle: state the variation, the need it creates, and the quantity that drives the method.

## Pseudocode and Equation Discipline

- Use a caption that names the object, not a slogan.
- Put `Input:` and `Output:` in a flush-left block, with semicolon-separated parameters.
- Make every body line earn its place; do not add decorative comments.
- Use inline equation references such as `as per Eq.~\ref{...}` instead of comment-only cross references.
- Number displayed equations in method sections.
- Prefer single-line equations unless alignment genuinely helps the reader.

## Quality Bar

- The core observation must be concrete enough that a reader could rederive the algorithm from it.
- The proof must match the described algorithm, not a different idealized version.
- Complexity must name the variables it depends on.
- The section should feel like a guided derivation from problem to method to proof.
- If a sentence is only there to sound polished, cut it.
