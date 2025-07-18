import numpy as np
from scipy.stats import norm 
from .base import optionModel
class BlackScholes(optionModel):
        def __init__(self,stock_price, strike_price, volatility, expire_time, risk_rate):
            """
            Initializes variables used in Black-Scholes formula .

            stock_price: current stock price
            strike_price: strike price for option cotract
            expire_time: option contract maturity/exercise date
            risk_rate: returns on risk-free assets (assumed to be constant until expiry date)
            volatility: volatility of the underlying asset (standard deviation of asset's log returns)
            """
            self.stock_price = stock_price
            self.strike_price = strike_price
            self.expire_time = expire_time / 365
            self.risk_rate = risk_rate
            self.volatility = volatility

        def call_option_price(self):
            """
            Preforms calculation for call options based on the given formula
            Formula: S*N(d1) - PresentValue(K)*N(d2)
            """
            PV_K = self.strike_price*np.exp(-self.risk_rate*self.expire_time)
            d1 = (np.log(self.stock_price/self.strike_price) + (self.risk_rate + (self.volatility**2)/2) * self.expire_time)/(self.volatility*np.sqrt(self.expire_time))
            d2 = d1 - self.volatility*np.sqrt(self.expire_time)
            return ((norm.cdf(d1)*self.stock_price) - (norm.cdf(d2)*PV_K))

        def put_option_price(self):
            """
            Preforms calculation for call options based on the given formula
            Formula: PresentValue(K)*N(-d2) - S*N(-d1)
            """
            PV_K = self.strike_price*np.exp(-self.risk_rate*self.expire_time)
            d1 = (np.log(self.stock_price/self.strike_price) + (self.risk_rate + (self.volatility**2)/2) * self.expire_time)/(self.volatility*np.sqrt(self.expire_time))
            d2 = d1 - self.volatility*np.sqrt(self.expire_time)
            return ((norm.cdf(-d2)*PV_K) - (norm.cdf(-d1)*self.stock_price))

