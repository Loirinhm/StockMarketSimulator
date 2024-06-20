from app.models.user import User
from app.services.market_service import MarketService

class TransactionService:
    def __init__(self):
        self.market_service = MarketService()

    def buy_stock(self, user, stock_symbol, quantity, price):
        stock = self.market_service.get_stock(stock_symbol)
        if stock and user.buy_stock(stock, quantity, price):
            print(f"Successfully bought {quantity} shares of {stock_symbol} at {price:.2f} each.")
            self.market_service.update_stock_price(stock_symbol, price)
        else:
            print("Transaction failed. Please check your balance and the stock symbol.")

    def sell_stock(self, user, stock_symbol, quantity, price):
        stock = self.market_service.get_stock(stock_symbol)
        if stock and user.sell_stock(stock, quantity, price):
            print(f"Successfully sold {quantity} shares of {stock_symbol} at {price:.2f} each.")
            self.market_service.update_stock_price(stock_symbol, price)
        else:
            print("Transaction failed. Please check your portfolio and the stock symbol.")