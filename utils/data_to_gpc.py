from google.cloud import storage
from grab_mtgjson import getUrl
from scryfall_api import raw_scryfall
import os
import json 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:/mtg_project/auth/gcs_key.json"

bucket_name = "tg-data-jw"
destination_raw_mtgJson = "raw/mtgjson_all_cards.json"
destination_raw_scryfall = "raw/image_price_scryfall.json"

def upload_raw_mtgJson_from_memory(bucket_name, contents, destination_blob_name):
    if contents == 'skip':
        print("No changes detected — skipping MTGJSON upload.")
        return
    
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    json_string = json.dumps(contents)
    blob.upload_from_string(json_string, content_type="application/json")

    print(f"Uploaded {destination_blob_name} to bucket {bucket_name} successfully.")


def upload_raw_price_image_scryfall_from_memory(bucket_name, contents, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    json_string = json.dumps(contents)
    blob.upload_from_string(json_string, content_type="application/json")

    print(f"Uploaded {destination_blob_name} to bucket {bucket_name} successfully.")


def upload_clean_daily_price_from_memory(bucket_name, contents, destination_blob_name):
    pass


def upload_clean_mtgJson_catalog_from_memory(bucket_name, contents, destination_blob_name):
    pass


def main():
    raw_mtgJson_contents = getUrl()
    raw_scryfall_contents = raw_scryfall()

    upload_raw_mtgJson_from_memory(bucket_name, raw_mtgJson_contents, destination_raw_mtgJson)
    upload_raw_price_image_scryfall_from_memory(bucket_name, raw_scryfall_contents, destination_raw_scryfall)


if __name__ == "__main__":
    main()
