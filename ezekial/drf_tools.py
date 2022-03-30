# SQL DB UPDATES
import pandas as pd
from pathlib import Path
# https://anaconda.org/conda-forge/python-dotenv
# conda install -c conda-forge python-dotenv -y
from dotenv import load_dotenv
import os
# import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
# !yes | pip install yfinance
# import yfinance as yf
import warnings
warnings.filterwarnings("ignore")
import requests
import yahooprophet as yfp
import alphaprophet as alpha_op

# Have to convert from matplotlib figure to .png
def yahoo_make_and_save_ticker_plot(ticker_path='data/S&P500 tickers.csv', forecast_img_path='images/forecast_temp/forecast.png', start_date='2019-1-1', forecast_ahead=90, url="http://127.0.0.1:8000/ds"):
    """
    Scrapes yfinance from tickers provided in 'data/S&P500 tickers.csv',
    then uses Ezekial package to generate forecast plots.
    Plots are then encdoded and stored in the Djanog server API, using
    REQUESTS and a POST.
    
    Parameters
    ----------
    ticker_path : str
        Path from function to ticker data.
        Should be a .csv file with a header col named 'Symbol'.
        Selects top 500 tickers, due to yfinance public ip api limits.
        Defaults to data/S&P500 tickers.csv
        
    forecast_img_path : str
        Path to dir where encoded plot images are saved.
        Defaults to 'images/forecast_temp/forecast.png'.
        
    start_date : str
        YYYY-MM-DD format, this is the start date of the returned df.
        Defaults to 2019-1-1
        
    forecast_ahead : int
        Number of days for FB Prophet to forecast.
        Defaults to 90.
    
    url : str
        URL to send Django API POST's.
        Defaults to "http://127.0.0.1:8000/ds".
    
    See Also
    --------
    yfinance.Ticker() : https://pypi.org/project/yfinance/
    prophet.Prophet() : https://facebook.github.io/prophet/docs/quick_start.html#python-api

    Examples
    --------
    >>> yahoo_make_and_save_ticker_plot()
    
    >>> load_dotenv()
        url = os.getenv("DJANGO_SERVER_URL")
        yahoo_make_and_save_ticker_plot(
            ticker_path = '../data/S&P500 tickers.csv', 
            forecast_img_path = '../images/forecast_temp/forecast.png',
            url = url) 
    
    >>> 
    """
        
    def load_tickers(ticker_path):
        """
        Takes five hundred tickers, which is max calls of yfinance for public ip.
        """
        ticker_file_path = Path(ticker_path)
        ticker_df = pd.read_csv(ticker_file_path)
        prophet_ticker_list = ticker_df['Symbol'].head(500).to_list()
        return prophet_ticker_list

    # return load_tickers('data/S&P500 tickers.csv')
    
    def make_plots(url):
        """
        Makes and encodes the plots and POST's to Django API.
        """
        
        # REMOVE [:3] TO RUN FULL LIST 
        for tick in load_tickers(ticker_path)[:30]:
            try:
                yfp_obj = yfp.YahooProphet(tick, start_date, forecast_ahead, forecast_img_path)
                
                json_post = {
                    "ticker": f"{tick}",
                    "time": f"Day",
                    "encoded_string": f"{yfp_obj.encode_plot()}"
                }
                
                print(f"+++ {tick} success!")
                try:
                    requests.post(url,json_post)
                except:
                    print(f"\t--- {tick} failed ---")
            except:
                print(f"\t--- {tick} failed ---")
                print("\n\n\tyfinance API daily limit reached.")
            
    make_plots(url)
    
    
