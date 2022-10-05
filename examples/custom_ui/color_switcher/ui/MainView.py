from examples.custom_ui.color_switcher.ui.ContainerView import ContainerView
from examples.custom_ui.color_switcher.ui.TextView import TextView
from examples.custom_ui.ui.base.View import View


class MainView(View):
    def __init__(self):
        self.container_view = ContainerView()

    def show(self):
        print(f"""
{self.container_view}
""")
