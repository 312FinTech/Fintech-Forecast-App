import pandas as pd
from prophet import Prophet
# from ezekial.prophet import Prophet
import yfinance as yf
# https://facebook.github.io/prophet/docs/quick_start.html#python-api
import base64
from pathlib import Path

class YahooProphet:
    """
    Class that accepts a yahoo finance `yf_ticker`, `start_date` (yyyy-dd-mm), `forecast_ahead`
    Used with `forecast_df()`, `plot()`, `plotly_plot()`, `forecast_all()`, 'encode_plot' methods. For more info on FB Prophet visit.
    https://facebook.github.io/prophet/docs/quick_start.html#python-api
    
    Parameters
    ----------
    yf_ticker : str
        Must be ticker accepted by yfinance.
        Default ticker is 'BTC-USD'
        
    start_date : str
        YYYY-MM-DD format, this is the start date of the returned df.
        Defaults to 2019-1-1
        
    forecast_ahead : int
        Number of days for FB Prophet to forecast.
        Defaults to 90.

    forecast_img_path : str
        Path to dir where encoded plot images are to be saved.
        Defaults to 'images/forecast_temp/forecast.png'.

    See Also
    --------
    yfinance.Ticker() : https://pypi.org/project/yfinance/
    prophet.Prophet() : https://facebook.github.io/prophet/docs/quick_start.html#python-api

    Examples
    --------
    >>> YahooProphet()
    
    >>> 
    
    >>> 
    
    """
    
    def __init__(self, yf_ticker='BTC-USD', start_date='2019-1-1', forecast_ahead=90, forecast_img_path='images/forecast_temp/forecast.png'):
        self.yf_ticker = yf_ticker
        self.start_date = start_date
        self.forecast_ahead = forecast_ahead
        self.forecast_img_path = forecast_img_path
    
        df0 = pd.DataFrame()
        df0 = yf.Ticker(self.yf_ticker).history(start=self.start_date)['Close'].rename(self.yf_ticker)
        
        df_prophet = pd.DataFrame()
        # Facebook Prophet needs one column named 'ds' & 'y'
        df_prophet['y'] = df0

        df_prophet['ds'] = df_prophet.index
        df_prophet = df_prophet[['ds','y']]
        df_prophet.reset_index(drop=True, inplace=True)
        
        
        m = Prophet()
        m.fit(df_prophet)
        future = m.make_future_dataframe(periods=self.forecast_ahead)
        forecast = m.predict(future)
        self.forecast = forecast
        self.m = m
    
    def forecast_all(self):
        """Returns a Facebook Prophet dataframe and forecast charts."""
        
        fig1 = self.m.plot(self.forecast)
        fig2 = self.m.plot_components(self.forecast)
        
        for x in range(0, 2):
            if x == 0:
                return self.forecast_df()
            else:
                return fig1
    
    def forecast_df(self):
        """Returns a Facebook Prophet dataframe."""
        return self.forecast
    
    def plot(self):
        """Returns 4 charts on forecast of input pandas series."""
        fig1 = self.m.plot(self.forecast)
        # fig2 = self.m.plot_components(self.forecast)
        return fig1
    
    def plotly_plot(self):
        """Returns plotly plot of forecasted pandas series."""
        from prophet.plot import plot_plotly, plot_components_plotly

        fig1 = plot_plotly(self.m, self.forecast, trend=True)
        fig2 = self.m.plot_components(self.forecast)
        return fig1
    
    def encode_plot(self):
        """
        Saves image and encoded byte string of forecast plot().
        File(s) located in images/forecast_temp/forecast.png
        and images/forecast_temp/encoded.bin
        """
        # Look for more effecient method to rather than saving prior to converting to byte string.
        # Have to convert from matplotlib figure to .png
        # forecast_img_path = Path('images/forecast_temp/forecast.png')
        prophet_plot = self.plot()
        prophet_plot.savefig(self.forecast_img_path)
        
        # Create the converted image to string
        with open(self.forecast_img_path, "rb") as image2string:
            converted_string = base64.b64encode(image2string.read())
            
        return converted_string

    # For Testing Purposes Only
    # def decode_plot(self):
    #     """
    #     Decodes plot from encode_plot() and saves as,
    #     images/forecast_temp/decoded.png
    #     """
    #     # USE API CALL HERE FIRST 
    #     # MAY NEED TO SAVE FIRST FOR READING IN BINARY MODE & SETTING AS A VAR
    #     forecast_img_path = Path('images/forecast_temp/encoded.bin')
    #     file = open(forecast_img_path, 'rb')
    #     byte = file.read()
    #     file.close()
    #     # Decode string and save as a .png
    #     forecast_decoded_img_path = Path('images/forecast_temp/decoded.png')
    #     decodeit = open(forecast_decoded_img_path, 'wb')
    #     decodeit.write(base64.b64decode((byte)))
    #     decodeit.close()