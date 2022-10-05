from action import Action
from number import Number


class State:
    data = {
        "number": Number(0)
    }

    @classmethod
    def dispatch(cls, action: Action):
        if action.name == "updateNumber":
            cls.data["number"].update_number(action.payload["number"])
        else:
            raise Exception("Unknown action")
