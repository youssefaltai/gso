from action import Action
from observer import Observer
from state import State


class ButtonViewUI(Observer):
    def __init__(self, text):
        State.data["number"].attach_observer(self)
        self.text = TextViewUI(text)
        self.on_click_handlers = []

    def add_on_click_listener(self, handler):
        self.on_click_handlers.append(handler)

    def click(self):
        for handler in self.on_click_handlers:
            handler()

    def __repr__(self):
        return f"[{self.text}]"

    def notify(self, action):
        if action.name == "updateNumber":
            self.text.update_text(f'{action.payload["number"]}')


class TextViewUI:
    def __init__(self, text):
        self.text = text

    def update_text(self, new_text):
        self.text = new_text

    def __repr__(self):
        return f"{self.text}"


class ColoredViewUI(Observer):
    def __init__(self, color, parity):
        State.data["number"].attach_observer(self)

        self.parity = parity
        self.color = color

    def update_color(self, new_color):
        self.color = new_color

    def notify(self, action):
        if action.name == "updateNumber":
            if self.parity == "even":
                self.update_color("red" if action.payload["number"] % 2 == 0 else "blue")
            else:
                self.update_color("blue" if action.payload["number"] % 2 == 0 else "red")

    def __repr__(self):
        return f"{self.color}"


class ContainerViewUI:
    def __init__(self):
        self.left = ColoredViewUI("red", "even")
        self.number = ButtonViewUI(f"{State.data['number'].value()}")
        self.number.add_on_click_listener(
            lambda:
            State.dispatch(
                Action(
                    "updateNumber",
                    {"number": State.data["number"].value() + 1}
                )
            )
        )
        self.right = ColoredViewUI("blue", "odd")

    def __repr__(self):
        return f"{self.left} {self.number} {self.right}"


class MainUI:
    def __init__(self, title):
        self.title = TextViewUI(title)
        self.container = ContainerViewUI()

    def __repr__(self):
        return f"""{'-' * len(self.title.text)}
{self.title}
{'-' * len(self.title.text)}
{self.container}"""
