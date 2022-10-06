import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from examples.color_switcher.gtk.ui.Colored import Colored
from examples.color_switcher.gtk.ui.NumberButton import NumberButton


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(500, 500)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(widget=self.box)

        self.button = NumberButton()
        self.colored = Colored()

        self.box.pack_start(child=self.button, expand=True, fill=True, padding=0)
        self.box.pack_start(child=self.colored, expand=True, fill=True, padding=0)
