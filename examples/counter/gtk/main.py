import gi

from core.globalstate import GlobalState
from examples.counter.gtk.ui.MainWindow import MainWindow
from examples.counter.state.counterstate import CounterState

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


def main():
    GlobalState.set('counter', CounterState())

    window = MainWindow()
    window.connect('destroy', Gtk.main_quit)
    window.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
