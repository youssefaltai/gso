import abc

from core.action import Action


class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def notify_state_changed(self, action: Action):
        pass
