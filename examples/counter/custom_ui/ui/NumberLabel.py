from core.globalstate import GlobalState
from core.observer import Observer
from examples.counter.custom_ui.customui.Label import Label


class NumberLabel(
    Label,
    Observer
):
    def notify_state_changed(self, action):
        match action.name:
            case "numberChanged":
                self.update_text(f"{GlobalState.counter.number.value}")

    def __init__(self):
        Label.__init__(self, text=f"{GlobalState.counter.number.value}")
        self.observe(GlobalState.counter.number)
