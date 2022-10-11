import gi

from core.globalstate import GlobalState
from core.observer import Observer
from examples.notes.action.add_note import AddNote

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk


class MainWindow(
    Gtk.Window,
    Observer,
    metaclass=type(
        'GtkWindowObserver',
        (type(Gtk.Window), type(Observer)),
        {}
    )
):
    def notify_state_changed(self, action):
        if isinstance(action, AddNote):
            note_item = Gtk.ListBoxRow()
            box = Gtk.Box()
            note_label = Gtk.Label(label=action.note)
            box.pack_start(child=note_label, expand=True, fill=True, padding=0)
            note_item.add(box)
            self.notes_list.add(note_item)
            self.show_all()

    def __init__(self):
        Gtk.Window.__init__(self)
        self.observe(GlobalState.get('notes').notes)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        self.notes_list = Gtk.ListBox()
        self.box.pack_start(child=self.notes_list, expand=True, fill=True, padding=0)

        self.entry = Gtk.Entry()
        self.box.pack_start(child=self.entry, expand=False, fill=True, padding=0)

        self.entry.connect('key-press-event', self.handle_on_key_pressed_entry)

    def handle_on_key_pressed_entry(self, widget, eventkey):
        note = widget.get_text()
        if eventkey.keyval == Gdk.KEY_Return:
            GlobalState.get('notes').handle_user_input(note)
            widget.set_text('')
