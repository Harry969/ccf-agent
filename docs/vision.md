# Vision

`ccf-agent` treats paper writing as an agent workflow rather than a single prompt.

The motivating observation is simple: a strong model becomes much more useful when it is surrounded by the right constraints. Long reasoning helps with structure, few-shot examples define pacing, context prompts prevent drift, a writing-style skill preserves voice, and a harness catches the boring omissions that humans often notice only after fatigue sets in.

The project is not tied to one model. The reference recipe uses `opus4.7-max thinking` as a named example, but the repository keeps model choice in configuration so users can swap providers, local models, or API clients.

## Design Principles

- The paper remains the user's paper; the agent should expose assumptions instead of inventing facts.
- LaTeX is the primary artifact, because paper workflows need diffs, comments, and compilation.
- Prompts are versioned beside examples and harness checks, so writing quality can improve through regression testing.
- The harness is intentionally lightweight at first. It should catch missing structure, not pretend to replace expert review.
