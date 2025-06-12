# create a class "programmer" for storing information of few programmers working at microsoft


class Programer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programer("Adan", 120000, 245001)
print(p.name, p.salary, p.pin, p.company)
r = Programer("Rahil", 120000, 245001)
print(r.name, r.salary, r.pin, r.company)