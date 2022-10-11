from core.observable import Observable
from examples.notes.action.add_note import AddNote


class NotesState:
    def __init__(self):
        self.__notes_list = Observable([])

    @property
    def notes(self):
        return self.__notes_list

    def add_note(self, note):
        self.__notes_list.apply(AddNote(note))
