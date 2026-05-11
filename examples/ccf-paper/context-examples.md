# Context Examples

These examples are distilled rhetorical anchors. They describe reusable paragraph shapes without copying a paper's claims or results.

## E1. Gap-first opener

- Intent: state the common practice, name the pressure point, then ask the precise question the subsection will answer.
- Use when: the method replaces a fixed rule with an adaptive one.
- Shape: prior rule -> observed variation -> why the rule fails -> current mechanism.
- Safe lexical choices: fixed ratio, variation, bottleneck, adaptive rule, required budget.

## E2. Observation-recall opener

- Intent: tie back to an earlier figure, statistic, or example, then introduce the quantity that measures it.
- Use when: the subsection formalizes a phenomenon already shown in the introduction.
- Shape: prior observation -> hypothesis -> definition -> why this definition is operational.
- Safe lexical choices: we previously observed, to measure, preserve, localize, quantify.

## E3. Constraint-first opener

- Intent: name a hard implementation or mathematical constraint before introducing the construction that respects it.
- Use when: the section bridges a continuous object and a discrete algorithmic object.
- Shape: constraint -> why direct use fails -> constructed object -> reuse scope.
- Safe lexical choices: addressed by, built once, reused, compatible with, one-shot plan.

## E4. Defect-diagnosis opener

- Intent: isolate the exact defect of a previous representation, then state the repair.
- Use when: binary, coarse, or uncalibrated signals must be replaced by a smoother object.
- Shape: representation defect -> two concrete consequences -> replacement object.
- Safe lexical choices: hard-edged, inadequate, multi-scale, boundary-aware, source term.

## Pseudocode Fingerprint

- Captions name the object, not a slogan.
- Input and Output are flush-left and semicolon-separated.
- Output is one object unless the method truly returns a tuple.
- Body lines should be tensor-op grain or phase grain, but not a drifting mixture.
- Equation references belong inline as `as per Eq.~\\ref{...}`, not in decorative comments.

## Equation Fingerprint

- Displayed equations in method sections should be numbered.
- Use single-line equations when they fit.
- Use `aligned` only when there is a real chain of equalities, with `&` anchored before `=`.
- Declare symbols before the equation or in a tight trailing `where` clause.
- Pack two or three parallel definitions with `\\qquad`; split larger packs.
