# -*- coding: utf-8 -*-

import os
import sys
import csv

# -----------------------------------------------------------------------------

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import ccxt  # noqa: E402

binance = ccxt.binanceje()
symbols = ['BTC', 'ETH', 'LTC']
base = 'GBP'

def get_top_of_book(symbol, base, exchange):
    orderbook = exchange.fetch_order_book(f'{symbol}/{base}')
    bid = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None
    return bid, ask

def get_balances():
    """
    Needs to read in static, offline balances (bank, wallets etc) and merge with
    online exchange balances.
    """
    return {'BTC': 0.5, 'ETH': 3, 'LTC': 10, 'GBP': 300}

def evaluate_portfolio(symbols, base, exchange, top_of_book, balances):
    values = {s: top_of_book[s][0] * balances[s] for s in symbols}
    values[base] = balances[base]
    return values

if __name__ == "__main__":
    top_of_book = {s: get_top_of_book(s, base, binance) for s in symbols}
    balances = get_balances()
    evaluation = evaluate_portfolio(symbols, base, binance, top_of_book, balances)
    print(evaluation)

