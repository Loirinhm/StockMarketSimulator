import logging
from app.services.market_service import MarketService
from app.services.transaction_service import TransactionService
from app.models.user import User
from app.interface import StockMarketInterface
from app.models.stock import EuropeanStock, AmericanStock
from config import Config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting Stock Market Simulator")
    
    market_service = MarketService()
    transaction_service = TransactionService()

    # Load initial data
    market_service.load_stocks()
    users = User.load_users()

    # Main application loop
    while True:
        print("\n1. View stocks")
        print("2. Buy stocks")
        print("3. Sell stocks")
        print("4. View portfolio")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            market_service.display_stocks()
        elif choice == '2':
            user_id = int(input("Enter user ID: "))
            stock_symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            transaction_service.buy_stock(users[user_id], stock_symbol, quantity, price)
        elif choice == '3':
            user_id = int(input("Enter user ID: "))
            stock_symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            transaction_service.sell_stock(users[user_id], stock_symbol, quantity, price)
        elif choice == '4':
            user_id = int(input("Enter user ID: "))
            users[user_id].display_portfolio()
        elif choice == '5':
            logger.info("Exiting Stock Market Simulator")
            break
        else:
            print("Invalid choice. Please try again.")

    # Save data before exiting
    market_service.save_stocks()
    User.save_users(users)

if __name__ == "__main__":
    app = StockMarketInterface()
    app.mainloop()