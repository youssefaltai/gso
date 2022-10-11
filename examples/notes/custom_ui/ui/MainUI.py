from core.globalstate import GlobalState
from core.observer import Observer
from examples.customui.base.View import View
from examples.notes.action.add_note import AddNote


class MainUI(
    View,
    Observer
):
    def __init__(self):
        self.observe(GlobalState.get('notes').notes)
        self.notes = []

    def show(self):
        if len(self.notes) == 0:
            print("Empty notes list")
        for note in self.notes:
            print(note)

    def loop(self):
        while True:
            self.show()
            self.handle_user_input(note=input("> "))

    def handle_user_input(self, note):
        GlobalState.get('notes').add_note(note)

    def notify_state_changed(self, action):
        if isinstance(action, AddNote):
            self.notes.append(action.note)
