# Context Prompt

Bind the draft to a concrete paper, venue, reader, and evidence boundary.

## Required Context

- Paper goal: what the section should persuade the reader to understand.
- Target venue/style: top conference paper, CCF-style algorithm chapter, or hybrid.
- Reader model: what the reader knows, what they do not know, and where they are likely to get stuck.
- Source material: problem statement, method notes, proof sketch, experiments, code, or reference chapter.
- Non-goals: claims, examples, citations, or terminology that must not appear.

## Default Reader Model

Assume the reader can program and understands common data structures, but may not yet see why the final construction is inevitable. The writing should therefore expose the path from naive thinking to the core observation and then to the final method.

## Output Boundary

- Do not replace a missing proof with confidence.
- Do not hide complexity under "obvious" or "straightforward".
- Do not write disconnected tips; each paragraph should advance the argument.
- If a section depends on a theorem, experiment, or citation that is not in context, insert a clear author note instead of fabricating it.
- If the context is a reference chapter, borrow rhetorical shape, not claims or numbers.
