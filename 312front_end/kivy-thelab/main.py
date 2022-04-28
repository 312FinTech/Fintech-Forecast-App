from cgitb import text
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, BooleanProperty 
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(0, 100):
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)

class ScrollViewExample(ScrollView):
    pass

class WidgetExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")
    # slider_value_txt = StringProperty("Value")
    text_input_str = StringProperty("foo")

    def on_button_click(self):
        print("Button Clicked")
        if self.count_enabled: 
            self.count += 1
            self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):
        print("toggle state" + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    # def on_slider_value(self, widget):
        # print("Slider: " + str(int(widget.value)))
        # self.slider_value_txt = str(int(widget.value))
    
    def on_text_validate(self, widget):
        self.text_input_str = widget.text
        
        


class GridLayoutExample(GridLayout):
    pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation= "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="c")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""

class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

TheLabApp().run()
