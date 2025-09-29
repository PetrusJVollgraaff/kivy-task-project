from . import *

class EditorScreen(MDScreen, GlobalElements):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name="editor"

        layout = MDBoxLayout(orientation='vertical')
        layout.add_widget(self.topBar(title="Create ToDo"))

        self.add_widget(layout)

    