from flask import Flask, request, jsonify, render_template
from query_rag import ask_with_rag
import json
from datetime import datetime
import os

app = Flask(__name__)
LOG_FILE = "logs/threats.json"

@app.route("/")
def index():
    # Load logs for dashboard
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []
    return render_template("index.html", logs=logs[::-1])  # Latest first

@app.route("/check_log", methods=["POST"])
def check_log():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"response": "No input"})

    response = ask_with_rag(text)
    action = "Blocked" if any(word in response.lower() for word in ["unsafe", "malicious", "phishing"]) else "Allowed"

    log_entry = {
        "url": text,
        "analysis": response,
        "action": action,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Save to log
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []
    logs.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000)
    
    
