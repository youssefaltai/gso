from PySide6.QtWidgets import QMainWindow

from examples.color_switcher.pyside6.ui.ContainerWidget import ContainerWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.show()

        self.container_widget = ContainerWidget()
        self.setCentralWidget(self.container_widget)

