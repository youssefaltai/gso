from examples.counter.custom_ui.customui.Label import Label
from examples.counter.custom_ui.customui.base.View import View


class Button(View):
    def __init__(self, text):
        self.text = Label(text)
        self.on_click_handlers = []

    def add_on_click_listener(self, handler):
        self.on_click_handlers.append(handler)

    def click(self):
        for handler in self.on_click_handlers:
            handler()

    def show(self):
        return f"[{self.text}]"

    def __repr__(self):
        return self.show()
