from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

import warnings
warnings.filterwarnings("ignore")

from ezekial import yahooprophet as yfp

# class LoginScreen(GridLayout):
class LoginScreen(Widget):

    # self.inside = Widget()
    ticker = ObjectProperty(None)
    start_date = ObjectProperty(None)
    days_to_forecast = ObjectProperty(None)

    # def __init__(self, **kwargs):
    #     super(LoginScreen, self).__init__(**kwargs)
        
        # self.cols = 1

        # self.inside = GridLayout()
        # self.inside.cols = 2

        # self.inside.add_widget(Label(text='Ticker: '))
        # self.ticker = TextInput(multiline=False)
        # self.inside.add_widget(self.ticker)
        
        # self.inside.add_widget(Label(text='Start Data From: \n(YYYY-MM-DD)'))
        # self.start_date = TextInput(multiline=False)
        # self.inside.add_widget(self.start_date)
        
        # self.inside.add_widget(Label(text='Days to Forecast: '))
        # self.days_to_forecast = TextInput(multiline=False)
        # self.inside.add_widget(self.days_to_forecast)

        # # Add inside as row 1/2
        # self.add_widget(self.inside)

        # self.submit = Button(text='Forecast', font_size=40)
        # self.submit.bind(on_press=self.press_forecast_button)
        # self.add_widget(self.submit)


    # def press_forecast_button(self, instance):
    #     """
    #     When Forecast button is pressed, YahooProphet is called and returns forecast to terminal.
    #     """
    #     print("Pressed Forecast Button")
    #     yfp_obj = yfp.YahooProphet(self.ticker.text, self.start_date.text, int(self.days_to_forecast.text))
    #     print(yfp_obj.forecast_df().tail(int(self.days_to_forecast.text)))


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()