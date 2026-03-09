---
name: file-processing-template
description: Process files in bulk with deterministic naming, format conversion, filtering, and safe write patterns. Use when renaming large file sets, generating transformed copies, organizing directories, or applying repeatable file-level operations.
---

# File Processing Template

Use this template for batch file operations with preview-first safety.

## Quick Start

1. Define file rules in `references/file-ops-checklist.md`.
2. Copy `assets/rename-rules.csv` and adapt pattern rules.
3. Run `scripts/batch_rename.py --dry-run` first.
4. Execute without dry-run only after verifying preview output.

## Workflow

### 1. Scope Input Set

- Restrict by extension or glob pattern.
- Exclude hidden/system paths.
- Record total candidate count before writes.

### 2. Plan Transform

- Build deterministic target names.
- Detect collisions before applying changes.
- Keep backup/rollback strategy explicit.

### 3. Execute Safely

- Run preview mode first.
- Apply atomic rename operations.
- Log old and new paths for traceability.

## Resource Usage

- Use `scripts/batch_rename.py` for extension-scoped renames with dry-run.
- Read `references/file-ops-checklist.md` before destructive operations.
- Keep rename mapping examples in `assets/rename-rules.csv`.
