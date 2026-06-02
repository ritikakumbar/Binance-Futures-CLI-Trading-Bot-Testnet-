from binance.client import Client
from dotenv import load_dotenv
import os
import logging

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

logging.basicConfig(
    filename="logs/binance.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def place_order(symbol, side, order_type, quantity, price=None, stop_price=None):

    print("FUNCTION CALLED ✅")

    try:
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity
        }

        # MARKET handled directly
        if order_type.upper() == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        elif order_type.upper() == "STOP_LIMIT":
            params["type"] = "STOP"
            params["stopPrice"] = stop_price
            params["price"] = price
            params["timeInForce"] = "GTC"

        logging.info(f"REQUEST: {params}")

        response = client.futures_create_order(**params)

        logging.info(f"RESPONSE: {response}")

        return response

    except Exception as e:
        logging.error(str(e))
        print("ERROR ❌", e)
        raise