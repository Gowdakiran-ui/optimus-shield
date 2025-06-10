import requests
from rich import print
from datetime import datetime

API_KEY = " "
BASE_URL = "https://otx.alienvault.com/api/v1"
LOG_FILE = "optimus_prime/ingest/otx_threat_log.txt"

def fetch_and_log_threats(limit=5):
    url = f"{BASE_URL}/pulses/subscribed"
    headers = {
        "X-OTX-API-KEY": API_KEY
    }
    params = {
        "limit": limit
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            with open(LOG_FILE, "a", encoding="utf-8") as log:
                for pulse in data.get("results", []):
                    log.write(f"\n# Pulse: {pulse['name']}\n")
                    for indicator in pulse.get("indicators", []):
                        timestamp = datetime.utcnow().isoformat()
                        entry = f"{timestamp} | {indicator['type']} | {indicator['indicator']}\n"
                        log.write(entry)
                        print(f"[green]Logged:[/green] {entry.strip()}")
            print(f"[bold cyan]✔ Threat indicators saved to:[/bold cyan] {LOG_FILE}")
        else:
            print(f"[red]Failed to fetch:[/red] {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"[red]Error:[/red] {e}")

if __name__ == "__main__":
    fetch_and_log_threats(limit=10)
