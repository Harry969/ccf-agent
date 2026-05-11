# Example Context

The project is a reusable open-source template for writing top-conference-style algorithm papers.

The agent recipe is:

```text
opus4.7-max thinking + few-shot + harness + context prompt
+ personal writing style skill + ccf agent writes paper
```

The paper should emphasize that the model is not enough by itself. The value comes from binding a strong reasoning model to a reproducible writing protocol:

- context prompt fixes the paper goal and boundaries,
- few-shot example fixes pacing and technical density,
- personal style skill fixes author voice,
- LaTeX template fixes the artifact shape,
- harness catches missing required signals,
- human review remains the final authority.

The default algorithm section format should include problem framing, baseline and bottleneck, core observation, algorithm design, correctness proof, complexity, and edge cases.

For this repository, the best reference shape is a chapter that starts from a real drafting bottleneck, exposes the core observation, and then turns that observation into a local loop, a proof obligation, and a complexity statement.
