# Day 28 - Polymorphism in OOPs

class Dog:
    def sound(self):
        print("Dog: Bhow Bhow 🐶")
    
    def sleep(self):
        print("Dog: 8 hours sota hai")


class Cat:
    def sound(self):
        print("Cat: Meow Meow 🐱")
    
    def sleep(self):
        print("Cat: 16 hours soti hai")


class Bird:
    def sound(self):
        print("Bird: Chee Chee 🐦")
    
    def sleep(self):
        print("Bird: 12 hours sota hai")


# Same function name "sound()" sab me hai
# Par output alag alag aa raha hai - ise hi Polymorphism kehte hain

animals = [Dog(), Cat(), Bird()]

for animal in animals:
    animal.sound()   # Same function
    animal.sleep()   # Same function
    print("---")
