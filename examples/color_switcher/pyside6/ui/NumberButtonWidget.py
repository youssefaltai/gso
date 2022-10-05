from PySide6.QtWidgets import QPushButton, QSizePolicy

from core.action import Action
from core.observer import Observer
from examples.color_switcher.state.state import State


class NumberButtonWidget(
    QPushButton,
    Observer,
    metaclass=type('QPushButtonObserverMetaClass', (type(QPushButton), type(Observer)), {})
):
    def __init__(self, text: str) -> None:
        QPushButton.__init__(self, text=text)
        Observer.__init__(self)
        State.number.attach_observer(self)
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)

        self.clicked.connect(
            lambda:
            State.dispatch(
                Action(
                    "updateNumber", {
                        "number": State.number.value() + 1
                    }
                )
            )
        )

    def notify(self, action: Action):
        match action.name:
            case "updateNumber":
                self.setText(f"{State.number.value()}")
