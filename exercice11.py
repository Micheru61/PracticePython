#!usr/bin/python3.4

"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no
divisors.). You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
"""

def test_prime(number):
    divisor_numbers = 0
    divisor_numbers_list = []
    if number in (0, 1):
        print("{} is not a prime number".format(number))
        return
    for i in range(2,10):
        if i == number:
            continue
        elif number % i == 0:
            divisor_numbers += 1
            divisor_numbers_list.append(i)

    if divisor_numbers > 0:
        print("{} has {} diviros : {}, it is not a prime number".format(number, len(divisor_numbers_list),divisor_numbers_list))
    else:
        print("{} has no divisors, it is a prime number".format(number))

def input_number():
    try:
        number = int(input("Please enter a number to check whether it is a prime number or not\n: "))
        return number
    except ValueError:
        return input_number()

number = input_number()

test_prime(number)