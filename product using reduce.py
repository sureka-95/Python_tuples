#using functools library to import reduce function
from functools import reduce


#create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Using reduce() to multiply all numbers
product = reduce(lambda x, y: x * y, numbers)


# print Output
print(product)  