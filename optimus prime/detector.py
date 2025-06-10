import re
from rich import print

SUSPICIOUS_PATTERNS = [
    r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)",
    r"Connection attempt from (\d+\.\d+\.\d+\.\d+)",
    r"Port scan detected from (\d+\.\d+\.\d+\.\d+)",
    r"Possible DDoS attack",
]

def detect_threats(log_lines):
    threats = []
    
    for line in log_lines:
        for pattern in SUSPICIOUS_PATTERNS:
            match = re.search(pattern, line)
            if match:
                ip = match.group(1) if match.groups() else "N/A"
                threats.append({
                    "type": pattern,
                    "ip": ip,
                    "log": line.strip()
                })
                print(f"[red][!] Threat detected:[/red] {line.strip()}")
    
    return threats
