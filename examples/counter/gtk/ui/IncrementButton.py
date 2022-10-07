import gi

from core.globalstate import GlobalState

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from core.action import Action


class IncrementButton(
    Gtk.Button
):
    def __init__(self, label: str = None):
        Gtk.Button.__init__(self, label=label)
        self.add(widget=Gtk.Image.new_from_icon_name("list-add-symbolic", Gtk.IconSize.BUTTON))

        self.connect(
            'clicked',
            lambda btn:
            GlobalState.counter.dispatch(
                Action(
                    'incrementNumber',
                    {
                        "amount": 1
                    }
                )
            )
        )
