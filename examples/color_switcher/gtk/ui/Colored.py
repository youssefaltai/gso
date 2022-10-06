import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from core.observer import Observer
from examples.color_switcher.state.state import State


class Colored(
    Gtk.Box,
    Observer,
    metaclass=type('GtkBoxObserver', (type(Gtk.Box), type(Observer)), {})
):

    def __init__(self):
        Gtk.Box.__init__(self)
        State.number.attach_observer(self)
        self.get_style_context().add_class(f'{self.color()}')

    def color(self):
        if State.number.value() % 2 == 0:
            return "red"
        else:
            return "blue"

    def notify_state_changed(self, action):
        match action.name:
            case "updateNumber":
                self.get_style_context().remove_class("red")
                self.get_style_context().remove_class("blue")
                self.get_style_context().add_class(f'{self.color()}')
