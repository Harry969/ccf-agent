# Context Prompt

Use this context layer to bind the agent to a particular paper, venue, reader, and technical boundary.

## Required Context

- Paper goal: what the paper or chapter must persuade the reader to understand.
- Target venue/style: conference paper, CCF-style algorithm explanation, teaching chapter, or hybrid.
- Reader model: what the reader already knows and where they are likely to get stuck.
- Source material: problem statement, method notes, proof sketch, experiments, or code.
- Non-goals: claims, sections, terminology, or examples that must not appear.

## Default Reader Model

The reader can program and understands common data structures, but may not yet see why the central algorithm is inevitable. The writing should therefore expose the path from naive thinking to the final method.

## Output Boundary

- Do not replace a missing proof with confidence.
- Do not hide complexity under "obvious" or "straightforward".
- Do not write a list of disconnected tips; each paragraph should advance the argument.
- If a section depends on a theorem, experiment, or citation that is not in context, insert a clear author note instead of fabricating it.
