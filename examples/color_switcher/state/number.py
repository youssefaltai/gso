from core.action import Action
from core.observable import Observable


class Number(Observable):
    def __init__(self, initial_value: int) -> None:
        super(Number, self).__init__(initial_value)

    def update_number(self, new_number: int) -> None:
        self._value = new_number
        self._notify(Action("updateNumber", {}))