from binance.client import Client
import os
from dotenv import load_dotenv
from logger import log_info, log_error

load_dotenv()

client = Client(
    os.getenv("BINANCE_API_KEY"),
    os.getenv("BINANCE_API_SECRET")
)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"


def place_order(symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity
        }

        if order_type.upper() == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        log_info(f"REQUEST: {params}")

        response = client.futures_create_order(**params)

        log_info(f"RESPONSE: {response}")

        return response

    except Exception as e:
        log_error(str(e))
        raise