🔨 Windows Build / Packaging Excellence (FastAPI + Vite/React) — v2.0

Use this playbook when preparing a Python FastAPI application (serving a Vite/React UI as static assets) for Windows desktop distribution.

GOAL: Build optimization + security hardening + antivirus compatibility.
TARGET: 0 detections on VirusTotal; ACCEPTABLE: ≤2 generic/heuristic detections (document and investigate).

1) PYINSTALLER SPEC FILE CONFIGURATION (Canonical + AV-friendly)
1.1 Critical security settings (do not change lightly)

These settings reduce AV false positives and increase Windows compatibility:

block_cipher = None (no encryption — encryption can trigger heuristics)

upx = False (NEVER use UPX — common AV trigger)

debug = False (debug patterns look suspicious)

strip = False (stripping can break compatibility and look suspicious)

Always include:

version = version_info_path (Windows version resource)

manifest = manifest_path (Windows security manifest)

console policy:

beta/testing: console=True

RELEASE: console=False (MANDATORY)

1.2 Data files pattern (FastAPI + Vite/React)

For this stack, static assets must be bundled.

Monorepo flow:

Build frontend:

cd apps/web

npm install

npm run build

Copy:

apps/web/dist → apps/api/static

Bundle apps/api/static via PyInstaller datas (CRITICAL)

Data files pattern example (adapted from your earlier proven approach):

static (frontend assets) — REQUIRED

data/reference (JSON/reference)

config/master/templates (as needed)

optional seed DB file (only if you intentionally ship it)

Verify sources exist before build (warn if missing).

1.3 Recommended exclusions (reduce size & AV triggers)

Keep production builds lean by excluding dev/test stacks, unused drivers, heavy libs, etc.

IMPORTANT POLICY:

tkinter must be excluded unless explicitly required (e.g., license activation dialog).
If it IS required, document why and remove it from excludes for that release.

2) WINDOWS VERSION INFO FILE (build/version_info.txt)

Create this file for Windows executable metadata (reputation + trust signals):

Key points to keep:

all version numbers must be numeric (x.x.x.x; no “beta” text)

OriginalFilename must match the actual EXE name

Comments should include your GitHub/website URL (verification)

Use the template from the earlier prompt as the base. (Keep it in repo under build/version_info.txt.)

3) WINDOWS MANIFEST FILE (build/app.manifest)

Create this XML manifest to declare Windows security + compatibility attributes.

Critical properties:

requestedExecutionLevel level="asInvoker" (no admin prompt = less suspicious)

supportedOS IDs (declares legitimate Windows targeting)

DPI awareness + long path awareness (modern app behavior)

Common-Controls dependency (standard Windows UI controls)

Why this helps (keep this rationale in mind):

asInvoker: no privilege escalation

supportedOS: legitimate targeting

dpiAwareness: expected modern behavior

common-controls: standard UI components

4) STATIC FILE PATH RESOLUTION (Bundled vs Dev)

For FastAPI apps serving static web UIs, bundled static files need dynamic resolution.
Use this approach (MEIPASS + fallbacks):

Dev mode: resolve relative to source tree

Bundled mode: resolve relative to sys._MEIPASS

Fallback paths for newer PyInstaller layouts: _internal/static, cwd/static

Mount static in FastAPI using the resolved directory:

Monorepo note:

In dev, static may be served from apps/api/static (after you copy dist)

In release, the bundled static should be found by the resolver

5) INNO SETUP INSTALLER CONFIGURATION (build/installer.iss)

If you distribute an installer, use Inno Setup with trust-friendly defaults.

Essential settings (carry over as-is, adapt names):

PrivilegesRequired=lowest (user-level install = less suspicious)

LicenseFile=LICENSE_FULL.txt

WizardStyle=modern

VersionInfoVersion must be numeric (no “beta” text)

Uninstall behavior and optional uninstall cleanup section

5.1 LICENSE_FULL.txt template

Include a clear license + terms + privacy + disclaimer + support section (template from earlier prompt).

6) PRE-DISTRIBUTION CHECKLIST (Do not skip)

Build verification checklist:

app starts without errors

features work in bundled mode

static files load correctly

DB operations work

file I/O works

no missing module errors

Security verification:

version info visible in file properties

no UAC prompt on launch (manifest working)

EXE size reasonable (not “compressed suspiciously”)

Installer verification (if using Inno):

license displays

install dir choice works

shortcuts work

app launches after install

uninstall appears in Add/Remove Programs and removes cleanly

VirusTotal check policy:

upload installer

target 0 detections

acceptable ≤2 generic/heuristic detections

record SHA256 for traceability

7) CODE SIGNING (Production)

Code signing is one of the strongest levers for AV + SmartScreen reputation.

Free option (OSS) — SignPath:

URL: https://about.signpath.io/oss-code-signing

requirements: public repo, OSI license, Code of Conduct, active history

benefit: free EV-equivalent signing path

Paid options (examples; costs vary):

DigiCert (EV)

Sectigo (EV)

SSL.com (Standard)

Signing command template:

use SHA256 + timestamping

sign EXE (and preferably DLLs too)

8) FALSE POSITIVE SUBMISSION (If needed)

If any AV still flags after all optimizations, submit false positive reports:

Microsoft, Avast, Kaspersky, ESET, Bitdefender, Norton

(Keep the vendor table from the earlier prompt.)

9) QUICK REFERENCE COMMANDS

Keep these handy for release operations:

build with PyInstaller (clean + noconfirm)

compile Inno Setup installer (ISCC.exe)

compute SHA256 hash

verify version info embedded

check file size

10) PROVEN RESULTS (Use as a benchmark, not a guarantee)

The earlier prompt reports a proven benchmark of improved VirusTotal results for a FastAPI + React bundle:

before: detections present

after: 0/72 detections
Key factors cited:

UPX disabled

manifest asInvoker

complete version info + URL

professional installer with license

Note: detection outcomes can vary by environment, certificate reputation, and vendor heuristics, but this benchmark is the target posture.

11) Stack-specific policies (this repo)

Frontend build tool: Vite (Node + npm install)

Static assets must be bundled and resolvable in dev + bundled modes

Release builds must set: console=False

tkinter excluded unless explicitly required (license dialog etc.)

Canonical spec must live in repo (no local-only specs)

Meaningful build profile changes require ADR

END FILE