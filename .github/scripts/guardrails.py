import os
import re
import subprocess
import sys

def sh(cmd: str) -> str:
    return subprocess.check_output(cmd, shell=True, text=True).strip()

def main():
    base = os.getenv("GITHUB_BASE_REF")
    if base:
        sh("git fetch --depth=1 origin +refs/heads/*:refs/remotes/origin/*")
        diff = sh(f"git diff --name-only origin/{base}...HEAD")
    else:
        diff = sh("git diff --name-only HEAD~1...HEAD")

    changed = [x for x in diff.splitlines() if x.strip()]
    changed_set = set(changed)

    def changed_any(prefixes):
        return any(any(f.startswith(p) for p in prefixes) for f in changed_set)

    backend_core = changed_any(["apps/api/"])
    frontend_core = changed_any(["apps/web/"])
    api_touched = changed_any(["apps/api/routers/"])
    db_touched = changed_any(["apps/api/models/", "apps/api/db/"])

    docs_adr_changed = any(f.startswith("docs/decisions/") and f.endswith(".md") for f in changed_set)
    api_contract_changed = "docs/contracts/API.md" in changed_set
    db_contract_changed = "docs/contracts/DB_SCHEMA.md" in changed_set

    pr_body = os.getenv("PR_BODY", "") or ""
    adr_just = re.search(r"ADR not required because:", pr_body, re.IGNORECASE)

    failures = []

    if api_touched and not api_contract_changed:
        failures.append("API routes changed but docs/contracts/API.md was not updated.")

    if db_touched and not db_contract_changed:
        failures.append("DB layer changed but docs/contracts/DB_SCHEMA.md was not updated.")

    if (backend_core or frontend_core) and not docs_adr_changed and not adr_just:
        failures.append("Code changed but no ADR and no 'ADR not required because:' in PR body.")

    if failures:
        print("\nGUARDRAILS FAILED:\n- " + "\n- ".join(failures))
        sys.exit(1)

    print("Guardrails OK.")

if __name__ == "__main__":
    main()