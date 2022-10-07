from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget, QStyleOption, QStyle

from core.action import Action
from core.globalstate import GlobalState
from core.observer import Observer


class ColoredWidget(
    QWidget,
    Observer,
    metaclass=type('QWidgetObserverMetaClass', (type(QWidget), type(Observer)), {})
):
    def __init__(self, parity: str) -> None:
        super(ColoredWidget, self).__init__()
        self.observe(GlobalState.colorswitcher.number)
        self.parity = parity
        self.update_color(self.color())

    def color(self):
        match self.parity:
            case "even":
                return "red" if GlobalState.colorswitcher.number.value() % 2 == 0 else "blue"
            case "odd":
                return "red" if GlobalState.colorswitcher.number.value() % 2 != 0 else "blue"

    def update_color(self, new_color: str) -> None:
        self.setStyleSheet(f"background-color: {new_color}")

    def notify_state_changed(self, action: Action):
        match action.name:
            case "updateNumber":
                self.update_color(self.color())

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)
