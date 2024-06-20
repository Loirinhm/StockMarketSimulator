import os
import pickle
from config import Config

class User:
    def __init__(self, id, name, balance, stocks=None, quantities=None, values_spent=None):
        self.id = int(id)
        self.name = str(name)
        self.balance = float(balance)
        self.stocks = stocks or []
        self.quantities = quantities or []
        self.values_spent = values_spent or []

    def buy_stock(self, stock, quantity, price):
        total_cost = quantity * price
        if self.balance >= total_cost:
            self.balance -= total_cost
            if stock in self.stocks:
                index = self.stocks.index(stock)
                self.quantities[index] += quantity
                self.values_spent[index] += total_cost
            else:
                self.stocks.append(stock)
                self.quantities.append(quantity)
                self.values_spent.append(total_cost)
            return True
        return False

    def sell_stock(self, stock, quantity, price):
        if stock in self.stocks:
            index = self.stocks.index(stock)
            if self.quantities[index] >= quantity:
                self.quantities[index] -= quantity
                self.values_spent[index] -= (self.values_spent[index] / self.quantities[index]) * quantity
                self.balance += quantity * price
                if self.quantities[index] == 0:
                    del self.stocks[index]
                    del self.quantities[index]
                    del self.values_spent[index]
                return True
        return False

    def display_portfolio(self):
        print(f"\nPortfolio for {self.name} (ID: {self.id}):")
        print(f"Balance: {self.balance:.2f} {Config.BASE_CURRENCY}")
        print("\nStocks:")
        for stock, quantity, value_spent in zip(self.stocks, self.quantities, self.values_spent):
            print(f"{stock.symbol}: {quantity} shares, {value_spent:.2f} {Config.BASE_CURRENCY} spent")

    @classmethod
    def load_users(cls):
        users = []
        if not os.path.exists(Config.DATA_DIR):
            os.makedirs(Config.DATA_DIR)
            return users  # Return an empty list if the directory was just created

        user_files = [f for f in os.listdir(Config.DATA_DIR) if f.startswith('user_') and f.endswith('.pkl')]
        for file in user_files:
            with open(os.path.join(Config.DATA_DIR, file), 'rb') as f:
                user = pickle.load(f)
                users.append(user)
        return users

    @classmethod
    def save_users(cls, users):
        for user in users:
            file_name = f"user_{user.id}.pkl"
            with open(os.path.join(Config.DATA_DIR, file_name), 'wb') as f:
                pickle.dump(user, f)