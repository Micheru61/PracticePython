#!usr/bin/python3.4

"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are
common between the lists (without duplicates). Make sure your program works on two lists
of different sizes.

Extras:

    Randomly generate two lists to test this.
    Write this in one line of Python
    (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

"""

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


print("the common elements in a and b are : {}".format(list(set([i for i in a if i in b]))))

print("===============================================================\nExtra\n\
===============================================================")

a,b = [random.randint(1,20) for i in range(random.randint(1,10))], [random.randint(1,20) for i in range(random.randint(1,10))]

print("a = ", a)
print("b = ", b)

print("The common figures between a and b are : {}".format(list(set([i for i in a if i in b] + [i for i in b if i in a]))))


