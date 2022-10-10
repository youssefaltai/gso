import logging


class GlobalState:
    __states = dict()

    @classmethod
    def get(cls, state_key):
        state = cls.__states.get(state_key, None)
        if state is None:
            logging.warning(f'GlobalState "{state_key}" does NOT exist.')
        return state

    @classmethod
    def set(cls, state_key, state):
        if cls.__states.get(state_key, None) is not None:
            logging.warning(f'Overriding GlobalState "{state_key}".')
        cls.__states[state_key] = state
