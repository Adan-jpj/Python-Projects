class Employee:
    language = "py"
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")
        



Adan = Employee("Adan", 130000, "Javascript")
# Adan.name = "Adan"
print(Adan.name,Adan.salary, Adan.language)

# Rahil = Employee()