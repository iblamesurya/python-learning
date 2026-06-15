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
