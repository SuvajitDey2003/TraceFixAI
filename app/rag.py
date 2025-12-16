import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("app/error_index.faiss")

# Load error data
with open("data/errors/errors.json") as f:
    data = json.load(f)

def retrieve_similar_errors(query: str, k: int = 2):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)

    results = []
    for idx in indices[0]:
        results.append(data[idx])

    return results
