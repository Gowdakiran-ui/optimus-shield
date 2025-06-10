from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
import os
from openai import OpenAI
import requests

# Connect to Qdrant
client = QdrantClient(host="localhost", port=6333)
COLLECTION_NAME = "threat_logs"

# Sentence embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Your Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or "get_api key"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + GEMINI_API_KEY

def ask_with_rag(query):
    # Embed the input
    vector = model.encode(query).tolist()

    # Query vector DB
    search_result = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        limit=5
    )

    # Build context from top matches
    context = "\n".join([hit.payload["text"] for hit in search_result])

    # Construct prompt
    prompt = f"""You are a cyber threat analyst. Based on the following logs, answer the question: "{query}"

Logs:
{context}
"""

    # Call Gemini API
    response = requests.post(GEMINI_URL, json={
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    })

    result = response.json()
    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "Unable to get a valid response."
