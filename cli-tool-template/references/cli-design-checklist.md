# CLI Design Checklist

## Contract

- Command purpose fits in one sentence.
- Required vs optional parameters are explicit.
- Exit codes are predictable.

## Safety

- Include `--dry-run` for destructive actions.
- Guard write operations behind explicit confirmation.
- Fail fast on invalid inputs.

## Operability

- Support `--help` with concrete examples.
- Print concise success/failure summaries.
- Keep output parse-friendly for automation where practical.
