with open("suspicious_email.txt", "r", encoding="utf-8") as file:
    content = file.read().lower()

checks = {
    "urgent language": "urgent" in content,
    "password request": "password" in content,
    "suspicious microsoft impersonation": "micr0soft" in content,
    "account lockout threat": "lockout" in content or "suspension" in content,
    "suspicious link": "http://" in content
}

print("Phishing Check Results:\n")
for item, result in checks.items():
    print(f"{item}: {'Detected' if result else 'Not detected'}")