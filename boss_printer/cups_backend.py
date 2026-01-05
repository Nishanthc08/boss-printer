"""CUPS integration layer for boss-printer.

This module provides a thin wrapper around common CUPS CLI tools so that the
GUI can remain decoupled from the specific commands.

Commands used (must be available on the system):
- lpstat
- lpoptions
- lp
"""

from __future__ import annotations

from dataclasses import dataclass
from subprocess import CalledProcessError, check_output, run, CompletedProcess
from typing import List, Optional, Tuple


@dataclass
class Printer:
    name: str
    is_default: bool
    description: str | None = None
    device_uri: str | None = None


def _run_cmd(args: list[str]) -> str:
    """Run a command and return stdout as text.

    Raises CalledProcessError if the command fails.
    """

    out = check_output(args, text=True)
    return out


def list_printers() -> List[Printer]:
    """Return a list of printers known to CUPS.

    Uses `lpstat -p -d` to get printer list and default.
    """

    try:
        out = _run_cmd(["lpstat", "-p", "-d"])
    except CalledProcessError:
        return []

    default_name: Optional[str] = None
    printers: list[Printer] = []

    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("system default destination:"):
            # e.g. "system default destination: HP_LaserJet"
            default_name = line.split(":", 1)[1].strip()
        elif line.startswith("printer "):
            # e.g. "printer HP_LaserJet is idle.  enabled since ..."
            parts = line.split()
            if len(parts) >= 2:
                name = parts[1]
                printers.append(Printer(name=name, is_default=False, description=None))

    # Mark default
    if default_name is not None:
        for p in printers:
            if p.name == default_name:
                p.is_default = True
                break

    return printers


def get_default_printer() -> Optional[str]:
    """Return the default printer name, or None if not set."""

    try:
        out = _run_cmd(["lpstat", "-d"])
    except CalledProcessError:
        return None

    for line in out.splitlines():
        line = line.strip()
        if line.startswith("system default destination:"):
            return line.split(":", 1)[1].strip()
    return None


def set_default_printer(name: str) -> Tuple[bool, Optional[str]]:
    """Set the default printer. Returns (True, None) on success or (False, detail) on failure."""

    try:
        run(["lpoptions", "-d", name], check=True)
        return True, None
    except CalledProcessError as e:
        return False, str(e)
    except FileNotFoundError as e:
        return False, str(e)


def print_test_page(name: str) -> Tuple[bool, Optional[str]]:
    """Send a simple test page to the given printer.

    This uses `lp -d <name>` with a small text payload.
    Returns (success, detail).
    """

    test_text = "Boss Printer Test Page\n\nIf you can read this, printing works.\n"
    try:
        proc = run(["lp", "-d", name], input=test_text, text=True, check=True)
        return (proc.returncode == 0), None
    except CalledProcessError as e:
        return False, str(e)
    except FileNotFoundError as e:
        return False, str(e)


def open_queue(name: str) -> Tuple[bool, Optional[str]]:
    """Open the print queue using a generic tool.

    On many desktops `system-config-printer` can show queues. As a very
    simple first implementation, run it if present; otherwise return False
    with a reason.
    """

    try:
        run(["system-config-printer"], check=False)
        return True, None
    except FileNotFoundError as e:
        return False, str(e)
    except CalledProcessError as e:
        return False, str(e)
