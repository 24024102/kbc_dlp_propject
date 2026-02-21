import os
import re
import json
from tabulate import tabulate

def load_config():
    with open('rules.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def scan_emails():
    config = load_config()
    rules = config.get('rules', [])
    thresholds = config.get('thresholds', {"critical": 70, "warning": 25})
    if not os.path.exists('emails'):
        print(" Folder 'emails' not found! Run generator.py first.")
        return
    email_files = os.listdir('emails')
    results_for_table = []
    for filename in email_files:
        path = os.path.join('emails', filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            total_score = 0
            detected = []

            for rule in rules:
                if re.search(rule['pattern'], content):
                    total_score += rule['points']
                    detected.append(rule['id'])

            
            if total_score >= thresholds.get('critical', 70):
                status = " CRITICAL"
            elif total_score >= thresholds.get('warning', 25):
                status = " WARNING"
            else:
                status = "CLEAN"

            results_for_table.append([filename, total_score, status, ", ".join(detected)])

    print(tabulate(results_for_table, headers=["File", "Score", "Status", "Detected"], tablefmt="fancy_grid"))

if __name__ == "__main__":
    scan_emails()