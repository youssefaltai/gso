from action import Action
from observable import Observable


class Number(Observable):
    def __init__(self, initial_value):
        super(Number, self).__init__(initial_value)

    def update_number(self, new_number):
        self._value = new_number
        self._notify(Action("updateNumber", {
            "number": self.value()
        }))
