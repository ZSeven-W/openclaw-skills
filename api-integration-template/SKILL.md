---
name: api-integration-template
description: Build and maintain authenticated API integrations with predictable request/response handling, retries, pagination, and error classification. Use when implementing REST/JSON API calls, syncing external systems, troubleshooting API failures, or creating reusable API client scripts.
---

# API Integration Template

Use this template to implement API integration skills quickly and safely.

## Quick Start

1. Define API constraints in `references/integration-checklist.md`.
2. Copy `assets/request-template.json` and fill endpoint, auth, and payload shape.
3. Run `scripts/api_request.py` for a baseline call.
4. Add endpoint-specific logic only after baseline call succeeds.

## Workflow

### 1. Capture Contract

- Record base URL, auth type, and required headers.
- Record idempotent vs non-idempotent endpoints.
- Record pagination model (`page`, `cursor`, or `next_url`).

### 2. Validate Auth

- Load secret from environment variables only.
- Perform a read-only endpoint call first.
- Fail early on missing token, invalid scope, or expired credentials.

### 3. Execute Requests Safely

- Retry transient failures only (`429`, `500`, `502`, `503`, `504`).
- Use bounded retries with backoff and jitter.
- Log request metadata without leaking secrets.

### 4. Normalize and Persist

- Convert responses to deterministic JSON.
- Keep an `errors` array with error class and status code.
- Persist outputs to a timestamped file for replay/debugging.

## Resource Usage

- Use `scripts/api_request.py` for authenticated calls with retry and optional body input.
- Read `references/integration-checklist.md` before implementing a new integration.
- Start from `assets/request-template.json` to avoid inconsistent input shape.

## Customization Points

- Replace token header logic if API uses API key or OAuth refresh flow.
- Add endpoint-specific validators in script output post-processing.
- Extend retry list only if API docs recommend it.
