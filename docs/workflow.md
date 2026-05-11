# Workflow

The default workflow is:

1. Fill a JSON config with the target paper, model profile, LaTeX template, style skill, and few-shot file.
2. Run `ccf-agent render` to create a model-ready prompt bundle.
3. Send the prompt bundle to the chosen model/API.
4. Place the generated LaTeX into the paper scaffold.
5. Run `ccf-agent evaluate` on the result.
6. Use `prompts/review.md` to revise sections that fail checks or feel technically weak.

## Model/API Integration

This repository does not ship API credentials or a mandatory provider adapter. That is deliberate. Many users will run the prompt bundle through Claude, OpenAI, local models, IDE agents, or custom harnesses.

Recommended orchestration contract:

- Read `build/prompt.md`.
- Send it to the selected model with the configured reasoning/thinking profile.
- Save the model output to `paper/sections/<section>.tex`.
- Run the harness.
- Keep model output, harness result, and human edits in version control.

## Human Review

The harness checks for structure. A human author still owns:

- correctness of the theorem or algorithm,
- appropriateness of claims for the target venue,
- citation quality,
- experiment validity,
- final voice and taste.
