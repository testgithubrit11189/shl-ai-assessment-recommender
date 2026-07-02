import json


class SHLRetriever:

    def __init__(self):
        with open(
            "data/shl_product_catalog_fixed.json",
            "r",
            encoding="utf-8"
        ) as f:
            self.catalog = json.load(f)

        print("Retriever Ready!")

    def search(self, query, top_k=5):

        query = query.lower()

        scored = []

        for item in self.catalog:

            text = (
                item.get("name", "")
                + " "
                + item.get("description", "")
                + " "
                + " ".join(item.get("keys", []))
            ).lower()

            score = 0

            for word in query.split():
                if word in text:
                    score += 1

            scored.append((score, item))

        scored.sort(reverse=True, key=lambda x: x[0])

        recommendations = []

        for score, item in scored[:top_k]:

            recommendations.append({
                "name": item["name"],
                "url": item["link"],
                "description": item.get("description", ""),
                "test_type": item.get("keys", ["Unknown"])[0]
            })

        return recommendations