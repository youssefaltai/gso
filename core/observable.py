import abc


class Observable(metaclass=abc.ABCMeta):
    def __init__(self, initial_value):
        self.__value = initial_value
        self.__observers = []

    @property
    def value(self):
        return self.__value

    # FIXME: value setter should not be visible to UI components, only Observable subclasses.
    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def attach_observer(self, observer):
        self.__observers.append(observer)

    # FIXME: Users should not need to call self._Observable__notify,
    #  they should easily select actions to be fired.
    def __notify(self, *actions):
        for observer in self.__observers:
            for action in actions:
                observer.notify_state_changed(action)
