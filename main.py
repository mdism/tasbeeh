from kivymd.app import MDApp
from kivy.properties import NumericProperty
from kivy.lang import Builder


class CounterApp(MDApp):
    counter = NumericProperty(0)

    def build(self):
        self.root = Builder.load_file('layout.kv')
        return self.root

    def increment_counter(self):
        self.counter += 1
        self.root.ids.counter_label.text = str(self.counter)


if __name__ == '__main__':
    CounterApp().run()
