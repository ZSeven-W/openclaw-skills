# File Operations Checklist

## Safety

- Always support preview mode.
- Detect filename collisions before writes.
- Avoid in-place mutation when conversion may fail.

## Determinism

- Use explicit naming rules.
- Keep ordering stable (e.g., lexical sort).
- Emit operation log for auditing.

## Recovery

- Keep a path mapping (`from`, `to`) for rollback.
- Use temporary directory for risky conversions.
- Fail fast on permission errors.
