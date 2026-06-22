# Day 14 - Regular Expressions (regex)

import re

# basic pattern matching
print("=== Basic Pattern Matching ===")
text = "My phone number is 123-456-7890 and email is surya@example.com"

# search for a pattern
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
if phone:
    print(f"Found phone: {phone.group()}")

email = re.search(r'[\w.]+@[\w.]+\.\w+', text)
if email:
    print(f"Found email: {email.group()}")

# findall - find all matches
print("\n=== Find All ===")
sentence = "The price is $10.50 and the tax is $1.05, total $11.55"
prices = re.findall(r'\$\d+\.\d{2}', sentence)
print(f"All prices: {prices}")

# groups - extract parts of a match
print("\n=== Groups ===")
date_str = "Today is 2026-06-22 and tomorrow is 2026-06-23"
dates = re.finditer(r'(\d{4})-(\d{2})-(\d{2})', date_str)
for match in dates:
    year, month, day = match.groups()
    print(f"Date: {match.group()} -> Year: {year}, Month: {month}, Day: {day}")

# substitution
print("\n=== Substitution ===")
messy_text = "Hello    World   this   has    weird    spacing"
clean = re.sub(r'\s+', ' ', messy_text)
print(f"Cleaned: {clean}")

# split with regex
print("\n=== Split ===")
data = "apple;banana,cherry|dragonfruit orange"
fruits = re.split(r'[;,|\s]+', data)
print(f"Fruits: {fruits}")

# common patterns practice
print("\n=== Common Patterns ===")

# validate email
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

test_emails = ["surya@gmail.com", "bad@", "test@co.uk", "nope"]
for e in test_emails:
    print(f"  {e}: {'valid' if is_valid_email(e) else 'invalid'}")

# extract hashtags
tweet = "Learning #Python today! #day14 #coding is fun #100DaysOfCode"
hashtags = re.findall(r'#\w+', tweet)
print(f"\nHashtags: {hashtags}")

# password strength checker
def check_password(pw):
    checks = {
        "8+ chars": len(pw) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', pw)),
        "lowercase": bool(re.search(r'[a-z]', pw)),
        "digit": bool(re.search(r'\d', pw)),
        "special": bool(re.search(r'[!@#$%^&*]', pw)),
    }
    return checks

password = "MyP@ss1234"
result = check_password(password)
print(f"\nPassword '{password}':")
for check, passed in result.items():
    print(f"  {check}: {'✓' if passed else '✗'}")
