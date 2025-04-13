from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('whatever.kv')

class MyLayout(Widget):
    pass

    # infinite keywords
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()