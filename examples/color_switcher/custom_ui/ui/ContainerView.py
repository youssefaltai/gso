from core.action import Action
from examples.color_switcher.state.state import State
from examples.color_switcher.custom_ui.ui.ButtonView import ButtonView
from examples.color_switcher.custom_ui.ui.ColoredView import ColoredView
from examples.color_switcher.custom_ui.customui.base.View import View


class ContainerView(View):
    def __init__(self):
        self.colored_view = ColoredView("even")
        self.button_view = ButtonView(f"{State.number.value()}")

        self.button_view.add_on_click_listener(
            lambda:
            State.dispatch(
                Action(
                    "updateNumber",
                    {"number": State.number.value() + 1}
                )
            )
        )

    def show(self):
        return f"{self.button_view}\n{self.colored_view}"

    def __repr__(self):
        return self.show()
