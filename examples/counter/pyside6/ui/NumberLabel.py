from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QSizePolicy

from core.globalstate import GlobalState
from core.observer import Observer
from examples.counter.action.update_number import UpdateNumber


class NumberLabel(
    QLabel,
    Observer,
    metaclass=type('QLabelObserver', (type(QLabel), type(Observer)), {})
):
    def __init__(self, parent):
        QLabel.__init__(self, parent=parent)
        self.observe(GlobalState.get("counter").number)
        self.setText(f'{GlobalState.get("counter").number.value}')
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def notify_state_changed(self, action):
        if isinstance(action, UpdateNumber):
            self.setText(f'{GlobalState.get("counter").number.value}')
