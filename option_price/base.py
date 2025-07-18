from enum import Enum
# allows setting of fixed set variables  
from abc import abstractmethod, ABC 

class Option_type(Enum):
    Option_call= 'Call Option'
    Option_put= 'Put Option'

class optionModel(ABC):
    """Abstract class defining interface for option pricing models."""

    def calculate_option_price(self, option_type):
        if option_type == Option_type.Option_call.value:
            return self.call_option_price()
        elif option_type == Option_type.Option_put.value:
            return self.put_option_price()
        else: 
            return -1 
        
    @classmethod
    @abstractmethod
    def call_option_price(cls):
        """Calculates option price for call option."""
        pass

    @classmethod
    @abstractmethod
    def put_option_price(cls):
        """Calculates option price for put option."""
        pass

