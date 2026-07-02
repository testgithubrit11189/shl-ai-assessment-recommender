import json

with open("data/shl_product_catalog.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(type(data))
print("Total Assessments:", len(data))
print("First Assessment Name:", data[0]["name"])
print("First Assessment Link:", data[0]["link"])