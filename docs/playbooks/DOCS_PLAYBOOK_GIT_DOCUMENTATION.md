Repo Documentation Playbook (GitHub Hygiene, Generic) — v1.2

This playbook is cross-stack (works for any tech stack).
Use it when:

the repo is public, OR

you want release-grade repo hygiene, OR

you’re onboarding collaborators and want consistent contribution flow.

This playbook complements split SSoT docs. It does not replace them.

0) Goal and philosophy

Goal: make the repo understandable, safe to contribute to, and easy to operate.

Philosophy:

Keep canonical engineering truth in split SSoT docs:

docs/ssot/INDEX.md is the entry point

docs/ssot/GOVERNANCE.md defines enforceable rules

docs/contracts/* is API + DB truth

docs/quality/* is testing + security truth

docs/decisions/* is ADR truth

Public-facing documentation should be short and link to SSoT docs rather than duplicating them.

Avoid “docs drift” by keeping one canonical place for each kind of truth.

1) Minimum recommended “Community Health” files (public or shared repos)

These are the standard GitHub-visible docs that improve collaboration and trust.

1.1 README.md (root)
Required for public repos; recommended for shared internal repos.

Keep it short:

What this project is (1 paragraph)

Quickstart (dev)

Test commands

Where authoritative docs live (docs/ssot/INDEX.md)

How to report security issues (link SECURITY.md)

DO NOT duplicate:

architecture details

contract tables

exhaustive endpoints lists
Instead: link to docs/architecture and docs/contracts.

1.2 SECURITY.md (root)
Required for public repos; recommended for internal repos too.

Must include:

private vulnerability reporting instructions

expected response window (e.g., “within 72 hours”)

supported versions policy

link to docs/quality/SECURITY.md for internal baseline

1.3 CONTRIBUTING.md (root)
Required for public repos; recommended for shared internal repos.

Must include:

setup summary (links to docs/quality/TESTING.md)

PR expectations (link to docs/ssot/GOVERNANCE.md and PR template)

“tests + evidence” rule

ADR rule: when required and how to link

1.4 LICENSE (root)
Required for public repos. Choose explicitly.

1.5 CODE_OF_CONDUCT.md (root)
Recommended for public repos. Helps with community trust and qualifies for some tooling/programs.

1.6 SUPPORT.md (optional)
Recommended for public repos if you want to direct users to:

issues vs discussions

support channels

SLA expectations (if any)

2) GitHub meta hygiene (should exist in the template)

These should exist and be consistent with GOVERNANCE:

.github/PULL_REQUEST_TEMPLATE.md

.github/workflows/ci.yml (or multiple workflows)

.github/ISSUE_TEMPLATE/*

bug

feature

epic

CODEOWNERS

Rules:

PR template must include: scope/why/non-goals, tests run + results, docs updated checklist, ADR link or “not required” justification.

Issue templates should force acceptance criteria and reproduction steps where relevant.

3) Required GitHub settings (manual configuration checklist)

This is NOT in code; you must set it in GitHub settings.

Branch protection / rulesets for main:

Require PR to merge

Require CI status checks to pass

Require at least 1 approval (recommended)

Require CODEOWNERS review (recommended for teams)

Disallow force push to main

Require conversation resolution before merge (recommended)

Optionally require signed commits (advanced)

Repository settings:

Disable “merge without review” paths if you want strict governance.

Enable security alerts / dependency scanning features as available.

4) Release hygiene (public or production-grade repos)

Canonical change log:

docs/ssot/CHANGELOG.md is the canonical changelog.

Release process:

Use tags/releases to publish versions.

Mark published versions as FROZEN in The_Project_Offloader.md version table.

Release notes should be derived from CHANGELOG (copy/paste section).

Supported versions policy:

Document in SECURITY.md which versions are supported and for how long.

5) Security documentation (public posture)

5.1 Root SECURITY.md should specify:

where to report vulnerabilities privately (email or GitHub security advisories)

what not to do (don’t open public issues for vulnerabilities)

a response timeline expectation

supported versions

link to docs/quality/SECURITY.md

5.2 If you use GitHub Security Advisories:

Enable “security advisories” in repo settings

Use the advisory workflow for coordinated disclosure

6) Documentation “no bloat” rule (drift prevention)

Keep markdown docs under ~300 lines when possible.

Split big docs by topic and link via docs/ssot/INDEX.md.

One source of truth per topic; avoid repeated copies across docs.

7) Templates you can copy (short + effective)

7.1 README.md minimal template

Project Name

One paragraph describing the project.

Quickstart

Backend:

(link or commands)

Frontend:

(link or commands)

Tests

See docs/quality/TESTING.md

Documentation (SSoT)

Start here: docs/ssot/INDEX.md

Security

See SECURITY.md

7.2 SECURITY.md minimal template

Security Policy
Reporting a Vulnerability

Please do NOT open a public issue.

Report privately via:

GitHub Security Advisories (preferred): <repo url>/security/advisories/new
OR

Email: security@your-domain.com

We aim to respond within: 72 hours.

Supported Versions

Supported: latest release and/or last N minor versions (define policy)

Unsupported: everything else

Additional Security Notes

See docs/quality/SECURITY.md for internal baseline expectations.

7.3 CONTRIBUTING.md minimal template

Contributing
Setup

See docs/quality/TESTING.md for setup and test commands.

Pull Requests

Follow .github/PULL_REQUEST_TEMPLATE.md

CI must pass

Include test evidence (commands + results)

Update docs/contracts when relevant:

API changes → docs/contracts/API.md

DB changes → docs/contracts/DB_SCHEMA.md

Security/auth/audit changes → docs/quality/SECURITY.md

ADRs

An ADR is required for architecture/security/audit/DB migrations/API versioning/CI-governance/testing strategy changes.
See docs/ssot/GOVERNANCE.md and docs/decisions/ADR-0001-template.md.

8) When to apply this playbook vs skip it

Apply fully when:

repo is public

repo is internal but shared across teams

you want open contribution + predictable governance

You can skip most of it (for now) when:

repo is private and single-developer
BUT: still keep split SSoT docs, CI, and PR discipline strong.

9) “Docs readiness” acceptance criteria

Consider docs hygiene “complete” when:

README exists (if public/shared) and links to docs/ssot/INDEX.md

SECURITY.md exists (if public) and provides private reporting path

CONTRIBUTING.md exists (if public/shared) and points to GOVERNANCE + TESTING

CI exists and is required

PR template enforces tests + docs + ADR linkage

Issue templates exist and enforce clarity

Branch protections are enabled and match GOVERNANCE

END FILE: docs/playbooks/DOCS_PLAYBOOK_GIT_DOCUMENTATION.md