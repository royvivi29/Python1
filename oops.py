class Wallet:
   def __init__(self, balance):
       self.__balance = balance 

   def deposit(self, amount):
       if amount > 0:
           self.__balance += amount 

   def withdraw(self, amount):
       if 0 < amount <= self.__balance:
           self.__balance -= amount 

account = Wallet(500)
print(account.__balance) 

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} is going {self.speed} km/h")


c1 = Car("Tesla")
c1.accelerate()