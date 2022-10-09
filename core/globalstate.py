class GlobalState:
    __lock = False

    @classmethod
    def create(cls, **states):
        if cls.__lock:
            raise Exception("GlobalState can only be created once.")
        for key, value in states.items():
            setattr(cls, key, value)
        cls.__lock = True
