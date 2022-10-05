import abc

from core.action import Action


class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def notify(self, action: Action):
        pass
