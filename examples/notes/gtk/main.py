import gi

from examples.notes.gtk.ui.MainWindow import MainWindow

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from core.globalstate import GlobalState
from examples.notes.state.notesstate import NotesState


def main():
    GlobalState.set("notes", NotesState())

    window = MainWindow()
    window.connect('destroy', Gtk.main_quit)
    window.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
