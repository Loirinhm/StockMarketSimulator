from abc import ABC, abstractmethod
from currency_converter import CurrencyConverter
from config import Config

class Stock(ABC):
    def __init__(self, symbol, company, currency, last_price, pe_ratio):
        self.symbol = str(symbol)
        self.company = str(company)
        self.currency = str(currency)
        self.pe_ratio = float(pe_ratio)
        self.last_price = self.convert_currency(float(last_price))

    @abstractmethod
    def convert_currency(self, value):
        pass

    def update_price(self, new_price):
        self.last_price = self.convert_currency(float(new_price))

    def __str__(self):
        return f"{self.symbol} - {self.company}: {self.last_price:.2f} {Config.BASE_CURRENCY}"

class EuropeanStock(Stock):
    def convert_currency(self, value):
        converter = CurrencyConverter()
        if self.currency != Config.BASE_CURRENCY:
            return converter.convert(value, self.currency, Config.BASE_CURRENCY)
        return value

class AmericanStock(Stock):
    def convert_currency(self, value):
        converter = CurrencyConverter()
        if self.currency != Config.BASE_CURRENCY:
            return converter.convert(value, self.currency, Config.BASE_CURRENCY)
        return value