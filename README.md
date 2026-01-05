# boss-printer

Linux Printer Management GUI aimed at simplifying printer setup and centralizing print operations, with a focus on government-office workflows.

## Overview

boss-printer is a desktop GUI tool for Linux that:
- Simplifies printer discovery, setup, and driver configuration
- Centralizes common printing operations (test pages, queue management, defaults)
- Exposes government-office–specific workflows (bulk document handling, stamp/seal overlays, strict defaults)
- Wraps common CLI tools (CUPS utilities, lpstat, lpadmin, etc.) behind a single, user-friendly interface

## High-Level Goals
- Be usable by non-technical staff with minimal training
- Provide predictable, repeatable printer behavior across machines
- Reduce support load by surfacing clear errors and auto-fix suggestions
- Remain distro-friendly (Debian-first, but not Debian-only) and avoid locking into any single desktop environment

## Initial Feature Scope (v0.1)
- Printer discovery (via CUPS) and listing
- Add / remove printer from GUI
- View and manage print queue for a selected printer
- Basic printer settings: default printer, page size, orientation, duplex toggle
- Print test page
- Simple log view for recent print actions and errors

## Government-Office–Focused Features (Planned)
See `docs/future_enhancements.md` for the evolving list. Initial ideas include:
- Predefined profiles ("Dispatch", "Accounts", "Records", etc.)
- Watermark / seal presets
- Enforcing b/w-only printing for some departments
- Bulk printing helpers with templated cover sheets

## Tech Stack (Proposed)
- Language: Python (for fast iteration and strong Linux ecosystem)
- GUI Toolkit: GTK (via PyGObject) or Qt (via PySide6) — final choice TBD
- Printing backend: CUPS via system commands and/or Python bindings

## Repo Layout (proposed)
- `boss_printer/` – application source
- `docs/` – documentation (including future enhancements and worklog)
- `tests/` – automated tests (unit, integration where feasible)
- `scripts/` – helper scripts (dev setup, packaging helpers)

## Project Management Docs
This repository includes the following project-tracking docs:
- `README.md` – this file, project overview and usage
- `docs/PROGRESS.md` – current milestone status and checklist
- `docs/worklog.md` – day-by-day (or session-by-session) log of progress
- `docs/future_enhancements.md` – backlog of ideas beyond current scope

## Getting Started (Dev)

### Prerequisites
- Debian or other Linux distro with CUPS installed and running
- Python 3.10+ (TBD based on your environment)
- `pip` / `venv` for dependency management

### Basic Dev Setup (Draft)
```bash
cd ~/Desktop/nishu/projects/boss-printer
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

> NOTE: Packaging and a proper `pyproject.toml`/`setup.cfg` will be added once the stack is finalized.

## Status
- Project scaffold: IN PROGRESS
- Core GUI design: IN PROGRESS
- CUPS integration: IN PROGRESS
- Packaging: NOT STARTED

For a detailed, date-based breakdown, see `docs/PROGRESS.md` and `docs/worklog.md`.

For how to run and use the current prototype UI, see `docs/usage.md`.