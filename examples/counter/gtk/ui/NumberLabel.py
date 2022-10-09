import gi

from core.globalstate import GlobalState
from examples.counter.action.update_number import UpdateNumber

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from core.observer import Observer


class NumberLabel(
    Gtk.Label,
    Observer,
    metaclass=type('GtkLabelObserver', (type(Gtk.Label), type(Observer)), {})
):
    def __init__(self):
        Gtk.Label.__init__(self)
        self.observe(GlobalState.counter.number)
        self.set_label(f"{GlobalState.counter.number.value}")

    def notify_state_changed(self, action):
        if isinstance(action, UpdateNumber):
            self.set_label(f"{GlobalState.counter.number.value}")
