from pathlib import Path
import re
import json

path = Path("data/shl_product_catalog.json")

text = path.read_text(encoding="utf-8")

# Strings ke beech wale newline hatao
text = re.sub(r'("name"\s*:\s*"[^"]*)\n\s*([^"]*")', r'\1 \2', text)

# Agar aur aise cases hon to repeat karo
for _ in range(10):
    new_text = re.sub(r'("name"\s*:\s*"[^"]*)\n\s*([^"]*")', r'\1 \2', text)
    if new_text == text:
        break
    text = new_text

Path("data/shl_product_catalog_fixed.json").write_text(
    text,
    encoding="utf-8"
)

data = json.loads(text)

print("Loaded Successfully!")
print("Total Assessments:", len(data))
print("First:", data[0]["name"])