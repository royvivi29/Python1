class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")
    
dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

#here i call the bark method
dog_1.bark()
dog_2.bark()