import abc
from typing import Any

from core.action import Action
from core.observer import Observer


class Observable(metaclass=abc.ABCMeta):
    def __init__(self, initial_value) -> None:
        self._value = initial_value
        self.__observers: list[Observer] = []

    def value(self) -> Any:
        return self._value

    def attach_observer(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def _notify(self, action: Action) -> None:
        for observer in self.__observers:
            observer.notify_state_changed(action)
