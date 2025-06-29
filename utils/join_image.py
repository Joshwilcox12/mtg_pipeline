import pandas as pd
from parse_mtgjson import get_card_data
from scryfall_api import  submit_image




def join_images():
    cards_df = get_card_data()
    image_df = submit_image()

    image_df = image_df.copy()

    image_df.rename(columns={"id": "scryfallId"}, inplace=True)

    image_df = image_df[["scryfallId", "image_uris.large"]]

    image_df.rename(columns={"image_uris.large": "image_url"}, inplace=True)

    merged_df = cards_df.merge(image_df, on="scryfallId", how="left")


    print(merged_df.head(5))
    merged_df.to_csv("output/combined.csv",  index=False, encoding="utf-8-sig")



join_images()