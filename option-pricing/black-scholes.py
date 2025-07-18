import numpy as np
from scipy.stats import norm 

def call_option_price(stock_price, strike_price, volatility, expire_time, risk_rate ):
    """
    Preforms calculation for call options based on the given formula
    Formula: S*N(d1) - PresentValue(K)*N(d2)
    """
    PV_K = strike_price*np.exp(-risk_rate*expire_time)
    d1 = (np.log(stock_price/strike_price) + (risk_rate + [volatility**2]/2) * expire_time)/(volatility*np.sqrt(expire_time))
    d2 = d1 - volatility*np.sqrt(expire_time)
    return ((norm.cdf(d1)*stock_price) - (norm.cdf(d2)*PV_K))

def put_option_price(stock_price, strike_price, volatility, expire_time, risk_rate ):
    """
    Preforms calculation for call options based on the given formula
    Formula: PresentValue(K)*N(-d2) - S*N(-d1)
    """
    PV_K = strike_price*np.exp(-risk_rate*expire_time)
    d1 = (np.log(stock_price/strike_price) + (risk_rate + [volatility**2]/2) * expire_time)/(volatility*np.sqrt(expire_time))
    d2 = d1 - volatility*np.sqrt(expire_time)
    return ((norm.cdf(-d2)*PV_K) - (norm.cdf(-d1)*stock_price))

