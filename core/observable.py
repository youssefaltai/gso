import abc


class Observable(metaclass=abc.ABCMeta):
    def __init__(self, initial_value):
        self._value = initial_value
        self.__observers = []

    def value(self):
        return self._value

    def attach_observer(self, observer):
        self.__observers.append(observer)

    def _notify(self, action):
        for observer in self.__observers:
            observer.notify(action)
