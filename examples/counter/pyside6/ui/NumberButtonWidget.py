from PySide6.QtWidgets import QPushButton, QSizePolicy

from core.action import Action
from core.globalstate import GlobalState
from core.observer import Observer


class NumberButtonWidget(
    QPushButton,
    Observer,
    metaclass=type('QPushButtonObserverMetaClass', (type(QPushButton), type(Observer)), {})
):
    def __init__(self, text: str) -> None:
        QPushButton.__init__(self, text=text)
        Observer.__init__(self)
        GlobalState.colorswitcher.number.attach_observer(self)
        self.observe(GlobalState.colorswitcher.number)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

        self.clicked.connect(
            lambda:
            GlobalState.colorswitcher.dispatch(
                Action(
                    "updateNumber", {
                        "number": GlobalState.colorswitcher.number.value() + 1
                    }
                )
            )
        )

    def notify_state_changed(self, action: Action):
        match action.name:
            case "updateNumber":
                self.setText(f"{GlobalState.colorswitcher.number.value()}")
