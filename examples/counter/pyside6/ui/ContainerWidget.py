from PySide6.QtWidgets import QWidget, QHBoxLayout

from examples.counter.pyside6.ui.DecrementButton import DecrementButton
from examples.counter.pyside6.ui.IncrementButton import IncrementButton
from examples.counter.pyside6.ui.NumberLabel import NumberLabel


class ContainerWidget(QWidget):
    def __init__(self) -> None:
        super(ContainerWidget, self).__init__()
        self.setLayout(QHBoxLayout(self))

        self.inc_button = IncrementButton(self)
        self.dec_button = DecrementButton(self)
        self.number_label = NumberLabel(self)

        self.layout().addWidget(self.dec_button)
        self.layout().addWidget(self.number_label)
        self.layout().addWidget(self.inc_button)
