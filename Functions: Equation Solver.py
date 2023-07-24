import math
from math import sqrt

# Testing the functions
a = 2
b = 5
c = 6


# Sum of numbers
def sum(a, b, c):
    return a + b + c


# Product of numbers
def product(a, b, c):
    return a * b * c


# Finds largest number
def largest(a, b, c):
    return max(a, b, c)


# Finds smallest number
def smallest(a, b, c):
    return min(a, b, c)


# Finds area if possible
def area(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        s = (a + b + c)/2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        return "No triangle exists with side lengths a, b, and c"


# Displays the functions
print("a: ", a)
print("b: ", b)
print("c: ", c)
print(" ")
print("Sum: ", sum(a, b, c))
print("Product: ", product(a, b, c))
print("Smallest: ", smallest(a, b, c))
print("Largest: ", largest(a, b, c))
print("Area: ", area(a, b, c))

