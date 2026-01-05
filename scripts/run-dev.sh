#!/usr/bin/env bash

# Simple dev launcher for boss-printer
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="${SCRIPT_DIR}/.."

cd "${PROJECT_ROOT}"

python3 -m boss_printer "$@"
