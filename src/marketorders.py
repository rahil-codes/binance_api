import logging
import os
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Setup logging
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

class MarketOrders:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        logger.info("Initialized MarketOrders (testnet=%s)", testnet)

    def place_market_order(self, symbol, side, quantity):
        try:
            logger.info("Placing MARKET order: %s %s %s", side, quantity, symbol)
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=quantity
            )
            logger.info("MARKET_ORDER_RESPONSE: %s", order)
            print("✅ Market order placed:", order)
            return order
        except BinanceAPIException as e:
            logger.error("Market order failed: %s", e)
            print("❌ Error:", e)
            return None
