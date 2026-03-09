# Data Quality Rules

## Minimum Checks

- Required columns exist.
- Primary key uniqueness threshold is acceptable.
- Null rates for critical fields remain below project threshold.

## Transformation Rules

- Prefer additive columns over destructive replacement.
- Keep source column names in a mapping table.
- Reject records that fail hard constraints; do not silently coerce.

## Reporting Rules

- Emit row counts before and after processing.
- Emit count of rejected rows with reason categories.
- Emit per-column null count for critical fields.
