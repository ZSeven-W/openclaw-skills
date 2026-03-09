# Integration Checklist

## Required Inputs

- `base_url`
- `endpoint`
- `method`
- `auth_type` (`bearer`, `api_key`, `none`)
- `timeout_seconds`

## Auth Rules

- Keep credentials in environment variables.
- Never write credentials to logs.
- Validate auth with a read-only endpoint before write endpoints.

## Retry Rules

- Retry only transient status codes: `429, 500, 502, 503, 504`.
- Use max 4 attempts unless API guidance says otherwise.
- Use exponential backoff.

## Output Rules

- Emit JSON with stable key ordering when possible.
- Include source request metadata: URL, method, status, duration.
- Include machine-readable error category on failure.
