import json
import sqlite3
import pandas as pd


 #list of keys(columns) I want and think are important for this project
 #  
keys = ["setCode", "uuid", "name", "borderColor", "colors", "convertedManaCost", "edhrecRank", "edhrecSaltiness",
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

     

def necessaryValue(json):
    final_list = []
#append that dic to the list
    set_data = json["data"]
    #key 10E, value.....
    # for each sets information, store the info of the key: cards and it's values(card data in a dic) in cards
    for sets_id, sets_info in set_data.items():
        cards = sets_info.get("cards", [])
        #cards is a list of dictionary info of each card, for each card in this list store the key value pair into card_info, and we loop through only the keys we want
        for card in cards:
           card_info = {k: card.get(k, None) for k in keys}
           card_url = card_info.get('purchaseUrls',{})
           if isinstance(card_url, dict):
               for site, url in card_url.items():
                   card_info[site] = url
               
           card_info.pop("purchaseUrls", None)   
              
           final_list.append(card_info)
    # final_list.pop('purchaseUrls')
    return final_list
    
def save_to_csv(ls):
    df = pd.DataFrame(ls)

    df.to_csv("output/test_mtg.csv",  index=False, encoding="utf-8-sig")

    print(f"total cards processed: {len(df)}")


def main():
    data = openJson()
    mainValue = necessaryValue(data)
    save_to_csv(mainValue)

if __name__ == "__main__":
    main()


    

