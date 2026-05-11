# Logic Judge Instance

This example shows how to call `prompts/logic-judge.md` on a generated sentence.

```text
JUDGE MODE:
sentence

SECTION:
Algorithm Chapter Drafting

TARGET:
The context prompt controls facts, the few-shot example controls pacing, the style skill controls voice, and the harness checks whether required technical signals remain present.

SURROUNDING CONTEXT:
The key observation is that writing quality can be decomposed into explicit constraints. The context prompt controls facts, the few-shot example controls pacing, the style skill controls voice, and the harness checks whether required technical signals remain present. This decomposition lets the author improve one source of failure without changing the entire agent.

CANONICAL TERMS:
context prompt; few-shot example; style skill; harness; LaTeX output contract
```

Expected verdict:

```text
VERDICT: keep
WHY: The sentence names the four control surfaces and explains what each one owns. It adds concrete structure after the broader key-observation sentence.
AXIS SCORES:
  logical_contribution: keep - maps control surfaces
  novelty_in_paragraph: keep - adds ownership
  causal_direction:     keep - premise to mechanism
  plain_english_shape:  keep - direct list
  terminology_aligned:  keep - canonical terms
REPLACEMENT INTENT:
  n/a
```
