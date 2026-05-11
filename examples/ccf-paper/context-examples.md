# Context Examples

This file is a generic version of the reference `kv` context pack. It is designed for top-conference and CCF-style algorithm chapters.

The examples below are rhetorical fingerprints, not factual sources. Borrow opener intent, equation placement, pseudocode grain, and lexical register. Do not borrow claims, numbers, citations, or domain-specific terminology.

## Opener Families

### P1. Gap-first plus rhetorical pivot

- Use when: the subsection replaces a fixed rule with an adaptive rule.
- Shape: prior practice -> observed variation -> why the fixed rule fails -> question or handle owned by this subsection.
- Good phrases: fixed ratio, static budget, variation, task-dependent, required amount.
- Avoid: declaring the new method before the gap is visible.

### P2. Observation recall plus definition

- Use when: the introduction or prior section already showed an empirical pattern.
- Shape: recall observation -> hypothesis -> define the quantity that tests or uses it.
- Good phrases: we previously observed, based on this observation, to measure, to validate, define.
- Avoid: introducing a metric before explaining what uncertainty it resolves.

### P3. Recap plus central insight

- Use when: two earlier quantities must be combined.
- Shape: recap the two quantities -> ask the combination question -> state the insight that chooses the combination rule.
- Good phrases: complementary metrics, natural question, central insight, motivates.
- Avoid: adding both scores without explaining why one should dominate.

### Q1. Experimental-setup framing

- Use when: a subsection reports observations before a method.
- Shape: declare probe, model or dataset family, baseline comparison, then list findings.
- Good phrases: serving as a case study, for comparison, summarize our observations.
- Avoid: using this shape for purely theoretical derivations.

### Q2. Defect-diagnosis framing

- Use when: a prior representation is coarse, unstable, or too discrete.
- Shape: name the defect -> explain the mechanism causing it -> show the consequence -> announce the repair.
- Good phrases: crucial drawback, tends to, mapped to extremes, disproportionately, repair.
- Avoid: calling something defective without naming the exact failure mode.

### M1. Constraint-first motivation

- Use when: a method must respect an implementation or mathematical constraint.
- Shape: hard constraint -> why prior methods violate it -> proposed replacement -> compatibility consequence.
- Good phrases: prevents compatibility, optimized implementation, effective proxy, lightweight estimator.
- Avoid: overclaiming speed or compatibility without stating the constraint.

### M2. Phenomenon plus need plus handle

- Use when: variation across instances creates the need for adaptive allocation.
- Shape: phenomenon -> inefficiency if ignored -> quantity that captures the phenomenon -> how it drives the method.
- Good phrases: diverse patterns, inefficient usage, quantifies, focused or diffused, allocation.
- Avoid: jumping from phenomenon to full pipeline before the handle is named.

## Mapping Table

| Subsection role | Best opener | What the first paragraph must do |
|---|---|---|
| Localization or retrieval | M2 or P2 | State the phenomenon, then introduce the quantity that localizes it. |
| Field, score, or representation construction | Q2 or P3 | Diagnose the old representation and announce the new continuous or structured object. |
| Budgeting, planning, or allocation | M1 or P1 | State the hard constraint, then introduce the reusable plan or allocation rule. |
| Ablation or observation section | Q1 | Declare the probe and comparison before listing observations. |

## Safe Lexical Inventory

Verbs:

- adopt
- observe
- hypothesize
- define
- introduce
- compute
- estimate
- quantify
- preserve
- retain
- validate
- motivate

Noun phrases:

- fixed ratio
- layer-wise variation
- attention pattern
- complementary metrics
- central insight
- natural question
- crucial drawback
- effective proxy
- importance estimator
- dispersion
- focused or diffused
- hypothesis

Avoid:

- utilize
- yield
- denote
- materialize into
- subsequently
- remarkable
- elegant
- novel as a decoration
- precisely when

## Pseudocode Taxonomy

Use this when judging or drafting algorithm blocks.

1. **Caption.** One line. Name the object or procedure. No subtitle colon.
2. **Input and Output.** Use flush-left `\textbf{Input:}` and `\textbf{Output:}`. Inputs are semicolon-separated. Output is one object unless the procedure truly returns a tuple.
3. **Tensor-op grain.** Each body line maps to one assignment or vectorized operation. Best when the procedure is computational.
4. **Phase grain.** A few `\STATE \textbf{// Stage N: ...}` markers divide the body. Best for pipelines.
5. **Math-recurrence grain.** Each line mirrors an equation. Use only when the algorithm is essentially a recurrence.
6. **Mixed grain.** Phase headers plus tensor-op lines inside each phase. Best for end-to-end pipelines.
7. **Sub-procedure.** Use `\textsc{FunctionName}` when a block is reused and should be judged separately.
8. **Symbol reuse.** Every symbol in the body must appear in the Input block or a previous line.
9. **Comment strategy.** Put equation references inline, for example `as per Eq.~\ref{eq:score}`. Avoid decorative `\COMMENT{Eq.~...}`.

## Equation Taxonomy

Use this when judging displayed equations.

1. **Numbering.** Method-section equations should be numbered or labelled.
2. **Single vs multi-line.** Prefer single-line equations. Use `aligned` or `split` only for equality chains or genuine multi-part definitions.
3. **Alignment anchor.** In `aligned`, put `&` immediately before `=`.
4. **Symbol weight.** Keep new symbols shallow. Avoid nested subscripts and stacked accents.
5. **Declaration placement.** Bind symbols in the sentence before the equation, a trailing `where` clause, or a prior equation in the same subsection.
6. **Font families.** Use `\mathbb{R}` for spaces, `\mathcal{}` for sets/plans/families, and `\mathbf{}` only for dense tensors when the paper uses it globally.
7. **Packing.** Pack two or three parallel definitions with `\quad` or `\qquad`; split larger packs.

## Generic Section Verdict

A strong generated method section should have:

- one first paragraph that states the whole pipeline in stage order,
- one subsection per constructed object,
- every displayed equation introduced by prose,
- every algorithm line bound by Input or prior lines,
- one local complexity paragraph per major procedure,
- a final end-to-end complexity paragraph when the method is a pipeline.
