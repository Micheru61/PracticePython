#!usr/bin/python.3.4
import sys
import math

nombre = int()

try:
    nombre = int(input("Please, enter a whole number\n: "))
except TypeError:
    print("You did not enter a whole number, the programm will be terminated")
    sys.exit(0)

msg = ""
msg2 = ""

if nombre%2 == 0:
    msg = "The number {} is even".format(nombre)
else:
    msg = "The number {} is odd".format(nombre)

print(msg)

if nombre%4 == 0:
    msg2 = "The number {} is a multiple of 4".format(nombre)
else:
    msg2 = msg2 = "The number {} is a not multiple of 4".format(nombre)

nombre2 = int()

try:
    nombre2 = int(input("Please enter a second whole number to divide into the first one\n: "))
except TypeError:
    print("You did not enter a whole number, the programm will be terminated")
    sys.exit(0)

if nombre%nombre2 == 0:
    print("The number {} is evenly divided by {}, ({})".format(nombre, nombre2, round(nombre/nombre2,2)))
else:
    print("The number {} is not evenly divided by {}, ({})".format(nombre, nombre2, round(nombre/nombre2,2)))
