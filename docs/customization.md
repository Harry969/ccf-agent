# Customization

`ccf-agent` is designed so users can replace the important pieces without editing code.

## Replace Context

Set `context.source` in your config to a Markdown file that contains the real paper notes. Good context includes:

- problem statement,
- contribution bullets,
- notation,
- method sketch,
- proof outline,
- known limitations,
- experiment table notes,
- target venue constraints.

## Replace Style

Set `style.path` to your own writing skill. A useful style skill should say what to do and what to avoid. It should not be a vague personality description.

## Replace Few-Shot

Set `few_shot.path` to an example section that has the exact density you want. The model will imitate structure, pacing, and proof granularity more reliably when the few-shot file is close to the target task.

## Replace Review Context

Set `review.context_examples` to a Markdown file containing rhetorical anchors, opener patterns, pseudocode fingerprints, and equation form notes. Set `review.canonical_terms` to the noun phrases and symbols the paper must use consistently.

You can create a first draft of this file from local paper notes:

```powershell
python -m ccf_agent.cli context-brief --source md_output --out build/context-brief.md
```

Then edit the brief by hand before using it in a model call. The brief should preserve structure and writing patterns, not copied claims.

## Replace Model

Edit the `model` block:

```json
{
  "provider": "anthropic",
  "name": "opus4.7-max",
  "reasoning": "max thinking",
  "temperature": 0.2
}
```

These fields are descriptive metadata for the prompt bundle. Your own runner decides how to translate them into actual API parameters.
