#!usr/bin/python3.4

import sys

liste = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in range(len(liste)):
    if liste[i] < 5:
        print("The element #{} of the list, '{}' is less than 5".format(i+1,liste[i]))
    elif liste[i] ==5:
        print("The element #{} of the list, '{}' is equal to 5".format(i+1, liste[i]))
    else:
        print("The element #{} of the list, '{}' is greater than 5".format(i+1, liste[i]))

print("The item in the list less than 5 are {}".format([i for i in liste if i < 5]))

try:
    nombre = int(input("\nPlease enter a whole number greater or equal to 0\n: "))
except TypeError:
    print("You did not enter a whole number greater or equal to 0, the program will be terminated")
    sys.exit(0)

print("The value less than the number {} in the list are : {}".format(nombre, [i for i in liste if i < nombre]))
