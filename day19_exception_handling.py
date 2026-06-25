# Day 19 - Exception Handling

# Basic try/except/else/finally
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete.")

# Custom exception
class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative number not allowed: {value}")

def check_positive(n):
    if n < 0:
        raise NegativeNumberError(n)
    return n

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(e)

# Context managers with exceptions
class ManagedResource:
    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Resource released")
        return False  # Don't suppress exceptions

with ManagedResource():
    print("Working with resource")
