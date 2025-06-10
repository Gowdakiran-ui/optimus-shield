from ingest.log_reader import read_logs
from detector import detect_threats

if __name__ == "__main__":
    logs = read_logs(r"C:\Users\Kiran gowda.A\OneDrive\Documents\vs code\optimus prime\optimus_prime\ingest\data_sample.log")
    threats = detect_threats(logs)

    if threats:
        print(f"\n[bold red]Total Threats Detected:[/bold red] {len(threats)}\n")
    else:
        print("[green]No threats detected. System is clean.[/green]")
