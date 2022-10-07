from PySide6.QtWidgets import QWidget, QVBoxLayout

from core.globalstate import GlobalState
from examples.counter.pyside6.ui.ColoredWidget import ColoredWidget
from examples.counter.pyside6.ui.NumberButtonWidget import NumberButtonWidget


class ContainerWidget(QWidget):
    def __init__(self) -> None:
        super(ContainerWidget, self).__init__()
        self.setLayout(QVBoxLayout(self))

        self.number_button_widget: NumberButtonWidget = NumberButtonWidget(f"{GlobalState.colorswitcher.number.value()}")
        self.colored_widget: ColoredWidget = ColoredWidget("even")

        self.layout().addWidget(self.number_button_widget)
        self.layout().addWidget(self.colored_widget)
