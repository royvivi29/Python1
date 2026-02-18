class Person:
    name = "vivek Kumar Ray"
    occupation = "Software Engineer"
    netWorth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a = Person()

print(a.name, a.occupation)
a.info()

class Person:

    def __init__(self, name, occupation):
        print("Hey I am person")
        self.name = name 
        self.occupation = occupation

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Vivek", "Frontend developer")
a.info()
