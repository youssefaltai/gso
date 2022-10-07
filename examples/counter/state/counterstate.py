from core.action import Action
from core.state import State
from examples.counter.state.number import Number


class CounterState(State):
    def __init__(self):
        self.number: Number = Number(0)

    def dispatch(self, action: Action) -> None:
        match action.name:
            case "incrementNumber":
                self.number.increment(action.payload["amount"])
            case "decrementNumber":
                self.number.decrement(action.payload["amount"])
            case other:
                raise Exception(f"Unknown action: {other}")
