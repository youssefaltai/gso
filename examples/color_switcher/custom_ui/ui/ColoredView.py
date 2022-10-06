from core.observer import Observer
from examples.color_switcher.state.state import State
from examples.color_switcher.custom_ui.customui.base.View import View


class ColoredView(View, Observer):
    def __init__(self, parity):
        State.number.attach_observer(self)
        self.parity: str = parity
        self.update_color(self.color())

    def update_color(self, new_color: str) -> None:
        self.displayed_color = new_color

    def notify_state_changed(self, action):
        match action.name:
            case "updateNumber":
                self.update_color(self.color())

    def color(self):
        match self.parity:
            case "even":
                return "red" if State.number.value() % 2 == 0 else "blue"
            case "odd":
                return "red" if State.number.value() % 2 != 0 else "blue"

    def show(self):
        return f"{self.color()}"

    def __repr__(self):
        return self.show()
