import os

folders = [
    "optimus_prime/ingest",
    "optimus_prime/agents/detection",
    "optimus_prime/agents/analysis",
    "optimus_prime/agents/decision",
    "optimus_prime/agents/execution",
    "optimus_prime/tools",
    "optimus_prime/logs",
    "optimus_prime/configs",
    "optimus_prime/tests",
    "optimus_prime/dashboard",
]

files = {
    "optimus_prime/main.py": "",
    "optimus_prime/README.md": "# Optimus Prime: Cyber Threat Response Agent\n",
    "optimus_prime/configs/config.yaml": "llm_model: 'mistral'\nthreat_threshold: 0.8\n",
    "optimus_prime/requirements.txt": "fastapi\nuvicorn\npsutil\nscikit-learn\nrich\npyyaml\n",
    "optimus_prime/Dockerfile": (
        "FROM python:3.10-slim\n"
        "WORKDIR /app\n"
        "COPY . .\n"
        "RUN pip install --no-cache-dir -r requirements.txt\n"
        "CMD [\"python\", \"main.py\"]\n"
    ),
    "optimus_prime/ingest/data_sample.log": "# sample apache or system logs here\n",
    "optimus_prime/tools/ip_blocker.py": "# Blocks IP locally\n",
    "optimus_prime/tools/port_disabler.py": "# Shuts down port\n",
    "optimus_prime/tools/notifier.py": "# Sends alerts to Telegram/email\n",
    "optimus_prime/agents/detection/detector.py": "# ML or rule-based anomaly detection\n",
    "optimus_prime/agents/analysis/llm_threat_analyzer.py": "# Uses local LLM to classify threat\n",
    "optimus_prime/agents/decision/decision_maker.py": "# Decides actions based on threat type\n",
    "optimus_prime/agents/execution/tool_executor.py": "# Calls blocking or alert tools\n",
    "optimus_prime/tests/test_detector.py": "# Unit test for detection\n",
    "optimus_prime/tests/test_tool_executor.py": "# Test IP blocking mock\n",
    "optimus_prime/dashboard/app.py": "# Optional Streamlit dashboard\n",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("✅ Optimus Prime file structure created successfully!")
