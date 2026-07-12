class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show(self):
        print(self.brand, self.color)

C1 = Car("BMW", "Black")
C2 = Car("AUDI", "White")
C1.show()
C2.show()
