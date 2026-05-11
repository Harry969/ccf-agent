# KV Reference Map

This project is a genericized version of the local `kv` workflow. The source
folder is not copied wholesale because most files are paper-specific data,
converted PDFs, or AnomalyKV prose. The reusable parts are mapped as follows.

## Direct Mapping

| KV reference file | Generic repository file | What is preserved |
|---|---|---|
| `kv/main/_tools/logic_judge_harness.md` | `prompts/logic-judge.md` | sentence judge, pseudocode-line judge, equation-form judge, strict verdict blocks, anti-patterns, calibration examples |
| `kv/main/_tools/context_examples.md` | `examples/ccf-paper/context-examples.md` | opener families, lexical inventory, pseudocode taxonomy, equation taxonomy, section-level verdict checklist |
| `kv/main/algorithm_chapter.tex` | `templates/latex/method-chapter.tex` | three-stage method shape, local equations, object-named algorithms, sub-procedure pattern, local and end-to-end complexity, edge-case handling |
| `kv/skills_and_context/skills/kv-algo-chapter.md` | `skills/paper-algorithm-chapter.md` | chapter trigger, top-conference method-section rules, pseudocode discipline, equation discipline, review loop |
| `kv/main/algorithm_chapter.md` and `kv/main/algorithm_chapter_zh.md` | `prompts/algorithm-chapter.md` and `examples/few-shot/algorithm-chapter.md` | problem framing, bottleneck, observation, algorithm, correctness, complexity, edge cases |

## Not Copied By Design

- `kv/md_output*`: converted literature notes. Use `ccf-agent context-brief` to
  build a compact brief from a user's own corpus instead of shipping a
  domain-specific paper dump.
- `kv/example/*.pdf` and spreadsheets: paper-specific source materials, not
  part of the reusable template.
- `kv/main/neurips_2026.tex`: venue-specific shell. The repository keeps a
  generic LaTeX template and lets users swap venue files through config.
- Bilingual AnomalyKV prose files: useful as writing examples, but the open
  template remains English-first and model-agnostic. A user can add a bilingual
  style skill through `style.path`.

## Coverage Checklist

When comparing future changes against `kv`, keep these pieces present:

- prompt bundle includes system, orchestrator, context, paper writer, algorithm
  chapter prompt, style skill, chapter skill, few-shot example, user context,
  context examples, canonical terms, review protocol, and output contract;
- chapter template contains problem framing, baseline and bottleneck, core
  observation, staged construction, equations, object-named pseudocode,
  correctness or guarantee text, complexity, and edge cases;
- logic judge supports sentence, pseudocode, and equation modes with strict
  machine-readable verdict blocks;
- context examples separate rhetorical fingerprints from factual claims;
- deterministic harness and judge-pack remain available from the CLI.
