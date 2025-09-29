from . import *


class HomeScreen(MDScreen, GlobalElements):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name="home"

        layout = MDBoxLayout(orientation='vertical')
        layout.add_widget(self.topBar(title="To Do List"))
        layout.add_widget(self.scrollView())

        bottom = self.bottomBar()
        self.bottom_bar = self.topBar(icon="plus", type="bottom", mode="end", id="bottomBar")
        self.bottom_bar.bind(on_action_button = lambda instance: self.on_action_button())
        bottom.add_widget(self.bottom_bar)
        layout.add_widget(bottom)
        self.add_widget(layout)
    
    def scrollView(self):
        scoller = ScrollView()
        scoller.add_widget(MDList(id='todo_list'))
        return scoller
    
    def on_action_button(self):
        print("hello")
        self.manager.current = "editor"