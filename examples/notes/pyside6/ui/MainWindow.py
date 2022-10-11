from PySide6.QtWidgets import QMainWindow

from examples.notes.pyside6.ui.ContainerWidget import ContainerWidget


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.show()

        self.container = ContainerWidget()
        self.setCentralWidget(self.container)
