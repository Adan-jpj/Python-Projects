class Employee:
    language = "py" # This is a class attribute 
    salary = 1200000


Adan = Employee()
Adan.name = "Adan" # This is an instance attribute
print(Adan.name, Adan.language, Adan.salary)

Arham = Employee()
Arham.name = "Arham"
print(Arham.name, Arham.salary, Arham.language) 

# Here name is instance attribute and saalary and language are class attribute
# as they directtly belong to the class