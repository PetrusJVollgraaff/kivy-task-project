from . import *

class EditorScreen(MDScreen, GlobalElements):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name="editor"

        self.top_bar = self.topBar(title="Create ToDo", left_action_items=[["arrow-left", lambda x: self.home_page()]])        
        layout = MDBoxLayout(orientation='vertical')
        layout.add_widget(self.top_bar)

        self.add_widget(layout)

    def home_page(self):
        print("to home")
        self.manager.current = "home"
    