from core.observable import Observable
from examples.counter.action.decrement_number import DecrementNumber
from examples.counter.action.increment_number import IncrementNumber


class CounterState:
    def __init__(self):
        self.__number: Observable = Observable(0)

    @property
    def number(self):
        return self.__number

    def incrementNumber(self, amount):
        self.__number.apply(IncrementNumber(amount))

    def decrementNumber(self, amount):
        self.__number.apply(DecrementNumber(amount))
