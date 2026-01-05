# Developer docs

This file collects short how-tos useful to contributors working on the boss-printer
project on a local dev machine running Debian (or similar).

## Run tests

From the project root in the virtualenv:

```bash
source .myvenv/bin/activate  # or .venv
pytest -q
```

## Run the app (dev)

```bash
cd ~/Desktop/nishu/projects/boss-printer
source .myvenv/bin/activate
./scripts/run-dev.sh
```

## Linting

We recommend `ruff` for fast linting. Install in your venv and run:

```bash
pip install ruff
ruff .
```

## CI

See `.github/workflows/ci.yml` (added later) for the CI configuration used for
running tests and linters on pushes and PRs.
