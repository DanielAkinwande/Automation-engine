import os
from datetime import datetime

def generate_report(folder):
    files = os.listdir(folder)

    report = f"Report generated at {datetime.now()}\n"
    report += f"Total files: {len(files)}\n\n"

    for f in files:
        report += f + "\n"

    with open("logs/report.txt", "w") as file:
        file.write(report)

    return "logs/report.txt"