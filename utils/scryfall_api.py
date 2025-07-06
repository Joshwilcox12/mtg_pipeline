import requests
import pandas as pd
import os
import json
from io import StringIO




keys = ["id", "prices", "image_uris"]
price_keys = ["usd", "usd_foil","eur", "eur_foil"]
image_keys = ["large"]

def grab_api():
    url = 'https://api.scryfall.com/bulk-data'
    
    
    headers = {
        "User-Agent": "mtg-project/1.0 (joshuawilcox63@gmail.com)"
    }

    response = requests.get(url, headers=headers, timeout=20)

    return response
    
   
    
    
def get_download_url_default(response):

    if response.status_code == 200:
        data = response.json()["data"]
        for entry in data:
            if entry["name"] == "Default Cards":
                 # default-cards
                downloadUrl = entry["download_uri"]
               
        downloadResponse = requests.get(downloadUrl, timeout=60)
        info = downloadResponse.json()
        return info
    else:
        print(f"Request failed with status code {response.status_code}")


def clean_data(data):
        final_list = []
        for card in data:
             base_data = {k: card.get(k, None) for k in keys}

             prices = card.get("prices", {})
             selected_prices = {k: prices.get(k)for k in price_keys}

             base_data.update(selected_prices)

             images = card.get("image_uris",{})
             selected_images = {k: images.get(k) for k in image_keys}

             base_data.update(selected_images)

             final_list.append(base_data)

        return final_list

def price_only(catalog):
     
     for card in catalog:
          card.pop("image_uris", None)
          card.pop("prices", None)
          card.pop("large", None)
     df = pd.DataFrame(catalog) 
     return df


def image_only(catalog):
     
     for card in catalog:
          card.pop("image_uris", None)
          card.pop("prices", None)
          for k in price_keys:
               card.pop(k, None)

     df = pd.DataFrame(catalog) 
     return df
     
def submit_image():
     url = grab_api()
     default = get_download_url_default(url)
     clean = clean_data(default)
     finish = image_only(clean)
     return finish


def raw_scryfall():
    url = grab_api()
    default = get_download_url_default(url) 
    return default


def daily_price():
     url = grab_api()
     default = get_download_url_default(url)
     clean = clean_data(default)
     finish = price_only(clean)
     finish.to_csv("output/price.csv", index=False, encoding="utf-8-sig")
     buffer = StringIO()
     finish.to_csv(buffer, index=False, encoding="utf-8-sig")
     return buffer.getvalue()
     

