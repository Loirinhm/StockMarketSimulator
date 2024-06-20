import os
import pickle
from config import Config
from app.models.stock import EuropeanStock, AmericanStock

class MarketService:
    def __init__(self):
        self.stocks = []

    def load_stocks(self):
        self.stocks = []
        if not os.path.exists(Config.DATA_DIR):
            os.makedirs(Config.DATA_DIR)
            return

        stock_files = [f for f in os.listdir(Config.DATA_DIR) if f.endswith('.pkl') and not f.startswith('user_')]
        for file in stock_files:
            with open(os.path.join(Config.DATA_DIR, file), 'rb') as f:
                stock = pickle.load(f)
                self.stocks.append(stock)

    def save_stocks(self):
        for stock in self.stocks:
            file_name = f"{stock.symbol}.pkl"
            with open(os.path.join(Config.DATA_DIR, file_name), 'wb') as f:
                pickle.dump(stock, f)

    def _initialize_stocks(self):
        for symbol in Config.EUROPEAN_STOCKS:
            self.stocks.append(EuropeanStock(symbol, f"Company {symbol}", "EUR", 100.0, 15.0))
        for symbol in Config.AMERICAN_STOCKS:
            self.stocks.append(AmericanStock(symbol, f"Company {symbol}", "USD", 100.0, 20.0))

    def get_stock(self, symbol):
        return next((stock for stock in self.stocks if stock.symbol == symbol), None)

    def update_stock_price(self, symbol, new_price):
        stock = self.get_stock(symbol)
        if stock:
            stock.update_price(new_price)

    def display_stocks(self):
        print("\nAvailable Stocks:")
        for stock in self.stocks:
            print(stock)