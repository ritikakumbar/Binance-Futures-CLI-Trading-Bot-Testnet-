import logging

logging.basicConfig(
    filename="logs/binance.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log_info(msg):
    logging.info(msg)
    print("[INFO]", msg)

def log_error(msg):
    logging.error(msg)
    print("[ERROR]", msg)