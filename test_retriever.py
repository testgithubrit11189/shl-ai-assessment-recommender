from app.retriever import SHLRetriever

r = SHLRetriever()

results = r.search(
    "Java Developer with communication skills"
)

for item in results:

    print(item["name"])