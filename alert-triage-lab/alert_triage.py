import csv

print("Alert Triage Results:\n")

with open("alerts.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        severity = row["severity"].strip().lower()

        if severity == "high":
            action = "Investigate immediately and escalate if confirmed malicious."
        elif severity == "medium":
            action = "Review evidence, check related activity, and monitor closely."
        else:
            action = "Validate as normal activity or monitor as needed."

        print(f"Alert ID: {row['alert_id']}")
        print(f"Type: {row['alert_type']}")
        print(f"Source: {row['source']}")
        print(f"Severity: {row['severity']}")
        print(f"Recommended Action: {action}\n")