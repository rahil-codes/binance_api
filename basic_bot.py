import argparse
import logging
import os
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

class FuturesBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            # Use Binance Futures Testnet
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        logger.info("Binance Futures client initialized (testnet=%s)", testnet)

    def place_order(self, symbol, order_type, side, quantity, price=None):
        """Place a futures order (MARKET or LIMIT)."""
        try:
            logger.info("Placing %s order: %s %s %s", order_type, side, quantity, symbol)

            if order_type.upper() == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side.upper(),
                    type="MARKET",
                    quantity=quantity
                )
            elif order_type.upper() == "LIMIT":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side.upper(),
                    type="LIMIT",
                    timeInForce="GTC",
                    quantity=quantity,
                    price=price
                )
            else:
                raise ValueError("Unsupported order type")

            logger.info("%s_RESPONSE: %s", order_type.upper(), order)
            print(f"{order_type.upper()} order response:", order)
            return order

        except BinanceAPIException as e:
            logger.error("%s order failed: %s", order_type.upper(), e)
            print("❌ Error:", e)
            return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", "-s", help="Trading pair, e.g., BTCUSDT")
    parser.add_argument("--type", "-t", help="Order type: MARKET or LIMIT")
    parser.add_argument("--side", "-S", help="Order side: BUY or SELL")
    parser.add_argument("--qty", "-q", type=float, help="Quantity")
    parser.add_argument("--price", "-p", type=float, help="Price (for LIMIT orders)")
    args = parser.parse_args()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        logger.error("API key/secret not found. Set BINANCE_API_KEY and BINANCE_API_SECRET.")
        return

    bot = FuturesBot(api_key, api_secret, testnet=True)

    if args.symbol and args.type and args.side and args.qty:
        bot.place_order(args.symbol, args.type, args.side, args.qty, args.price)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
