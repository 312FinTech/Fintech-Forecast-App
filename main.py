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

# import warnings
# warnings.filterwarnings("ignore")

# from ezekial import yahooprophet as yfp
# from matplotlib import pyplot as plt

import time
############################################################
# import requests
# from dotenv import load_dotenv
import os
# import base64
import pybase64 as base64
# from pathlib import Path
from pathlib2 import Path
from PIL import Image as PILImage
from PIL import ImageFont, ImageDraw
# from PIL import ImageFont
# from PIL import ImageDraw 
############################################################

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

        # def get_image_paths(path1, path2):
        #     return [path1, path2]

        def select_ticker(req, result):
        # def chart_generation(self, req, result):
            try:
                django_api_dict = result
                # django_api_dict = self.django_get() 
                # except: print("URL GET FAIL")
                for dictionary in django_api_dict:   
                    try:
                        if dictionary['ticker'] == self.ticker:
                            encoded_plot = dictionary['encoded_string']
                            emoticons = dictionary['emoticons']

                            emoticons = emoticons.replace("'",'').replace(' 00:00:00', '').replace('[[', '').split('],')
                            emoticons = [emoticons[0].split(', '), emoticons[1].replace(' [', '').replace(']]', '').split(', ')]
                            # self.emoticons = emoticons
                            sentiment = dictionary['sentiment']
                            # self.sentiment = sentiment
                            
                    except: print("Ticker Not Found in Forecast Database")
                        # pass
            except: print("Kivy Request Fails")
                # pass

            # Decode string and save as a .png
            try:
                decodeit = open(self.img_path, 'wb')
                decodeit.write(base64.b64decode(encoded_plot[2:].encode()))
                decodeit.close()
                print("Image Saved Successfully")
                # forecast_image = Image(source='images/forecast_temp/decoded.png')
                forecast_image = 'images/forecast_temp/decoded.png'
                self.forecast_image = forecast_image

            except: 
                print('Error saving plot')
                # forecast_image = Image(source='images/forecast_temp/image_render_error.png')
                forecast_image = 'images/forecast_temp/image_render_error.png'
                self.forecast_image = forecast_image

            # def emoticon_generation(self):
            try:
                # if sentiment != "NULL": sentiment = round(float(sentiment), 3)
                # print(f'\n\tSENTIMENT_SCORE: {sentiment}\n{self.ticker} WEATHER FORECAST')
                # for day in range(len(emoticons[1])):
                #     if emoticons[1][day] == '0':
                #         print(f'🌪Thunderstorms on {emoticons[0][day]}')
                #     elif emoticons[1][day] == '1':
                #         print(f'🌨Rainy on {emoticons[0][day]}')
                #     elif emoticons[1][day] == '1':
                #         print(f'🌞Sunny on {emoticons[0][day]}')
                #     else:
                #         print(f'🌈 on {emoticons[0][day]}')
                        
                emoticon_output_string = f'\n  __________________________\n  ||{ticker} WEATHER FORECAST ||\n  ||Sentiment Score:        {sentiment}||\n  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯'
                emoticon_output_string += '\n ____________________________'
                for day in range(len(emoticons[1])):
                    if emoticons[1][day] == '0':
                        emoticon_output_string += f'\n|\U0001f32a Stormy               |  {emoticons[0][day]}|'
                        emoticon_output_string += '\n ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯'
                    elif emoticons[1][day] == '1':
                        emoticon_output_string += f'\n|\U0001f326 Rainy                 |  {emoticons[0][day]}|'
                        emoticon_output_string += '\n ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯'
                    elif emoticons[1][day] == '1':
                        emoticon_output_string += f'\n|\U0001f324 Overcast            |  {emoticons[0][day]}|'
                        emoticon_output_string += '\n ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯'
                    else:
                        emoticon_output_string += f'\n|\U0001f31e Sunny                 |  {emoticons[0][day]}|'
                        emoticon_output_string += '\n ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯'

                img = PILImage.new('RGB', (235, 500))

                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("images/forecast_temp/Symbola.ttf", 16)
                draw.text((0, 0),emoticon_output_string,font=font)
                img.save('images/forecast_temp/final_emoticon_report.png')
                # emos = Image(source='images/forecast_temp/final_emoticon_report.png')
                emos = 'images/forecast_temp/final_emoticon_report.png'
                self.emos = emos
                    # print(f'\n\tEMOTICON VALUE: {type(emoticons)}, \n{emoticons[0]}\n\n{emoticons[1]}\n\nSENTIMENT_SCORE{sentiment}')
                    # return f'\n\tEMOTICON VALUE: {emoticons}, SENTIMENT_SCORE{sentiment}'
            except: 
                print("Could Not Save Emoticon Report Ticker Not Found")
                # emos = Image(source='images/forecast_temp/emoticon_render_error.png')
                emos = 'images/forecast_temp/emoticon_render_error.png'
                self.emos = emos

            # get_image_paths(forecast_image, emos)
            # return [forecast_image, emos]
                             
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
        # USES .ENV FILE 
        # load_dotenv()
        # url = os.getenv("DJANGO_SERVER_URL")
        url = 'http://45.19.28.81:3555/ticker/'
        forecast_decoded_img_path = Path('images/forecast_temp/decoded.png')

        # save_ticker_image(url=url, img_path=forecast_decoded_img_path, ticker=self.ticker.text, time=self.time.text).select_ticker()
        pimg = save_ticker_image(url=url, img_path=forecast_decoded_img_path, ticker=self.ticker.text.upper())#.select_ticker()
        # time.sleep(.45)
        
        # print(pimg)
        # print(pimg.forecast_image, pimg.emos)

        # pimg = Image(source='images/forecast_temp/decoded.png')
        # self.add_widget(pimg)
        self.add_widget(Image(source=pimg.forecast_image))
        self.add_widget(Image(source=pimg.emos))

################################################################################################
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
