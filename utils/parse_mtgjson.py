import json
import sqlite3
import pandas as pd



with open("data/AllPrintings.json", "r", encoding="utf-8") as f:


    data = json.load(f)
    sets = data["data"]["10E"]

    


    # for card in data["data"]["10E"]["cards"]:
    #     print(card["name"])
    #     print("---")
    print(cards)
