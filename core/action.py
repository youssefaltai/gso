from typing import Any


class Action:
    def __init__(self, name: str, payload: dict[str, Any]):
        self.name: str = name
        self.payload: dict[str, Any] = payload
