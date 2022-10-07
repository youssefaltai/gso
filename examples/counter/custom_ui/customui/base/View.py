import abc


class View(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def show(self):
        pass
