class Dog:
    species = "French Bulldog" #Class Attribute

    def __init__(self, name):
        self.name = name  #instance attribute
    
print(Dog.species) # French Bulldog

dog1 = Dog("Jack")
print(dog1.name)        #Jack
print(dog1.species)     #Franch Bulldog

dog2 = Dog("Tom")
print(dog2.name)        #Tom
print(dog2.species)     #French Bulldog


class Dog:
    species = "French Bulldog"

    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return (f"{self.name} says woof woof!")
    
jack = Dog("Jack")
Jill = Dog("Jill")

print(jack.bark())
print(Jill.bark())