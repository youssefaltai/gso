from core.action import Action
from examples.custom_ui.state.number import Number


class State:
    data = {
        "number": Number(0)
    }

    @classmethod
    def dispatch(cls, action: Action):
        match action.name:
            case "updateNumber":
                cls.data["number"].update_number(action.payload["number"])
            case other:
                raise Exception(f"Unknown action: {other}")
