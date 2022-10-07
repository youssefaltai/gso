from core.state import State


class GlobalState:
    __lock = False

    @classmethod
    def create(cls, **states: State):
        if cls.__lock:
            raise Exception("GlobalState recreation is forbidden.")
        for key, value in states.items():
            setattr(cls, key, value)
        cls.__lock = True
