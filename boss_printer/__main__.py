"""Minimal GTK app entry point for boss-printer."""

import sys

try:
    import gi  # type: ignore

    gi.require_version("Gtk", "4.0")
    from gi.repository import Gtk
except Exception as exc:  # pragma: no cover
    print("Failed to import GTK 4 via PyGObject.")
    print("On Debian, install: sudo apt install python3-gi gir1.2-gtk-4.0")
    print(f"Details: {exc}")
    sys.exit(1)


class BossPrinterWindow(Gtk.ApplicationWindow):
    def __init__(self, app: Gtk.Application) -> None:
        super().__init__(application=app)
        self.set_title("Boss Printer")
        self.set_default_size(800, 600)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12, margin_top=12,
                      margin_bottom=12, margin_start=12, margin_end=12)

        label = Gtk.Label(label="Boss Printer – Linux Printer Management GUI")
        label.set_wrap(True)

        sub = Gtk.Label(
            label=(
                "This is a placeholder window. Next steps:\n"
                "- List printers via CUPS on the left.\n"
                "- Show selected printer details and actions on the right.\n"
            )
        )
        sub.set_wrap(True)

        box.append(label)
        box.append(sub)
        self.set_child(box)


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
