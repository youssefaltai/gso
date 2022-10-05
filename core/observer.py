import abc


class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def notify(self, action):
        pass
