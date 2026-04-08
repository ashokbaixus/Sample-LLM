from langchain.text_splitter import CharacterTextSplitter
import faiss
import numpy as np

documents = []
with open("data/sample.txt") as f:
    documents = f.read()

splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=50)
chunks = splitter.split_text(documents)

# Simple embedding simulation
vectors = np.random.rand(len(chunks), 128).astype("float32")

index = faiss.IndexFlatL2(128)
index.add(vectors)

def search(query):
    query_vector = np.random.rand(1, 128).astype("float32")
    D, I = index.search(query_vector, k=2)
    return [chunks[i] for i in I[0]]