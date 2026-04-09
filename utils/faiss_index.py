import faiss
import numpy as np

# FAISS works only with numpy arrrays (float 32)

def create_faiss_index(vectors):
    dimension = vectors.shape[1] # number of features

    index = faiss.IndexFlatL2(dimension)
    # L2 = Euclidean distance (simple + fast)

    index.add(vectors.astype('float32')) # add vectors to index

    return index


def search_index(index, query_vector, top_k=5):
    distance, indices = index.search(query_vector.astype('float32'), top_k)
    return distance, indices