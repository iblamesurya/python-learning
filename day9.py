# Day 9 - Exception Handling in Python

# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Multiple exceptions
def parse_number(value):
    try:
        return int(value)
    except ValueError:
        print(f"Cannot convert '{value}' to int")
        return None
    except TypeError:
        print(f"Invalid type: {type(value)}")
        return None

# try-except-else-finally
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    else:
        print(f"{a} / {b} = {result}")
        return result
    finally:
        print("Division operation complete.")

# Custom exception
class AgeError(Exception):
    def __init__(self, age, message="Age must be between 0 and 150"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def validate_age(age):
    if age < 0 or age > 150:
        raise AgeError(age)
    return age

# Testing
print(parse_number("42"))
print(parse_number("abc"))
divide(10, 2)
divide(5, 0)

try:
    validate_age(200)
except AgeError as e:
    print(f"AgeError: {e} (got {e.age})")
