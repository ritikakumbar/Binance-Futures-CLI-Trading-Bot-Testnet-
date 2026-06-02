import argparse
from binance_client import place_order

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

print("CLI STARTED")

# VALIDATION
if args.quantity <= 0:
    print("ERROR ❌ Quantity must be greater than 0")
    exit()

if args.type == "LIMIT" and args.price is None:
    print("ERROR ❌ LIMIT order requires price")
    exit()

print("\n===== ORDER REQUEST =====")
print("Symbol:", args.symbol)
print("Side:", args.side)
print("Type:", args.type)
print("Quantity:", args.quantity)

response = place_order(
    args.symbol,
    args.side,
    args.type,
    args.quantity,
    args.price
)

print("\n===== ORDER RESPONSE =====")
print(response)