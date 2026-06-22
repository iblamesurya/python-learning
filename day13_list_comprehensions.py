# Day 13 - Advanced Comprehensions and Generators

# --- List comprehensions (review + advanced) ---
print("=== Advanced List Comprehensions ===")

# nested list comprehension - flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(f"Flattened: {flat}")

# list comp with conditions
nums = range(1, 21)
fizzbuzz = [
    "FizzBuzz" if n % 15 == 0 else
    "Fizz" if n % 3 == 0 else
    "Buzz" if n % 5 == 0 else
    str(n)
    for n in nums
]
print(f"FizzBuzz: {fizzbuzz}")

# --- Dict comprehensions ---
print("\n=== Dict Comprehensions ===")
words = ["hello", "world", "python", "is", "awesome"]
word_lengths = {w: len(w) for w in words}
print(f"Word lengths: {word_lengths}")

# swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"Swapped: {swapped}")

# --- Set comprehensions ---
print("\n=== Set Comprehensions ===")
sentence = "the quick brown fox jumps over the lazy dog"
unique_lengths = {len(word) for word in sentence.split()}
print(f"Unique word lengths: {sorted(unique_lengths)}")

# --- Generators ---
print("\n=== Generators ===")

# generator function
def countdown(n):
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(f"  {num}...")
print("  Liftoff!")

# generator expression (like list comp but lazy)
squares_gen = (x**2 for x in range(1, 11))
print(f"\nGenerator type: {type(squares_gen)}")
print(f"First 3 squares: {[next(squares_gen) for _ in range(3)]}")
print(f"Remaining: {list(squares_gen)}")

# practical: infinite fibonacci generator
def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fib_generator()
first_10 = [next(fib) for _ in range(10)]
print(f"\nFirst 10 Fibonacci: {first_10}")

# generator pipeline - memory efficient data processing
def read_numbers():
    """Simulate reading data"""
    for i in range(1, 101):
        yield i

def filter_even(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

def square(nums):
    for n in nums:
        yield n ** 2

# chain generators together
pipeline = square(filter_even(read_numbers()))
result = sum(pipeline)
print(f"\nSum of squares of even numbers 1-100: {result}")
