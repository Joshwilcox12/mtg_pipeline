import requests
import os


def getUrl():
    url = "https://mtgjson.com/api/v5/AllPrintings.json"
    output_path = "data/AllPrintings.json"


    response = requests.get(url)

    if response.status_code == 200:
        new_data = response.content
        print("Download Success to memory")
    else:
        print("Download Failed:", response.status_code)


    if os.path.exists(output_path):
        with open(output_path, "rb") as f:
            current_data = f.read()

        if new_data == current_data:
            print("No changes -- download skipped today")
        
        else:
            with open(output_path, "wb") as f:
                f.write(new_data)
            print("Chnages detected, updating new data")
    else:
        with open(output_path, "wb") as f:
            f.write(new_data)
        print("File does not exist, download and create")

    return response.content
    

def main():
    getUrl()


if __name__ == "__main__":
    main()
