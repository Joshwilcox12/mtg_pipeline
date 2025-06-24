import json
import sqlite3
import pandas as pd


#open json file
with open("data/AllPrintings.json", "r", encoding="utf-8") as f:

#unnest each set to get info I want
    data = json.load(f)
#list of keys(columns) I want and think are important for this project
    keys = ["setCode", "uuid", "name", "borderColor", "colors", "convertedManaCost", "edhrecRank", "edhrecSaltiness",
            "faceFlavorName","faceManaValue", "finishes", "frameEffects", "isAlternative", "isFullArt",
            "isOnlineOnly", "isReprint", "isReserved", "keywords", "life", "manaCost", "manaValue",
            "number", "originalPrintings", "originalReleaseDate", "otherFaceIds", "power", "toughness",
            "printings", "purchaseUrls", "rarity", "side", "sourceProducts", "subsets", "supertypes", "text",
            "type", "types", "artist", "artistIds"]    


#list that contains each sets dictionary values I want
    final_list =[]

#append that dic to the list
    set_data = data["data"]
    
    #key 10E, value.....
    # for each sets information, store the info of the key: cards and it's values(card data in a dic) in cards
    for sets_id, sets_info in set_data.items():
        cards = sets_info.get("cards", [])
        #cards is a list of dictionary info of each card, for each card in this list store the key value pair into card_info, and we loop through only the keys we want
        for card in cards:
           card_info = {k: card.get(k, None) for k in keys}
           final_list.append(card_info)

df = pd.DataFrame(final_list)

df.to_csv("output/test_mtg.csv",  index=False, encoding="utf-8-sig")

print(f"total cards processed: {len(df)}")





    


