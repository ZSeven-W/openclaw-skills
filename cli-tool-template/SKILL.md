---
name: cli-tool-template
description: Create and extend command-line automation tools with clear argument contracts, safe defaults, dry-run support, and validation. Use when building project utilities, operational scripts, developer productivity commands, or repeatable terminal workflows.
---

# CLI Tool Template

Use this template to ship robust CLI skills that are safe for repeated use.

## Quick Start

1. Define command behavior in `references/cli-design-checklist.md`.
2. Copy `assets/arg-spec-template.yaml` and set arguments/options.
3. Generate a starter command with `scripts/new_cli.py`.
4. Add command logic and test `--dry-run` behavior first.

## Workflow

### 1. Define Command Contract

- Specify required positional arguments.
- Specify optional flags with defaults.
- Document side effects clearly.

### 2. Implement Safe Execution

- Add `--dry-run` for write/delete operations.
- Add `--yes` for non-interactive confirmation.
- Validate input paths and parameter ranges before action.

### 3. Emit Useful Output

- Return non-zero exit code on failure.
- Print machine-readable output when useful.
- Keep log output concise and actionable.

## Resource Usage

- Use `scripts/new_cli.py` to generate an argparse-based command skeleton.
- Read `references/cli-design-checklist.md` before adding new subcommands.
- Keep argument contracts in `assets/arg-spec-template.yaml`.
