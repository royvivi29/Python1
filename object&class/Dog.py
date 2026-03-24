class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

dog_1.bark()
dog_2.bark()

#  instance and class attributes
class Dog1:
    species = "French Bulldog" #class Attribute 

    def __init__(self, name):
        self.name = name   #Instance attribute

print(Dog1.species)

dog1_1 = Dog1("Jack")
print(dog1_1.name)
print(dog1_1.species)

dog2_1 = Dog1("Tom")
print(dog2_1.name)
print(dog2_1.species)