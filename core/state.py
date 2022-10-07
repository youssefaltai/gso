import abc

from core.action import Action


class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def dispatch(self, action: Action) -> None:
        pass
