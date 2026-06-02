import argparse
from binance_client import place_order

def main():
    parser = argparse.ArgumentParser(description="Binance Futures CLI Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT", "STOP_LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop_price", type=float)

    args = parser.parse_args()

    print("\nCLI STARTED")

    print("\n===== ORDER REQUEST =====")
    print("Symbol   :", args.symbol)
    print("Side     :", args.side)
    print("Type     :", args.type)
    print("Quantity :", args.quantity)

    if args.price:
        print("Price    :", args.price)

    if args.stop_price:
        print("StopPrice:", args.stop_price)

    # VALIDATION
    if args.type == "LIMIT" and args.price is None:
        print("ERROR ❌ LIMIT order requires price")
        return

    if args.type == "STOP_LIMIT":
        if args.price is None or args.stop_price is None:
            print("ERROR ❌ STOP_LIMIT requires price and stop_price")
            return

    try:
        response = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
            args.stop_price
        )

        print("\n===== ORDER RESPONSE =====")
        print(response)

        # 🔥 SUCCESS OUTPUT (ADDED FEATURE)
        if response:
            print("\nSUCCESS ✅ Order placed successfully")
            print("Order Type:", response.get("orderType"))
            print("Status:", response.get("algoStatus") or response.get("status"))

    except Exception as e:
        print("\nFAILED ❌", e)


if __name__ == "__main__":
    main()