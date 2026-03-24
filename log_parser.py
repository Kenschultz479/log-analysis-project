import csv

# Example log file (you can export logs later)
log_file = "sample_logs.txt"

keywords = ["failed", "error", "unauthorized"]

with open(log_file, "r") as file:
    lines = file.readlines()

suspicious = []

for line in lines:
    for word in keywords:
        if word in line.lower():
            suspicious.append(line.strip())

print("Suspicious Events Found:\n")

for event in suspicious:
    print(event)