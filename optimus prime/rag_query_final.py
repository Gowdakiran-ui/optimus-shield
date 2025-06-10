import json
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="get_key_fromenv")
gemini = genai.GenerativeModel("gemini-1.5-flash")  # Or "gemini-pro"

# Connect to Qdrant
client = QdrantClient(host="localhost", port=6333)
collection_name = "threat_logs"

# Load embedder
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_top_chunks(query, k=5):
    query_vector = model.encode(query).tolist()
    search_result = client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=k
    )
    return [hit.payload["text"] for hit in search_result]

def ask_with_rag(query):
    chunks = get_top_chunks(query)
    context = "\n".join(chunks)
    prompt = f"Context logs:\n{context}\n\nQuestion:\n{query}"
    response = gemini.generate_content(prompt)
    return response.text

# CLI to test
if __name__ == "__main__":
    while True:
        user_query = input("\n🧠 Ask about the logs: ")
        if user_query.strip().lower() in ['exit', 'quit']:
            break
        answer = ask_with_rag(user_query)
        print(f"\n💬 Gemini's Answer:\n{answer}")
