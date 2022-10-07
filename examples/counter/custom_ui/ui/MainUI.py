from core.action import Action
from core.globalstate import GlobalState
from examples.counter.custom_ui.customui.base.View import View
from examples.counter.custom_ui.ui.DecrementButton import DecrementButton
from examples.counter.custom_ui.ui.IncrementButton import IncrementButton
from examples.counter.custom_ui.ui.NumberLabel import NumberLabel


class MainUI(View):
    def __init__(self):
        self.number_label = NumberLabel()
        self.inc_button = IncrementButton()
        self.dec_button = DecrementButton()

        self.inc_button.add_on_click_listener(
            lambda:
            GlobalState.counter.dispatch(
                Action(
                    "incrementNumber",
                    {"amount": 1}
                )
            )
        )

        self.dec_button.add_on_click_listener(
            lambda:
            GlobalState.counter.dispatch(
                Action(
                    "decrementNumber",
                    {"amount": 1}
                )
            )
        )

    def show(self):
        print(f"{self.dec_button} {self.number_label} {self.inc_button}")
