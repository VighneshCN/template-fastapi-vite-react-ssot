# Windows Release Checklist (FastAPI + Vite/React + PyInstaller)

## Preflight
- [ ] Repo is clean
- [ ] CI green on release branch/tag
- [ ] Changelog updated
- [ ] Offloader version table updated (ACTIVE/FROZEN rules)

## Frontend (Vite)
- [ ] cd apps/web
- [ ] npm install
- [ ] npm run test
- [ ] npm run build
- [ ] Confirm apps/web/dist exists and has index.html

## Sync static to backend
- [ ] Copy apps/web/dist -> apps/api/static
- [ ] Confirm apps/api/static/index.html exists

## PyInstaller build
- [ ] UPX disabled, debug=false, strip=false, runtime_hooks=[]
- [ ] Version info + manifest embedded when present
- [ ] Single-folder COLLECT build
- [ ] Release policy: console=false (mandatory)
- [ ] tkinter excluded unless explicitly required (license dialog etc.)
- [ ] Run: pyinstaller tools/build/pyinstaller/fastapi_vite_profile.spec

## Smoke test
- [ ] Launch EXE from dist
- [ ] UI renders (static assets present)
- [ ] No missing module errors
- [ ] Critical workflows do not crash

## Signing + reputation
- [ ] Code-sign EXE (+ DLLs ideally) + timestamp
- [ ] VirusTotal preflight
- [ ] Submit false-positive reports if needed

## Publish & freeze
- [ ] Tag release
- [ ] Mark version FROZEN in offloader
- [ ] Archive signed artifacts
