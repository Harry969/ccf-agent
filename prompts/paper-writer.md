# Paper Writer Prompt

Draft a LaTeX paper section from the supplied context.

## Inputs

- `paper_goal`: the scientific or educational point of the paper.
- `section_name`: the section to write.
- `technical_notes`: facts, definitions, method details, proof sketches, or experiment notes.
- `target_venue`: formatting and rhetorical expectations.
- `style_skill`: author voice and forbidden expressions.
- `few_shot`: examples that define density, pacing, and structure.

## Output

Return only the requested LaTeX section unless the user asks for commentary.

The section should:

1. Start from the reader's current confusion or need.
2. Introduce notation before using it heavily.
3. Separate definitions, claims, and proof arguments.
4. Use equations or pseudocode only when they reduce ambiguity.
5. Mark missing facts as `\textbf{Author note: ...}`.
6. End with a transition that makes the next section natural.
