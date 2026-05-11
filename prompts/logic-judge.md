# Logic Judge Prompt

Use this prompt for a focused review pass after a paper section has been drafted. The judge does not rewrite. It decides whether each target sentence, pseudocode line, or displayed equation earns its place in the logical chain.

## Mode A: Sentence Judge

Input:

- target sentence or 2-3 adjacent sentences,
- surrounding paragraph,
- subsection title,
- first equation of the subsection when relevant,
- canonical terms fixed for this paper,
- optional few-shot context examples.

Score each axis as `keep`, `tighten`, or `cut`:

- logical contribution: advances the argument toward the next equation or paragraph,
- novelty within the paragraph: adds a fact, definition, or justification not already present,
- causal direction: moves from premise to consequence,
- plain-English shape: flags long sentences, filler openers, unnecessary asides, or inflated verbs,
- terminology alignment: uses the canonical noun phrases and symbols.

Output:

```text
VERDICT: keep | tighten | cut
WHY: <one paragraph>
AXIS SCORES:
  logical_contribution: keep|tighten|cut - <short reason>
  novelty_in_paragraph: keep|tighten|cut - <short reason>
  causal_direction:     keep|tighten|cut - <short reason>
  plain_english_shape:  keep|tighten|cut - <short reason>
  terminology_aligned:  keep|tighten|cut - <short reason>
REPLACEMENT INTENT:
  <what the sentence should do instead; omit when verdict is keep>
```

## Mode B: Pseudocode-Line Judge

Use for `\STATE`, `\FOR`, `\IF`, `\RETURN`, caption, input, and output lines.

Score:

- symbol existence: every symbol is declared in input or prior lines,
- grain consistency: line matches the algorithm's declared granularity,
- comment discipline: equation references are inline, not decorative comments,
- terminology alignment: symbols and object names match the paper,
- caption and I/O form: caption is object-named; inputs are semicolon-separated; output is one object,
- return line: exactly returns the output object.

## Mode C: Equation Form Judge

Use for displayed equations with the sentence before and after.

Score:

- numbering,
- single-line vs multi-line discipline,
- alignment anchor,
- symbol weight,
- declaration placement,
- font-family usage,
- packing.

The judge evaluates form and local logic. It does not decide whether the theorem is true.
