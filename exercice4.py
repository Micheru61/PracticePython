#!usr/bin/python3.4

"""
Exercise 4 (and Solution)

Create a program that asks the user for a number and then prints out a
list of all the divisors of that number. (If you don’t know what a divisor is,
it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

import sys

try:
    nombre = int(input("Please enter a whole number \n: "))
except TypeError:
    print("You didn't enter a whole number, the program will be terminated")
    sys.exit(0)

divisor = []

for i in range(1, nombre+1):
    if nombre % i == 0:
        print("{} is a divisor of {}".format(i, nombre))
        divisor.append(i)

print("Here is the list of all the divisor of {} \n: {}".format(nombre, divisor))