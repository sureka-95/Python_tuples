# Import the 'reduce' function from the 'functools' module

from functools import reduce

# Define a lambda function 'fib_series' that generates a Fibonacci series up to 'n' elements
# It uses the 'reduce()' function along with a lambda function and an initial list [0, 1] to generate the Fibonacci series

fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

# Print the Fibonacci series up to n elements
print("Fibonacci series upto n:")

# To get n as user input
n=int(input("enter n:" ))

#print the output
print(fib_series(n))