# Have to convert from matplotlib figure to .png
def alpha_make_and_save_ticker_plot(alpha_api_key, ticker_path='data/alpha_vantage_listing_status.csv', forecast_img_path='images/forecast_temp/forecast.png', time_interval='60min', forecast_ahead=12, url="http://127.0.0.1:8000/ds"):
    """
    Scrapes yfinance from tickers provided in 'data/alpha_vantage_listing_status.csv',
    then uses Ezekial package to generate forecast plots.
    Plots are then encdoded and stored in the Djanog server API, using
    REQUESTS and a POST.
    
    Parameters
    ----------
    ticker_path : str
        Path from function to ticker data.
        Should be a .csv file with a header col named 'Symbol'.
        Selects top 500 tickers, due to yfinance public ip api limits.
        Defaults to 'data/alpha_vantage_listing_status.csv'.
        
    forecast_img_path : str
        Path to dir where encoded plot images are saved.
        Defaults to 'images/forecast_temp/forecast.png'.
        
    start_date : str
        YYYY-MM-DD format, this is the start date of the returned df.
        Defaults to 2019-1-1
        
    forecast_ahead : int
        Number of days for FB Prophet to forecast.
        Defaults to 90.
    
    url : str
        URL to send Django API POST's.
        Defaults to "http://127.0.0.1:8000/ds".
    
    See Also
    --------
    https://www.alphavantage.co/
    prophet.Prophet() : https://facebook.github.io/prophet/docs/quick_start.html#python-api

    Examples
    --------
    >>> alpha_make_and_save_ticker_plot()
    
    >>> load_dotenv()
        url = os.getenv("DJANGO_SERVER_URL")
        load_dotenv()
        AV_KEY = os.getenv("APLHA_VANTAGE_KEY")
        alpha_make_and_save_ticker_plot(
            alpha_api_key = AV_KEY,
            ticker_path = '../data/S&P500 tickers.csv', 
            forecast_img_path = '../images/forecast_temp/forecast.png',
            time_interval='60min',
            forecast_ahead=12,
            url = url)
    
    >>> 
    """
        
    def load_tickers(ticker_path):
        """
        Takes five hundred tickers, which is max calls of yfinance for public ip.
        """
        ticker_file_path = Path(ticker_path)
        ticker_df = pd.read_csv(ticker_file_path)
        prophet_ticker_list = ticker_df['Symbol'].head(500).to_list()
        return prophet_ticker_list

    # return load_tickers('data/S&P500 tickers.csv')
    
    def make_plots(url):
        """
        Makes and encodes the plots and POST's to Django API.
        """
        
        # REMOVE [:3] TO RUN FULL LIST 
        for tick in load_tickers(ticker_path)[:30]:
            try:
                alpha_op_obj = alpha_op.AlphaProphet(alpha_key = alpha_api_key, alpha_ticker = tick, time_interval = time_interval, forecast_ahead = forecast_ahead, forecast_img_path = forecast_img_path)
                
                json_post = {
                    "ticker": f"{tick}",
                    "time": f"{time_interval}",
                    "encoded_string": f"{alpha_op_obj.encode_plot()}"
                }
                
                print(f"+++ {tick} success!")
                try:
                    requests.post(url,json_post)
                except:
                    print(f"\t--- {tick} failed ---")
            except:
                print(f"\t--- {tick} failed ---")
                print("\n\n\Alpha Advantage API limit reached.")
            
    make_plots(url)
    
    
    
# Get
def django_get(url):
    """
    load_dotenv()
    url = os.getenv("DJANGO_SERVER_URL")
    django_api_dict = django_get(url)
    django_api_dict
    """
    response = requests.get(url)
    response_json = response.json()
    return response_json

# Delete
def clear_django_sql_db(url):
    """
    Clears the sql db in the django api.
    "DJANGO_SERVER_URL" is provided in .env file.
    
    load_dotenv()
    url = os.getenv("DJANGO_SERVER_URL")
    clear_django_sql_db(url = url)
    """
    
    try:
        # load_dotenv()
        # url = os.getenv("DJANGO_SERVER_URL")
        
        django_api_items = django_get(url)
        
        if len(django_api_items) != 0:
            for x, index_id in enumerate(django_api_items):
                x += 1
                str_indx = str(index_id['id'])
                
                if x == 1:
                    url += str(str_indx)
                    requests.delete(url)
                    # print(f'entered if block\t{url}')
                else:
                    try:
                        url = url[:-len(str_indx)] + str_indx
                        requests.delete(url)
                        # print(f'entered else block\t{url}')
                    # For when the number of digits change
                    except:
                        url = url[:-len(str_indx)] + str_indx + 1
                        requests.delete(url)                    
                        # print(f'entered else block\t{url}')
            print(f"Django SQL DB cleared:\n\n{django_get(url)}")
        else:
            print(f"Django SQL DB Already empty:\n\n{django_get(url)}")
    except:
        print(f"Django server did not clear:\n\n{django_get(url)}")