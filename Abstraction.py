# Day 30 - Abstraction in OOPs
from abc import ABC, abstractmethod

# Abstract Class - iska direct object nahi banega
class Vehicle(ABC):
    
    @abstractmethod
    def start(self):  # abstract method - sirf declare kiya
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    def fuel_type(self):  # normal method bhi ho sakta hai
        print("Petrol ya Diesel use hota hai")

# Car class - Vehicle ko inherit kiya
class Car(Vehicle):
    def start(self):
        print("Car: Key ghumao aur start 🚗")
    
    def stop(self):
        print("Car: Brake dabao aur stop")

# Bike class - Vehicle ko inherit kiya  
class Bike(Vehicle):
    def start(self):
        print("Bike: Self button dabao aur start 🏍️")
    
    def stop(self):
        print("Bike: Brake + Gear down karke stop")

# Objects banana
print("=== Car ===")
c1 = Car()
c1.start()
c1.fuel_type()
c1.stop()

print("\n=== Bike ===")
b1 = Bike()
b1.start()
b1.stop()
