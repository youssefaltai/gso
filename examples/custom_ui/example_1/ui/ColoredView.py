from core.observer import Observer
from examples.custom_ui.example_1.state.state import State
from examples.custom_ui.example_1.ui.base.View import View


class ColoredView(View, Observer):
    def __init__(self, color, parity):
        State.number.attach_observer(self)

        self.parity = parity
        self.color = color

    def update_color(self, new_color):
        self.color = new_color

    def notify(self, action):
        match action.name:
            case "updateNumber":
                match self.parity:
                    case "even":
                        self.update_color("red" if action.payload["number"] % 2 == 0 else "blue")
                    case "odd":
                        self.update_color("blue" if action.payload["number"] % 2 == 0 else "red")

    def show(self):
        return f"{self.color}"

    def __repr__(self):
        return self.show()
