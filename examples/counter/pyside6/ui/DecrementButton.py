from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QSizePolicy

from core.action import Action
from core.globalstate import GlobalState


class DecrementButton(QPushButton):
    def __init__(self, parent):
        QPushButton.__init__(self, parent=parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setIcon(QIcon("./../icons/list-remove-symbolic.svg"))
        self.clicked.connect(
            lambda:
            GlobalState.get("counter").decrementNumber(1)
        )
