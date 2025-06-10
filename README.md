
🧠 LLM-Powered Threat Detection (RAG Pipeline)

1. Documents (Threat Intel): Curated threat intelligence data loaded and embedded.
2. Vector DB: Indexed using Qdrant, running in Docker.
3. Query Pipeline:
   - User inputs a URL
   - Relevant threat context retrieved via semantic search
   - LLM (via OpenRouter or Gemini) gives human-readable analysis

Output: A threat classification + action decision (Allowed / Blocked)

💾 Vector DB Setup (Qdrant)



* Collection: threat_docs
* Embedding model: sentence-transformers/all-MiniLM-L6-v2


🖥️ Live Dashboard

Shows all past threat detections sorted by time, with color-coded blocks:

* ✅ Green: Safe & Allowed
* ❌ Red: Malicious or Phishing → Block
 📚 Technologies Used

* 🐍 Python + Flask
* 💡 Google Gemini (LLM)
* 🧠 Qdrant (Vector DB)
* 🧩 Sentence Transformers
* 🌐 Chrome Extension (JS)
* 🧪 Bootstrap 5 (Frontend)

🛠️ Future Upgrades

 [ ] Real-time integration with browser API
[ ] Auto-block malicious domains
[ ] Alert system (Email / Telegram)
[ ] Threat feed from open cyber sources (e.g., VirusTotal, AbuseIPDB)

 🧑‍💻 Author

Made with ⚡ by [Kiran Gowda A](https://github.com/Gowdakiran-ui)
