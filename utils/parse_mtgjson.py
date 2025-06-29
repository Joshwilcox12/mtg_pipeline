import json
import sqlite3
import pandas as pd


 #list of keys(columns) I want and think are important for this project
 #  
keys = ["setCode", "uuid", "Identifiers", "name", "borderColor", "colors", "convertedManaCost", "edhrecRank", "edhrecSaltiness",
                "faceFlavorName","faceManaValue", "finishes", "frameEffects", "isAlternative", "isFullArt",
                "isOnlineOnly", "isReprint", "isReserved", "keywords", "life", "manaCost", "manaValue",
                "number", "originalPrintings", "originalReleaseDate", "otherFaceIds", "power", "toughness",
                "printings", "purchaseUrls", "rarity", "side", "sourceProducts", "subsets", "supertypes", "text",
                "type", "types", "artist", "artistIds"]    
#open json file
def openJson():
    with open("data/AllPrintings.json", "r", encoding="utf-8") as f:
           data = json.load(f)
    return data


def extract_card_info(card: dict, keys: list) -> dict:
    card_info = {k: card.get(k, None) for k in keys}
    card_url = card_info.get('purchaseUrls',{})
    if isinstance(card_url, dict):
        for site, url in card_url.items():
            card_info[site] = url
        scryfall_id = card.get("identifiers", {}).get("scryfallId")
        if scryfall_id:
            card_info["scryfallId"] = scryfall_id    
        card_info.pop("purchaseUrls", None)   
        card_info.pop("Identifiers",None)
    return card_info
              
        
     

def necessaryValue(json):
    final_list = []

    set_data = json["data"]
    
    for sets_id, sets_info in set_data.items():
        cards = sets_info.get("cards", [])
        
        for card in cards:
           card_info = extract_card_info(card, keys)
           final_list.append(card_info)
   
    return final_list   

def get_card_data():
    data = openJson()
    mainValue = necessaryValue(data)
    df = pd.DataFrame(mainValue)
    return df


def main():
    df = get_card_data()
    df.to_csv("output/card_catalog.csv",  index=False, encoding="utf-8-sig")

    print(f"total cards processed: {len(df)}")

if __name__ == "__main__":
    main()


    

