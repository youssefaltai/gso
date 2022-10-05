from core.action import Action
from examples.custom_ui.color_switcher.state.number import Number


class State:
    number = Number(0)

    @classmethod
    def dispatch(cls, action: Action):
        match action.name:
            case "updateNumber":
                cls.number.update_number(action.payload["number"])
            case other:
                raise Exception(f"Unknown action: {other}")
