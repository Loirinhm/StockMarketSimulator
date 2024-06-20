from tkinter import *
from tkinter.ttk import *

from app.services.market_service import MarketService
from app.services.transaction_service import TransactionService
from app.models.user import User
from config import Config

class Table:
    def __init__(self, root, num_rows, num_columns, data):
        self.root = root
        self.num_rows = int(num_rows)
        self.num_columns = int(num_columns)
        self.data = data

        for i in range(num_rows):
            for j in range(num_columns):
                self.e = Entry(root, width=20, fg='black',
                               font=('Arial', 10), justify=CENTER)
                self.e.grid(row=i, column=j)
                self.e.insert(END, data[i][j])

def stocks_to_list(stocks):
    stock_list = [('STOCK', 'NAME', 'CURRENCY', 'CURRENT PRICE - EUR', 'P/E RATIO')]
    for stock in stocks:
        stock_list.append((stock.symbol, stock.company, stock.currency, f"{stock.last_price:.2f}", f"{stock.pe_ratio:.2f}"))
    return stock_list

class StockMarketInterface(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('500x500')
        self.title('Stock Market Simulator')

        self.market_service = MarketService()
        self.transaction_service = TransactionService()
        self.users = User.load_users()
        
        self.market_service.load_stocks()

        label_1 = Label(self, text='Users', font=('Arial', 20))
        label_1.pack(padx=20, pady=20)

        self.create_user_buttons()

    def create_user_buttons(self):
        for i, user in enumerate(self.users, start=1):
            button = Button(self, text=f'User {i}', command=lambda u=user: self.open_user_window(u))
            button.pack(padx=20, pady=20)

    def open_user_window(self, user):
        user_window = Toplevel(self)
        user_window.geometry('800x800')
        user_window.title(f'User {user.id}')

        def show_available_stocks():
            stocks_window = Toplevel(user_window)
            stocks_window.title('Stocks available on the market')

            stock_list = stocks_to_list(self.market_service.stocks)
            num_rows = len(stock_list)
            num_columns = 5
            Table(stocks_window, num_rows, num_columns, stock_list)

        stocks_button = Button(user_window, text="Available Stocks", font=('Arial', 16), command=show_available_stocks)
        stocks_button.place(x=20, y=20)

        balance_label = Label(user_window, text=f"Balance: {user.balance:.2f} {Config.BASE_CURRENCY}", font=('Arial', 16))
        balance_label.place(x=450, y=25)

        self.create_buy_sell_interface(user_window, user)
        self.create_portfolio_display(user_window, user)

    def create_buy_sell_interface(self, window, user):
        buy_label = Label(window, text='Buy Stock', font=('Arial', 16))
        buy_label.place(x=20, y=100)

        sell_label = Label(window, text='Sell Stock', font=('Arial', 16))
        sell_label.place(x=420, y=100)

        for i, (action, x) in enumerate([('Buy', 30), ('Sell', 430)]):
            symbol_label = Label(window, text='Enter stock symbol', font=('Arial', 8))
            symbol_label.place(x=x, y=140)
            symbol_entry = Text(window, height=1, width=25, font=('Arial', 11))
            symbol_entry.place(x=x, y=160)

            quantity_label = Label(window, text='Enter quantity', font=('Arial', 8))
            quantity_label.place(x=x, y=190)
            quantity_entry = Text(window, height=1, width=25, font=('Arial', 11))
            quantity_entry.place(x=x, y=210)

            price_label = Label(window, text='Enter price', font=('Arial', 8))
            price_label.place(x=x, y=240)
            price_entry = Text(window, height=1, width=25, font=('Arial', 11))
            price_entry.place(x=x, y=260)

            def create_transaction(action):
                symbol = symbol_entry.get(1.0, "end-1c")
                quantity = int(quantity_entry.get(1.0, "end-1c"))
                price = float(price_entry.get(1.0, "end-1c"))
                
                if action == 'Buy':
                    self.transaction_service.buy_stock(user, symbol, quantity, price)
                else:
                    self.transaction_service.sell_stock(user, symbol, quantity, price)
                
                symbol_entry.delete(1.0, END)
                quantity_entry.delete(1.0, END)
                price_entry.delete(1.0, END)
                
                self.update_portfolio_display(window, user)
                balance_label.config(text=f"Balance: {user.balance:.2f} {Config.BASE_CURRENCY}")

            button = Button(window, text=action, font=('Arial', 16), command=lambda a=action: create_transaction(a))
            button.place(x=x, y=300)

    def create_portfolio_display(self, window, user):
        portfolio_label = Label(window, text='Portfolio', font=('Arial', 20))
        portfolio_label.place(x=100, y=400)

        self.update_portfolio_display(window, user)

    def update_portfolio_display(self, window, user):
        portfolio_data = [('STOCK', 'QUANTITY', 'VALUE')]
        for stock, quantity, value in zip(user.stocks, user.quantities, user.values_spent):
            portfolio_data.append((stock.symbol, str(quantity), f"{value:.2f}"))

        num_rows = len(portfolio_data)
        num_columns = 3

        frame = Frame(window)
        frame.place(x=110, y=450)
        
        for widget in frame.winfo_children():
            widget.destroy()

        Table(frame, num_rows, num_columns, portfolio_data)

if __name__ == "__main__":
    app = StockMarketInterface()
    app.mainloop()