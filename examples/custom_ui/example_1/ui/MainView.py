from examples.custom_ui.example_1.ui.ContainerView import ContainerView
from examples.custom_ui.example_1.ui.TextView import TextView
from examples.custom_ui.example_1.ui.base.View import View


class MainView(View):
    def __init__(self, title):
        self.title_text_view = TextView(title)
        self.container_view = ContainerView()

    def show(self):
        print(f"""
{self.title_text_view}
{self.container_view}
""")
