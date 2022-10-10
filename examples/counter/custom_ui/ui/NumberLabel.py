from core.globalstate import GlobalState
from core.observer import Observer
from examples.counter.action.update_number import UpdateNumber
from examples.counter.custom_ui.customui.Label import Label


class NumberLabel(
    Label,
    Observer
):
    def __init__(self):
        Label.__init__(self, text=f'{GlobalState.get("counter").number.value}')
        self.observe(GlobalState.get("counter").number)

    def notify_state_changed(self, action):
        if isinstance(action, UpdateNumber):
            self.update_text(f'{GlobalState.get("counter").number.value}')
