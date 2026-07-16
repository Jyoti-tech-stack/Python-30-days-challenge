# 1. CLASS + OBJECT + CONSTRUCTOR
class Employee:
    def __init__(self, name, salary):  # Constructor
        self.name = name
        self.salary = salary
    
    def show_details(self):  # Method
        print(f"Name: {self.name}, Salary: {self.salary} LPA")

# 2. INHERITANCE
class Programmer(Employee):  # Employee ko inherit kiya
    def __init__(self, name, salary, language):
        super().__init__(name, salary)  # Parent ka constructor call
        self.language = language
    
    def show_details(self):  # Method Override
        print(f"Name: {self.name}, Salary: {self.salary} LPA, Language: {self.language}")
    
    def code(self):
        print(f"{self.name} is coding in {self.language}")

# 3. OBJECT BANAO AUR CHALAO
emp1 = Employee("Avni", 98)
emp1.show_details()

prog1 = Programmer("Jiya", 12, "Python")
prog1.show_details()
prog1.code()

# 4. CLASS METHOD EXAMPLE
class Student:
    school = "ABC School"  # Class variable
    
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
    
    def show_school(self):
        print(f"{self.name} studies in {self.school}")

s1 = Student("Riya")
s1.show_school()
Student.change_school("XYZ School")
s1.show_school()
