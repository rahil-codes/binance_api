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

class LimitOrders:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        logger.info("Initialized LimitOrders (testnet=%s)", testnet)

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            logger.info("Placing LIMIT order: %s %s %s @ %s", side, quantity, symbol, price)
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )
            logger.info("LIMIT_ORDER_RESPONSE: %s", order)
            print("✅ Limit order placed:", order)
            return order
        except BinanceAPIException as e:
            logger.error("Limit order failed: %s", e)
            print("❌ Error:", e)
            return None


if __name__ == "__main__":  # ✅ must be outside class
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    bot = LimitOrders(api_key, api_secret, testnet=True)
    bot.place_limit_order("BTCUSDT", "SELL", 0.001, 120000)
