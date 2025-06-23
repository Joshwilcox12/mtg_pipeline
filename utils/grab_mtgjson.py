import requests

url = "https://mtgjson.com/api/v5/AllPrintings.json"
output_path = "data/AllPrintings.json"


response = requests.get(url)

if response.status_code == 200:
    with open(output_path,"wb") as f:
        f.write(response.content)
    print("Download Success")
else:
    print("Download Failed:", response.status_code)
