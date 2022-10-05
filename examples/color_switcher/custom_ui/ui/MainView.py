from examples.color_switcher.custom_ui.ui.ContainerView import ContainerView
from examples.color_switcher.custom_ui.customui.base.View import View


class MainView(View):
    def __init__(self):
        self.container_view = ContainerView()

    def show(self):
        print(f"""
{self.container_view}
""")
