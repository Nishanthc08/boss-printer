"""Minimal GTK app entry point for boss-printer with printer list UI."""

import sys
from typing import Optional

try:
    import gi  # type: ignore

    gi.require_version("Gtk", "4.0")
    from gi.repository import Gtk
except Exception as exc:  # pragma: no cover
    print("Failed to import GTK 4 via PyGObject.")
    print("On Debian, install: sudo apt install python3-gi gir1.2-gtk-4.0")
    print(f"Details: {exc}")
    sys.exit(1)

from . import cups_backend


class BossPrinterWindow(Gtk.ApplicationWindow):
    def __init__(self, app: Gtk.Application) -> None:
        super().__init__(application=app)
        self.set_title("Boss Printer")
        self.set_default_size(1000, 600)

        # Main layout: horizontal pane – left list, right details
        paned = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        self.set_child(paned)

        # Left: printers list
        self.printer_store = Gtk.ListStore(str, bool)
        self.printer_view = Gtk.TreeView(model=self.printer_store)

        renderer_text = Gtk.CellRendererText()
        col = Gtk.TreeViewColumn("Printers", renderer_text, text=0)
        self.printer_view.append_column(col)

        select = self.printer_view.get_selection()
        select.connect("changed", self.on_printer_selected)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_child(self.printer_view)
        scrolled.set_min_content_width(250)

        paned.set_start_child(scrolled)

        # Right: details + actions
        right_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=12,
            margin_top=12,
            margin_bottom=12,
            margin_start=12,
            margin_end=12,
        )

        self.label_title = Gtk.Label(label="Select a printer")
        self.label_title.set_xalign(0.0)
        self.label_status = Gtk.Label(label="")
        self.label_status.set_xalign(0.0)

        # Action log (show last 5 actions)
        self.action_log: list[str] = []
        self.label_log = Gtk.Label(label="")
        self.label_log.set_xalign(0.0)

        btn_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        self.btn_set_default = Gtk.Button(label="Set default")
        self.btn_test_page = Gtk.Button(label="Print test page")
        self.btn_open_queue = Gtk.Button(label="Open queue")
        self.btn_refresh = Gtk.Button(label="Refresh list")

        self.btn_set_default.connect("clicked", self.on_set_default_clicked)
        self.btn_test_page.connect("clicked", self.on_test_page_clicked)
        self.btn_open_queue.connect("clicked", self.on_open_queue_clicked)
        self.btn_refresh.connect("clicked", self.on_refresh_clicked)

        btn_box.append(self.btn_set_default)
        btn_box.append(self.btn_test_page)
        btn_box.append(self.btn_open_queue)
        btn_box.append(self.btn_refresh)

        right_box.append(self.label_title)
        right_box.append(self.label_status)
        right_box.append(self.label_log)
        right_box.append(btn_box)

        paned.set_end_child(right_box)

        self._load_printers()
        self._update_buttons_enabled_state()

    # --- Helpers ---------------------------------------------------------

    def _load_printers(self) -> None:
        self.printer_store.clear()
        printers = cups_backend.list_printers()
        if not printers:
            self.label_title.set_text("No printers found (CUPS)")
            self.label_status.set_text("")
            return

        for p in printers:
            display = f"{p.name}"
            if p.is_default:
                display += " (default)"
            self.printer_store.append([display, p.is_default])

        self.label_title.set_text("Select a printer")
        self.label_status.set_text("")

    def _get_selected_printer_name(self) -> Optional[str]:
        selection = self.printer_view.get_selection()
        model, tree_iter = selection.get_selected()
        if tree_iter is None:
            return None
        display_name = model[tree_iter][0]
        # Strip " (default)" suffix if present
        if display_name.endswith(" (default)"):
            return display_name[:-10]
        return display_name

    def _show_error(self, message: str, detail: Optional[str] = None) -> None:
        """Display a simple error dialog and also update the status label."""

        self.label_status.set_text(message)
        self._append_action_log(f"ERROR: {message}")

        dialog = Gtk.MessageDialog(
            transient_for=self,
            modal=True,
            buttons=Gtk.ButtonsType.OK,
            message_type=Gtk.MessageType.ERROR,
            text=message,
        )
        if detail:
            dialog.format_secondary_text(detail)
        dialog.connect("response", lambda d, _r: d.destroy())
        dialog.show()

    def _append_action_log(self, msg: str) -> None:
        self.action_log.insert(0, msg)
        # keep last 5
        self.action_log = self.action_log[:5]
        self.label_log.set_text("Recent: " + " | ".join(self.action_log))

    def _update_buttons_enabled_state(self) -> None:
        has_selection = self._get_selected_printer_name() is not None
        self.btn_set_default.set_sensitive(has_selection)
        self.btn_test_page.set_sensitive(has_selection)
        self.btn_open_queue.set_sensitive(has_selection)

    # --- Callbacks -------------------------------------------------------

    def on_printer_selected(self, selection: Gtk.TreeSelection) -> None:
        name = self._get_selected_printer_name()
        self._update_buttons_enabled_state()
        if not name:
            self.label_title.set_text("Select a printer")
            self.label_status.set_text("")
            return

        default = cups_backend.get_default_printer()
        is_default = default == name
        self.label_title.set_text(name)
        self.label_status.set_text(
            "Status: default printer" if is_default else "Status: not default"
        )

    def on_set_default_clicked(self, button: Gtk.Button) -> None:  # noqa: ARG002
        name = self._get_selected_printer_name()
        if not name:
            self._show_error("No printer selected")
            return
        ok, detail = cups_backend.set_default_printer(name)
        if ok:
            self.label_status.set_text(f"Set default printer to {name}")
            self._append_action_log(f"Set default: {name}")
            self._load_printers()
        else:
            self._show_error("Failed to set default printer", detail)

    def on_test_page_clicked(self, button: Gtk.Button) -> None:  # noqa: ARG002
        name = self._get_selected_printer_name()
        if not name:
            self._show_error("No printer selected")
            return
        ok, detail = cups_backend.print_test_page(name)
        if ok:
            self.label_status.set_text("Test page sent")
            self._append_action_log(f"Printed test page: {name}")
        else:
            self._show_error("Failed to send test page", detail)

    def on_open_queue_clicked(self, button: Gtk.Button) -> None:  # noqa: ARG002
        name = self._get_selected_printer_name()
        if not name:
            self._show_error("No printer selected")
            return
        ok, detail = cups_backend.open_queue(name)
        if ok:
            self.label_status.set_text("Opened queue (if available)")
            self._append_action_log(f"Opened queue: {name}")
        else:
            self._show_error("Could not open queue tool", detail)

    def on_refresh_clicked(self, button: Gtk.Button) -> None:  # noqa: ARG002
        self._load_printers()
        self._append_action_log("Refreshed printer list")
        self._update_buttons_enabled_state()


class BossPrinterApp(Gtk.Application):
    def __init__(self) -> None:
        super().__init__(application_id="com.example.boss_printer")

    def do_activate(self) -> None:  # type: ignore[override]
        win = self.props.active_window
        if not win:
            win = BossPrinterWindow(self)
        win.present()


def main(argv: list[str] | None = None) -> int:
    app = BossPrinterApp()
    return app.run(argv or sys.argv)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
