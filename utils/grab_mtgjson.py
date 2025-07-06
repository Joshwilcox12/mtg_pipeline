import requests
import os
import json

def getUrl():
    url = "https://mtgjson.com/api/v5/AllPrintings.json"
    output_path = "data/AllPrintings.json"

    response = requests.get(url)

    if response.status_code != 200:
        print("Download Failed:", response.status_code)
        return "skip"

    new_data = response.json()
    new_bytes = json.dumps(new_data).encode("utf-8")

    if os.path.exists(output_path):
        with open(output_path, "rb") as f:
            current_data = f.read()

        if new_bytes == current_data:
            print("No changes -- download skipped today")
            return "skip"
        else:
            with open(output_path, "wb") as f:
                f.write(new_bytes)
            print("Changes detected, updating new data")
            return new_data
    else:
        with open(output_path, "wb") as f:
            f.write(new_bytes)
        print("File does not exist, download and create")
        return new_data


def main():
    getUrl()


if __name__ == "__main__":
    main()
