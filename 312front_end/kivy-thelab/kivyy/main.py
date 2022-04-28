from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('box.kv')

class MyLayout(Widget):
    pass

class MyGridLayout(Widget):

    ticker = ObjectProperty(None)
    date = ObjectProperty(None)
    forecast= ObjectProperty(None)
    
    def press(self):
        ticker = self.ticker.text
        date = self.date.text
        forecast= self.forecast.text

        # printin screen 
        # self.add_widget(Label(text= f"Forecasting for {ticker}, for the next {forecast} days. "))
        print(f'Forecasting for {ticker}, for the next {forecast} days.')

        # clear the input boxes 
        self.ticker.text= ""
        self.date.text= ""
        self.forecast.text= ""

class BoxApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    BoxApp().run()