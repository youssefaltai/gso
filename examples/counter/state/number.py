from core import gso
from core.action import Action
from core.observable import Observable


class Number(Observable):
    def __init__(self, initial_value):
        Observable.__init__(self)
        self.__value = initial_value

    @property
    def value(self):
        return self.__value

    @gso.update(Action("numberChanged", {}))
    def increment(self, amount):
        self.__value += amount

    @gso.update(Action("numberChanged", {}))
    def decrement(self, amount):
        self.__value -= amount
