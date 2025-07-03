import requests
import os

def getUrl():
    url = "https://mtgjson.com/api/v5/AllPrintings.json"
    output_path = "data/AllPrintings.json"

    response = requests.get(url)

    if response.status_code != 200:
        print("Download Failed:", response.status_code)
        return "skip"  # fail gracefully

    new_data = response.content
    print("Download Success to memory")

    # Compare against existing file
    if os.path.exists(output_path):
        with open(output_path, "rb") as f:
            current_data = f.read()

        if new_data == current_data:
            print("No changes -- download skipped today")
            return "skip"
        else:
            with open(output_path, "wb") as f:
                f.write(new_data)
            print("Changes detected, updating new data")
            return new_data
    else:
        # File doesn't exist yet
        with open(output_path, "wb") as f:
            f.write(new_data)
        print("File does not exist, download and create")
        return new_data


def main():
    getUrl()


if __name__ == "__main__":
    main()
