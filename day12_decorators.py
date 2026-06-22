# Day 12 - Decorators and Closures

# closures - a function that remembers the environment it was created in
def make_multiplier(factor):
    def multiplier(n):
        return n * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")

# basic decorator
def timer_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_sum(n):
    """Sum numbers from 1 to n slowly"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(f"Sum: {slow_sum(100000)}")

# decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    return f"Hello, {name}!"

print(greet("Surya"))

# practical example: memoization decorator
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
            print(f"  Computing {func.__name__}({args})")
        else:
            print(f"  Cache hit for {func.__name__}({args})")
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"\nFibonacci(10) = {fibonacci(10)}")
print(f"Fibonacci(10) again = {fibonacci(10)}")

# class-based decorator
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} time(s)")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    return "Hello!"

say_hello()
say_hello()
say_hello()
