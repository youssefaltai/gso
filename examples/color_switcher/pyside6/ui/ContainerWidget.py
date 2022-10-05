from PySide6.QtWidgets import QWidget, QHBoxLayout

from examples.color_switcher.pyside6.ui.ColoredWidget import ColoredWidget
from examples.color_switcher.pyside6.ui.NumberButtonWidget import NumberButtonWidget
from examples.color_switcher.state.state import State


class ContainerWidget(QWidget):
    def __init__(self) -> None:
        super(ContainerWidget, self).__init__()
        self.setLayout(QHBoxLayout(self))

        self.left_colored_widget: ColoredWidget = ColoredWidget("even")
        self.right_colored_widget: ColoredWidget = ColoredWidget("odd")
        self.number_button_widget: NumberButtonWidget = NumberButtonWidget(f"{State.number.value()}")

        self.layout().addWidget(self.left_colored_widget)
        self.layout().addWidget(self.number_button_widget)
        self.layout().addWidget(self.right_colored_widget)
