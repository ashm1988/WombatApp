from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup

kv2 = Builder.load_file("new.kv")


class Widgets(Widget):
    def btn(self):
        show_popup()


class P(FloatLayout):
    pass

class NewApp(App):
    def build(self):
        return Widgets()


def show_popup():
    show = P()

    popupWindow = Popup(title="Popup window",
                        content=show,
                        size_hint=(None, None),
                        size=(400,400))
    popupWindow.open()


if __name__ == '__main__':
    NewApp().run()
