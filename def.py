def square(num):
    return num ** 2
print(square(4))

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

square = lambda x: x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers)