from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QSizePolicy

from core.globalstate import GlobalState
from core.observer import Observer


class NumberLabel(
    QLabel,
    Observer,
    metaclass=type('QLabelObserver', (type(QLabel), type(Observer)), {})
):
    def __init__(self, parent):
        QLabel.__init__(self, parent=parent)
        self.observe(GlobalState.counter.number)
        self.setText(f"{GlobalState.counter.number.value}")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def notify_state_changed(self, action):
        match action.name:
            case "numberChanged":
                self.setText(f"{GlobalState.counter.number.value}")
