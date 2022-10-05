from core.action import Action
from examples.color_switcher.state.number import Number


class State:
    number: Number = Number(0)

    @classmethod
    def dispatch(cls, action: Action) -> None:
        match action.name:
            case "updateNumber":
                cls.number.update_number(action.payload["number"])
            case other:
                raise Exception(f"Unknown action: {other}")
