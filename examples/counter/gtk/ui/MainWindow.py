import gi

from examples.counter.gtk.ui.DecrementButton import DecrementButton
from examples.counter.gtk.ui.NumberLabel import NumberLabel

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from examples.counter.gtk.ui.IncrementButton import IncrementButton


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Counter")

        self.button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.add(self.button_box)

        self.inc_button = IncrementButton()
        self.number_label = NumberLabel()
        self.dec_button = DecrementButton()
        self.inc_button.set_size_request(60, 60)
        self.number_label.set_size_request(60, 60)
        self.dec_button.set_size_request(60, 60)

        self.button_box.pack_start(child=self.dec_button, expand=True, fill=True, padding=0)
        self.button_box.pack_start(child=self.number_label, expand=True, fill=True, padding=0)
        self.button_box.pack_start(child=self.inc_button, expand=True, fill=True, padding=0)

