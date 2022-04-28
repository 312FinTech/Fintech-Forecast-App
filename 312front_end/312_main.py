from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder
# from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv= Builder.load_file("312.kv")

# class MyLayout(Widget):
#     pass


class MyApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    MyApp().run()