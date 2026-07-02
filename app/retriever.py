import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SHLRetriever:

    def __init__(self):

        with open(
            "data/shl_product_catalog_fixed.json",
            "r",
            encoding="utf-8"
        ) as f:
            self.catalog = json.load(f)

        self.documents = []

        for item in self.catalog:

            text = f"""
            {item.get("name","")}
            {item.get("description","")}
            {' '.join(item.get("keys",[]))}
            {' '.join(item.get("job_levels",[]))}
            {' '.join(item.get("languages",[]))}
            """

            self.documents.append(text)

        self.vectorizer = TfidfVectorizer(stop_words="english")

        self.matrix = self.vectorizer.fit_transform(self.documents)

        print("Retriever Ready!")

    def search(self, query, top_k=5):

        query_vector = self.vectorizer.transform([query])

        scores = cosine_similarity(query_vector, self.matrix)[0]

        top = scores.argsort()[::-1][:top_k]

        recommendations = []

        for idx in top:

            item = self.catalog[idx]

            recommendations.append(
                {
                    "name": item["name"],
                    "url": item["link"],
                    "description": item.get("description", ""),
                    "test_type": item.get("keys", ["Unknown"])[0]
                    if item.get("keys")
                    else "Unknown",
                }
            )

        return recommendations