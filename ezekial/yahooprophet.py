import pandas as pd
from prophet import Prophet
# from ezekial.prophet import Prophet
import yfinance as yf
# https://facebook.github.io/prophet/docs/quick_start.html#python-api

class YahooProphet:
    """Class that accepts a yahoo finance `yf_ticker`, `start_date` (yyyy-dd-mm), `forecast_ahead`
    Used with `forecast_df()`, `plot()`, `plotly_plot()`, & `forecast_all()` methods. For more info on FB Prophet visit.
    https://facebook.github.io/prophet/docs/quick_start.html#python-api"""
    
    def __init__(self, yf_ticker, start_date, forecast_ahead):
        self.yf_ticker = yf_ticker
        self.start_date = start_date
        self.forecast_ahead = forecast_ahead
    
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
        fig2 = self.m.plot_components(self.forecast)
        return fig1
    
    def plotly_plot(self):
        """Returns plotly plot of forecasted pandas series."""
        from prophet.plot import plot_plotly, plot_components_plotly

        fig1 = plot_plotly(self.m, self.forecast, trend=True)
        fig2 = self.m.plot_components(self.forecast)
        return fig1