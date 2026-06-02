# 🚀 Binance Futures CLI Trading Bot (Testnet)

## 📌 Project Overview
This project is a Python CLI application that connects to Binance Futures Testnet and allows users to place Market and Limit orders using command-line inputs.

It demonstrates API integration, CLI design, validation, and logging.

---

## ✨ Features
- Place MARKET orders
- Place LIMIT orders
- BUY / SELL support
- CLI-based input handling (argparse)
- Input validation (quantity, price checks)
- Structured logging of requests & responses
- Modular architecture (API + CLI separation)

---

## 🏗️ Project Structure

binance-futures-cli/
│
├── cli.py # CLI entry point
├── binance_client.py # Binance API logic
├── logger.py # Logging helper
├── .env # API keys (not uploaded)
├── requirements.txt
└── logs/
└── binance.log

---

## ⚙️ Setup Instructions

### 1. Clone repository
```bash
git clone <your-repo-url>
cd binance-futures-cli

2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt

4. Create .env file
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret

API Setup (Testnet)
Go to Binance Futures Testnet:
https://testnet.binancefuture.com/
Login using GitHub or Google
Create API key
Add it to .env

How to Run
📈 MARKET ORDER
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

LIMIT ORDER
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000

Example Output
CLI STARTED

===== ORDER REQUEST =====
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001

===== ORDER RESPONSE =====
Order ID: 123456789
Status  : NEW
Logging

All API requests and responses are stored in:
logs/binance.log

Example log format:
2026-06-02 | INFO | REQUEST: {...}
2026-06-02 | INFO | RESPONSE: {...}




