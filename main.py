from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty

# import warnings
# warnings.filterwarnings("ignore")

# from ezekial import yahooprophet as yfp
# from matplotlib import pyplot as plt

# import time

import requests
from dotenv import load_dotenv
import os
import base64
from pathlib import Path

# class save_ticker_image:
#     def __init__(self, url, img_path, ticker, time):
#         self.url = url
#         self.img_path = img_path
#         self.ticker = ticker
#         self.time = time
    
#     def django_get(self):
#         response = requests.get(self.url)
#         response_json = response.json()
#         return response_json

#     def select_ticker(self):
#         django_api_dict = self.django_get()
#         for dictionary in django_api_dict:   
#             try:
#                 if dictionary['ticker'] == self.ticker and dictionary['time'] == self.time:
#                     encoded_plot = dictionary['encoded_string']
#             except: return print("Ticker Not Found in Forecast Database")
#         # Decode string and save as a .png
#         try:
#             decodeit = open(self.img_path, 'wb')
#             decodeit.write(base64.b64decode(encoded_plot[2:].encode()))
#             decodeit.close()
#             print("Image Saved Successfully")
#         except: return print("Could Not Save Plot Ticker Not Found")

class save_ticker_image:
    def __init__(self, url, img_path, ticker):
        self.url = url
        self.img_path = img_path
        self.ticker = ticker
    
    def django_get(self):
        response = requests.get(self.url)
        response_json = response.json()
        return response_json

    def select_ticker(self):
        django_api_dict = self.django_get()
        for dictionary in django_api_dict:   
            try:
                if dictionary['ticker'] == self.ticker:
                    encoded_plot = dictionary['encoded_string']
                    emoticons = dictionary['emoticons']

            except: return print("Ticker Not Found in Forecast Database")
        # Decode string and save as a .png
        try:
            decodeit = open(self.img_path, 'wb')
            decodeit.write(base64.b64decode(encoded_plot[2:].encode()))
            decodeit.close()
            print("Image Saved Successfully")
            print(f'\n\t{emoticons}')
        except: return print("Could Not Save Plot Ticker Not Found")

class LoginScreen(GridLayout):
# class LoginScreen(Screen):

# class Floatlayout():

# class LoginScreen(Widget):

    # # self.inside = Widget()
    # ticker = ObjectProperty(None)
    # start_date = ObjectProperty(None)
    # days_to_forecast = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        wimg = Image(source='images/312fintech_ver04.png')
        self.add_widget(wimg)

        self.inside.add_widget(Label(text='Ticker: '))
        self.ticker = TextInput(multiline=False)
        self.inside.add_widget(self.ticker)

        # self.inside.add_widget(Label(text='Time (Day, 60min): '))
        # self.time = TextInput(multiline=False)
        # self.inside.add_widget(self.time)
        
        # self.inside.add_widget(Label(text='Start Data From: \n(YYYY-MM-DD)'))
        # self.start_date = TextInput(multiline=False)
        # self.inside.add_widget(self.start_date)
        
        # self.inside.add_widget(Label(text='Days to Forecast: '))
        # self.days_to_forecast = TextInput(multiline=False)
        # self.inside.add_widget(self.days_to_forecast)

        # Add inside as row 1/2
        self.add_widget(self.inside)

        self.submit = Button(text='Forecast', font_size=40)
        self.submit.bind(on_press=self.press_forecast_button)
        self.add_widget(self.submit)


    def press_forecast_button(self, instance):
        """
        When Forecast button is pressed, YahooProphet is called and returns forecast to terminal.
        """

        ############################################################################
        ###                         DJANGO API CALL                              ###
        ############################################################################
        # USES .ENV FILE 
        load_dotenv()
        url = os.getenv("DJANGO_SERVER_URL")
        forecast_decoded_img_path = Path('images/forecast_temp/decoded.png')

        # save_ticker_image(url=url, img_path=forecast_decoded_img_path, ticker=self.ticker.text, time=self.time.text).select_ticker()
        save_ticker_image(url=url, img_path=forecast_decoded_img_path, ticker=self.ticker.text.upper()).select_ticker()
        # time.sleep(1)
        
        pimg = Image(source='images/forecast_temp/decoded.png')
        self.add_widget(pimg)

        ##ORIGINAL##
        # print("Pressed Forecast Button")
        # yfp_obj = yfp.YahooProphet(self.ticker.text, self.start_date.text, int(self.days_to_forecast.text))
        # # print(yfp_obj.forecast_df().tail(int(self.days_to_forecast.text)))
        # pimg = yfp_obj.plot()
        # pimg.savefig('images/forecast.png')

        # # time.sleep(3)
        # pimg = Image(source='images/forecast.png')
        # self.add_widget(pimg)

        # ######################################
        # ## CHECKING EZEKIAL DECODING METHOD ##
        # ###  TO BE REPLAECD WITH API CALL  ###
        # ######################################
        # print("Pressed Forecast Button")

        # yfp_obj = yfp.YahooProphet(self.ticker.text, self.start_date.text, int(self.days_to_forecast.text))
        # ####################################################################
        # yfp_obj.encode_plot()
        # yfp_obj.decode_plot()
        # ## Load decoded image
        # # forecast_decoded_img_path = Path('images/forecast_temp/decoded.png')
        # pimg = Image(source='images/forecast_temp/decoded.png')
        # self.add_widget(pimg)


class ForecastWindow(Screen):
    # def __init__(self, **kwargs):
    #     super(LoginScreen, self).__init__(**kwargs)

    #     wimg = Image(source='images/312fintech_ver04.png')
    #     self.add_widget(wimg)
    pass


class MyApp(App):

    def build(self):
        return LoginScreen()
        # sm = ScreenManager()
        # sm.add_widget(LoginScreen())
        # sm.add_widget(ForecastWindow(name='forecast'))

        # return sm

if __name__ == '__main__':
    MyApp().run()