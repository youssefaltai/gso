import sys

from core.globalstate import GlobalState
from examples.counter.action.decrement_number import DecrementNumber
from examples.counter.action.increment_number import IncrementNumber
from examples.custom_ui.customui.base.View import View
from examples.custom_ui.ui.DecrementButton import DecrementButton
from examples.custom_ui.ui.IncrementButton import IncrementButton
from examples.custom_ui.ui.NumberLabel import NumberLabel


class MainUI(View):
    def __init__(self):
        self.number_label = NumberLabel()
        self.inc_button = IncrementButton()
        self.dec_button = DecrementButton()

        self.inc_button.add_on_click_listener(
            lambda:
            GlobalState.get("counter").number.apply(IncrementNumber(1))
        )

        self.dec_button.add_on_click_listener(
            lambda:
            GlobalState.get("counter").number.apply(DecrementNumber(1))
        )

    def show(self):
        print(f"{self.dec_button} {self.number_label} {self.inc_button}")

    def loop(self):
        while True:
            self.show()
            self.process(command=input("> "))

    def process(self, command):
        if command == "+":
            self.inc_button.click()
        elif command == "-":
            self.dec_button.click()
        elif command == "q":
            sys.exit()
