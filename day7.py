# Day 7 - Functions and Lambda Expressions

# Regular function
def greet(name):
    return f"Hello, {name}!"

# Function with default argument
def power(base, exp=2):
    return base ** exp

# Lambda function
square = lambda x: x * x
cube = lambda x: x ** 3

# Higher-order functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, numbers))
squared = list(map(lambda x: x ** 2, numbers))

from functools import reduce
total = reduce(lambda x, y: x + y, numbers)

# *args and **kwargs
def show_info(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

print(greet("Surya"))
print(power(3))
print(power(2, 10))
print("Square of 5:", square(5))
print("Cube of 3:", cube(3))
print("Even numbers:", evens)
print("Squared numbers:", squared)
print("Sum:", total)
show_info("python", "learning", day=7, topic="functions")
