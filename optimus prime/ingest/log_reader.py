import os

def read_logs(log_path):
    if not os.path.exists(log_path):
        raise FileNotFoundError(f"Log file not found: {log_path}")
    
    with open(log_path, 'r') as f:
        lines = f.readlines()
    
    return lines
