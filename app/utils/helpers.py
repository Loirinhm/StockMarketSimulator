import pytz
from datetime import datetime
from config import Config

def is_market_open(stock):
    now = datetime.now(pytz.UTC)
    if stock.symbol in Config.EUROPEAN_STOCKS:
        market_open = Config.EUROPE_OPEN
        market_close = Config.EUROPE_CLOSE
    elif stock.symbol in Config.AMERICAN_STOCKS:
        market_open = Config.AMERICA_OPEN
        market_close = Config.AMERICA_CLOSE
    else:
        return False

    current_time = now.time()
    return market_open <= current_time <= market_close

def validate_user_input(prompt, validator):
    while True:
        try:
            value = input(prompt)
            return validator(value)
        except ValueError as e:
            print(f"Invalid input: {e}")