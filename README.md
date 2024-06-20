# Stock Market Simulator

This project is a simple stock market simulator that allows users to buy and sell stocks from European and American markets. Developed as part of the Programming Fundamentals course on the Computer Engeneering Degree.

## Features

- View available stocks and their current prices
- Buy and sell stocks
- View user portfolios
- Real-time currency conversion
- Simulated market hours for European and American markets

## Installation

1. Clone the repository:
  git clone https://github.com/yourusername/stock-market-simulator.git
  cd stock-market-simulator

2. Create a virtual environment:
  python -m venv venv
  source venv/bin/activate  # On Windows, use venv\Scripts\activate

3. Install the required packages:
  pip install -r requirements.txt

## Usage

To run the simulator: python main.py

Follow the on-screen prompts to navigate through the simulator.

## Configuration

You can modify the `config.py` file to change various parameters of the simulation, such as:

- File paths for data storage
- Market opening and closing times
- List of available stocks
- Base currency for conversions
- Simulation interval

## Testing

To run the tests: python -m unittest discover tests

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
