from core.globalstate import GlobalState
from examples.notes.custom_ui.ui.MainUI import MainUI
from examples.notes.state.notesstate import NotesState


def main():
    GlobalState.set("notes", NotesState())

    main_ui = MainUI()
    main_ui.loop()


if __name__ == '__main__':
    main()
