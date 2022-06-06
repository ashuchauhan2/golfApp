from kivy.uix.button import Button

from kivy import args

from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout

from kivy.uix.image import Image
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.slider import Slider

Builder.load_file("golfApp.kv")


class mainScreen(Screen):
    pass

class startScreen(Screen):
    pass

class courseScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(mainScreen(name='main'))
        sm.add_widget(startScreen(name='start'))
        sm.add_widget(courseScreen(name='course'))
        return sm


if __name__ == '__main__':
    TestApp().run()
