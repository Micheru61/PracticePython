#!usr/bin/python3.4

"""
Ask the user for a string and print out whether this string
is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

def ask_for_word():         # fonction to ask for a word and check its validity
    mot = input("Please, enter a word to check if it is a palindrome\n: ")
    mot = mot.lower()
    if not mot.isalpha():
        print("The word entered is invalid, please enter a valid word")
        return ask_for_word()
    else:
        return mot

mot = ask_for_word()

mot_inverse = mot[::-1]

if mot == mot_inverse:
    print("The word {} is a palindrome".format(mot.capitalize()))
else:
    print("The word {} is not a palindrome".format(mot.capitalize()))