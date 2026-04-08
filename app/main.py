from fastapi import FastAPI
from app.rag import search
from app.bedrock import query_llm

app = FastAPI()

@app.get("/ask")
def ask(query: str):
    context = search(query)
    prompt = f"Context: {context}\nQuestion: {query}"
    response = query_llm(prompt)
    return {"response": response}