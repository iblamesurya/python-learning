# Day 3 - Lists Practice

# 1. Create and access a list
fruits = ["apple", "banana", "mango", "orange", "grapes"]
print("Fruits list:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 2. List slicing
print("\nFirst 3 fruits:", fruits[:3])
print("Last 2 fruits:", fruits[-2:])

# 3. Add and remove elements
fruits.append("pineapple")
print("\nAfter append:", fruits)
fruits.remove("banana")
print("After remove:", fruits)

# 4. List sorting
numbers = [42, 7, 19, 3, 88, 55, 1]
numbers.sort()
print("\nSorted numbers:", numbers)
numbers.sort(reverse=True)
print("Sorted descending:", numbers)

# 5. List comprehension - squares
squares = [x ** 2 for x in range(1, 11)]
print("\nSquares 1-10:", squares)

# 6. Filter with list comprehension
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print("Even squares:", even_squares)

# 7. Find max, min, sum
data = [15, 3, 27, 8, 42, 11]
print(f"\nData: {data}")
print(f"Max: {max(data)}, Min: {min(data)}, Sum: {sum(data)}")
print(f"Average: {sum(data) / len(data):.2f}")

# 8. Check if element exists
print("\nIs 'mango' in fruits?", "mango" in fruits)
print("Is 'banana' in fruits?", "banana" in fruits)
# Day 3 - Loops Practice

# 1. Print numbers 1 to 10 using for loop
print("Numbers 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# 2. Sum of numbers 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(f"Sum of 1 to 100: {total}")

# 3. Multiplication table of a number
def multiplication_table(n):
    print(f"\nMultiplication table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

multiplication_table(5)

# 4. While loop - countdown
print("\nCountdown:")
count = 10
while count >= 0:
    print(count, end=" ")
    count -= 1
print()

# 5. FizzBuzz
print("\nFizzBuzz (1-20):")
for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 6. Print only even numbers from a list using loop
numbers = [3, 8, 15, 22, 7, 44, 11, 6]
print("\nEven numbers from list:", [n for n in numbers if n % 2 == 0])

