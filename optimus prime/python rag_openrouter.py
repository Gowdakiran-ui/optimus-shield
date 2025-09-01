import google.generativeai as genai

genai.configure(api_key="enter_your_apikey")

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_answer(context, query):
    prompt = f"Context:\n{context}\n\nQuestion:\n{query}"
    response = model.generate_content(prompt)
    return response.text

# Usage
answer = generate_answer("India's capital is New Delhi.", "What is the capital of India?")
print(answer)

