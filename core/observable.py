import abc


class Observable(metaclass=abc.ABCMeta):
    def __init__(self):
        self.__observers = []

    def attach_observer(self, observer):
        self.__observers.append(observer)

    def __notify(self, *actions):
        for observer in self.__observers:
            for action in actions:
                observer.notify_state_changed(action)
