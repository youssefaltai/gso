import sys

from PySide6.QtWidgets import QApplication

from examples.color_switcher.pyside6.ui.MainWindow import MainWindow


def main():
    app = QApplication([])
    main_window = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
