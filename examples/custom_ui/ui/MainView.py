from examples.custom_ui.ui.ContainerView import ContainerView
from examples.custom_ui.ui.TextView import TextView
from examples.custom_ui.ui.base.View import View


class MainView(View):
    def __init__(self, title):
        self.title_text_view = TextView(title)
        self.container_view = ContainerView()

    def show(self):
        print(f"""
{self.title_text_view}
{self.container_view}
""")
