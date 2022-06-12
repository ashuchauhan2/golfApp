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

class instructionsScreen(Screen):
    pass

class startScreen(Screen):
    pass

class courseScreen(Screen):
    pass

class courseScreen1(Screen):
    pass

class courseScreen2(Screen):
    pass

class courseScreen3(Screen):
    pass

class courseScreen4(Screen):
    pass

class courseScreen5(Screen):
    pass

class courseScreen6(Screen):
    pass

class courseScreen7(Screen):
    pass

class courseScreen8(Screen):
    pass

class courseScreen9(Screen):
    pass

class courseScreen10(Screen):
    pass

class courseScreen11(Screen):
    pass

class courseScreen12(Screen):
    pass

class courseScreen13(Screen):
    pass

class courseScreen14(Screen):
    pass

class courseScreen15(Screen):
    pass

class courseScreen16(Screen):
    pass

class courseScreen17(Screen):
    pass

class courseScreen18(Screen):
    pass

class courseScreen19(Screen):
    pass

class courseScreen20(Screen):
    pass

class TestApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(mainScreen(name='main'))
        sm.add_widget(instructionsScreen(name='instructions'))
        sm.add_widget(startScreen(name='start'))
        sm.add_widget(courseScreen(name='course'))
        sm.add_widget(courseScreen1(name='course1'))
        sm.add_widget(courseScreen2(name='course2'))
        sm.add_widget(courseScreen3(name='course3'))
        sm.add_widget(courseScreen4(name='course4'))
        sm.add_widget(courseScreen5(name='course5'))
        sm.add_widget(courseScreen6(name='course6'))
        sm.add_widget(courseScreen7(name='course7'))
        sm.add_widget(courseScreen8(name='course8'))
        sm.add_widget(courseScreen9(name='course9'))
        sm.add_widget(courseScreen10(name='course10'))
        sm.add_widget(courseScreen11(name='course11'))
        sm.add_widget(courseScreen12(name='course12'))
        sm.add_widget(courseScreen13(name='course13'))
        sm.add_widget(courseScreen14(name='course14'))
        sm.add_widget(courseScreen15(name='course15'))
        sm.add_widget(courseScreen16(name='course16'))
        sm.add_widget(courseScreen17(name='course17'))
        sm.add_widget(courseScreen18(name='course18'))
        sm.add_widget(courseScreen19(name='course19'))
        sm.add_widget(courseScreen20(name='course20'))
        return sm


if __name__ == '__main__':
    TestApp().run()
