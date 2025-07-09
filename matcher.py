import faiss
import numpy as np
from catalog import PRODUCTS
from utils import embed_text

embeddings = [embed_text(p["description"]) for p in PRODUCTS]
dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def find_best_match(user_bio: str):
    query_vec = embed_text(user_bio)
    _, indices = index.search(np.array([query_vec]), k=2)
    return [PRODUCTS[i] for i in indices[0]]
