from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.app import App
from kivy.lang import Builder


class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.phone_book = {"Bob Ross, James Campbell, Johnny Depp, Hank Hill"}

    def build(self):
        self.title = "Dynamic Widget"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widget()
        return self.root

    def create_widget(self):
        for name in self.phone_book:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicWidgetsApp().run()
