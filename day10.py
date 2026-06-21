# Day 10 - Object-Oriented Programming (OOP) Basics

# Class definition
class Animal:
    # Class variable
    kingdom = "Animalia"

    def __init__(self, name, sound):
        self.name = name  # instance variable
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def __str__(self):
        return f"Animal({self.name})"

# Inheritance
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")
        self.breed = breed

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"

    def speak(self):  # Method override
        return f"{self.name} barks: WOOF WOOF!"

class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Meow")
        self.indoor = indoor

    def purr(self):
        return f"{self.name} purrs..."

# Encapsulation with private attributes
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

# Testing
dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers")

print(dog.speak())
print(dog.fetch("ball"))
print(cat.speak())
print(cat.purr())
print(f"Kingdom: {Animal.kingdom}")

account = BankAccount("Surya", 1000)
account.deposit(500)
print(f"Balance: {account.get_balance()}")
