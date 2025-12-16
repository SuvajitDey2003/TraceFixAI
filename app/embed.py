from sentence_transformers import SentenceTransformer
import json
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/errors/errors.json") as f:
    data = json.load(f)

texts = [item["error"] + " " + item["cause"] for item in data]
embeddings = model.encode(texts)

dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(np.array(embeddings))

faiss.write_index(index, "app/error_index.faiss")

print("FAISS index created successfully")
