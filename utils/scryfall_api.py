import requests
import pandas as pd
import os

def grab_api():
    url = 'https://api.scryfall.com/bulk-data'
    output_path = "data/scryfall.json"
    
    headers = {
        "User-Agent": "mtg-project/1.0 (joshuawilcox63@gmail.com)"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        oracle_bulk = data["data"][0]
        name= oracle_bulk["name"]
        updateTime = oracle_bulk["updated_at"]
        downloadUrl = oracle_bulk["download_uri"]
        print(oracle_bulk["download_uri"])
        print(oracle_bulk["size"])
        downloadResponse = requests.get(downloadUrl)
    
        with open(output_path, "wb") as f:
            print(f"downloading {name}, the update time is: {updateTime}")
            f.write(downloadResponse.content)
 

    else:
        print(f"Request failed with status code {response.status_code}")

grab_api()