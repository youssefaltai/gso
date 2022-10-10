import sys

from PySide6.QtWidgets import QApplication

from core.globalstate import GlobalState
from examples.counter.pyside6.ui.MainWindow import MainWindow
from examples.counter.state.counterstate import CounterState


def main():
    GlobalState.set("counter", CounterState())

    app = QApplication([])
    main_window = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
