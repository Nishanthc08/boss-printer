# Usage

## Running the app (development)

From the project root:

```bash
cd ~/Desktop/nishu/projects/boss-printer
source .myvenv/bin/activate  # or .venv, depending on your setup
./scripts/run-dev.sh
```

This will start the GTK application with a two-pane layout:

- **Left pane** – list of printers discovered via CUPS (`lpstat`).
- **Right pane** – details and actions for the selected printer.

## Printer list

The left pane shows printers reported by CUPS. The default printer is indicated
with a "(default)" suffix in the list.

Use the **Refresh list** button on the right to re-query CUPS (e.g. after
adding/removing printers or changing the default outside the app).

## Selecting a printer

Click a printer in the list to select it. The right pane will update to show:

- The printer name
- Whether it is currently the default printer

## Actions

With a printer selected, you can:

- **Set default** – set the selected printer as the system default using
  `lpoptions -d NAME`.
- **Print test page** – send a small text test page to the selected printer
  using `lp -d NAME`.
- **Open queue** – attempt to open a system print queue tool
  (currently `system-config-printer` if available).

If an action fails (for example, if CUPS commands are unavailable or the
operation is rejected), the app will show a simple error dialog and also update
the status label in the right pane.
