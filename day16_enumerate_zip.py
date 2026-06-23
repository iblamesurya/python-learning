# Day 16 - enumerate, zip, map, filter, reduce

from functools import reduce

# --- enumerate ---
print("=== enumerate ===")
languages = ["Python", "JavaScript", "Rust", "Go", "Java"]

# instead of: for i in range(len(languages))
for i, lang in enumerate(languages, start=1):
    print(f"  {i}. {lang}")

# useful in real life: find index of items
scores = [85, 92, 78, 95, 88, 91]
top_scores = [(i, s) for i, s in enumerate(scores) if s >= 90]
print(f"\nTop scores (index, score): {top_scores}")

# --- zip ---
print("\n=== zip ===")
names = ["Surya", "Raj", "Priya", "Ankit"]
cities = ["Hyderabad", "Mumbai", "Delhi", "Bangalore"]
ages = [22, 25, 23, 24]

# combine multiple lists into tuples
for name, city, age in zip(names, cities, ages):
    print(f"  {name} from {city}, age {age}")

# create dict from two lists
name_city = dict(zip(names, cities))
print(f"\nName->City: {name_city}")

# unzip with zip(*)
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print(f"Numbers: {numbers}, Letters: {letters}")

# --- map ---
print("\n=== map ===")
temps_celsius = [0, 20, 37, 100]
temps_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps_celsius))
print(f"Celsius:    {temps_celsius}")
print(f"Fahrenheit: {temps_fahrenheit}")

# map with multiple iterables
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
products = list(map(lambda x, y: x * y, a, b))
print(f"\nProducts: {products}")

# --- filter ---
print("\n=== filter ===")
numbers = range(1, 21)
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(f"Even numbers: {evens}")

words = ["hello", "", "world", "", "python", ""]
non_empty = list(filter(None, words))  # None removes falsy values
print(f"Non-empty: {non_empty}")

# --- reduce ---
print("\n=== reduce ===")
nums = [1, 2, 3, 4, 5]
product = reduce(lambda acc, x: acc * x, nums)
print(f"Product of {nums}: {product}")

# find longest word
words = ["Python", "is", "absolutely", "amazing", "for", "beginners"]
longest = reduce(lambda a, b: a if len(a) >= len(b) else b, words)
print(f"Longest word: {longest}")

# --- chaining them together ---
print("\n=== Chaining: Real-world Example ===")
students = [
    {"name": "Surya", "grade": 92},
    {"name": "Raj", "grade": 67},
    {"name": "Priya", "grade": 88},
    {"name": "Ankit", "grade": 45},
    {"name": "Maya", "grade": 95},
]

# filter passing students -> extract names -> enumerate
passing = filter(lambda s: s["grade"] >= 70, students)
names = map(lambda s: f"{s['name']} ({s['grade']})", passing)
for rank, name in enumerate(names, start=1):
    print(f"  #{rank}: {name}")
