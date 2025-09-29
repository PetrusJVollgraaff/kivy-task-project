from . import *

class MyToDoList(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        sm = ScreenManager()

        sm.add_widget(HomeScreen())
        sm.add_widget(EditorScreen())

        sm.current = "home"
        return sm
    