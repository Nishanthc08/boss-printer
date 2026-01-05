# Future Enhancements

This document tracks ideas that go beyond the initial MVP. Items here are not commitments; they are a backlog to prioritize over the 50-day timeline.

## 1. Government-Office Workflow Features
- **Department Profiles**: Per-department printer presets (b/w only, duplex off, fixed tray, etc.).
- **Official Seal / Watermark**:
  - Apply standard government seal to the first page only or all pages.
  - Configurable opacity and placement presets.
- **Letterhead Templates**:
  - Store standard letterhead PDFs and auto-merge with outgoing prints.
  - One-click toggle for "Print with letterhead".
- **Bulk Printing Assistant**:
  - Queue multiple documents and define a print recipe (e.g., 3 copies, first page on letterhead, rest plain).
- **Confidential Print Mode**:
  - Forced headers/footers with classification tags (e.g., CONFIDENTIAL, INTERNAL).

## 2. Administration & Control
- **Policy Enforcement**:
  - Restrict color printing for some users/departments.
  - Enforce duplex for long documents.
- **Usage Analytics** (privacy-aware):
  - Count pages per department, per printer.
  - Simple CSV export for monthly reporting.
- **Role-Based Access (Lightweight)**:
  - Admin mode vs regular staff mode (hidden advanced controls).

## 3. UX Improvements
- **Guided Setup Wizard**:
  - Step-by-step add-printer flow with clear progress indicators.
- **Error Helper**:
  - Map common CUPS/driver errors to friendly text and suggested fixes.
- **Test Suites**:
  - "Connectivity test", "Driver test", "Sample document test".

## 4. Technical Enhancements
- **Multiple Backend Support**:
  - Abstract CUPS calls so other backends can be plugged in later if needed.
- **Config Sync**:
  - Export/import printer settings between machines.
- **Packaging**:
  - Debian package (.deb), Flatpak/AppImage for broader distro coverage.

## 5. Nice-to-Have Ideas
- **Dark Mode & Accessibility Tweaks** (high contrast, larger fonts presets).
- **Kiosk Mode** for frontline counters.
- **Scriptable Hooks**:
  - Run a script before/after printing (e.g., log to an internal system).

As the project evolves, items here should be promoted into milestones in `docs/PROGRESS.md` or closed if out of scope.
