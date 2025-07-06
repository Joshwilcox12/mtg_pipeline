import pandas as pd
from io import StringIO
from parse_mtgjson import get_card_data
from scryfall_api import  submit_image




def join_images():
    cards_df = get_card_data()
    image_df = submit_image()

    image_df = image_df.copy()

    image_df.rename(columns={"id": "scryfallId"}, inplace=True)

    image_df = image_df[["scryfallId", "large"]]

    image_df.rename(columns={"large": "image_url"}, inplace=True)

    merged_df = cards_df.merge(image_df, on="scryfallId", how="left")
    

    
    merged_df.to_csv("output/combined.csv",  index=False, encoding="utf-8-sig")
    
    buffer = StringIO()
    merged_df.to_csv(buffer, index=False, encoding="utf-8-sig")
    return buffer.getvalue()
  





