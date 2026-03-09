---
name: web-scraping-template
description: Extract structured data from websites with robots awareness, request throttling, selector-based parsing, and reproducible output. Use when collecting data from public pages, monitoring page changes, or converting HTML content into JSON/CSV datasets.
---

# Web Scraping Template

Use this template to build polite and maintainable scraping skills.

## Quick Start

1. Record site constraints and allowed paths in `references/scraping-playbook.md`.
2. Copy `assets/selectors-template.yaml` and define extraction selectors.
3. Run `scripts/scrape_static.py` against one URL first.
4. Add pagination and batching only after single-page extraction is stable.

## Workflow

### 1. Check Access Policy

- Read robots.txt when present.
- Avoid protected/private areas.
- Respect terms and rate limits.

### 2. Build Deterministic Selectors

- Prefer stable IDs/data attributes over brittle class chains.
- Extract text content and links separately.
- Keep fallback selector strategy documented.

### 3. Throttle and Retry

- Add fixed delay between requests.
- Retry transient errors with small backoff.
- Stop on repeated blocks/captcha.

### 4. Validate Output

- Verify required fields per record.
- Track source URL and scrape timestamp.
- Emit structured JSON for downstream processing.

## Resource Usage

- Use `scripts/scrape_static.py` for static pages without browser automation.
- Read `references/scraping-playbook.md` for policy and reliability rules.
- Keep extraction configuration in `assets/selectors-template.yaml`.
