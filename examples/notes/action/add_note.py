from core.action import Action


class AddNote(Action):
    def __init__(self, note):
        self.note = note

    def __call__(self, notes_list):
        return [*notes_list, self.note]
