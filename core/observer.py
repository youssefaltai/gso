import abc


class Observer(metaclass=abc.ABCMeta):
    def observe(self, observable):
        observable.attach_observer(self)

    @abc.abstractmethod
    def notify_state_changed(self, action):
        pass
