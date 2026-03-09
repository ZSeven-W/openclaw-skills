# OpenClaw Skills

> Reusable skill templates for OpenClaw AI agents

A collection of production-ready skill templates for building AI agents with OpenClaw. Each template includes working scripts, reference docs, and asset configs.

![OpenClaw](https://img.shields.io/badge/OpenClaw-Skills-blue?style=flat)
![MIT License](https://img.shields.io/badge/License-MIT-green.svg)

## Why OpenClaw Skills?

Skip the boilerplate. These templates give you working foundations for common AI agent workflows — just copy, customize, and deploy.

## Templates

### 1. API Integration (`api-integration-template`)
Authenticated REST/JSON API workflows with retries, timeouts, and structured responses.

**Features:**
- Retry logic with exponential backoff
- Timeout handling
- Request/response logging
- Auth header support

**Files:** `SKILL.md`, `scripts/api_request.py`, `references/integration-checklist.md`, `assets/request-template.json`

---

### 2. Data Processing (`data-processing-template`)
Repeatable CSV/tabular data cleaning with validation and quality reporting.

**Features:**
- Required column checks
- Data trimming
- Summary metrics
- Transform specs

**Files:** `SKILL.md`, `scripts/process_csv.py`, `references/data-quality-rules.md`, `assets/transform-spec.yaml`

---

### 3. Web Scraping (`web-scraping-template`)
Policy-aware static page scraping with deterministic extraction.

**Features:**
- robots.txt compliance
- Selector-based parsing
- JSON/CSV output
- Rate limiting

**Files:** `SKILL.md`, `scripts/scrape_static.py`, `references/scraping-playbook.md`, `assets/selectors-template.yaml`

---

### 4. CLI Tool (`cli-tool-template`)
Build safe CLI utilities with clear argument contracts.

**Features:**
- Argparse setup
- Dry-run mode
- Safe file operations
- Usage examples

**Files:** `SKILL.md`, `scripts/new_cli.py`, `references/cli-design-checklist.md`, `assets/arg-spec-template.yaml`

---

### 5. File Processing (`file-processing-template`)
Bulk file operations with collision detection.

**Features:**
- Batch renaming
- Collision detection
- Preview mode
- Operation logging

**Files:** `SKILL.md`, `scripts/batch_rename.py`, `references/file-ops-checklist.md`, `assets/rename-rules.csv`

---

## Usage

### Quick Start

1. Clone this repo:
```bash
git clone https://github.com/ZSeven-W/openclaw-skills.git
cd openclaw-skills
```

2. Choose a template and copy to your OpenClaw skills directory:
```bash
cp -r api-integration-template/ ~/.nvm/.../openclaw/skills/my-api-skill/
```

3. Customize the files for your use case

### Validation

Validate any skill with skill-cli:
```bash
skill-cli validate ./api-integration-template
```

## Requirements

- OpenClaw installed
- Python 3.8+ (for scripts)
- skill-cli (optional, for validation)

## Contributing

Contributions welcome! Add new templates or improve existing ones.

## License

MIT
