from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
# https://kivy.org/doc/stable/api-kivy.network.urlrequest.html

# import time
############################################################
# from dotenv import load_dotenv
import os
import pybase64 as base64
from pathlib2 import Path
############################################################

###############################################################################################
class save_ticker_image:
    def __init__(self, url, img_path, ticker):
        self.url = url
        self.img_path = img_path
        self.ticker = ticker
        if self.ticker == '':
            self.ticker = 'AMZN'
    
    # DEPRICATED FROM kivy.network.urlrequest import UrlRequest
    # def django_get(self):
        # response = requests.get(self.url)
        # response_json = response.json()
        # return response_json

        def select_ticker(req, result):
            try:
                django_api_dict = result
                # django_api_dict = self.django_get() #DEPRECATED
                # except: print("URL GET FAIL") #DEPRECATED
                for dictionary in django_api_dict:   
                    try:
                        if dictionary['ticker'] == self.ticker:
                            encoded_plot = dictionary['encoded_string']
                            emoticons = dictionary['emoticons']

                            emoticons = emoticons.replace("'",'').replace(' 00:00:00', '').replace('[[', '').split('],')
                            emoticons = [emoticons[0].split(', '), emoticons[1].replace(' [', '').replace(']]', '').split(', ')]

                            sentiment = dictionary['sentiment']

                    except: print("Ticker Not Found in Forecast Database")
                        # pass
            except: print("Kivy Request Fails")
                # pass
            
            # Decode string and save as a .png
            try:
                decodeit = open("image.png", 'wb')
                decodeit.write(base64.b64decode(encoded_plot[2:].encode()))
                decodeit.close()
                print("Image Saved Successfully")
                if sentiment != "NULL": sentiment = round(float(sentiment), 3)
                print(f'\n\t  __________________________\n\t  ||{ticker} WEATHER FORECAST ||\n\t  ||SENTIMENT_SCORE: {sentiment}||\n\t  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
                print('\t ____________________________')
                for day in range(len(emoticons[1])):
                    if emoticons[1][day] == '0':
                        print(f'\t|🌪 Thunderstorms |{emoticons[0][day]}|')
                        print('\t ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
                    elif emoticons[1][day] == '1':
                        print(f'\t|🌨 Rainy         |{emoticons[0][day]}|')
                        print('\t ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
                    elif emoticons[1][day] == '1':
                        print(f'\t|🌞 Sunny        |{emoticons[0][day]}|')
                        print('\t ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
                    else:
                        print(f'\t|🌈 on           |{emoticons[0][day]}|')
                        print('\t ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')

                # print(f'\n\tEMOTICON VALUE: {type(emoticons)}, \n{emoticons[0]}\n\n{emoticons[1]}\n\nSENTIMENT_SCORE{sentiment}')
                # return f'\n\tEMOTICON VALUE: {emoticons}, SENTIMENT_SCORE{sentiment}'
            except: return print("Could Not Save Plot Ticker Not Found")
        
        req = UrlRequest(self.url, select_ticker).wait()

###############################################################################################
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

#################################################################################################
    def press_forecast_button(self, instance):
        """
        When Forecast button is pressed, YahooProphet is called and returns forecast to terminal.
        """

        ############################################################################
        ###                         DJANGO API CALL                              ###
        ############################################################################
        # USES .ENV FILE #DEPRECATED for testing purposes only
        # load_dotenv() #DEPRECATED for testing purposes only
        # url = os.getenv("DJANGO_SERVER_URL") #DEPRECATED for testing purposes only
        url = 'http://SERVER_IP/ticker/'
        forecast_decoded_img_path = Path('images/forecast_temp/decoded.png')

        # save_ticker_image(url=url, img_path=forecast_decoded_img_path, ticker=self.ticker.text, time=self.time.text).select_ticker()
        save_ticker_image(url=url, img_path=forecast_decoded_img_path, ticker=self.ticker.text.upper())#.select_ticker()
        
        pimg = Image(source='images/forecast_temp/decoded.png')
        self.add_widget(pimg)

##################################################################################################
# class ForecastWindow(Screen):
#     # def __init__(self, **kwargs):
#     #     super(LoginScreen, self).__init__(**kwargs)

#     #     wimg = Image(source='images/312fintech_ver04.png')
#     #     self.add_widget(wimg)
#     pass
##################################################################################################

class MyApp(App):

    def build(self):
        # self.icon = 'myicon.png'
        return LoginScreen()
        # sm = ScreenManager()
        # sm.add_widget(LoginScreen())
        # sm.add_widget(ForecastWindow(name='forecast'))

        # return sm

if __name__ == '__main__':
    MyApp().run()
