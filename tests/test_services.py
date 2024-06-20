import unittest
from unittest.mock import patch
from app.services.market_service import MarketService
from app.services.transaction_service import TransactionService
from app.models.user import User
from app.models.stock import EuropeanStock

class TestMarketService(unittest.TestCase):
    def setUp(self):
        self.market_service = MarketService()

    def test_load_stocks(self):
        self.market_service.load_stocks()
        self.assertGreater(len(self.market_service.stocks), 0)

    def test_get_stock(self):
        self.market_service.load_stocks()
        stock = self.market_service.get_stock("AAPL")
        self.assertIsNotNone(stock)
        self.assertEqual(stock.symbol, "AAPL")

class TestTransactionService(unittest.TestCase):
    def setUp(self):
        self.transaction_service = TransactionService()
        self.user = User(1, "John Doe", 10000.0)

    @patch('app.services.market_service.MarketService.get_stock')
    def test_buy_stock(self, mock_get_stock):
        mock_stock = EuropeanStock("NESN.SW", "Nestle", "CHF", 100.0, 15.0)
        mock_get_stock.return_value = mock_stock
        
        self.transaction_service.buy_stock(self.user, "NESN.SW", 10, 100.0)
        self.assertEqual(self.user.balance, 9000.0)
        self.assertEqual(len(self.user.stocks), 1)

if __name__ == '__main__':
    unittest.main()