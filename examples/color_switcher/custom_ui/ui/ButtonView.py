from core.observer import Observer
from examples.color_switcher.state.state import State
from examples.color_switcher.custom_ui.ui.TextView import TextView
from examples.color_switcher.custom_ui.customui.base.View import View


class ButtonView(View, Observer):
    def __init__(self, text):
        State.number.attach_observer(self)
        self.text = TextView(text)
        self.on_click_handlers = []

    def add_on_click_listener(self, handler):
        self.on_click_handlers.append(handler)

    def click(self):
        for handler in self.on_click_handlers:
            handler()

    def notify_state_changed(self, action):
        match action.name:
            case "updateNumber":
                self.text.update_text(f'{State.number.value()}')

    def show(self):
        return f"[{self.text}]"

    def __repr__(self):
        return self.show()
