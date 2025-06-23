import json
import sqlite3
import pandas as pd



with open("data/AtomicCards.json", "r", encoding="utf-8") as f:


    data = json.load(f)
    meta = data["meta"]
    cards = data["data"]
    card_data = cards.get('"Brims" Barone, Midway Mobster')
    first_five =  list(cards.keys())[:5]

print(card_data[0].keys())

