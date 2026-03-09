# Scraping Playbook

## Compliance First

- Confirm scraping is allowed.
- Honor robots directives when applicable.
- Avoid collecting personal/sensitive data unless explicitly permitted.

## Reliability

- Use stable selectors.
- Keep user-agent explicit and non-deceptive.
- Implement delay between requests to reduce load.

## Output Contract

- Include `source_url` and `scraped_at` per record.
- Keep schema stable between runs.
- Store raw HTML snapshot when debugging extraction failures.
