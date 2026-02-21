import os
import re
import json

def load_rules():
    with open('rules.json', 'r') as f:
        return json.load(f)
def scan_emails():
    rules = load_rules()
    email_files = os.listdir('emails')
    print(f"Starting  DLP scan in {len(email_files)} files...\n")
    for filename in email_files:
        path = os.path.join('emails', filename)
        with open(path, 'r', encoding= 'utf-8') as f:
            content = f.read()
            found_issues = []
            servity = "Clean"

    for name, pattern in rules['critical'].items():
         if re.search(pattern, content):
            found_issues.append(name)
            servity ="CRITICAL"
    if servity != "CRITICAL":
        for name, pattern in rules['medium'].items():
            found_issues.append(name)
            servity = "WARNING"
    status_icon = "+" if servity == "Clean" else "-"
    print(f"{status_icon} File: {filename} | Status: {servity} | Issues: {', '.join(found_issues)}")
if __name__ == "__main__":
    scan_emails()
        


                