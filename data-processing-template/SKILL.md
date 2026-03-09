---
name: data-processing-template
description: Process tabular datasets with repeatable cleaning, schema checks, type normalization, and quality reporting. Use when transforming CSV/TSV exports, preparing analytics-ready data, validating required columns, or building deterministic ETL-style scripts.
---

# Data Processing Template

Use this template for reliable dataset transforms with explicit quality gates.

## Quick Start

1. Define the expected schema in `references/data-quality-rules.md`.
2. Copy `assets/transform-spec.yaml` and customize column mappings.
3. Run `scripts/process_csv.py` on a sample file.
4. Inspect generated summary metrics before scaling to full data.

## Workflow

### 1. Profile First

- Count rows and null rates.
- Check duplicate keys.
- Verify required columns are present.

### 2. Normalize Types

- Strip whitespace from string columns.
- Parse numeric/date fields deterministically.
- Keep invalid values in a dedicated error column.

### 3. Apply Transform Rules

- Rename columns through an explicit mapping table.
- Drop only explicitly listed columns.
- Preserve an immutable raw key when possible.

### 4. Emit Outputs

- Write cleaned output file.
- Write summary JSON with row counts and quality metrics.
- Write rejected rows when validation fails.

## Resource Usage

- Use `scripts/process_csv.py` for required-column checks, trimming, and summary stats.
- Read `references/data-quality-rules.md` before adding transformations.
- Keep per-project mapping in `assets/transform-spec.yaml`.
