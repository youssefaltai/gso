import abc


class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def dispatch(self, action) -> None:
        pass
