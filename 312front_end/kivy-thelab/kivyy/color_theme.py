from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.app import MDApp


Builder.load_file('color_theme.kv')

class MyLayout(Widget):
    pass

class MainApp (MDApp):
    def build(self):
        return MyLayout()
        

if __name__== '__main__':
    MainApp().run()