from core.action import Action
from state.state import State
from ui.ButtonView import ButtonView
from ui.ColoredView import ColoredView
from ui.base.View import View


class ContainerView(View):
    def __init__(self):
        self.left_view = ColoredView("red", "even")
        self.number_button_view = ButtonView(f"{State.data['number'].value()}")
        self.right_view = ColoredView("blue", "odd")

        self.number_button_view.add_on_click_listener(
            lambda:
            State.dispatch(
                Action(
                    "updateNumber",
                    {"number": State.data["number"].value() + 1}
                )
            )
        )

    def show(self):
        return f"{self.left_view} {self.number_button_view} {self.right_view}"

    def __repr__(self):
        return self.show()