Binance Futures Order Bot (Testnet)

A CLI-based trading bot for Binance USDT-M Futures Testnet.  
Supports Market and Limit orders with logging and error handling.

  Project Structure
- src/market_orders.py → Market order logic
- src/limit_orders.py → Limit order logic
- bot.log → Log file (API requests, responses, errors)
- report.pdf → Report with screenshots & explanation


Setup Instructions

Clone or download this repository.

Install dependencies:

pip install python-binance


Create Binance Testnet API keys from:
  https://testnet.binancefuture.com

Set your API keys in PowerShell (Windows):

setx BINANCE_API_KEY "your_api_key_here"
setx BINANCE_API_SECRET "your_api_secret_here"


 Open a new PowerShell window after running the above commands so the keys take effect.

  Running the Bot
Market Order

Place a BUY market order on BTCUSDT:

python src\market_orders.py BTCUSDT BUY 0.01

Limit Order

Place a SELL limit order on BTCUSDT at 25000 USDT:

python src\limit_orders.py BTCUSDT SELL 0.01 25000

  Notes

This bot runs on the Binance Futures Testnet, so no real funds are used.

All logs are saved in bot.log.

Extendable for more order types if needed.