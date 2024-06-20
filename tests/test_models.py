import unittest
from app.models.stock import EuropeanStock, AmericanStock
from app.models.user import User

class TestStock(unittest.TestCase):
    def test_european_stock_creation(self):
        stock = EuropeanStock("NESN.SW", "Nestle", "CHF", 100.0, 15.0)
        self.assertEqual(stock.symbol, "NESN.SW")
        self.assertIsInstance(stock.last_price, float)

    def test_american_stock_creation(self):
        stock = AmericanStock("AAPL", "Apple Inc.", "USD", 150.0, 20.0)
        self.assertEqual(stock.symbol, "AAPL")
        self.assertIsInstance(stock.last_price, float)

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "John Doe", 10000.0)
        self.stock = EuropeanStock("NESN.SW", "Nestle", "CHF", 100.0, 15.0)

    def test_buy_stock(self):
        result = self.user.buy_stock(self.stock, 10, 100.0)
        self.assertTrue(result)
        self.assertEqual(self.user.balance, 9000.0)
        self.assertEqual(len(self.user.stocks), 1)

    def test_sell_stock(self):
        self.user.buy_stock(self.stock, 10, 100.0)
        result = self.user.sell_stock(self.stock, 5, 110.0)
        self.assertTrue(result)
        self.assertEqual(self.user.balance, 9550.0)
        self.assertEqual(self.user.quantities[0], 5)

if __name__ == '__main__':
    unittest.main()