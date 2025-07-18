from datetime import datetime, timedelta
import yfinance as yf 
import matplotlib.pyplot as plt 
import pandas as pd 

class Ticker:
    def get_historical_data(ticker, start_date=None, end_date=None):
        try:
            if start_date is None:
                start_date = datetime.now() - timedelta(days=365)
            if end_date is None:
                end_date = datetime.now()

            stock = yf.Ticker(ticker)
            data = stock.history(start=start_date, end=end_date)

            if data.empty:
                raise ValueError (f"No data found for {ticker}")
            return data 
        except Exception as e:
            raise Exception(f"Error fetching data for ticker {ticker}: {str(e)}")
        
    def get_columns(data):
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input should be dataframe")
        return list(data.columns)

    def get_last_price(data, column_name):
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input should be dataframe")
        if column_name not in data.columns:
            raise ValueError(f"Column name: {column_name} not in dataframe")
        return data[column_name].iloc[-1]

    def plot_data(data, ticker, column_name):
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")
        if column_name not in data.columns:
            raise ValueError(f"Column '{column_name}' not found in the DataFrame")
        
        plt.figure(figsize=(10, 6))
        data[column_name].plot()
        plt.ylabel(column_name)
        plt.xlabel('Date')
        plt.title(f'Historical data for {ticker} - {column_name}')
        plt.legend(loc='best')
        return plt