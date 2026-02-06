class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

car_1 = Car("red", "Toyota corolla")
car_2 = Car("green", "Lamborghini Revelto")

# print(car_1.model)  #Toyota corolla
# print(car_2.model)  #Lamborghini Revelto

# print(car_1.color)  #red
# print(car_2.color)  #green


class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def describe(self):
        return f"This car is a {self.color} {self.model}"

car_1= Car("red", "Toyota Corolla")
car_2 = Car("Green", "Lamborghini Revuelto" )

print(car_1.describe())
print(car_2.describe())