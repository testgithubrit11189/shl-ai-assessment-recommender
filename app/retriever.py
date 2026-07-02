import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class SHLRetriever:

    def __init__(self):

        # Load SHL Catalog
        with open(
            "data/shl_product_catalog_fixed.json",
            "r",
            encoding="utf-8"
        ) as f:
            self.catalog = json.load(f)

        # Load Embedding Model
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        # Create searchable documents
        self.documents = []

        for item in self.catalog:

            document = f"""
Name:
{item.get("name", "")}

"description": item.get("description", "")[:250] + "..."
if item.get("description")
else ""

Skills:
{' '.join(item.get("keys", []))}

Job Levels:
{' '.join(item.get("job_levels", []))}

Languages:
{' '.join(item.get("languages", []))}

Duration:
{item.get("duration", "")}

Remote:
{item.get("remote", "")}

Adaptive:
{item.get("adaptive", "")}
"""

            self.documents.append(document)

        print("Creating embeddings...")

        self.embeddings = self.model.encode(
            self.documents,
            convert_to_numpy=True,
            show_progress_bar=True
        )

        print("Retriever Ready!")

    def search(self, query, top_k=5):

        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        )

        similarity_scores = cosine_similarity(
            query_embedding,
            self.embeddings
        )[0]

        top_indices = np.argsort(
            similarity_scores
        )[::-1][:top_k]

        recommendations = []

        for idx in top_indices:

            item = self.catalog[idx]

            recommendations.append(
                {
                    "name": item.get("name"),
                    "url": item.get("link"),
                    "description": item.get("description"),
                    "test_type": item.get("keys", ["Unknown"])[0] if item.get("keys") else "Unknown"
                }
            )

        return recommendations