from google.cloud import storage
from grab_mtgjson import getUrl
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:/mtg_project/auth/gcs_key.json"

bucket_name = "tg-data-jw"

contents = getUrl()

destination_blob_name = "raw/mtgjson_all_cards.json"



def upload_blob_from_memory(bucket_name, contents, destination_blob_name):

   
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_blob_name)


    blob.upload_from_string(contents)


    print(
        f"Uploaded {destination_blob_name} to bucket {bucket_name} successfully."
    )

upload_blob_from_memory(bucket_name, contents, destination_blob_name)