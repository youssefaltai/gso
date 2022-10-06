import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from core.action import Action
from core.observer import Observer
from examples.color_switcher.state.state import State


class NumberButton(
    Gtk.Button,
    Observer,
    metaclass=type('GtkButtonObserver', (type(Gtk.Button), type(Observer)), {})
):
    def __init__(self, label: str = None):
        Gtk.Button.__init__(self, label=label)
        State.number.attach_observer(self)
        self.set_label(label=f"{State.number.value()}")

        self.connect(
            'clicked',
            lambda btn:
            State.dispatch(
                Action(
                    'updateNumber',
                    {
                        "number": State.number.value() + 1
                    }
                )
            )
        )

    def notify_state_changed(self, action):
        match action.name:
            case 'updateNumber':
                self.set_label(f'{State.number.value()}')
