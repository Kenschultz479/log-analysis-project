from collections import Counter
import re

log_file = "sample_logs.txt"
failed_ips = []

with open(log_file, "r", encoding="utf-8") as file:
    for line in file:
        if "Failed login from" in line:
            match = re.search(r"from ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", line)
            if match:
                failed_ips.append(match.group(1))

counts = Counter(failed_ips)

print("Brute Force Detection Results:\n")

found = False
for ip, count in counts.items():
    if count >= 3:
        found = True
        print("ALERT: Possible brute force attack detected")
        print(f"Source IP: {ip}")
        print(f"Failed attempts: {count}\n")

if not found:
    print("No brute force pattern detected.")