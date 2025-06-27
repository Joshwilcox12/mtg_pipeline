import requests
import pandas as pd
import os
import json

def grab_api():
    url = 'https://api.scryfall.com/bulk-data'
    
    
    headers = {
        "User-Agent": "mtg-project/1.0 (joshuawilcox63@gmail.com)"
    }

    response = requests.get(url, headers=headers, timeout=20)
    
    keys = ["id", "prices", "image_uris"]
    
    if response.status_code == 200:
        data = response.json()["data"]
        for entry in data:
            if entry["name"] == "Default Cards":
                 # default-cards
                downloadUrl = entry["download_uri"]
                file_size = entry["size"]
                print(entry["name"])
                print(downloadUrl)
                print(file_size)

        downloadResponse = requests.get(downloadUrl, timeout=60)
        info = downloadResponse.json()

        

        # Extract required keys from each card
        final_list = [{k: card.get(k, None) for k in keys} for card in info]
        df = pd.json_normalize(final_list)  # Flatten nested keys
          # Avoid printing huge DataFrame
        df.to_csv("output/image_prices.csv",  index=False, encoding="utf-8-sig")
    else:
        print(f"Request failed with status code {response.status_code}")

grab_api()
