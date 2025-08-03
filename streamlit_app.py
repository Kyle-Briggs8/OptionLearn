import streamlit as st
import pandas as pd 
import matplotlib.pyplot as olt
from option_price import BlackScholes, Ticker
import yfinance as yf 
from datetime import datetime, timedelta

def get_data(ticker):
    try: 
        data = Ticker.get_historical_data(ticker)
        return data 
    except Exception as e:
        st.error(f"error getting data")
        return None

def get_price(ticker):
    try:
        data = yf.Ticker(ticker).history(period='1d')
        return data['Close'].iloc[-1]
    except Exception as e:
        st.error("error getting price")
        return None 


st.title("Black Scholes Test")

st.write("### Input data")

ticker_value = st.text_input("Ticker Symbol")

current_price = get_price(ticker_value)

if current_price is not None:
    strike= round(current_price,2)
    max_strike= round(current_price*2,2)
    min_strike= max(0.1,round(current_price*.5,2))

    strike_price = st.number_input('Strike price', max_value=max_strike,min_value=min_strike, value=strike, step=.01)
    st.caption(f"The price at which the option can be exercised. Range: ${min_strike:.2f} to ${max_strike:.2f}")

else:
    strike_price = st.number_input('Strike price', min_value=0.01, value=100.0, step=0.01)
    st.caption("The price at which the option can be exercised. Enter a valid ticker to see a suggested range.")
    
risk_free_rate = st.slider('Risk Free Rate (%)', min_value=0, max_value=100, step=5)
st.caption("The theoretical rate of return of an investment with zero risk. Usually based on government bonds. 0% means no risk-free return, 100% means doubling your money risk-free (unrealistic).")

volatility = st.slider('Volatility (%)',min_value=0, max_value=100, step=5)
st.caption("A measure of the stock's price variability. Higher values indicate more volatile stocks. 0% means no volatility (unrealistic), 100% means extremely volatile.")

exercise_date = st.date_input('Exercise date', min_value=datetime.today() + timedelta(days=1), value=datetime.today() + timedelta(days=365))
st.caption("The date when the option can be exercised")

if st.button(f'Calculate Option Price for {ticker_value}'):
    try:
        with st.spinner('Fetching data...'):
            data = get_data(ticker_value)

        if data is not None and not data.empty:
            st.write("Data fetched successfully:")
            st.write(data.tail())
            
            fig = Ticker.plot_data(data, ticker_value, 'Close')
            st.pyplot(fig)

            spot_price = Ticker.get_last_price(data, 'Close')
            risk_free_rate = risk_free_rate / 100
            volatility = volatility / 100
            days_to_maturity = (exercise_date - datetime.now().date()).days

            BSM = BlackScholes(stock_price=spot_price, strike_price=strike_price, expire_time=days_to_maturity, risk_rate=risk_free_rate, volatility=volatility)
            call_option_price = BSM.calculate_option_price('Call Option')
            put_option_price = BSM.calculate_option_price('Put Option')

            st.subheader(f'Call option price: {call_option_price:.2f}')
            st.subheader(f'Put option price: {put_option_price:.2f}')
        else:
            st.error("Unable to proceed with calculations due to data fetching error.")
    except Exception as e:
        st.error(f"Error during calculation: {str(e)}")
else:
    st.info("Click 'Calculate option price' to see results.")   

