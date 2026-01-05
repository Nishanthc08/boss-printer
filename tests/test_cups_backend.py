from unittest.mock import patch
import boss_printer.cups_backend as cb

LPSTAT_OUTPUT = "system default destination: HP_LaserJet\nprinter HP_LaserJet is idle.  enabled\nprinter Office_Printer is idle. enabled\n"

@patch("boss_printer.cups_backend._run_cmd", return_value=LPSTAT_OUTPUT)
def test_list_printers(mock_run):
    printers = cb.list_printers()
    names = [p.name for p in printers]
    assert "HP_LaserJet" in names
    assert "Office_Printer" in names
    assert any(p.is_default for p in printers)
