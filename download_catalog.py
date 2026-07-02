import requests

url = "https://tcp-us-prod-rnd.shl.com/voiceRater/shl-ai-hiring/shl_product_catalog.json"

response = requests.get(url)

print("Status:", response.status_code)

with open("data/shl_product_catalog.json", "wb") as f:
    f.write(response.content)

print("Downloaded Successfully!")