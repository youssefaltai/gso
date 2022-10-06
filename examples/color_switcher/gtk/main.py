import gi

from examples.color_switcher.gtk.ui.MainWindow import MainWindow

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk, Gio


def main():
    css_provider = Gtk.CssProvider()
    css_file = Gio.File.new_for_path("ui/style.css")
    css_provider.load_from_file(css_file)

    Gtk.StyleContext.add_provider_for_screen(
        screen=Gdk.Screen.get_default(),
        provider=css_provider,
        priority=Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )

    window = MainWindow()
    window.connect('destroy', Gtk.main_quit)
    window.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
