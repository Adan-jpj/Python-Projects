class Employee:
    language = "py"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")
        



Adan = Employee()
Adan.language = "JavaScript"
print( Adan.language, Adan.salary)
Adan.getInfo()
Adan.greet()
Employee.getInfo(Adan)
