import sys

from PySide6.QtWidgets import QApplication

from core.globalstate import GlobalState
from examples.notes.pyside6.ui.MainWindow import MainWindow
from examples.notes.state.notesstate import NotesState


def main():
    GlobalState.set('notes', NotesState())

    app = QApplication([])
    main_window = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
