# 1. POLYMORPHISM - Ek naam, alag kaam
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Bhow Bhow")

class Cat(Animal):
    def sound(self):
        print("Meow Meow")

# Same function, alag output
for animal in [Dog(), Cat(), Animal()]:
    animal.sound()

# 2. ENCAPSULATION - Data ko chupana
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # __ = Private variable
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):  # Public method se access
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print("Balance:", acc.get_balance())

# 3. STATIC METHOD - Object ki zarurat nahi
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print("Sum:", Math.add(5, 10))

# 4. MULTIPLE INHERITANCE
class Father:
    def skills(self):
        print("Coding")

class Mother:
    def skills(self):
        print("Designing")

class Child(Father, Mother):  # Dono se inherit
    pass

c = Child()
c.skills()  # Father wali pehle aayegi
