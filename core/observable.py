import abc


class Observable(metaclass=abc.ABCMeta):
    def __init__(self, value):
        self.__value = value
        self.__observers = []

    @property
    def value(self):
        return self.__value

    def apply(self, action):
        self.__value = action(self.__value)
        self.__notify(action)

    def attach_observer(self, observer):
        self.__observers.append(observer)

    def __notify(self, *actions):
        for observer in self.__observers:
            for action in actions:
                observer.notify_state_changed(action)
