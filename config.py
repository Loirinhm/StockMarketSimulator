import os
from datetime import time

class Config:
    # File paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, 'data')

    # Market opening times
    AMERICA_OPEN = time(9, 0, 0)
    AMERICA_CLOSE = time(22, 0, 0)
    EUROPE_OPEN = time(8, 0, 0)
    EUROPE_CLOSE = time(22, 30, 0)

    # Stock lists
    EUROPEAN_STOCKS = ['NESN.SW', 'ASML.AS', 'ROG.SW', 'AZN.L', 'SHEL.L']
    AMERICAN_STOCKS = ['AAPL', 'MSFT', 'AMZN', 'TSLA', 'GOOGL']

    # Currency conversion
    BASE_CURRENCY = 'EUR'

    # Simulation parameters
    SIMULATION_INTERVAL = 60  # seconds