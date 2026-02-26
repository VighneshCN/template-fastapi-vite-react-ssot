# Security Baseline (SSoT)

## Auth (baseline expectation)
- Email OTP -> JWT issuance is the default expected pattern.
- Decide TTL, rate limits, lockouts (ADR if meaningful).

## Authorization
- Define roles/permissions model (ADR if meaningful).

## Admin boundary
- Admin functions must be protected; no “admin by obscurity”.

## Audit logging (required)
Audit must be timestamped, persistent, and reviewable.
Minimum fields:
- timestamp, actor, action, resource, metadata, ip, user_agent

Must record:
- auth attempts, OTP verification, token issuance/refresh/revoke
- admin actions
- destructive ops / exports

## OWASP hygiene (baseline)
- input validation
- safe error handling (no secret leaks)
- CORS configured intentionally
- secrets not committed to repo
