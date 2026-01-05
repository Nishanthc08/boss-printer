# Project Progress – boss-printer

Timeline target: **50 days** from project start.

> Update this file as you complete tasks. The goal is to always know "where we are" at a glance.

## Milestones Overview

1. **M1 – Project Foundation (Days 1–5)**
   - [ ] Confirm tech stack (Python + GTK/Qt) and CUPS integration approach
   - [ ] Initialize repo structure and basic Python package
   - [ ] Basic dev environment tooling (`venv`, formatting, linting)

2. **M2 – Core Printer Management (Days 6–18)**
   - [ ] List printers via CUPS
   - [ ] Show printer details and status
   - [ ] Set default printer from GUI
   - [ ] Add/remove printer (wrapping CUPS tools)
   - [ ] View and manage print queues

3. **M3 – Usability & Stability (Days 19–30)**
   - [ ] Polish core GUI layout and navigation
   - [ ] Add error handling and user-friendly messages
   - [ ] Logging of key actions and errors
   - [ ] Basic automated tests for CUPS integration and UI logic

4. **M4 – Government-Office Features (Days 31–45)**
   - [ ] Implement at least one "department profile" preset
   - [ ] Simple watermark/seal support (minimal UI)
   - [ ] Bulk printing helper (basic version)

5. **M5 – Wrap-Up & Packaging (Days 46–50)**
   - [ ] Basic packaging (at least one format, e.g., Debian package or simple installer script)
   - [ ] Documentation pass (user guide + admin notes)
   - [ ] Final bug-bash and polish

## Current Status Snapshot

- **Today**: _Not yet updated_
- **Current Milestone**: M1 – Project Foundation
- **Risks / Blockers**: _None recorded yet_

## Detailed Task Checklist

### M1 – Project Foundation
- [ ] Choose GUI toolkit (GTK vs Qt) and note rationale in `docs/worklog.md`
- [ ] Create initial Python package structure: `boss_printer/`
- [ ] Add basic entry point (CLI or small launcher script)
- [ ] Add `pyproject.toml` or equivalent for dependencies
- [ ] Set up `black`/`isort`/`flake8` or similar tooling

### M2 – Core Printer Management
- [ ] Implement CUPS integration layer (wrapper functions or class)
- [ ] Display printers list in GUI
- [ ] Show printer status (idle, printing, error)
- [ ] Actions: set default, pause/resume, cancel job
- [ ] Job history view (recent jobs)

### M3 – Usability & Stability
- [ ] Refine layout for non-technical users (large buttons, clear labels)
- [ ] Add simple settings panel (e.g., default view, language if needed)
- [ ] Add log viewer inside the app
- [ ] Add unit tests for critical logic

### M4 – Government-Office Features
- [ ] Define 2–3 example department profiles
- [ ] Implement profile selector in UI
- [ ] Implement simple watermark (text/image) in print pipeline
- [ ] Implement minimal bulk print helper (select multiple files, apply a recipe)

### M5 – Wrap-Up & Packaging
- [ ] Prepare minimal user guide in `docs/`
- [ ] Add CHANGELOG or release notes for v0.1
- [ ] Create a basic packaging script or instructions

Update this document frequently so you always know how close you are to the 50-day goal.
