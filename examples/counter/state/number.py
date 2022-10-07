from core.action import Action
from core.observable import Observable


class Number(Observable):
    def __init__(self, initial_value):
        Observable.__init__(self, initial_value)

    def increment(self, amount):
        self.value += amount
        self._Observable__notify(Action("numberChanged", {}))

    def decrement(self, amount):
        self.value -= amount
        self._Observable__notify(Action("numberChanged", {}))
