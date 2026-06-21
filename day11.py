# Day 11 - Modules, Packages, and Standard Library

import math
import random
import datetime
import json
from collections import Counter, defaultdict
from itertools import combinations, permutations

# math module
print("=== Math Module ===")
print(f"Pi: {math.pi}")
print(f"Sqrt of 144: {math.sqrt(144)}")
print(f"Ceil(4.3): {math.ceil(4.3)}")
print(f"Floor(4.9): {math.floor(4.9)}")
print(f"Factorial(6): {math.factorial(6)}")

# random module
print("\n=== Random Module ===")
print(f"Random int (1-10): {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['Python', 'Java', 'Go', 'Rust'])}")
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(f"Shuffled: {nums}")

# datetime module
print("\n=== Datetime Module ===")
now = datetime.datetime.now()
print(f"Now: {now.strftime('%Y-%m-%d %H:%M:%S')}")
today = datetime.date.today()
print(f"Today: {today}")
birthday = datetime.date(2000, 1, 1)
age_days = (today - birthday).days
print(f"Days since 2000-01-01: {age_days}")

# json module
print("\n=== JSON Module ===")
data = {"name": "Surya", "skills": ["Python", "AWS"], "learning_day": 11}
json_str = json.dumps(data, indent=2)
print(json_str)
parsed = json.loads(json_str)
print(f"Parsed name: {parsed['name']}")

# collections
print("\n=== Collections ===")
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
print(f"Word count: {count}")
print(f"Most common: {count.most_common(2)}")

# itertools
print("\n=== Itertools ===")
letters = ['A', 'B', 'C']
print(f"Combinations of 2: {list(combinations(letters, 2))}")
print(f"Permutations of 2: {list(permutations(letters, 2))}")
