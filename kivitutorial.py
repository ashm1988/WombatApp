from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout


class playingApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text='this label')

        f.add_widget(l)
        s.add_widget(l)
        return f


def main():
    playingApp().run()


if __name__ == '__main__':
    main()
