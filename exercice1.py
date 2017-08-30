#!usr/bin/python3.4

from datetime import date

annee = date.today().year


prenom = ""
while prenom == "":
    prenom = input("Please input your name \n: ")

age = 0
while age == 0:
    try:
        age = int(input("Please input the age you'll have at the end of this year ('{}') \n:".format(annee)))
    except TypeError:
        age = 0
        print("Please enter a whole number !")

nombre = 0
while nombre == 0:
    try:
        nombre = int(input("Please enter how many time you wish the respone to be printed out on the screen \n"))
    except TypeError:
        nombre = 0
        print("Please enter a whole number !")

print(("{}, You'll have 100 years in {}, hope i'll see you then :) \n".format(prenom, 100 - age + annee))*nombre)
