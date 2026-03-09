# OpenClaw Skill Template Library

Location: `/Users/fini/.openclaw/workspace-coder/clawd-skills`

## Templates

### 1. api-integration-template
Reusable starter for authenticated API workflows (REST/JSON) with retries, timeout handling, and structured response output.

- Core files: `SKILL.md`, `scripts/api_request.py`, `references/integration-checklist.md`, `assets/request-template.json`

### 2. data-processing-template
Starter for repeatable CSV/tabular data cleaning with required-column checks, trimming, and summary metrics.

- Core files: `SKILL.md`, `scripts/process_csv.py`, `references/data-quality-rules.md`, `assets/transform-spec.yaml`

### 3. web-scraping-template
Starter for policy-aware static-page scraping with deterministic extraction and JSON output.

- Core files: `SKILL.md`, `scripts/scrape_static.py`, `references/scraping-playbook.md`, `assets/selectors-template.yaml`

### 4. cli-tool-template
Starter for building safe CLI utilities with clear argument contracts and dry-run-first behavior.

- Core files: `SKILL.md`, `scripts/new_cli.py`, `references/cli-design-checklist.md`, `assets/arg-spec-template.yaml`

### 5. file-processing-template
Starter for bulk file operations with collision detection and preview-first renaming workflows.

- Core files: `SKILL.md`, `scripts/batch_rename.py`, `references/file-ops-checklist.md`, `assets/rename-rules.csv`
