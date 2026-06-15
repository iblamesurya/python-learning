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
