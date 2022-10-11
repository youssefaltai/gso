from examples.custom_ui.customui.Button import Button


class DecrementButton(Button):
    def __init__(self):
        Button.__init__(self, "-")
